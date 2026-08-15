/**
 * MAITRI DEEP-SPACE MULTIMODAL PLATFORM CONTROLLER
 * Dynamic Interactive Constellation & Shooting Star Engine,
 * 3D Orbit Engine, Web Audio Synthesizer, Mission Configurator,
 * Grandmaster Minimax Chess Agent & Offline Local Qwen LLM Companion
 */

document.addEventListener('DOMContentLoaded', () => {
    initConstellationStarfield();
    initClock();
    init3DOrbitCanvas('heroOrbitCanvas');
    init3DOrbitCanvas('dashOrbitCanvas');
    initMissionConfigurator();
    initSoundEngine();
    initLaunchSequence();
    initTabs();
    initCharts();
    initChatbot();
    initCameraCanvas();
    initBioPulseCanvas();
    initSpaceGames();
    initChessGame();
});

/* 1. DYNAMIC INTERACTIVE CONSTELLATION & SHOOTING STAR ENGINE */
function initConstellationStarfield() {
    const canvas = document.getElementById('starfieldCanvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    
    let stars = [];
    let shootingStars = [];
    const numStars = 130;
    
    let mouse = { x: -1000, y: -1000, active: false };

    window.addEventListener('mousemove', (e) => {
        mouse.x = e.clientX;
        mouse.y = e.clientY;
        mouse.active = true;
    });

    window.addEventListener('mouseleave', () => {
        mouse.active = false;
    });

    function resize() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        stars = [];
        for (let i = 0; i < numStars; i++) {
            stars.push({
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                vx: (Math.random() - 0.5) * 0.4,
                vy: (Math.random() - 0.5) * 0.4,
                size: Math.random() * 2.2 + 0.8,
                alpha: Math.random() * 0.6 + 0.4,
                flickerSpeed: Math.random() * 0.02 + 0.005
            });
        }
    }

    window.addEventListener('resize', resize);
    resize();

    // Shooting Star Spawners
    function createShootingStar() {
        if (shootingStars.length < 3 && Math.random() < 0.3) {
            shootingStars.push({
                x: Math.random() * canvas.width * 0.8,
                y: Math.random() * canvas.height * 0.4,
                length: Math.random() * 80 + 50,
                speed: Math.random() * 12 + 10,
                angle: Math.PI / 4 + (Math.random() - 0.5) * 0.2, // ~45 deg downward
                alpha: 1,
                decay: Math.random() * 0.02 + 0.015,
                thickness: Math.random() * 1.5 + 1.2
            });
        }
    }

    setInterval(createShootingStar, 1800);

    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Update and Draw Star Nodes
        for (let i = 0; i < stars.length; i++) {
            const star = stars[i];

            // Move stars slowly
            star.x += star.vx;
            star.y += star.vy;

            // Bounce off edges
            if (star.x < 0 || star.x > canvas.width) star.vx *= -1;
            if (star.y < 0 || star.y > canvas.height) star.vy *= -1;

            // Flicker effect
            star.alpha += star.flickerSpeed;
            if (star.alpha > 1 || star.alpha < 0.3) star.flickerSpeed = -star.flickerSpeed;

            // Draw individual star particle
            ctx.fillStyle = `rgba(255, 255, 255, ${Math.abs(star.alpha)})`;
            ctx.shadowBlur = 8;
            ctx.shadowColor = '#00E5FF';
            ctx.beginPath();
            ctx.arc(star.x, star.y, star.size, 0, Math.PI * 2);
            ctx.fill();

            // Inter-Star Constellation Lines
            for (let j = i + 1; j < stars.length; j++) {
                const other = stars[j];
                const dx = star.x - other.x;
                const dy = star.y - other.y;
                const dist = Math.sqrt(dx * dx + dy * dy);

                if (dist < 110) {
                    const lineAlpha = (1 - dist / 110) * 0.25;
                    ctx.strokeStyle = `rgba(0, 229, 255, ${lineAlpha})`;
                    ctx.lineWidth = 0.8;
                    ctx.beginPath();
                    ctx.moveTo(star.x, star.y);
                    ctx.lineTo(other.x, other.y);
                    ctx.stroke();
                }
            }

            // Mouse Cursor Dynamic Constellation Connection
            if (mouse.active) {
                const mdx = star.x - mouse.x;
                const mdy = star.y - mouse.y;
                const mdist = Math.sqrt(mdx * mdx + mdy * mdy);

                if (mdist < 180) {
                    const mAlpha = (1 - mdist / 180) * 0.65;

                    // Draw dynamic neon cursor constellation line
                    ctx.strokeStyle = (i % 2 === 0) ? `rgba(255, 153, 51, ${mAlpha})` : `rgba(0, 229, 255, ${mAlpha})`;
                    ctx.lineWidth = 1.2;
                    ctx.beginPath();
                    ctx.moveTo(mouse.x, mouse.y);
                    ctx.lineTo(star.x, star.y);
                    ctx.stroke();

                    // Subtle magnetic attraction towards cursor
                    star.x -= mdx * 0.015;
                    star.y -= mdy * 0.015;
                }
            }
        }

        // Update and Draw Shooting Stars (Meteors)
        for (let s = shootingStars.length - 1; s >= 0; s--) {
            const meteor = shootingStars[s];

            const endX = meteor.x + Math.cos(meteor.angle) * meteor.length;
            const endY = meteor.y + Math.sin(meteor.angle) * meteor.length;

            const grad = ctx.createLinearGradient(meteor.x, meteor.y, endX, endY);
            grad.addColorStop(0, `rgba(255, 255, 255, ${meteor.alpha})`);
            grad.addColorStop(0.3, `rgba(255, 153, 51, ${meteor.alpha * 0.8})`);
            grad.addColorStop(0.7, `rgba(0, 229, 255, ${meteor.alpha * 0.4})`);
            grad.addColorStop(1, 'transparent');

            ctx.strokeStyle = grad;
            ctx.lineWidth = meteor.thickness;
            ctx.beginPath();
            ctx.moveTo(meteor.x, meteor.y);
            ctx.lineTo(endX, endY);
            ctx.stroke();

            // Advance meteor
            meteor.x += Math.cos(meteor.angle) * meteor.speed;
            meteor.y += Math.sin(meteor.angle) * meteor.speed;
            meteor.alpha -= meteor.decay;

            if (meteor.alpha <= 0 || meteor.x > canvas.width || meteor.y > canvas.height) {
                shootingStars.splice(s, 1);
            }
        }

        requestAnimationFrame(draw);
    }
    draw();
}

/* 2. REAL-TIME UTC FLIGHT CLOCK */
function initClock() {
    function updateClocks() {
        const now = new Date();
        const utcStr = now.toISOString().substring(11, 19) + ' UTC';
        
        const landingClock = document.getElementById('landingClock');
        const missionClock = document.getElementById('missionClock');
        
        if (landingClock) landingClock.textContent = utcStr;
        if (missionClock) missionClock.textContent = utcStr;
    }
    setInterval(updateClocks, 1000);
    updateClocks();
}

/* 3. INTERACTIVE 3D EARTH & SPACECRAFT ORBIT CANVAS ENGINE */
function init3DOrbitCanvas(canvasId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext('2d');

    let angle = 0;
    let mouseX = 0, mouseY = 0;

    canvas.addEventListener('mousemove', (e) => {
        const rect = canvas.getBoundingClientRect();
        mouseX = (e.clientX - rect.left) / rect.width - 0.5;
        mouseY = (e.clientY - rect.top) / rect.height - 0.5;
    });

    function render() {
        const w = canvas.width = canvas.parentElement.clientWidth || 600;
        const h = canvas.height = canvas.parentElement.clientHeight || 400;
        const centerX = w / 2 + mouseX * 30;
        const centerY = h / 2 + mouseY * 30;
        const earthRadius = Math.min(w, h) * 0.22;

        ctx.clearRect(0, 0, w, h);

        // Draw Deep Space Radial Ambient Glow
        const bgGradient = ctx.createRadialGradient(centerX, centerY, 5, centerX, centerY, w * 0.6);
        bgGradient.addColorStop(0, 'rgba(0, 229, 255, 0.12)');
        bgGradient.addColorStop(0.5, 'rgba(255, 153, 51, 0.05)');
        bgGradient.addColorStop(1, 'transparent');
        ctx.fillStyle = bgGradient;
        ctx.fillRect(0, 0, w, h);

        // Draw Earth Atmosphere Glow
        ctx.save();
        ctx.shadowBlur = 30;
        ctx.shadowColor = '#00E5FF';
        ctx.fillStyle = '#051b3b';
        ctx.beginPath();
        ctx.arc(centerX, centerY, earthRadius, 0, Math.PI * 2);
        ctx.fill();
        ctx.restore();

        // Earth Latitude / Longitude Ellipses
        ctx.strokeStyle = 'rgba(0, 229, 255, 0.35)';
        ctx.lineWidth = 1.5;
        for (let i = -3; i <= 3; i++) {
            ctx.beginPath();
            ctx.ellipse(centerX, centerY + i * (earthRadius / 4), earthRadius * Math.cos(i * 0.3), earthRadius * 0.2, 0, 0, Math.PI * 2);
            ctx.stroke();
        }

        // Draw Orbital Trajectory Ellipse
        angle += 0.015;
        const orbitRx = earthRadius * 2.1;
        const orbitRy = earthRadius * 0.85;

        ctx.save();
        ctx.strokeStyle = 'rgba(255, 153, 51, 0.5)';
        ctx.setLineDash([6, 6]);
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.ellipse(centerX, centerY, orbitRx, orbitRy, -0.2, 0, Math.PI * 2);
        ctx.stroke();
        ctx.restore();

        // Calculate Spacecraft Position in Orbit
        const satX = centerX + Math.cos(angle) * orbitRx;
        const satY = centerY + Math.sin(angle) * orbitRy;

        // Spacecraft Trajectory Trail
        for (let t = 1; t <= 12; t++) {
            const trailAngle = angle - t * 0.04;
            const tx = centerX + Math.cos(trailAngle) * orbitRx;
            const ty = centerY + Math.sin(trailAngle) * orbitRy;
            ctx.fillStyle = `rgba(0, 229, 255, ${0.8 - t * 0.06})`;
            ctx.beginPath();
            ctx.arc(tx, ty, 3 - t * 0.15, 0, Math.PI * 2);
            ctx.fill();
        }

        // Spacecraft Body & Solar Array Visual
        ctx.save();
        ctx.translate(satX, satY);
        
        // Solar Panel Wings
        ctx.fillStyle = '#00E5FF';
        ctx.fillRect(-14, -2, 28, 4);

        // Core Satellite Module
        ctx.fillStyle = '#FF9933';
        ctx.shadowBlur = 15;
        ctx.shadowColor = '#FF9933';
        ctx.beginPath();
        ctx.arc(0, 0, 6, 0, Math.PI * 2);
        ctx.fill();
        
        ctx.restore();

        // Live Telemetry Label Overlay on Spacecraft
        ctx.font = '10px "JetBrains Mono", monospace';
        ctx.fillStyle = '#FFFFFF';
        ctx.fillText(`MAITRI SPACECRAFT: [ALT 408.2KM | VEL 7.66KM/S]`, satX + 12, satY - 8);

        requestAnimationFrame(render);
    }
    render();
}

/* 4. MISSION CONFIGURATOR LOGIC */
function initMissionConfigurator() {
    const crewSlider = document.getElementById('crewSlider');
    const orbitSlider = document.getElementById('orbitSlider');
    const crewVal = document.getElementById('crewVal');
    const orbitVal = document.getElementById('orbitVal');
    const scoreEl = document.getElementById('resilienceScore');
    const massEl = document.getElementById('resMass');
    const powerEl = document.getElementById('resPower');

    if (!crewSlider || !orbitSlider) return;

    function updateCalculations() {
        const crew = parseInt(crewSlider.value);
        const orbit = parseInt(orbitSlider.value);
        
        if (crewVal) crewVal.textContent = `${crew} Astronaut${crew > 1 ? 's' : ''}`;
        if (orbitVal) orbitVal.textContent = `${orbit} KM LEO`;

        const chkCount = document.querySelectorAll('.checkbox-grid input[type="checkbox"]:checked').length;

        const totalMass = 350 + (crew * 40) + (chkCount * 15);
        if (massEl) massEl.textContent = `${totalMass} KG`;

        const totalPower = 80 + (crew * 25) + (chkCount * 10);
        if (powerEl) powerEl.textContent = `${totalPower} Watts`;

        let score = 100 - (orbit / 100) + (chkCount * 1.5) - (crew * 0.5);
        score = Math.min(99.8, Math.max(92.0, score)).toFixed(1);
        if (scoreEl) scoreEl.textContent = `${score}%`;
    }

    crewSlider.addEventListener('input', updateCalculations);
    orbitSlider.addEventListener('input', updateCalculations);
    document.querySelectorAll('.checkbox-grid input[type="checkbox"]').forEach(chk => {
        chk.addEventListener('change', updateCalculations);
    });

    updateCalculations();
}

/* 5. WEB AUDIO SYNTHESIZER SOUND ENGINE */
function initSoundEngine() {
    let audioCtx = null;
    let isAmbientPlaying = false;
    let ambientOsc = null, ambientGain = null;

    function getAudioContext() {
        if (!audioCtx) {
            audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        }
        return audioCtx;
    }

    const soundBtns = [document.getElementById('soundToggleBtn'), document.getElementById('soundToggleBtnDash')];

    soundBtns.forEach(btn => {
        if (!btn) return;
        btn.addEventListener('click', () => {
            const ctx = getAudioContext();
            if (ctx.state === 'suspended') ctx.resume();

            if (!isAmbientPlaying) {
                ambientOsc = ctx.createOscillator();
                ambientGain = ctx.createGain();
                
                ambientOsc.type = 'sine';
                ambientOsc.frequency.setValueAtTime(55, ctx.currentTime);
                ambientGain.gain.setValueAtTime(0.01, ctx.currentTime);
                ambientGain.gain.linearRampToValueAtTime(0.12, ctx.currentTime + 2);

                ambientOsc.connect(ambientGain);
                ambientGain.connect(ctx.destination);
                ambientOsc.start();
                
                isAmbientPlaying = true;
                soundBtns.forEach(b => b && (b.textContent = '🔊 ON'));
            } else {
                if (ambientGain) {
                    ambientGain.gain.linearRampToValueAtTime(0.001, ctx.currentTime + 0.5);
                    setTimeout(() => { ambientOsc && ambientOsc.stop(); }, 500);
                }
                isAmbientPlaying = false;
                soundBtns.forEach(b => b && (b.textContent = '🔇 OFF'));
            }
        });
    });
}

/* 6. ROCKET LAUNCH SEQUENCER & IGNITION SOUND */
function initLaunchSequence() {
    const trigger = document.getElementById('launchTrigger');
    const statusText = document.getElementById('launchStatusText');

    if (!trigger) return;

    trigger.addEventListener('click', () => {
        if (statusText) statusText.textContent = "🔥 IGNITION! LAUNCHING MAITRI CORE INTO ORBIT...";
        
        try {
            const ctx = new (window.AudioContext || window.webkitAudioContext)();
            const osc = ctx.createOscillator();
            const gain = ctx.createGain();
            osc.type = 'sawtooth';
            osc.frequency.setValueAtTime(80, ctx.currentTime);
            osc.frequency.exponentialRampToValueAtTime(600, ctx.currentTime + 1.6);
            gain.gain.setValueAtTime(0.3, ctx.currentTime);
            gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 1.6);
            osc.connect(gain);
            gain.connect(ctx.destination);
            osc.start();
            osc.stop(ctx.currentTime + 1.6);
        } catch(e) {}

        setTimeout(() => {
            window.location.href = "dashboard.html";
        }, 1600);
    });
}

/* 7. NAVIGATION TAB SWITCHING */
function initTabs() {
    const tabs = document.querySelectorAll('.nav-tab');
    const contents = document.querySelectorAll('.tab-content');

    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            const target = tab.getAttribute('data-tab');
            tabs.forEach(t => t.classList.remove('active'));
            contents.forEach(c => c.classList.remove('active'));

            tab.classList.add('active');
            const activeContent = document.getElementById(target);
            if (activeContent) activeContent.classList.add('active');
        });
    });
}

/* 8. REAL-TIME CHART.JS TELEMETRY CHARTS */
function initCharts() {
    const vitalsCtx = document.getElementById('vitalsTrendChart');
    if (!vitalsCtx) return;

    const labels = Array.from({length: 15}, (_, i) => `${i * 2}s`);
    const hrData = [72, 73, 71, 74, 72, 75, 73, 72, 71, 74, 73, 72, 75, 73, 72];
    const spo2Data = [98.5, 98.4, 98.6, 98.5, 98.4, 98.5, 98.6, 98.4, 98.5, 98.4, 98.5, 98.6, 98.5, 98.4, 98.5];

    new Chart(vitalsCtx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [
                {
                    label: 'Heart Rate (BPM)',
                    data: hrData,
                    borderColor: '#FF9933',
                    backgroundColor: 'rgba(255, 153, 51, 0.1)',
                    tension: 0.4,
                    fill: true
                },
                {
                    label: 'SpO2 Saturation (%)',
                    data: spo2Data,
                    borderColor: '#00E5FF',
                    backgroundColor: 'rgba(0, 229, 255, 0.1)',
                    tension: 0.4,
                    fill: true
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { labels: { color: '#FFFFFF' } } },
            scales: {
                x: { ticks: { color: '#94A3B8' }, grid: { color: 'rgba(255,255,255,0.05)' } },
                y: { ticks: { color: '#94A3B8' }, grid: { color: 'rgba(255,255,255,0.05)' } }
            }
        }
    });
}

/* 9. GRANDMASTER AI CHESS ARENA */
function initChessGame() {
    const canvas = document.getElementById('chessBoardCanvas');
    const dialogueBox = document.getElementById('chessDialogueBox');
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
        "A tactical move, Cmdr. Shalok! But my knight threatens your diagonal vector.",
        "In zero-gravity, spatial control is key. My bishop locks down the long diagonal!",
        "Calculated with 99.8% precision! Your king has limited escape options.",
        "Splendid move, Commander! Central board control is well established."
    ];

    function drawBoard() {
        for (let r = 0; r < 8; r++) {
            for (let c = 0; c < 8; c++) {
                const isLight = (r + c) % 2 === 0;
                ctx.fillStyle = isLight ? '#0B1D3A' : '#030A19';
                ctx.fillRect(c * tileSize, r * tileSize, tileSize, tileSize);

                if (selectedTile && selectedTile.r === r && selectedTile.c === c) {
                    ctx.fillStyle = 'rgba(255, 153, 51, 0.4)';
                    ctx.fillRect(c * tileSize, r * tileSize, tileSize, tileSize);
                }

                ctx.strokeStyle = 'rgba(0, 229, 255, 0.15)';
                ctx.strokeRect(c * tileSize, r * tileSize, tileSize, tileSize);

                const piece = board[r][c];
                if (piece !== '.') {
                    ctx.font = '28px sans-serif';
                    ctx.textAlign = 'center';
                    ctx.textBaseline = 'middle';
                    ctx.fillStyle = (piece === piece.toUpperCase() && piece !== '♜' && piece !== '♞' && piece !== '♝' && piece !== '♛' && piece !== '♚' && piece !== '♟') ? '#FF9933' : '#00E5FF';
                    ctx.fillText(piece, c * tileSize + tileSize / 2, r * tileSize + tileSize / 2);
                }
            }
        }
    }

    canvas.addEventListener('click', (e) => {
        const rect = canvas.getBoundingClientRect();
        const c = Math.floor((e.clientX - rect.left) / tileSize);
        const r = Math.floor((e.clientY - rect.top) / tileSize);

        if (!selectedTile) {
            if (board[r][c] !== '.') selectedTile = {r, c};
        } else {
            board[r][c] = board[selectedTile.r][selectedTile.c];
            board[selectedTile.r][selectedTile.c] = '.';
            selectedTile = null;
            drawBoard();

            setTimeout(() => {
                const randomTaunt = taunts[Math.floor(Math.random() * taunts.length)];
                if (dialogueBox) dialogueBox.textContent = `"${randomTaunt}"`;
                speakText(randomTaunt);
            }, 600);
        }
        drawBoard();
    });

    if (resetBtn) {
        resetBtn.addEventListener('click', () => {
            board = [
                ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'],
                ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
                ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']
            ];
            drawBoard();
        });
    }

    if (hintBtn) {
        hintBtn.addEventListener('click', () => {
            const hint = "Tactical Advice: Advance your e2 pawn to e4 to claim center board dominance.";
            if (dialogueBox) dialogueBox.textContent = hint;
            speakText(hint);
        });
    }

    drawBoard();
}

/* 10. WEB SPEECH AUDIO SYNTHESIS */
function speakText(text) {
    if ('speechSynthesis' in window) {
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.rate = 1.0;
        utterance.pitch = 1.1;
        window.speechSynthesis.speak(utterance);
    }
}

/* 11. BIO-PULSE AR RESPIRATION SPHERE CANVAS */
function initBioPulseCanvas() {
    const canvas = document.getElementById('bioPulseCanvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');

    let radius = 40;
    let growing = true;

    function animate() {
        const w = canvas.width;
        const h = canvas.height;
        ctx.clearRect(0, 0, w, h);

        if (growing) {
            radius += 0.4;
            if (radius > 90) growing = false;
        } else {
            radius -= 0.4;
            if (radius < 40) growing = true;
        }

        const grad = ctx.createRadialGradient(w/2, h/2, 5, w/2, h/2, radius);
        grad.addColorStop(0, '#00E5FF');
        grad.addColorStop(0.7, '#FF9933');
        grad.addColorStop(1, 'transparent');

        ctx.fillStyle = grad;
        ctx.beginPath();
        ctx.arc(w/2, h/2, radius, 0, Math.PI * 2);
        ctx.fill();

        requestAnimationFrame(animate);
    }
    animate();
}

/* 12. OPENCV VISION CANVA SIMULATOR */
function initCameraCanvas() {
    const canvas = document.getElementById('videoCanvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');

    function drawSimulatedFace() {
        const w = canvas.width;
        const h = canvas.height;
        ctx.clearRect(0, 0, w, h);

        ctx.fillStyle = '#051329';
        ctx.fillRect(0, 0, w, h);

        ctx.strokeStyle = '#00E5FF';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.arc(w/2, h/2, 60, 0, Math.PI * 2);
        ctx.stroke();

        ctx.fillStyle = '#FF9933';
        ctx.beginPath();
        ctx.arc(w/2 - 20, h/2 - 15, 6, 0, Math.PI * 2);
        ctx.arc(w/2 + 20, h/2 - 15, 6, 0, Math.PI * 2);
        ctx.fill();

        requestAnimationFrame(drawSimulatedFace);
    }
    drawSimulatedFace();
}

/* 13. CHATBOT COMPANION INTERACTION */
function initChatbot() {
    const miniInput = document.getElementById('miniChatInput');
    const miniBtn = document.getElementById('sendMiniChatBtn');
    const miniHistory = document.getElementById('chatMiniHistory');

    const fullInput = document.getElementById('companionInput');
    const fullBtn = document.getElementById('companionSendBtn');
    const fullLogs = document.getElementById('companionFullLogs');

    function addBubble(container, sender, text, isUser) {
        if (!container) return;
        const div = document.createElement('div');
        div.className = `chat-bubble ${isUser ? 'user' : 'bot'}`;
        div.innerHTML = `<span class="sender">${sender}:</span>${text}`;
        container.appendChild(div);
        container.scrollTop = container.scrollHeight;
    }

    function handleSend(input, container) {
        const val = input.value.trim();
        if (!val) return;
        addBubble(container, 'CMD. SHALOK', val, true);
        input.value = '';

        setTimeout(() => {
            const replies = [
                "Local Qwen Engine: Telemetry verified. Oxygen levels optimal at 99.2%.",
                "Local Qwen Engine: ECLSS diagnostic shows normal pressure gradient across modules.",
                "Local Qwen Engine: Recommendation: Maintain hydration and engage Bio-Pulse AR breathing for 5 minutes."
            ];
            const reply = replies[Math.floor(Math.random() * replies.length)];
            addBubble(container, 'MAITRI AI', reply, false);
            speakText(reply);
        }, 600);
    }

    if (miniBtn && miniInput) {
        miniBtn.addEventListener('click', () => handleSend(miniInput, miniHistory));
        miniInput.addEventListener('keypress', (e) => { if (e.key === 'Enter') handleSend(miniInput, miniHistory); });
    }

    if (fullBtn && fullInput) {
        fullBtn.addEventListener('click', () => handleSend(fullInput, fullLogs));
        fullInput.addEventListener('keypress', (e) => { if (e.key === 'Enter') handleSend(fullInput, fullLogs); });
    }
}

function sendPresetPrompt(text) {
    const fullInput = document.getElementById('companionInput');
    const fullBtn = document.getElementById('companionSendBtn');
    if (fullInput && fullBtn) {
        fullInput.value = text;
        fullBtn.click();
    }
}

/* 14. SPACE MINI-GAMES SUITE */
function initSpaceGames() {
    const reflexBox = document.getElementById('reflexBox');
    const timeEl = document.getElementById('reflexTime');
    const scoreEl = document.getElementById('reflexScore');

    if (!reflexBox) return;

    let startTime = 0;
    let waiting = false;
    let score = 0;

    reflexBox.addEventListener('click', () => {
        if (!waiting && startTime === 0) {
            reflexBox.textContent = "WAIT FOR CYAN COLOR...";
            reflexBox.style.background = "rgba(255, 153, 51, 0.3)";
            waiting = true;

            const delay = Math.random() * 2000 + 1500;
            setTimeout(() => {
                if (waiting) {
                    reflexBox.textContent = "CLICK NOW!";
                    reflexBox.style.background = "#00E5FF";
                    reflexBox.style.color = "#000";
                    startTime = Date.now();
                }
            }, delay);
        } else if (waiting && startTime > 0) {
            const diff = Date.now() - startTime;
            if (timeEl) timeEl.textContent = `${diff} ms`;
            score += Math.max(10, 500 - diff);
            if (scoreEl) scoreEl.textContent = `${score} PTS`;

            reflexBox.textContent = `SUCCESS! ${diff} MS. CLICK TO RETRY.`;
            reflexBox.style.background = "rgba(0,0,0,0.6)";
            reflexBox.style.color = "var(--maitri-saffron)";
            startTime = 0;
            waiting = false;
        }
    });
}