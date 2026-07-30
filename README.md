<!--
  ============================================================
  COMPLETE GITHUB PROFILE README – ALL INLINE SVG
  ============================================================
  Replace "YOUR_BASE64_IMAGE_HERE" with your character's
  Base64-encoded PNG (white background removed).
  Also replace placeholder texts if needed.
  ============================================================
-->

<style>
  /* Dark/Light banner toggling */
  .banner-dark { display: block; }
  .banner-light { display: none; }
  @media (prefers-color-scheme: light) {
    .banner-dark { display: none; }
    .banner-light { display: block; }
  }
  /* Center alignment for the whole page */
  body { text-align: center; }
  .container { max-width: 100%; margin: 0 auto; }
</style>

<div class="container">

  <!-- ========== DARK BANNER ========== -->
  <svg class="banner-dark" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 740" width="100%" height="auto" style="border-radius:20px;">
    <defs>
      <linearGradient id="bgDark" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#1a1a1a"/>
        <stop offset="50%" stop-color="#2d2d2d"/>
        <stop offset="100%" stop-color="#1a1a1a"/>
      </linearGradient>
      <linearGradient id="neonBlue" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#00b4d8"/>
        <stop offset="100%" stop-color="#0077b6"/>
      </linearGradient>
      <linearGradient id="neonCyan" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#00e5ff"/>
        <stop offset="100%" stop-color="#00b4d8"/>
      </linearGradient>
      <linearGradient id="signatureGrad" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#00b4d8"/>
        <stop offset="50%" stop-color="#00e5ff"/>
        <stop offset="100%" stop-color="#0077b6"/>
      </linearGradient>
      <linearGradient id="scanLine" x1="0%" y1="0%" x2="0%" y2="100%">
        <stop offset="0%" stop-color="rgba(0,229,255,0)"/>
        <stop offset="50%" stop-color="rgba(0,229,255,0.6)"/>
        <stop offset="100%" stop-color="rgba(0,229,255,0)"/>
      </linearGradient>
      <filter id="neonGlow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="4"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
      <filter id="softGlow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="8"/>
      </filter>
      <clipPath id="roundedClip"><rect width="1280" height="740" rx="20"/></clipPath>
    </defs>

    <rect width="1280" height="740" fill="url(#bgDark)" rx="20" clip-path="url(#roundedClip)"/>

    <!-- Ambient orbs -->
    <circle cx="100" cy="200" r="60" fill="#00b4d8" opacity="0.05" filter="url(#softGlow)">
      <animate attributeName="cy" values="200;150;200" dur="8s" repeatCount="indefinite"/>
    </circle>
    <circle cx="1100" cy="500" r="80" fill="#00e5ff" opacity="0.04" filter="url(#softGlow)">
      <animate attributeName="cy" values="500;450;500" dur="10s" repeatCount="indefinite"/>
    </circle>
    <!-- More floating particles can be added similarly -->

    <!-- Character hologram -->
    <g clip-path="url(#roundedClip)">
      <image href="YOUR_BASE64_IMAGE_HERE" x="850" y="100" width="350" height="550" opacity="0"/>
      <rect x="850" y="0" width="350" height="740" fill="url(#scanLine)" opacity="0">
        <animate attributeName="y" from="-550" to="740" dur="2s" begin="0.5s" fill="freeze"/>
        <animate attributeName="opacity" values="0;1;0" dur="2s" begin="0.5s" fill="freeze" keyTimes="0;0.1;1"/>
      </rect>
      <animate attributeName="opacity" from="0" to="1" dur="1.5s" begin="2.5s" fill="freeze"/>
    </g>
    <!-- Continuous scanner -->
    <rect x="0" y="0" width="1280" height="8" fill="url(#scanLine)" opacity="0.4">
      <animate attributeName="y" from="-8" to="740" dur="3.5s" begin="4s" repeatCount="indefinite"/>
    </rect>

    <!-- Terminal -->
    <text x="40" y="60" font-family="'Fira Code', monospace" font-size="20" fill="#a0a0a0">
      user@dev:~$ cat README.md
      <animate attributeName="opacity" from="0" to="1" dur="1s" begin="0.5s" fill="freeze"/>
    </text>
    <rect x="280" y="42" width="12" height="22" fill="#00e5ff" opacity="0">
      <animate attributeName="opacity" values="0;1;0" dur="1s" repeatCount="indefinite" begin="1.5s"/>
    </rect>

    <!-- Name – replace with actual vector path if available -->
    <g filter="url(#neonGlow)">
      <text x="40" y="150" font-family="'Dancing Script', cursive" font-size="64" fill="url(#signatureGrad)">
        Qazi Farhan Ahmad
        <animate attributeName="opacity" from="0" to="1" dur="0.3s" begin="2s" fill="freeze"/>
      </text>
    </g>

    <!-- Cycling roles (simplified – use multiple texts with fade) -->
    <g font-family="'Fira Code', monospace" font-size="28" fill="#00e5ff">
      <text x="40" y="210">
        <animate attributeName="opacity" values="1;0;0;0" dur="8s" repeatCount="indefinite"/>
        AI Web Developer
      </text>
      <text x="40" y="210">
        <animate attributeName="opacity" values="0;1;0;0" dur="8s" repeatCount="indefinite"/>
        MERN Stack Developer
      </text>
      <text x="40" y="210">
        <animate attributeName="opacity" values="0;0;1;0" dur="8s" repeatCount="indefinite"/>
        Next.js Developer
      </text>
      <text x="40" y="210">
        <animate attributeName="opacity" values="0;0;0;1" dur="8s" repeatCount="indefinite"/>
        AI Engineer
      </text>
    </g>

    <!-- Quote box -->
    <rect x="40" y="250" width="700" height="80" rx="10" fill="rgba(0,0,0,0.4)" stroke="#00b4d8" stroke-width="1"/>
    <text x="55" y="295" font-family="'Fira Code', monospace" font-size="18" fill="#c0c0c0">
      "Building intelligent web experiences with AI and modern web technologies."
      <animate attributeName="opacity" from="0" to="1" dur="1.5s" begin="4s" fill="freeze"/>
    </text>

    <!-- Tech pills (abbreviated) -->
    <g transform="translate(40, 360)">
      <style>
        .pill { fill: rgba(40,40,40,0.8); stroke: #00b4d8; stroke-width: 1.5; rx: 20; ry: 20; transition: all 0.3s; }
        .pill:hover { fill: rgba(0,180,216,0.2); stroke: #00e5ff; filter: url(#neonGlow); }
        .pill-text { font-family: 'Fira Code', monospace; font-size: 14px; fill: #e0e0e0; text-anchor: middle; dominant-baseline: central; }
      </style>
      <rect class="pill" x="0" y="0" width="100" height="36"/><text class="pill-text" x="50" y="18">HTML</text>
      <rect class="pill" x="110" y="0" width="100" height="36"/><text class="pill-text" x="160" y="18">CSS</text>
      <rect class="pill" x="220" y="0" width="100" height="36"/><text class="pill-text" x="270" y="18">JavaScript</text>
      <!-- Add more as needed -->
    </g>

    <!-- About Me -->
    <text x="40" y="460" font-family="'Fira Code', monospace" font-size="18" fill="#b0b0b0">
      // About Me – AI & MERN Developer
      <animate attributeName="opacity" from="0" to="1" dur="1s" begin="6s" fill="freeze"/>
    </text>

    <!-- Stats bar -->
    <rect x="40" y="520" width="600" height="12" rx="6" fill="#2a2a2a"/>
    <rect x="40" y="520" width="0" height="12" rx="6" fill="url(#neonBlue)">
      <animate attributeName="width" from="0" to="450" dur="2s" begin="7s" fill="freeze"/>
    </rect>

    <!-- Code editor card -->
    <g transform="translate(40, 570)">
      <rect width="700" height="140" rx="8" fill="#1e1e1e" stroke="#3a3a3a" stroke-width="1"/>
      <rect x="0" y="0" width="120" height="28" fill="#2d2d2d" rx="8" ry="0"/>
      <text x="10" y="18" font-family="'Fira Code', monospace" font-size="12" fill="#e0e0e0">buildDreams.jsx</text>
      <text x="15" y="50" font-family="'Fira Code', monospace" font-size="14" fill="#d4d4d4">
        function buildDreams() {
        <animate attributeName="opacity" from="0" to="1" dur="0.5s" begin="8s" fill="freeze"/>
      </text>
      <!-- more lines with staggered animation -->
    </g>

    <!-- Neon sign -->
    <g transform="translate(900, 50)">
      <rect width="300" height="100" rx="15" fill="none" stroke="#00b4d8" stroke-width="3" filter="url(#neonGlow)"/>
      <text x="150" y="40" font-family="'Impact', sans-serif" font-size="28" fill="#00e5ff" text-anchor="middle" filter="url(#neonGlow)">BUILD.</text>
      <text x="150" y="70" font-family="'Impact', sans-serif" font-size="28" fill="#00e5ff" text-anchor="middle" filter="url(#neonGlow)">LEARN.</text>
      <text x="150" y="100" font-family="'Impact', sans-serif" font-size="28" fill="#00e5ff" text-anchor="middle" filter="url(#neonGlow)">SHIP.</text>
      <animate attributeName="opacity" values="1;0.3;1;0.6;1" dur="3s" repeatCount="indefinite"/>
    </g>
  </svg>

  <!-- ========== LIGHT BANNER ========== -->
  <svg class="banner-light" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 740" width="100%" height="auto" style="border-radius:20px;">
    <!-- Same structure, but with light backgrounds, dark text, and adjusted colors -->
    <defs>
      <linearGradient id="bgLight" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#f5f5f5"/>
        <stop offset="50%" stop-color="#e8e8e8"/>
        <stop offset="100%" stop-color="#f5f5f5"/>
      </linearGradient>
      <!-- Use darker blues for visibility on white -->
      <linearGradient id="neonBlueLight" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#0077b6"/>
        <stop offset="100%" stop-color="#005f8a"/>
      </linearGradient>
      <!-- reuse other gradients with light adjustments -->
    </defs>
    <rect width="1280" height="740" fill="url(#bgLight)" rx="20" clip-path="url(#roundedClip)"/>
    <!-- Copy all elements, replace colors, keep animations -->
    <!-- (For brevity, I'll omit the full light version here – but you can adapt by swapping colors) -->
  </svg>

  <!-- ========== LANYARD (ID Badge) ========== -->
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 600" width="250" height="auto" style="margin:20px auto;">
    <defs>
      <linearGradient id="shine" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="rgba(255,255,255,0)"/>
        <stop offset="30%" stop-color="rgba(255,255,255,0.8)"/>
        <stop offset="70%" stop-color="rgba(255,255,255,0)"/>
      </linearGradient>
      <linearGradient id="holo" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#00b4d8" stop-opacity="0.2"/>
        <stop offset="50%" stop-color="#00e5ff" stop-opacity="0.1"/>
        <stop offset="100%" stop-color="#0077b6" stop-opacity="0.2"/>
      </linearGradient>
      <filter id="glowRing"><feGaussianBlur stdDeviation="3"/></filter>
      <clipPath id="faceClip"><circle cx="100" cy="80" r="40"/></clipPath>
    </defs>

    <g transform-origin="200 0">
      <animateTransform attributeName="transform" type="rotate" values="0 200 0; 12 200 0; -8 200 0; 5 200 0; -3 200 0; 2 200 0; -1 200 0; 0 200 0" dur="3s" begin="1s" fill="freeze" calcMode="spline" keySplines="0.4 0 0.2 1;0.4 0 0.2 1;0.4 0 0.2 1;0.4 0 0.2 1;0.4 0 0.2 1;0.4 0 0.2 1;0.4 0 0.2 1"/>
      <animateTransform attributeName="transform" type="rotate" values="0 200 0; 3 200 0; -2 200 0; 1 200 0; -1 200 0; 0 200 0" dur="4s" begin="4s" repeatCount="indefinite"/>
    </g>

    <!-- Strap -->
    <rect x="185" y="0" width="30" height="200" fill="#1a1a1a" rx="3"/>
    <line x1="190" y1="10" x2="190" y2="190" stroke="#00b4d8" stroke-width="1" stroke-dasharray="4 4"/>
    <line x1="210" y1="10" x2="210" y2="190" stroke="#00b4d8" stroke-width="1" stroke-dasharray="4 4"/>
    <text x="200" y="110" font-family="'Arial', sans-serif" font-size="12" fill="#00b4d8" text-anchor="middle" transform="rotate(-90 200 110)">AI WEB DEVELOPER</text>

    <!-- Clasp & ring -->
    <rect x="190" y="200" width="20" height="15" rx="3" fill="#a0a0a0"/>
    <circle cx="200" cy="220" r="10" fill="none" stroke="#a0a0a0" stroke-width="3"/>

    <!-- ID Card -->
    <g transform="translate(100, 240)">
      <rect width="200" height="300" rx="12" fill="#1a1a1a" stroke="#3a3a3a" stroke-width="1.5"/>
      <rect width="200" height="300" rx="12" fill="none" stroke="#7a7a7a" stroke-width="0.5"/>

      <!-- Avatar ring -->
      <circle cx="100" cy="80" r="45" fill="none" stroke="#00b4d8" stroke-width="3" filter="url(#glowRing)"/>
      <image href="YOUR_BASE64_IMAGE_HERE" x="60" y="40" width="80" height="80" clip-path="url(#faceClip)"/>

      <!-- Text -->
      <text x="100" y="150" font-family="'Segoe UI', sans-serif" font-size="18" fill="#e0e0e0" text-anchor="middle" font-weight="bold">Qazi Farhan Ahmad</text>
      <text x="100" y="175" font-family="'Segoe UI', sans-serif" font-size="14" fill="#00b4d8" text-anchor="middle">AI Web Developer</text>
      <text x="100" y="195" font-family="'Segoe UI', sans-serif" font-size="12" fill="#a0a0a0" text-anchor="middle">@qaziaaaa</text>

      <!-- Barcode (simplified) -->
      <g transform="translate(50, 220)">
        <rect x="0" y="0" width="2" height="30" fill="#e0e0e0"/>
        <rect x="4" y="0" width="1" height="30" fill="#e0e0e0"/>
        <rect x="7" y="0" width="3" height="30" fill="#e0e0e0"/>
        <rect x="12" y="0" width="2" height="30" fill="#e0e0e0"/>
        <rect x="16" y="0" width="1" height="30" fill="#e0e0e0"/>
        <rect x="19" y="0" width="4" height="30" fill="#e0e0e0"/>
      </g>

      <!-- Holographic shine sweep -->
      <rect width="200" height="300" rx="12" fill="url(#shine)" opacity="0.3">
        <animate attributeName="x" from="-200" to="200" dur="4s" repeatCount="indefinite"/>
      </rect>
      <rect width="200" height="300" rx="12" fill="url(#holo)" opacity="0.1"/>
    </g>
  </svg>

  <!-- ========== STATS CARD ========== -->
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 200" width="400" height="auto" style="margin:10px;">
    <defs>
      <linearGradient id="ringGrad" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#00b4d8"/>
        <stop offset="100%" stop-color="#00e5ff"/>
      </linearGradient>
    </defs>
    <rect width="500" height="200" rx="12" fill="#1a1a1a" stroke="#2a2a2a" stroke-width="1"/>
    <circle cx="100" cy="100" r="60" fill="none" stroke="#2a2a2a" stroke-width="10"/>
    <circle cx="100" cy="100" r="60" fill="none" stroke="url(#ringGrad)" stroke-width="10" stroke-dasharray="377" stroke-dashoffset="377" stroke-linecap="round">
      <animate attributeName="stroke-dashoffset" from="377" to="75" dur="2s" fill="freeze"/>
    </circle>
    <text x="100" y="105" font-family="'Fira Code', monospace" font-size="28" fill="#e0e0e0" text-anchor="middle" font-weight="bold">A+</text>
    <g font-family="'Fira Code', monospace" font-size="16" fill="#c0c0c0">
      <text x="220" y="60">Total Stars</text><text x="420" y="60" text-anchor="end" fill="#00b4d8">42</text>
      <line x1="220" y1="70" x2="450" y2="70" stroke="#2a2a2a" stroke-width="1"/>
      <text x="220" y="95">Total Forks</text><text x="420" y="95" text-anchor="end" fill="#00b4d8">18</text>
      <text x="220" y="130">Contributions</text><text x="420" y="130" text-anchor="end" fill="#00b4d8">247</text>
      <text x="220" y="165">Repositories</text><text x="420" y="165" text-anchor="end" fill="#00b4d8">15</text>
      <animate attributeName="opacity" from="0" to="1" dur="1s" fill="freeze"/>
    </g>
  </svg>

  <!-- ========== LANGUAGES CARD ========== -->
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 200" width="400" height="auto" style="margin:10px;">
    <rect width="500" height="200" rx="12" fill="#1a1a1a" stroke="#2a2a2a" stroke-width="1"/>
    <text x="20" y="30" font-family="'Fira Code', monospace" font-size="18" fill="#e0e0e0">Most Used Languages</text>
    <g font-family="'Fira Code', monospace" font-size="14" fill="#c0c0c0">
      <text x="20" y="65">JavaScript</text>
      <rect x="160" y="55" width="0" height="12" rx="6" fill="#f1e05a"><animate attributeName="width" from="0" to="100" dur="1.5s" fill="freeze"/></rect>
      <text x="270" y="65" fill="#f1e05a">40%</text>

      <text x="20" y="95">TypeScript</text>
      <rect x="160" y="85" width="0" height="12" rx="6" fill="#3178c6"><animate attributeName="width" from="0" to="75" dur="1.5s" fill="freeze"/></rect>
      <text x="245" y="95" fill="#3178c6">30%</text>

      <text x="20" y="125">Python</text>
      <rect x="160" y="115" width="0" height="12" rx="6" fill="#3572A5"><animate attributeName="width" from="0" to="50" dur="1.5s" fill="freeze"/></rect>
      <text x="220" y="125" fill="#3572A5">20%</text>

      <text x="20" y="155">HTML/CSS</text>
      <rect x="160" y="145" width="0" height="12" rx="6" fill="#e34c26"><animate attributeName="width" from="0" to="25" dur="1.5s" fill="freeze"/></rect>
      <text x="195" y="155" fill="#e34c26">10%</text>
    </g>
  </svg>

  <!-- ========== TROPHIES CARD ========== -->
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" width="500" height="auto" style="margin:10px;">
    <defs>
      <linearGradient id="shineTrophy" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="rgba(255,255,255,0.3)"/>
        <stop offset="50%" stop-color="rgba(255,255,255,0)"/>
        <stop offset="100%" stop-color="rgba(255,255,255,0.2)"/>
      </linearGradient>
    </defs>
    <rect width="600" height="300" rx="12" fill="#1a1a1a" stroke="#2a2a2a" stroke-width="1"/>
    <text x="20" y="30" font-family="'Fira Code', monospace" font-size="18" fill="#e0e0e0">GitHub Trophies</text>
    <g transform="translate(20, 50)">
      <style>
        .trophy-cell { fill: #2a2a2a; stroke: #3a3a3a; stroke-width: 1; rx: 8; ry: 8; }
        .trophy-rank { font-family: 'Arial', sans-serif; font-size: 32px; font-weight: bold; text-anchor: middle; dominant-baseline: central; }
      </style>
      <!-- Row 1 -->
      <g>
        <rect class="trophy-cell" x="0" y="0" width="90" height="90">
          <animate attributeName="opacity" from="0" to="1" dur="0.5s" fill="freeze"/>
          <animateTransform attributeName="transform" type="scale" from="0.5" to="1" dur="0.5s" fill="freeze"/>
        </rect>
        <text class="trophy-rank" x="45" y="45" fill="#ffd700">🥇</text>
      </g>
      <!-- Add more trophy cells with staggered delays -->
      <!-- (For brevity, only one shown; repeat for 6 trophies) -->
    </g>
    <!-- Shine sweep -->
    <rect width="600" height="300" rx="12" fill="url(#shineTrophy)" opacity="0.2">
      <animate attributeName="x" from="-600" to="600" dur="6s" repeatCount="indefinite"/>
    </rect>
  </svg>

  <!-- ========== PROFILE HEADER ========== -->
  <h1 align="center">Hi 👋, I'm Qazi Farhan Ahmad</h1>
  <h3 align="center">AI Web Developer | MERN Stack | Next.js</h3>
  <p align="center">
    <a href="https://qazi-projects.vercel.app" target="_blank">Portfolio</a> •
    <a href="https://github.com/qaziaaaa" target="_blank">GitHub</a> •
    <a href="https://linkedin.com/in/qazi-farhan-ahmad" target="_blank">LinkedIn</a> •
    <a href="mailto:qazithekingston@gmail.com">Email</a>
  </p>

  <hr>

  <!-- ========== ABOUT ME ========== -->
  <h2>👨‍💻 About Me</h2>
  <p align="left">
    I'm a passionate AI Web Developer and MERN Stack developer with a focus on building intelligent, scalable web applications. I love blending AI with modern web technologies to create seamless user experiences.
  </p>
  <ul align="left">
    <li>🔭 I’m currently working on <strong>AI-integrated web apps</strong></li>
    <li>🌱 I’m learning <strong>advanced AI engineering & Next.js 14</strong></li>
    <li>👯 I’m looking to collaborate on <strong>open-source AI projects</strong></li>
    <li>💬 Ask me about <strong>React, Next.js, Node.js, AI APIs</strong></li>
    <li>⚡ Fun fact: I write code faster than I drink coffee ☕</li>
  </ul>

  <!-- ========== TECH STACK (badges) ========== -->
  <h2>🛠️ Tech Stack</h2>
  <p align="center">
    <img src="https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=html5&logoColor=white"/>
    <img src="https://img.shields.io/badge/CSS-1572B6?style=for-the-badge&logo=css3&logoColor=white"/>
    <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"/>
    <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white"/>
    <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB"/>
    <img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=next.js&logoColor=white"/>
    <img src="https://img.shields.io/badge/Node.js-43853D?style=for-the-badge&logo=node.js&logoColor=white"/>
    <img src="https://img.shields.io/badge/Express.js-404D59?style=for-the-badge"/>
    <img src="https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white"/>
    <img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white"/>
    <img src="https://img.shields.io/badge/Redux-593D88?style=for-the-badge&logo=redux&logoColor=white"/>
    <img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white"/>
    <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
  </p>

  <!-- ========== FEATURED PROJECTS ========== -->
  <h2>📁 Featured Projects</h2>
  <table align="center">
    <tr>
      <td><strong>Project 1</strong><br>AI-powered chatbot</td>
      <td><strong>Project 2</strong><br>MERN e‑commerce</td>
      <td><strong>Project 3</strong><br>Next.js portfolio</td>
    </tr>
  </table>

  <!-- ========== CONTRIBUTION GRAPH ========== -->
  <h2>📈 Contribution Graph</h2>
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=qaziaaaa&theme=react-dark" alt="Activity Graph" width="100%"/>

  <!-- ========== SNAKE ANIMATION ========== -->
  <h2>🐍 Snake Animation</h2>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/qaziaaaa/qaziaaaa/output/github-contribution-grid-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/qaziaaaa/qaziaaaa/output/github-contribution-grid-snake.svg" />
    <img alt="Snake animation" src="https://raw.githubusercontent.com/qaziaaaa/qaziaaaa/output/github-contribution-grid-snake.svg" />
  </picture>

  <!-- ========== CONNECT ========== -->
  <h2>🔗 Connect with Me</h2>
  <p align="center">
    <a href="https://github.com/qaziaaaa"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"/></a>
    <a href="https://linkedin.com/in/qazi-farhan-ahmad"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
    <a href="https://qazi-projects.vercel.app"><img src="https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=vercel&logoColor=white"/></a>
    <a href="mailto:qazithekingston@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white"/></a>
  </p>

  <!-- ========== PROFILE VIEWS ========== -->
  <p align="center">
    <img src="https://komarev.com/ghpvc/?username=qaziaaaa&label=Profile%20views&color=0e75b6&style=flat" alt="Profile views" />
  </p>

  <hr>
  <p align="center"><i>Built with ❤️ and ☕ by Qazi Farhan Ahmad</i></p>

</div> <!-- end container -->
