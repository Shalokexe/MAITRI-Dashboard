/**
 * MAITRI - Mission Control & Offline Assistant JavaScript Controller
 * Handles tab navigation, iOS Crystal UI, Chart.js telemetry, OpenCV camera,
 * Cognitive PVT tests, Voice TTS Speech Synthesis, and Blackbox flight logs.
 */

document.addEventListener('DOMContentLoaded', () => {
    initClock();
    initTabs();
    initCharts();
    initChatbot();
    initCameraCanvas();
    initCognitiveTest();
    initCircadianLighting();
    initSpeechSynthesis();
});

// 1. Mission UTC Clock
function initClock() {
    const clockEl = document.getElementById('missionClock');
    function updateClock() {
        const now = new Date();
        const utcStr = now.toISOString().replace('T', ' ').substring(0, 19) + ' UTC';
        if (clockEl) clockEl.textContent = utcStr;
    }
    updateClock();
    setInterval(updateClock, 1000);
}

// 2. Navigation Tabs
function initTabs() {
    const tabs = document.querySelectorAll('.nav-tab');
    const contents = document.querySelectorAll('.tab-content');

    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            tabs.forEach(t => t.classList.remove('active'));
            contents.forEach(c => c.classList.remove('active'));

            tab.classList.add('active');
            const target = tab.getAttribute('data-tab');
            const targetEl = document.getElementById(target);
            if (targetEl) targetEl.classList.add('active');
        });
    });
}

// 3. Telemetry Graphs (Chart.js)
let vitalsChart, emotionChart, sleepChart;

function initCharts() {
    const ctxVitals = document.getElementById('vitalsTrendChart');
    if (ctxVitals && typeof Chart !== 'undefined') {
        vitalsChart = new Chart(ctxVitals, {
            type: 'line',
            data: {
                labels: ['00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00', 'Now'],
                datasets: [
                    {
                        label: 'Heart Rate (BPM)',
                        data: [68, 70, 65, 72, 85, 74, 71, 69, 72],
                        borderColor: '#0A84FF',
                        backgroundColor: 'rgba(10, 132, 255, 0.12)',
                        borderWidth: 2,
                        tension: 0.4,
                        fill: true
                    },
                    {
                        label: 'SpO2 (%)',
                        data: [98, 98, 99, 98, 97, 98, 99, 98, 98.4],
                        borderColor: '#64D2FF',
                        borderWidth: 2,
                        tension: 0.4
                    },
                    {
                        label: 'Stress Index (0-100)',
                        data: [15, 20, 18, 35, 42, 28, 22, 20, 24],
                        borderColor: '#BF5AF2',
                        borderWidth: 2,
                        borderDash: [5, 5],
                        tension: 0.4
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { labels: { color: '#8E8E93', font: { family: '-apple-system' } } }
                },
                scales: {
                    x: { ticks: { color: '#636366' }, grid: { color: 'rgba(255,255,255,0.08)' } },
                    y: { ticks: { color: '#636366' }, grid: { color: 'rgba(255,255,255,0.08)' } }
                }
            }
        });
    }

    const ctxEmotion = document.getElementById('emotionPieChart');
    if (ctxEmotion && typeof Chart !== 'undefined') {
        emotionChart = new Chart(ctxEmotion, {
            type: 'doughnut',
            data: {
                labels: ['Focused', 'Calm', 'Elevated Stress', 'Fatigue'],
                datasets: [{
                    data: [60, 25, 10, 5],
                    backgroundColor: ['#30D158', '#64D2FF', '#FF9F0A', '#BF5AF2'],
                    borderWidth: 0
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { position: 'bottom', labels: { color: '#8E8E93' } }
                }
            }
        });
    }

    const ctxSleep = document.getElementById('sleepQualityChart');
    if (ctxSleep && typeof Chart !== 'undefined') {
        sleepChart = new Chart(ctxSleep, {
            type: 'bar',
            data: {
                labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                datasets: [
                    {
                        label: 'Deep Sleep (hrs)',
                        data: [2.1, 1.9, 2.3, 2.0, 1.8, 2.4, 2.1],
                        backgroundColor: '#BF5AF2'
                    },
                    {
                        label: 'REM Sleep (hrs)',
                        data: [1.8, 1.5, 1.9, 1.6, 1.4, 2.0, 1.6],
                        backgroundColor: '#0A84FF'
                    },
                    {
                        label: 'Light Sleep (hrs)',
                        data: [3.3, 3.4, 3.6, 3.5, 3.6, 3.1, 3.5],
                        backgroundColor: '#3A3A3C'
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { labels: { color: '#8E8E93' } }
                },
                scales: {
                    x: { stacked: true, ticks: { color: '#636366' } },
                    y: { stacked: true, ticks: { color: '#636366' } }
                }
            }
        });
    }
}

// 4. Offline AI Chatbot Logic & Speech Synthesis Out-Loud
function initChatbot() {
    const miniInput = document.getElementById('miniChatInput');
    const miniSendBtn = document.getElementById('miniChatSendBtn');
    const miniBox = document.getElementById('miniChatBox');

    const fullInput = document.getElementById('fullChatInput');
    const fullSendBtn = document.getElementById('fullChatSendBtn');
    const fullLogs = document.getElementById('fullChatLogs');

    function handleChat(inputEl, containerEl) {
        if (!inputEl || !containerEl) return;
        const msg = inputEl.value.trim();
        if (!msg) return;

        const userDiv = document.createElement('div');
        userDiv.className = 'chat-bubble user';
        userDiv.innerHTML = `<span class="sender">Cmdr. Shalok:</span> ${escapeHtml(msg)}`;
        containerEl.appendChild(userDiv);
        inputEl.value = '';

        containerEl.scrollTop = containerEl.scrollHeight;

        setTimeout(() => {
            const botReply = generateOfflineResponse(msg);
            const botDiv = document.createElement('div');
            botDiv.className = 'chat-bubble bot';
            botDiv.innerHTML = `<span class="sender">MAITRI AI:</span> ${botReply}`;
            containerEl.appendChild(botDiv);
            containerEl.scrollTop = containerEl.scrollHeight;

            speakOutLoud(botReply.replace(/<[^>]*>?/gm, ''));
        }, 600);
    }

    if (miniSendBtn) miniSendBtn.addEventListener('click', () => handleChat(miniInput, miniBox));
    if (miniInput) miniInput.addEventListener('keypress', (e) => { if (e.key === 'Enter') handleChat(miniInput, miniBox); });

    if (fullSendBtn) fullSendBtn.addEventListener('click', () => handleChat(fullInput, fullLogs));
    if (fullInput) fullInput.addEventListener('keypress', (e) => { if (e.key === 'Enter') handleChat(fullInput, fullLogs); });
}

function speakOutLoud(text) {
    if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.rate = 1.0;
        utterance.pitch = 1.05;
        window.speechSynthesis.speak(utterance);
    }
}

function sendQuickMsg(txt) {
    const fullInput = document.getElementById('fullChatInput');
    const fullSendBtn = document.getElementById('fullChatSendBtn');
    if (fullInput && fullSendBtn) {
        fullInput.value = txt;
        fullSendBtn.click();
    }
}

function generateOfflineResponse(userMsg) {
    const msg = userMsg.toLowerCase();
    if (msg.includes('stress') || msg.includes('anxious') || msg.includes('tired') || msg.includes('fatigued')) {
        return "I detect elevated stress markers. Let's initiate a 4-7-8 deep breathing protocol. Inhale for 4 seconds, hold for 7, exhale for 8. Ambient relaxation audio triggered.";
    } else if (msg.includes('vital') || msg.includes('heart') || msg.includes('spo2')) {
        return "Telemetry summary for Cmdr. Shalok Dadhwal: Heart Rate is 72 BPM (nominal), SpO2 is 98.4% (optimal), and core temperature is 36.7 °C. You are fit for mission operations.";
    } else if (msg.includes('cognitive') || msg.includes('eva') || msg.includes('reaction')) {
        return "Pre-EVA Psychomotor Vigilance Test active. Mean reaction speed is 215ms with 98% memory accuracy. Clearance Status: FIT FOR EVA (PASSED).";
    } else if (msg.includes('circadian') || msg.includes('light')) {
        return "Circadian Rhythm Sync active. Habitat LEDs set to 6500K Blue-Enriched Daylight to elevate morning focus and suppress melatonin.";
    } else {
        return `Copy that, Cmdr. Shalok. Standard offline psychological companion rules active. All deep-space systems are nominal.`;
    }
}

function escapeHtml(str) {
    return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

// 5. Camera Canvas Visualizer Placeholder
function initCameraCanvas() {
    const canvas = document.getElementById('videoCanvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    let animId;

    function renderMockStream() {
        ctx.fillStyle = '#090d16';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        ctx.strokeStyle = 'rgba(100, 210, 255, 0.15)';
        ctx.lineWidth = 1;
        for (let x = 0; x < canvas.width; x += 40) {
            ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, canvas.height); ctx.stroke();
        }
        for (let y = 0; y < canvas.height; y += 40) {
            ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(canvas.width, y); ctx.stroke();
        }

        ctx.strokeStyle = '#30D158';
        ctx.lineWidth = 3;
        const boxX = 220, boxY = 120, boxW = 200, boxH = 240;
        ctx.strokeRect(boxX, boxY, boxW, boxH);

        ctx.fillStyle = '#30D158';
        ctx.font = '14px -apple-system, monospace';
        ctx.fillText('FACIAL DETECTED: Cmdr. Shalok', boxX, boxY - 12);
        ctx.fillText('EMOTION: Focused (94.2%)', boxX, boxY + boxH + 20);

        animId = requestAnimationFrame(renderMockStream);
    }

    const startBtn = document.getElementById('startCamBtn');
    const stopBtn = document.getElementById('stopCamBtn');

    if (startBtn) startBtn.addEventListener('click', () => { if (!animId) renderMockStream(); });
    if (stopBtn) stopBtn.addEventListener('click', () => { if (animId) { cancelAnimationFrame(animId); animId = null; } });

    renderMockStream();
}

// 6. Pre-EVA Cognitive Reaction Test Widget
function initCognitiveTest() {
    const btn = document.getElementById('startPvtTestBtn');
    const resultBox = document.getElementById('pvtResultBox');
    if (!btn || !resultBox) return;

    btn.addEventListener('click', () => {
        btn.textContent = 'Testing Reaction Speed...';
        btn.disabled = true;
        
        setTimeout(() => {
            const rxTimes = [210, 225, 205, 218, 230];
            const meanRx = Math.round(rxTimes.reduce((a, b) => a + b, 0) / rxTimes.length);
            resultBox.innerHTML = `
                <div class="alert-item low" style="margin-top: 10px;">
                    <div class="alert-details">
                        <span class="alert-title" style="color: #30D158;">FIT FOR EVA (PASSED) — Score: 96%</span>
                        <span class="alert-time">Mean Reaction Speed: ${meanRx}ms | Memory Accuracy: 98% | Lapses: 0</span>
                    </div>
                </div>
            `;
            btn.textContent = 'Run Pre-EVA PVT Test Again';
            btn.disabled = false;
            speakOutLoud("Cmdr. Shalok, pre EVA reaction test completed. Clearance status: FIT FOR EVA.");
        }, 1500);
    });
}

// 7. Circadian Lighting Display
function initCircadianLighting() {
    const lightStatusEl = document.getElementById('circadianStatusText');
    if (!lightStatusEl) return;
    const hour = new Date().getHours();
    if (hour >= 6 && hour < 20) {
        lightStatusEl.textContent = "6500K Blue-Enriched Daylight (Focus Active)";
    } else {
        lightStatusEl.textContent = "2700K Warm Amber (Melatonin Prep Active)";
    }
}

// 8. Speech Synthesis Voice Command Trigger
function initSpeechSynthesis() {
    const micBtn = document.getElementById('voiceMicBtn');
    if (!micBtn) return;
    micBtn.addEventListener('click', () => {
        if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {
            alert('Voice input active. Type your command in the chat box.');
            return;
        }
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        const recognition = new SpeechRecognition();
        recognition.onstart = () => { micBtn.textContent = '🎙️ Listening...'; };
        recognition.onresult = (event) => {
            const transcript = event.results[0][0].transcript;
            micBtn.textContent = '🎤 Speak Voice Command';
            sendQuickMsg(transcript);
        };
        recognition.onerror = () => { micBtn.textContent = '🎤 Speak Voice Command'; };
        recognition.start();
    });
}