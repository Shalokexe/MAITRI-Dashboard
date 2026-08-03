/**
 * ISRO GAGANYAAN MAITRI — EPIC 3-STAGE BOOT & MISSION CONTROL CONTROLLER
 * Stage 1: Pitch Black ASCII Art Terminal Typing
 * Stage 2: Animated Rocket Buffering Launch with Telemetry Progress
 * Stage 3: Unlock into ISRO Gaganyaan Mission Control Command Center
 */

document.addEventListener('DOMContentLoaded', () => {
    init3StageBoot();
    initStarfield();
    initClock();
    initTabs();
    initCharts();
    initChatbot();
    initCameraCanvas();
    initCognitiveTest();
    initCircadianLighting();
    initSpeechSynthesis();
});

// 1. EPIC 3-STAGE BOOT CONTROLLER
function init3StageBoot() {
    const bootOverlay = document.getElementById('epicBootOverlay');
    const stage1 = document.getElementById('bootStage1');
    const stage2 = document.getElementById('bootStage2');
    const asciiOutput = document.getElementById('asciiTerminalOutput');
    const rocketBar = document.getElementById('rocketProgressFill');
    const rocketText = document.getElementById('rocketTelemetryText');
    const skipBtn = document.getElementById('skipIntroBtn');

    if (!bootOverlay || !stage1 || !stage2) return;

    // Skip Intro Handler
    function skipIntro() {
        bootOverlay.classList.add('hidden');
    }
    if (skipBtn) skipBtn.addEventListener('click', skipIntro);

    const asciiLines = [
        "   ██████╗  █████╗  ██████╗  █████╗ ███╗   ██╗██╗   ██╗ █████╗  █████╗ ███╗   ██╗",
        "  ██╔════╝ ██╔══██╗██╔════╝ ██╔══██╗████╗  ██║╚██╗ ██╔╝██╔══██╗██╔══██╗████╗  ██║",
        "  ██║  ███╗███████║██║  ███╗███████║██╔██╗ ██║ ╚████╔╝ ███████║███████║██╔██╗ ██║",
        "  ██║   ██║██╔══██║██║   ██║██╔══██║██║╚██╗██║  ╚██╔╝  ██╔══██║██╔══██║██║╚██╗██║",
        "  ╚██████╔╝██║  ██║╚██████╔╝██║  ██║██║ ╚████║   ██║   ██║  ██║██║  ██║██║ ╚████║",
        "   ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝",
        "                [ ISRO AIR-GAPPED MAITRI MULTIMODAL AI CORE v1.0 ]"
    ];

    // STAGE 1: ASCII Art Typing Sequence
    let lineIdx = 0;
    const typeInterval = setInterval(() => {
        if (lineIdx < asciiLines.length) {
            asciiOutput.textContent += asciiLines[lineIdx] + "\n";
            lineIdx++;
        } else {
            clearInterval(typeInterval);
            // Transition to STAGE 2 after 1.2s
            setTimeout(startStage2, 1200);
        }
    }, 180);

    // STAGE 2: Rocket Launch Buffering Loader Sequence
    function startStage2() {
        stage1.classList.remove('active');
        stage2.classList.add('active');

        const telemetrySteps = [
            "IGNITION SEQUENCE START... LMV3 ROCKET FLIGHT NOMINAL",
            "CALCULATING ORBITAL INJECTION VELOCITY: 7.66 KM/S...",
            "LOADING OPENCV MULTIMODAL FACIAL VISION PIPELINE...",
            "AUTHENTICATING SQLITE AIR-GAPPED TELEMETRY DATABASE...",
            "VERIFYING PRE-EVA PSYCHOMOTOR VIGILANCE MODULES...",
            "ISRO MAITRI SYSTEMS 100% NOMINAL — UNLOCKING MISSION CONTROL"
        ];

        let progress = 0;
        let stepIdx = 0;

        const rocketInterval = setInterval(() => {
            progress += 2.5;
            if (rocketBar) rocketBar.style.width = progress + '%';

            if (progress % 16 === 0 && stepIdx < telemetrySteps.length) {
                if (rocketText) rocketText.textContent = telemetrySteps[stepIdx];
                stepIdx++;
            }

            if (progress >= 100) {
                clearInterval(rocketInterval);
                setTimeout(() => {
                    bootOverlay.classList.add('hidden');
                }, 500);
            }
        }, 40);
    }
}

// 2. Cosmic Starfield Background Canvas
function initStarfield() {
    const canvas = document.getElementById('starfieldCanvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    
    let stars = [];
    const numStars = 120;

    function resize() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        stars = [];
        for (let i = 0; i < numStars; i++) {
            stars.push({
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                size: Math.random() * 2 + 0.5,
                alpha: Math.random(),
                speed: Math.random() * 0.02 + 0.005
            });
        }
    }

    window.addEventListener('resize', resize);
    resize();

    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        stars.forEach(star => {
            star.alpha += star.speed;
            if (star.alpha > 1 || star.alpha < 0.2) star.speed = -star.speed;

            ctx.fillStyle = `rgba(255, 255, 255, ${Math.abs(star.alpha)})`;
            ctx.beginPath();
            ctx.arc(star.x, star.y, star.size, 0, Math.PI * 2);
            ctx.fill();
        });
        requestAnimationFrame(draw);
    }
    draw();
}

// 3. Mission UTC Clock
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

// 4. Navigation Tabs
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

// 5. Telemetry Graphs (Chart.js with ISRO Palette)
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
                        borderColor: '#FF9933',
                        backgroundColor: 'rgba(255, 153, 51, 0.15)',
                        borderWidth: 3,
                        tension: 0.4,
                        fill: true
                    },
                    {
                        label: 'SpO2 (%)',
                        data: [98, 98, 99, 98, 97, 98, 99, 98, 98.4],
                        borderColor: '#00E5FF',
                        borderWidth: 2,
                        tension: 0.4
                    },
                    {
                        label: 'Stress Index (0-100)',
                        data: [15, 20, 18, 35, 42, 28, 22, 20, 24],
                        borderColor: '#FFD700',
                        borderWidth: 2,
                        borderDash: [4, 4],
                        tension: 0.4
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { labels: { color: '#94A3B8', font: { family: '-apple-system', weight: 'bold' } } }
                },
                scales: {
                    x: { ticks: { color: '#94A3B8' }, grid: { color: 'rgba(255,255,255,0.06)' } },
                    y: { ticks: { color: '#94A3B8' }, grid: { color: 'rgba(255,255,255,0.06)' } }
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
                    backgroundColor: ['#00E676', '#00E5FF', '#FF9933', '#FFD700'],
                    borderWidth: 0
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { position: 'bottom', labels: { color: '#94A3B8' } }
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
                        backgroundColor: '#FF9933'
                    },
                    {
                        label: 'REM Sleep (hrs)',
                        data: [1.8, 1.5, 1.9, 1.6, 1.4, 2.0, 1.6],
                        backgroundColor: '#00E5FF'
                    },
                    {
                        label: 'Light Sleep (hrs)',
                        data: [3.3, 3.4, 3.6, 3.5, 3.6, 3.1, 3.5],
                        backgroundColor: '#1E293B'
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { labels: { color: '#94A3B8' } }
                },
                scales: {
                    x: { stacked: true, ticks: { color: '#94A3B8' } },
                    y: { stacked: true, ticks: { color: '#94A3B8' } }
                }
            }
        });
    }
}

// 6. Offline AI Chatbot Logic & Voice Speech Synthesis Out-Loud
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
            botDiv.innerHTML = `<span class="sender">ISRO MAITRI AI:</span> ${botReply}`;
            containerEl.appendChild(botDiv);
            containerEl.scrollTop = containerEl.scrollHeight;

            speakOutLoud(botReply.replace(/<[^>]*>?/gm, ''));
        }, 500);
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
        return "ISRO Gaganyaan protocol active: Elevated stress detected. Initiating 4-7-8 deep breathing relaxation cycle. Ambient acoustic music triggered.";
    } else if (msg.includes('vital') || msg.includes('heart') || msg.includes('spo2')) {
        return "Telemetry summary for Cmdr. Shalok Dadhwal: Heart Rate is 72 BPM (nominal), SpO2 is 98.4% (optimal), and core temperature is 36.7 °C. You are cleared for flight duties.";
    } else if (msg.includes('cognitive') || msg.includes('eva') || msg.includes('reaction')) {
        return "Pre-EVA Psychomotor Vigilance Test active. Mean reaction speed is 215ms with 98% memory accuracy. Clearance Status: FIT FOR EVA (PASSED).";
    } else if (msg.includes('circadian') || msg.includes('light')) {
        return "Circadian Rhythm Sync active. Habitat LEDs set to 6500K Blue-Enriched Daylight to elevate morning focus and suppress melatonin.";
    } else {
        return `Copy that, Cmdr. Shalok. ISRO Gaganyaan offline AI rules active. All orbital deep-space systems remain nominal.`;
    }
}

function escapeHtml(str) {
    return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

// 7. OpenCV Camera Stream HUD Canvas
function initCameraCanvas() {
    const canvas = document.getElementById('videoCanvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    let animId;
    let angle = 0;

    function renderMockStream() {
        ctx.fillStyle = '#030816';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        // Radar grid scan lines
        ctx.strokeStyle = 'rgba(0, 229, 255, 0.15)';
        ctx.lineWidth = 1;
        for (let x = 0; x < canvas.width; x += 40) {
            ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, canvas.height); ctx.stroke();
        }
        for (let y = 0; y < canvas.height; y += 40) {
            ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(canvas.width, y); ctx.stroke();
        }

        // Radar Scanner Line Animation
        angle += 0.03;
        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2;
        ctx.strokeStyle = 'rgba(255, 153, 51, 0.4)';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(centerX, centerY);
        ctx.lineTo(centerX + Math.cos(angle) * 220, centerY + Math.sin(angle) * 220);
        ctx.stroke();

        // Bounding box for facial tracking
        ctx.strokeStyle = '#00E676';
        ctx.lineWidth = 3;
        const boxX = 220, boxY = 120, boxW = 200, boxH = 240;
        ctx.strokeRect(boxX, boxY, boxW, boxH);

        ctx.fillStyle = '#00E676';
        ctx.font = '800 13px -apple-system, monospace';
        ctx.fillText('ISRO FACIAL DETECTED: Cmdr. Shalok', boxX, boxY - 12);
        ctx.fillText('EMOTION: Focused (94.2%)', boxX, boxY + boxH + 20);

        animId = requestAnimationFrame(renderMockStream);
    }

    const startBtn = document.getElementById('startCamBtn');
    const stopBtn = document.getElementById('stopCamBtn');

    if (startBtn) startBtn.addEventListener('click', () => { if (!animId) renderMockStream(); });
    if (stopBtn) stopBtn.addEventListener('click', () => { if (animId) { cancelAnimationFrame(animId); animId = null; } });

    renderMockStream();
}

// 8. Pre-EVA PVT Test Widget
function initCognitiveTest() {
    const btn = document.getElementById('startPvtTestBtn');
    const resultBox = document.getElementById('pvtResultBox');
    if (!btn || !resultBox) return;

    btn.addEventListener('click', () => {
        btn.textContent = 'Testing Psychomotor Reaction Speed...';
        btn.disabled = true;
        
        setTimeout(() => {
            const rxTimes = [210, 225, 205, 218, 230];
            const meanRx = Math.round(rxTimes.reduce((a, b) => a + b, 0) / rxTimes.length);
            resultBox.innerHTML = `
                <div class="alert-item low" style="margin-top: 10px;">
                    <div class="alert-details">
                        <span class="alert-title" style="color: #00E676;">FIT FOR EVA (PASSED) — Score: 96%</span>
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

// 9. Circadian Lighting Status
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

// 10. Voice Speech Recognition Trigger
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
