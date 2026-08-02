/**
 * MAITRI - Mission Control & Offline Assistant JavaScript Controller
 * Handles tab navigation, telemetry graphs, camera canvas mock, & chatbot dialogs.
 */

document.addEventListener('DOMContentLoaded', () => {
    initClock();
    initTabs();
    initCharts();
    initChatbot();
    initCameraCanvas();
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
    // Vitals Telemetry Trend Chart
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
                        borderColor: '#3b82f6',
                        backgroundColor: 'rgba(59, 130, 246, 0.1)',
                        borderWidth: 2,
                        tension: 0.4,
                        fill: true
                    },
                    {
                        label: 'SpO2 (%)',
                        data: [98, 98, 99, 98, 97, 98, 99, 98, 98.4],
                        borderColor: '#06b6d4',
                        borderWidth: 2,
                        tension: 0.4
                    },
                    {
                        label: 'Stress Index (0-100)',
                        data: [15, 20, 18, 35, 42, 28, 22, 20, 24],
                        borderColor: '#a855f7',
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
                    legend: { labels: { color: '#94a3b8' } }
                },
                scales: {
                    x: { ticks: { color: '#64748b' }, grid: { color: '#1e293b' } },
                    y: { ticks: { color: '#64748b' }, grid: { color: '#1e293b' } }
                }
            }
        });
    }

    // Emotion Pie Chart
    const ctxEmotion = document.getElementById('emotionPieChart');
    if (ctxEmotion && typeof Chart !== 'undefined') {
        emotionChart = new Chart(ctxEmotion, {
            type: 'doughnut',
            data: {
                labels: ['Focused', 'Calm', 'Elevated Stress', 'Fatigue'],
                datasets: [{
                    data: [60, 25, 10, 5],
                    backgroundColor: ['#10b981', '#06b6d4', '#f59e0b', '#8b5cf6'],
                    borderWidth: 0
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { position: 'bottom', labels: { color: '#94a3b8' } }
                }
            }
        });
    }

    // Sleep Quality Chart
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
                        backgroundColor: '#8b5cf6'
                    },
                    {
                        label: 'REM Sleep (hrs)',
                        data: [1.8, 1.5, 1.9, 1.6, 1.4, 2.0, 1.6],
                        backgroundColor: '#3b82f6'
                    },
                    {
                        label: 'Light Sleep (hrs)',
                        data: [3.3, 3.4, 3.6, 3.5, 3.6, 3.1, 3.5],
                        backgroundColor: '#334155'
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { labels: { color: '#94a3b8' } }
                },
                scales: {
                    x: { stacked: true, ticks: { color: '#64748b' } },
                    y: { stacked: true, ticks: { color: '#64748b' } }
                }
            }
        });
    }
}

// 4. Offline AI Chatbot Logic
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

        // Add Astronaut User Bubble
        const userDiv = document.createElement('div');
        userDiv.className = 'chat-bubble user';
        userDiv.innerHTML = `<span class="sender">Cmdr. Shalok:</span> ${escapeHtml(msg)}`;
        containerEl.appendChild(userDiv);
        inputEl.value = '';

        containerEl.scrollTop = containerEl.scrollHeight;

        // Generate Offline Bot Response
        setTimeout(() => {
            const botReply = generateOfflineResponse(msg);
            const botDiv = document.createElement('div');
            botDiv.className = 'chat-bubble bot';
            botDiv.innerHTML = `<span class="sender">MAITRI AI:</span> ${botReply}`;
            containerEl.appendChild(botDiv);
            containerEl.scrollTop = containerEl.scrollHeight;
        }, 600);
    }

    if (miniSendBtn) miniSendBtn.addEventListener('click', () => handleChat(miniInput, miniBox));
    if (miniInput) miniInput.addEventListener('keypress', (e) => { if (e.key === 'Enter') handleChat(miniInput, miniBox); });

    if (fullSendBtn) fullSendBtn.addEventListener('click', () => handleChat(fullInput, fullLogs));
    if (fullInput) fullInput.addEventListener('keypress', (e) => { if (e.key === 'Enter') handleChat(fullInput, fullLogs); });
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
        return "I detect elevated stress markers. Let's initiate a 4-7-8 deep breathing protocol. Inhale for 4 seconds, hold for 7, exhale for 8. I have also prepared an offline ambient audio session for you.";
    } else if (msg.includes('vital') || msg.includes('heart') || msg.includes('spo2')) {
        return "Telemetry summary for Cmdr. Shalok Dadhwal: Heart Rate is 72 BPM (nominal), SpO2 is 98.4% (optimal), and core temperature is 36.7 °C. You are fit for mission operations.";
    } else if (msg.includes('music') || msg.includes('song') || msg.includes('comedy')) {
        return "Accessing offline media vault... Found 14 ambient space tracks and 8 stand-up comedy audio files stored locally on edge storage.";
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
        ctx.fillStyle = '#0f172a';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        // Draw simulated Grid lines
        ctx.strokeStyle = 'rgba(56, 189, 248, 0.15)';
        ctx.lineWidth = 1;
        for (let x = 0; x < canvas.width; x += 40) {
            ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, canvas.height); ctx.stroke();
        }
        for (let y = 0; y < canvas.height; y += 40) {
            ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(canvas.width, y); ctx.stroke();
        }

        // Draw Bounding Box simulation
        ctx.strokeStyle = '#10b981';
        ctx.lineWidth = 3;
        const boxX = 220, boxY = 120, boxW = 200, boxH = 240;
        ctx.strokeRect(boxX, boxY, boxW, boxH);

        // Text Overlay
        ctx.fillStyle = '#10b981';
        ctx.font = '14px monospace';
        ctx.fillText('FACIAL DETECTED: Cmdr. Shalok', boxX, boxY - 12);
        ctx.fillText('EMOTION: Focused (94.2%)', boxX, boxY + boxH + 20);

        animId = requestAnimationFrame(renderMockStream);
    }

    const startBtn = document.getElementById('startCamBtn');
    const stopBtn = document.getElementById('stopCamBtn');

    if (startBtn) {
        startBtn.addEventListener('click', () => {
            if (!animId) renderMockStream();
        });
    }
    if (stopBtn) {
        stopBtn.addEventListener('click', () => {
            if (animId) {
                cancelAnimationFrame(animId);
                animId = null;
                ctx.fillStyle = '#020617';
                ctx.fillRect(0, 0, canvas.width, canvas.height);
            }
        });
    }

    renderMockStream();
}