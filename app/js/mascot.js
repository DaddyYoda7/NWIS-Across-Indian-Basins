/**
 * NWIS Interactive AI Mascot Component
 * Features:
 * - Positioned at bottom-right corner (compact, elegant size)
 * - Completely transparent background (no circle wrapper or black background)
 * - Large cute chubby cat silhouette matching reference with bottom purple ambient glow
 * - Cute compact glowing white oval eyes
 * - Instant zero-lag real-time cursor tracking (60fps rAF)
 * - 3-second synchronized blink cycle
 * - Interactive random thought bubble that displays engaging prompts every 7 seconds
 * - Floating interactive widget navigates to NWIS AI chatbot on click
 */

(function() {
  // SVG Template generator for the Mascot
  function createMascotSVG(idPrefix = 'mascot', size = 36) {
    return `
      <svg id="${idPrefix}-svg" class="mascot-interactive-svg select-none cursor-pointer filter drop-shadow-[0_4px_10px_rgba(0,0,0,0.22)] transition-transform hover:scale-108 active:scale-95" width="${size}" height="${size}" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <!-- Deep Dark Mascot Gradient with Purple Ambient Bottom Glow -->
          <linearGradient id="${idPrefix}-body-grad" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#0a0812" />
            <stop offset="60%" stop-color="#100d1c" />
            <stop offset="85%" stop-color="#2d1c52" />
            <stop offset="100%" stop-color="#583794" />
          </linearGradient>
          <!-- Eye Glow Filter -->
          <filter id="${idPrefix}-glow" x="-30%" y="-30%" width="160%" height="160%">
            <feGaussianBlur stdDeviation="1.0" result="blur" />
            <feMerge>
              <feMergeNode in="blur" />
              <feMergeNode in="SourceGraphic" />
            </feMerge>
          </filter>
        </defs>

        <!-- Prominent Cute Chubby Cat Mascot Body (Transparent Background) -->
        <path d="M 22,6 
                 C 26,6 31,12 36,18 
                 C 42,24 46,26 50,26 
                 C 54,26 58,24 64,18 
                 C 69,12 74,6 78,6 
                 C 82,6 87,14 90,26 
                 C 96,48 96,74 92,86 
                 C 86,97 70,98 50,98 
                 C 30,98 14,97 8,86 
                 C 4,74 4,48 10,26 
                 C 13,14 18,6 22,6 Z" 
              fill="url(#${idPrefix}-body-grad)" 
              stroke="#43316d" 
              stroke-width="1.0" 
        />

        <!-- Subtle ambient bottom highlight curve -->
        <path d="M 20,86 C 32,94 68,94 80,86" stroke="#714bbd" stroke-width="1.5" stroke-linecap="round" fill="none" opacity="0.45"/>

        <!-- Eye Group for Blinking -->
        <g id="${idPrefix}-eyes-container" class="mascot-eyes-group" style="transform-origin: 50px 58px; transition: transform 0.08s cubic-bezier(0.4, 0, 0.2, 1);">
          <!-- Left Cute Small White Oval Eye -->
          <g id="${idPrefix}-left-eye-track" class="mascot-eye-track" style="will-change: transform;">
            <ellipse cx="34" cy="57" rx="6.5" ry="11" fill="#ffffff" filter="url(#${idPrefix}-glow)" transform="rotate(-8 34 57)"/>
          </g>

          <!-- Right Cute Small White Oval Eye -->
          <g id="${idPrefix}-right-eye-track" class="mascot-eye-track" style="will-change: transform;">
            <ellipse cx="66" cy="57" rx="6.5" ry="11" fill="#ffffff" filter="url(#${idPrefix}-glow)" transform="rotate(8 66 57)"/>
          </g>
        </g>
      </svg>
    `;
  }

  // Interactive Questions & Prompts Pool (Clean icon + question pairs)
  const INTERACTIVE_PROMPTS = [
    { icon: "💡", text: "Need help analyzing Nahorkatiya NHK-01 mud loss?" },
    { icon: "⚡", text: "Want to inspect live geomechanics telemetry?" },
    { icon: "🔍", text: "Shall we explore Assam-Arakan basin stratigraphy?" },
    { icon: "💭", text: "Did you know Digboi Well No. 1 was spudded in 1889?" },
    { icon: "📊", text: "Want me to summarize latest PPAC petroleum stats?" },
    { icon: "🤖", text: "Have a question about the platform or general AI help?" },
    { icon: "🎯", text: "Want to run a kick simulation in Scenario Lab?" },
    { icon: "✨", text: "Hi! How can I assist your subsurface exploration today?" }
  ];

  // Inject Global Floating Mascot into DOM in Bottom-Right Corner
  function initGlobalFloatingMascot() {
    const existing = document.getElementById('nwis-floating-mascot-container');
    if (existing) {
      existing.remove();
    }

    const container = document.createElement('div');
    container.id = 'nwis-floating-mascot-container';
    container.className = 'fixed bottom-4 right-4 z-50 flex flex-col items-end select-none transition-all duration-300 bg-transparent';
    container.style.cursor = 'pointer';
    container.title = 'Chat with NWIS AI Assistant';

    container.innerHTML = `
      <!-- Elegant Thought Bubble (Properly aligned with icon & spacing, 3s show / 15s break) -->
      <div id="mascot-thought-bubble" class="mb-2.5 max-w-[260px] sm:max-w-[280px] p-3 rounded-2xl bg-white/95 backdrop-blur-xl border border-reflection/80 text-astral shadow-[0_10px_25px_rgba(32,56,72,0.12)] opacity-0 translate-y-2 pointer-events-auto transition-all duration-400 flex items-start space-x-2.5 relative group hover:border-astral/40 hover:shadow-md">
        <span id="mascot-thought-icon" class="text-base shrink-0 select-none">✨</span>
        <div class="flex-1 pr-1">
          <p id="mascot-thought-text" class="text-[12px] font-medium leading-snug text-astral tracking-tight select-none">
            Hi! How can I assist your subsurface analysis today?
          </p>
        </div>
        <!-- Tail pointing to top-right of mascot -->
        <div class="absolute -bottom-1.5 right-4 w-3.5 h-3.5 bg-white/95 border-r border-b border-reflection/80 rotate-45 pointer-events-none"></div>
      </div>

      <div class="relative flex items-center bg-transparent">
        <!-- Interactive Mascot SVG (Compact 44px, transparent background) -->
        <div id="global-mascot-mount" class="relative bg-transparent flex items-center justify-center">
          ${createMascotSVG('global-mascot', 44)}
        </div>
      </div>
    `;

    // Click handler on bubble or mascot to open NWIS AI Chatbot view
    container.addEventListener('click', (e) => {
      const bubble = e.target.closest('#mascot-thought-bubble');
      const textEl = document.getElementById('mascot-thought-text');
      const questionText = textEl ? textEl.textContent.trim() : '';

      if (window.location.hash !== '#nwis-ai') {
        window.location.hash = '#nwis-ai';
      }

      if (bubble && questionText && window.populateAndAskAI) {
        setTimeout(() => {
          window.populateAndAskAI(questionText);
        }, 200);
      }
    });

    document.body.appendChild(container);
  }

  // Thought Bubble Engine: 3 Seconds Visible -> 15 Seconds Break Cycle
  let thoughtIndex = 0;
  let thoughtTimer = null;

  function startThoughtCycle() {
    if (thoughtTimer) clearTimeout(thoughtTimer);

    function triggerNextQuestion() {
      const bubble = document.getElementById('mascot-thought-bubble');
      const iconEl = document.getElementById('mascot-thought-icon');
      const textEl = document.getElementById('mascot-thought-text');

      if (bubble && iconEl && textEl) {
        const item = INTERACTIVE_PROMPTS[thoughtIndex % INTERACTIVE_PROMPTS.length];
        thoughtIndex++;

        iconEl.textContent = item.icon;
        textEl.textContent = item.text;

        // Show bubble (stays for 3 seconds)
        bubble.classList.remove('opacity-0', 'translate-y-2');
        bubble.classList.add('opacity-100', 'translate-y-0');

        // Hide after exactly 3 seconds
        setTimeout(() => {
          if (bubble) {
            bubble.classList.remove('opacity-100', 'translate-y-0');
            bubble.classList.add('opacity-0', 'translate-y-2');
          }
        }, 3000); // 3 seconds visible
      }

      // Schedule next question after 3s visible + 15s break = 18s total cycle
      thoughtTimer = setTimeout(triggerNextQuestion, 18000);
    }

    // Initial question appears after 2 seconds on boot
    thoughtTimer = setTimeout(triggerNextQuestion, 2000);
  }

  // Ultra-Fast Real-Time Eye Tracking Calculator (Zero Latency)
  let ticking = false;
  let currentMouseX = window.innerWidth / 2;
  let currentMouseY = window.innerHeight / 2;

  function handleMouseMove(e) {
    currentMouseX = e.clientX;
    currentMouseY = e.clientY;
    if (!ticking) {
      window.requestAnimationFrame(() => {
        updateEyeTracking(currentMouseX, currentMouseY);
        ticking = false;
      });
      ticking = true;
    }
  }

  function updateEyeTracking(mouseX, mouseY) {
    const eyeContainers = [
      {
        svg: document.getElementById('global-mascot-svg'),
        left: document.getElementById('global-mascot-left-eye-track'),
        right: document.getElementById('global-mascot-right-eye-track')
      },
      {
        svg: document.getElementById('input-mascot-svg'),
        left: document.getElementById('input-mascot-left-eye-track'),
        right: document.getElementById('input-mascot-right-eye-track')
      }
    ];

    eyeContainers.forEach(item => {
      if (!item.svg || !item.left || !item.right) return;

      const rect = item.svg.getBoundingClientRect();
      const mascotCenterX = rect.left + rect.width / 2;
      const mascotCenterY = rect.top + rect.height / 2;

      const dx = mouseX - mascotCenterX;
      const dy = mouseY - mascotCenterY;
      const dist = Math.sqrt(dx * dx + dy * dy);

      // Max travel range inside face
      const maxOffset = 5.8;
      const moveFactor = Math.min(dist / 140, 1) * maxOffset;

      const angle = Math.atan2(dy, dx);
      const offsetX = Math.cos(angle) * moveFactor;
      const offsetY = Math.sin(angle) * moveFactor;

      item.left.style.transform = `translate3d(${offsetX.toFixed(2)}px, ${offsetY.toFixed(2)}px, 0)`;
      item.right.style.transform = `translate3d(${offsetX.toFixed(2)}px, ${offsetY.toFixed(2)}px, 0)`;
    });
  }

  // 3-Second Synchronized Blinking Engine
  function startBlinkingLoop() {
    setInterval(() => {
      const eyeGroups = document.querySelectorAll('.mascot-eyes-group');
      if (eyeGroups.length === 0) return;

      // Close eyes
      eyeGroups.forEach(g => {
        g.style.transform = 'scaleY(0.06)';
      });

      // Reopen after 120ms
      setTimeout(() => {
        eyeGroups.forEach(g => {
          g.style.transform = 'scaleY(1)';
        });
      }, 120);

    }, 3000); // 3 seconds loop
  }

  // Mouse move listener with active capture
  window.addEventListener('mousemove', handleMouseMove, { passive: true });

  // Export helper
  window.NWISMascot = {
    createMascotSVG,
    initGlobalFloatingMascot
  };

  // Initialize
  document.addEventListener('DOMContentLoaded', () => {
    initGlobalFloatingMascot();
    startBlinkingLoop();
    startThoughtCycle();
  });

  if (document.readyState === 'complete' || document.readyState === 'interactive') {
    initGlobalFloatingMascot();
    startBlinkingLoop();
    startThoughtCycle();
  }
})();
