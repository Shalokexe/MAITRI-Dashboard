/**
 * ISRO GAGANYAAN MAITRI — EPIC 3-STAGE BOOT & MISSION CONTROL CONTROLLER
 * Phase 11: ISRO Grandmaster AI Chess Arena with Spoken Taunts & Hints
 */

document.addEventListener('DOMContentLoaded', () => {
    initStarfield();
    initClock();
    initTabs();
    initCharts();
    initChatbot();
    initCameraCanvas();
    initCognitiveTest();
    initCircadianLighting();
    initSpeechSynthesis();
    initBioPulseCanvas();
    initSpaceGames();
    initChessGame();
});

// 1. Cosmic Starfield Background Canvas
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

// 2. PHASE 11: ISRO GRANDMASTER AI CHESS ARENA
function initChessGame() {
    const canvas = document.getElementById('chessBoardCanvas');
    const dialogueBox = document.getElementById('chessDialogueBox');
    const evalEl = document.getElementById('chessEvalScore');
    const resetBtn = document.getElementById('resetChessBtn');
    const hintBtn = document.getElementById('chessHintBtn');

    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const tileSize = canvas.width / 8;

    let board = [
        ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'],
        ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
        ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']
    ];

    let selectedTile = null;

    const taunts = [
        "A bold move, Cmdr. Shalok, but my knight fork threatens your rook!",
        "In zero-gravity, spatial vision is key. Notice how my bishop controls the long diagonal?",
        "Calculated with 99.8% precision! Your queen has limited escape vectors.",
        "Fascinating tactic, Commander! Ground control taught me to watch for back-rank mates."
    ];

    const hints = [
        "Tactical Advice: Your king is exposed on the e-file. Recommend castling kingside.",
        "Opportunity: Seize the central d-file with your rook for spatial dominance.",
        "Defensive Note: Protect your c3 knight before launching a kingside assault."
    ];

    function drawBoard() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        for (let r = 0; r < 8; r++) {
            for (let c = 0; c < 8; c++) {
                const isDark = (r + c) % 2 === 1;
                ctx.fillStyle = isDark ? '#07132B' : '#0B1D3A';
                ctx.fillRect(c * tileSize, r * tileSize, tileSize, tileSize);

                ctx.strokeStyle = 'rgba(0, 229, 255, 0.15)';
                ctx.strokeRect(c * tileSize, r * tileSize, tileSize, tileSize);

                if (selectedTile && selectedTile.r === r && selectedTile.c === c) {
                    ctx.fillStyle = 'rgba(255, 153, 51, 0.35)';
                    ctx.fillRect(c * tileSize, r * tileSize, tileSize, tileSize);
                }

                const piece = board[r][c];
                if (piece !== '.') {
                    ctx.font = '28px "SF Pro Display", sans-serif';
                    ctx.fillStyle = (r > 4 || piece === '♙' || piece === '♖' || piece === '♘' || piece === '♗' || piece === '♕' || piece === '♔') ? '#FF9933' : '#00E5FF';
                    ctx.textAlign = 'center';
                    ctx.textBaseline = 'middle';
                    ctx.fillText(piece, c * tileSize + tileSize / 2, r * tileSize + tileSize / 2);
                }
            }
        }
    }

    canvas.addEventListener('click', (e) => {
        const rect = canvas.getBoundingClientRect();
        const col = Math.floor((e.clientX - rect.left) / tileSize);
        const row = Math.floor((e.clientY - rect.top) / tileSize);

        if (!selectedTile) {
            if (board[row][col] !== '.') {
                selectedTile = { r: row, c: col };
            }
        } else {
            // Move Astronaut piece
            board[row][col] = board[selectedTile.r][selectedTile.c];
            board[selectedTile.r][selectedTile.c] = '.';
            selectedTile = null;
            drawBoard();

            // Trigger Agent Move & Spoken Taunt
            setTimeout(makeAgentMove, 600);
        }
        drawBoard();
    });

    function makeAgentMove() {
        // MAITRI AI Move
        const randomTaunt = taunts[Math.floor(Math.random() * taunts.length)];
        
        if (dialogueBox) {
            const tauntDiv = document.createElement('div');
            tauntDiv.className = 'chat-bubble bot';
            tauntDiv.innerHTML = `<span class="sender">ISRO MAITRI AI (Grandmaster Agent):</span> ${randomTaunt}`;
            dialogueBox.appendChild(tauntDiv);
            dialogueBox.scrollTop = dialogueBox.scrollHeight;
        }

        if (evalEl) evalEl.textContent = '+0.85 (White Advantage)';
        speakOutLoud(randomTaunt);
    }

    if (hintBtn) {
        hintBtn.addEventListener('click', () => {
            const randomHint = hints[Math.floor(Math.random() * hints.length)];
            if (dialogueBox) {
                const hintDiv = document.createElement('div');
                hintDiv.className = 'chat-bubble bot';
                hintDiv.style.borderColor = 'var(--isro-saffron)';
                hintDiv.innerHTML = `<span class="sender">MAITRI Tactical Hint:</span> ${randomHint}`;
                dialogueBox.appendChild(hintDiv);
                dialogueBox.scrollTop = dialogueBox.scrollHeight;
            }
            speakOutLoud(randomHint);
        });
    }

    if (resetBtn) {
        resetBtn.addEventListener('click', () => {
            selectedTile = null;
            drawBoard();
        });
    }

    drawBoard();
}

// 3. PHASE 10: SPACE MINI-GAMES SUITE
function initSpaceGames() {
    const reflexCanvas = document.getElementById('reflexGameCanvas');
    const reflexScoreEl = document.getElementById('reflexScore');
    const startReflexBtn = document.getElementById('startReflexGameBtn');

    if (reflexCanvas) {
        const ctx = reflexCanvas.getContext('2d');
        let score = 0;
        let isGameRunning = false;
        let targetX = 200, targetY = 130, targetRadius = 25;
        let spawnTime = Date.now();

        function spawnTarget() {
            targetX = Math.random() * (reflexCanvas.width - 80) + 40;
            targetY = Math.random() * (reflexCanvas.height - 80) + 40;
            spawnTime = Date.now();
        }

        function drawReflex() {
            ctx.fillStyle = '#010614';
            ctx.fillRect(0, 0, reflexCanvas.width, reflexCanvas.height);

            if (isGameRunning) {
                ctx.fillStyle = '#FF9933';
                ctx.shadowColor = '#00E5FF';
                ctx.shadowBlur = 20;
                ctx.beginPath();
                ctx.arc(targetX, targetY, targetRadius, 0, Math.PI * 2);
                ctx.fill();
                ctx.shadowBlur = 0;

                ctx.fillStyle = '#FFFFFF';
                ctx.font = '900 11px -apple-system, monospace';
                ctx.fillText('TARGET', targetX - 22, targetY + 4);
                requestAnimationFrame(drawReflex);
            } else {
                ctx.fillStyle = '#94A3B8';
                ctx.font = '800 14px -apple-system, sans-serif';
                ctx.fillText('CLICK "START REFLEX GAME" TO TEST ZERO-G REACTION SPEED', 30, reflexCanvas.height / 2);
            }
        }

        reflexCanvas.addEventListener('click', (e) => {
            if (!isGameRunning) return;
            const rect = reflexCanvas.getBoundingClientRect();
            const clickX = e.clientX - rect.left;
            const clickY = e.clientY - rect.top;

            const dist = Math.hypot(clickX - targetX, clickY - targetY);
            if (dist <= targetRadius) {
                const rxTime = Date.now() - spawnTime;
                score += 100;
                if (reflexScoreEl) reflexScoreEl.textContent = `Score: ${score} (${rxTime}ms)`;
                spawnTarget();
            }
        });

        if (startReflexBtn) {
            startReflexBtn.addEventListener('click', () => {
                score = 0;
                isGameRunning = true;
                if (reflexScoreEl) reflexScoreEl.textContent = 'Score: 0';
                spawnTarget();
                drawReflex();
            });
        }
        drawReflex();
    }

    const dockCanvas = document.getElementById('dockingGameCanvas');
    const dockStatusEl = document.getElementById('dockingStatus');
    const startDockBtn = document.getElementById('startDockingGameBtn');

    if (dockCanvas) {
        const ctx = dockCanvas.getContext('2d');
        let isDocking = false;
        let shuttleX = 60, shuttleY = 130;
        let distance = 100;

        function drawDocking() {
            ctx.fillStyle = '#010614';
            ctx.fillRect(0, 0, dockCanvas.width, dockCanvas.height);

            const ringX = 400, ringY = 130;
            ctx.strokeStyle = '#00E5FF';
            ctx.lineWidth = 4;
            ctx.beginPath();
            ctx.arc(ringX, ringY, 35, 0, Math.PI * 2);
            ctx.stroke();

            ctx.fillStyle = '#FF9933';
            ctx.beginPath();
            ctx.arc(shuttleX, shuttleY, 15, 0, Math.PI * 2);
            ctx.fill();

            if (isDocking) {
                shuttleX += 1.5;
                distance = Math.max(0, Math.round(100 - (shuttleX / ringX) * 100));
                if (dockStatusEl) dockStatusEl.textContent = `Distance: ${distance}m`;

                if (shuttleX >= ringX - 10) {
                    isDocking = false;
                    if (dockStatusEl) dockStatusEl.textContent = 'STATUS: DOCKED SUCCESSFULLY!';
                    speakOutLoud("Gaganyaan shuttle docked successfully with orbital space station.");
                } else {
                    requestAnimationFrame(drawDocking);
                }
            } else {
                ctx.fillStyle = '#94A3B8';
                ctx.font = '800 13px -apple-system, sans-serif';
                ctx.fillText('CLICK "START DOCKING SIM" TO COMMENCE THRUSTER APPROACH', 20, 30);
            }
        }

        if (startDockBtn) {
            startDockBtn.addEventListener('click', () => {
                shuttleX = 60;
                shuttleY = 130;
                isDocking = true;
                drawDocking();
            });
        }
        drawDocking();
    }
}

// 4. PHASE 8: BIO-PULSE AR RESPIRED COHERENCE SPHERE CANVAS
function initBioPulseCanvas() {
    const canvas = document.getElementById('bioPulseCanvas');
    const phaseText = document.getElementById('breathingPhaseText');
    const start478 = document.getElementById('start478Btn');
    const startBox = document.getElementById('startBoxBtn');
    const stopBio = document.getElementById('stopBioBtn');

    if (!canvas) return;
    const ctx = canvas.getContext('2d');

    let isRunning = false;
    let currentRadius = 50;
    let targetRadius = 50;

    function drawSphere() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2;

        currentRadius += (targetRadius - currentRadius) * 0.05;

        const grad = ctx.createRadialGradient(centerX, centerY, currentRadius * 0.2, centerX, centerY, currentRadius * 1.5);
        grad.addColorStop(0, 'rgba(255, 153, 51, 0.8)');
        grad.addColorStop(0.5, 'rgba(0, 229, 255, 0.4)');
        grad.addColorStop(1, 'rgba(0, 0, 0, 0)');

        ctx.fillStyle = grad;
        ctx.beginPath();
        ctx.arc(centerX, centerY, currentRadius * 1.5, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = '#FF9933';
        ctx.shadowColor = '#00E5FF';
        ctx.shadowBlur = 25;
        ctx.beginPath();
        ctx.arc(centerX, centerY, currentRadius, 0, Math.PI * 2);
        ctx.fill();
        ctx.shadowBlur = 0;

        if (isRunning) {
            requestAnimationFrame(drawSphere);
        }
    }

    function runBreathingSequence(technique) {
        isRunning = true;
        drawSphere();

        if (technique === '4-7-8') {
            executePhase("INHALING DEEPLY (4s)...", 110, 4000, () => {
                executePhase("HOLDING BREATH (7s)...", 110, 7000, () => {
                    executePhase("EXHALING SLOWLY (8s)...", 40, 8000, () => {
                        if (isRunning) runBreathingSequence('4-7-8');
                    });
                });
            });
        } else {
            executePhase("INHALING (4s)...", 110, 4000, () => {
                executePhase("HOLDING (4s)...", 110, 4000, () => {
                    executePhase("EXHALING (4s)...", 40, 4000, () => {
                        executePhase("HOLDING (4s)...", 40, 4000, () => {
                            if (isRunning) runBreathingSequence('box');
                        });
                    });
                });
            });
        }
    }

    function executePhase(label, radius, durationMs, nextCb) {
        if (!isRunning) return;
        if (phaseText) phaseText.textContent = label;
        targetRadius = radius;
        speakOutLoud(label);

        setTimeout(() => {
            if (isRunning) nextCb();
        }, durationMs);
    }

    if (start478) start478.addEventListener('click', () => { isRunning = false; setTimeout(() => runBreathingSequence('4-7-8'), 200); });
    if (startBox) startBox.addEventListener('click', () => { isRunning = false; setTimeout(() => runBreathingSequence('box'), 200); });
    if (stopBio) stopBio.addEventListener('click', () => { isRunning = false; targetRadius = 50; if (phaseText) phaseText.textContent = "COACH PAUSED"; });

    drawSphere();
}

// 5. Mission UTC Clock
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

// 6. Navigation Tabs
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

// 7. Telemetry Graphs (Chart.js with ISRO Palette)
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

// 8. Offline AI Chatbot Logic & Voice Speech Synthesis Out-Loud
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
        return "ISRO Gaganyaan protocol active: Elevated stress detected. Initiating 4-7-8 Bio-Pulse AR breathing cycle and Space Reaction Reflex Challenge.";
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

// 9. OpenCV Camera Stream HUD Canvas
function initCameraCanvas() {
    const canvas = document.getElementById('videoCanvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    let animId;
    let angle = 0;

    function renderMockStream() {
        ctx.fillStyle = '#030816';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        ctx.strokeStyle = 'rgba(0, 229, 255, 0.15)';
        ctx.lineWidth = 1;
        for (let x = 0; x < canvas.width; x += 40) {
            ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, canvas.height); ctx.stroke();
        }
        for (let y = 0; y < canvas.height; y += 40) {
            ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(canvas.width, y); ctx.stroke();
        }

        angle += 0.03;
        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2;
        ctx.strokeStyle = 'rgba(255, 153, 51, 0.4)';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(centerX, centerY);
        ctx.lineTo(centerX + Math.cos(angle) * 220, centerY + Math.sin(angle) * 220);
        ctx.stroke();

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

// 10. Pre-EVA PVT Test Widget
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

// 11. Circadian Lighting Status
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

// 12. Voice Speech Recognition Trigger
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
