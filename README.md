## T3L3PHATY

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" width="100%" height="100%">
  <defs>
    <!-- Dark Obsidian Background Gradient -->
    <radialGradient id="obsidian-dark" cx="50%" cy="50%" r="70%">
      <stop offset="0%" stop-color="#07070c" />
      <stop offset="60%" stop-color="#030306" />
      <stop offset="100%" stop-color="#000001" />
    </radialGradient>

    <!-- Translucent Blue Glass Silhouette Gradient (Subsurface Scattering Illusion) -->
    <linearGradient id="blue-glass-left" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0d2040" stop-opacity="0.2" />
      <stop offset="70%" stop-color="#153570" stop-opacity="0.4" />
      <stop offset="95%" stop-color="#00add8" stop-opacity="0.7" />
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0.9" />
    </linearGradient>

    <linearGradient id="blue-glass-right" x1="100%" y1="0%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#0d2040" stop-opacity="0.2" />
      <stop offset="70%" stop-color="#153570" stop-opacity="0.4" />
      <stop offset="95%" stop-color="#00add8" stop-opacity="0.7" />
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0.9" />
    </linearGradient>

    <!-- Plasma Energy Gradients -->
    <linearGradient id="plasma-core" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#bd00ff" />
      <stop offset="30%" stop-color="#ff0077" />
      <stop offset="50%" stop-color="#ffffff" />
      <stop offset="70%" stop-color="#ff0077" />
      <stop offset="100%" stop-color="#bd00ff" />
    </linearGradient>

    <!-- High-Definition Glow Filters (Octane Style) -->
    <filter id="octane-glow-heavy" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="12" result="blur1" />
      <feGaussianBlur stdDeviation="25" result="blur2" />
      <feMerge>
        <feMergeNode in="blur2" />
        <feMergeNode in="blur1" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <filter id="plasma-shimmer" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="4" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <!-- 16:9 Obsidian Void Canvas -->
  <rect width="960" height="540" fill="url(#obsidian-dark)" />

  <!-- Volumetric Cinema Background Rays -->
  <g opacity="0.15" filter="url(#octane-glow-heavy)">
    <ellipse cx="480" cy="270" rx="350" ry="120" fill="#673AB7" />
    <circle cx="480" cy="270" r="90" fill="#00add8" />
  </g>

  <!-- ================= LEFT SUBJECT (TRANSLUCENT GLASS) ================= -->
  <g id="left-silhouette">
    <!-- Back Glow -->
    <path d="M 120,480 C 140,360 110,220 180,140 C 240,70 340,90 360,170 C 375,200 390,240 375,260 L 395,285 L 375,305 L 380,335 C 370,360 340,380 320,400 C 300,420 310,480 310,480 Z" fill="url(#blue-glass-left)" />
    
    <!-- Core Golden Particle Brain Architecture (Inspired by 1674.jpg) -->
    <g fill="#ffb700" filter="url(#octane-glow-heavy)" opacity="0.85">
      <!-- Synaptic Node Clusters -->
      <circle cx="270" cy="180" r="5" fill="#ffffff" />
      <circle cx="240" cy="220" r="4" />
      <circle cx="310" cy="210" r="4.5" fill="#ffea00" />
      <circle cx="290" cy="150" r="3" />
      <circle cx="210" cy="190" r="4" />
      <circle cx="330" cy="250" r="5" fill="#ffffff" />
      <circle cx="260" cy="260" r="3.5" />
      
      <!-- Structural Neural Matrix Links -->
      <path d="M 210,190 L 240,220 L 270,180 L 290,150 L 310,210 L 330,250 L 260,260 Z" stroke="#ffa100" stroke-width="1.5" fill="none" opacity="0.4" />
      <path d="M 240,220 L 310,210 M 270,180 L 330,250" stroke="#ffea00" stroke-width="1" fill="none" opacity="0.3" />
      
      <!-- Dense Micro-Particle Cloud Density -->
      <g opacity="0.6">
        <circle cx="250" cy="170" r="1.5" /><circle cx="265" cy="195" r="2" /><circle cx="280" cy="175" r="1.5" />
        <circle cx="230" cy="205" r="1" /><circle cx="300" cy="190" r="2.5" /><circle cx="325" cy="220" r="1.5" />
        <circle cx="225" cy="180" r="2" /><circle cx="285" cy="235" r="1" /><circle cx="245" cy="245" r="2" />
        <circle cx="315" cy="165" r="1.5" /><circle cx="270" cy="140" r="2" /><circle cx="340" cy="200" r="1" />
      </g>
    </g>
  </g>

  <!-- ================= RIGHT SUBJECT (SYMMETRICAL MIRROR) ================= -->
  <g id="right-silhouette" transform="translate(960, 0) scale(-1, 1)">
    <!-- Back Glow -->
    <path d="M 120,480 C 140,360 110,220 180,140 C 240,70 340,90 360,170 C 375,200 390,240 375,260 L 395,285 L 375,305 L 380,335 C 370,360 340,380 320,400 C 300,420 310,480 310,480 Z" fill="url(#blue-glass-right)" />
    
    <!-- Core Golden Particle Brain Architecture (Inspired by 1674.jpg) -->
    <g fill="#ffb700" filter="url(#octane-glow-heavy)" opacity="0.85">
      <!-- Synaptic Node Clusters -->
      <circle cx="270" cy="180" r="5" fill="#ffffff" />
      <circle cx="240" cy="220" r="4" />
      <circle cx="310" cy="210" r="4.5" fill="#ffea00" />
      <circle cx="290" cy="150" r="3" />
      <circle cx="210" cy="190" r="4" />
      <circle cx="330" cy="250" r="5" fill="#ffffff" />
      <circle cx="260" cy="260" r="3.5" />
      
      <!-- Structural Neural Matrix Links -->
      <path d="M 210,190 L 240,220 L 270,180 L 290,150 L 310,210 L 330,250 L 260,260 Z" stroke="#ffa100" stroke-width="1.5" fill="none" opacity="0.4" />
      <!-- Dense Micro-Particle Cloud Density -->
      <g opacity="0.6">
        <circle cx="250" cy="170" r="1.5" /><circle cx="265" cy="195" r="2" /><circle cx="280" cy="175" r="1.5" />
        <circle cx="230" cy="205" r="1" /><circle cx="300" cy="190" r="2.5" /><circle cx="325" cy="220" r="1.5" />
        <circle cx="225" cy="180" r="2" /><circle cx="285" cy="235" r="1" /><circle cx="245" cy="245" r="2" />
      </g>
    </g>
  </g>

  <!-- ================= HIGH-POWERED TELEPATHIC BRIDGE ================= -->
  <!-- Spiraling Vortex of Gold Data Dust & Particles (Wrapping Layer) -->
  <g filter="url(#octane-glow-heavy)" fill="none" opacity="0.7">
    <path d="M 365,210 Q 420,150 480,210 T 595,210" stroke="#ffa500" stroke-width="1.5" stroke-dasharray="5,8" />
    <path d="M 365,210 Q 450,280 480,210 T 595,210" stroke="#ffea00" stroke-width="1" stroke-dasharray="3,6" />
    <path d="M 380,200 C 430,250 510,140 580,220" stroke="#ff7700" stroke-width="2" opacity="0.4" />
    
    <!-- Floating Data Particles Scattered Across the Arc -->
    <g fill="#ffea00" stroke="none">
      <circle cx="410" cy="185" r="2" /><circle cx="440" cy="230" r="3" fill="#ffffff" />
      <circle cx="475" cy="170" r="1.5" /><circle cx="500" cy="240" r="2.5" />
      <circle cx="530" cy="180" r="2" /><circle cx="560" cy="225" r="1.5" />
    </g>
  </g>

  <!-- Concentrated Plasma Arc Layer (Electric Purple & Magenta Lightning - Inspired by 1675.jpg) -->
  <g filter="url(#octane-glow-heavy)">
    <!-- Deep Outer Plasma Volumetric Aura -->
    <path d="M 365,210 L 400,205 L 425,225 L 460,200 L 490,220 L 525,195 L 550,215 L 595,210" fill="none" stroke="#bd00ff" stroke-width="14" opacity="0.4" stroke-linecap="round" stroke-linejoin="round" />
    
    <!-- Vivid Magenta Mid-Layer Dynamic Shockwave -->
    <path d="M 365,210 L 390,220 L 415,195 L 450,225 L 485,190 L 515,220 L 545,200 L 570,215 L 595,210" fill="none" stroke="#ff0077" stroke-width="6" opacity="0.8" stroke-linecap="round" stroke-linejoin="round" />
    
    <!-- Hyper-Concentrated Stark White Core Lightning Arc -->
    <path d="M 365,210 L 385,205 L 405,215 L 430,195 L 445,220 L 470,200 L 495,215 L 520,190 L 540,210 L 565,200 L 595,210" fill="none" stroke="#ffffff" stroke-width="2" filter="url(#plasma-shimmer)" stroke-linecap="round" stroke-linejoin="round" />
  </g>

  <!-- Additional Fine-Line High Frequency Arc Branches -->
  <g stroke="#00add8" stroke-width="1" fill="none" opacity="0.7" filter="url(#plasma-shimmer)">
    <path d="M 365,210 L 395,190 L 420,205 L 455,185" />
    <path d="M 595,210 L 560,225 L 535,210 L 500,230" />
  </g>

  <!-- Foreground Dynamic Core Flares at Impact Points (Prefrontal Cortex Intersections) -->
  <g filter="url(#octane-glow-heavy)">
    <circle cx="365" cy="210" r="10" fill="#ffffff" />
    <circle cx="365" cy="210" r="22" fill="#ff0077" opacity="0.5" />
    
    <circle cx="595" cy="210" r="10" fill="#ffffff" />
    <circle cx="595" cy="210" r="22" fill="#ff0077" opacity="0.5" />
  </g>
</svg>

### 📦 Core Programming Languages
![Python](https://img.shields.io/badge/Python_3.11-3776AB?style=for-the-badge&logo=python&logoColor=white) 

### ⚙️ Core Systems
![Gemini 3.1 Pro](https://img.shields.io/badge/Gemini_3.1_Pro-AI_Orchestration-8E75B2?style=for-the-badge&logo=googlebard&logoColor=white) 
![s3if_c0n8ious](https://img.shields.io/badge/s3if__c0n8ious-Metacognitive_Engine-FF0000?style=for-the-badge)
![Security Enclave](https://img.shields.io/badge/Security_Enclave-Biometric_Alignment-000000?style=for-the-badge&logo=security&logoColor=white)
![Polygraph Evaluation](https://img.shields.io/badge/Polygraph-Deception_Scoring-4CAF50?style=for-the-badge)

### 💻 Platform Support & Hardware Architecture
![BrainFlow](https://img.shields.io/badge/BrainFlow-EEG%2FEMG-00ADD8?style=for-the-badge)
![NeuroKit2](https://img.shields.io/badge/NeuroKit2-ECG%2FPPG-FF5722?style=for-the-badge)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer_Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Face_Mesh-00A65A?style=for-the-badge)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-8CAAEE?style=for-the-badge&logo=scipy&logoColor=white)

### 🛠️ DevOps, Infrastructure & Build Tools
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-Automated_Heal-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![Docker Compose](https://img.shields.io/badge/Docker_Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Black](https://img.shields.io/badge/Black-Code_Formatter-000000?style=for-the-badge)
![Flake8](https://img.shields.io/badge/Flake8-Linter-8A2BE2?style=for-the-badge)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)

### 🛡️ Cybersecurity & Offensive Auditing
![Biometric Matrix](https://img.shields.io/badge/Biometric_Matrix-Access_Control-8B0000?style=for-the-badge)
![Metacognitive Gating](https://img.shields.io/badge/Metacognitive_Gating-Safety_Boundary-D32F2F?style=for-the-badge)

### 🧠 Artificial Intelligence & Quantum
![Semantic Memory](https://img.shields.io/badge/Semantic_Memory-768--dim_Embeddings-673AB7?style=for-the-badge)
![Cognitive Alignment](https://img.shields.io/badge/Cognitive_Alignment-Dynamic_Calculation-FF9800?style=for-the-badge)

### ☁️ Cloud Providers
![AWS OpenSearch](https://img.shields.io/badge/AWS_OpenSearch-Vector_Engine-232F3E?style=for-the-badge&logo=amazonwebservices&logoColor=white)
![GCP BigQuery](https://img.shields.io/badge/GCP_BigQuery-Cloud_Analytics-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white)

### ⚡ Low-Level Infrastructure & Performance
![Asyncio](https://img.shields.io/badge/Asyncio-I%2FO-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Aiofiles](https://img.shields.io/badge/Aiofiles-Async_Logging-1565C0?style=for-the-badge)
![Psutil](https://img.shields.io/badge/Psutil-Host_Telemetry-4CAF50?style=for-the-badge)
![TypedDict](https://img.shields.io/badge/TypedDict-Strict_Schemas-009688?style=for-the-badge)

### 👥 Client Frameworks
![UI Render Loop](https://img.shields.io/badge/Display_Server-Real--Time_UI-E91E63?style=for-the-badge)

**T3L3PATHY** is an advanced, multi-modal biometric and cognitive sensor fusion mono-repo ecosystem. At its core, the project bridges the gap between human physiological computing and artificial intelligence by merging real-time biological data with a high-level cognitive orchestration system.

---

## What It Does
The architecture runs an asynchronous data pipeline orchestrated by Gemini 3.1 Pro, protected by a recursive metacognitive self-monitoring circuit breaker system named **`s3if-c0n8ious`**. The system processes data across several distinct layers:

* **Multi-Modal Data Ingestion:** Streams raw hardware telemetry from neural interfaces (EEG/EMG via BrainFlow), physiological tracking (ECG cardio buffers), kinetic sensors (IMU motion streams), and optical tracking (MediaPipe gaze and facial mesh metrics).
* **Asynchronous Multiplexing:** The `SensorMultiplexer` gathers all simultaneous hardware buffers and binds them into a single, highly structured data packet called a `T3l3pathyFrame`.
* **Identity & Cryptographic Verification:** A secure `SecurityEnclave` handles biometric matching (like fingerprint validation) to authenticate the operator before executing system actions.
* **Polygraph & Deception Scoring:** Analyzes stress indicators, baseline somatic variance, and autonomic arousal to calculate microstress coefficients.
* **Metacognitive Safety Gating:** The reflection engine computes a **Cognitive Alignment Factor**. If your biometric metrics or host system vitals (tracked via `psutil`) cross safety boundaries defined in `system_horizon.md`, the built-in circuit breaker suppresses system execution and triggers an environmental recalibration loop.
* **Enterprise Persistence:** Offloads long-term telemetry data locally to structured `.jsonl` logs, semantically indexes payloads into an AWS OpenSearch cluster using K-Nearest Neighbor (KNN) vector searches, and pipes historical trends into Google Cloud BigQuery for macro-analysis.

---

## Why This Is Cool
* **Hardware-to-Cognition Loop:** Instead of relying on manual inputs (like keyboards or touchscreens), it reads your physiological state (muscle tension, heart rate variability, neural focus, and eye tracking) to gauge intent and cognitive stress directly.
* **Self-Healing AI Safety Boundary:** The AI monitoring isn't just an external rulebook; it's a closed metacognitive loop. The framework acts as a biological firewall, assessing whether the operator's stress or focus levels match safe operating bounds before permitting the system to act.
* **Industrial-Grade Data Stack:** It turns messy biological noise into highly optimized semantic vectors, enabling an LLM to "remember" and query your past cognitive states over time using vector search mechanisms.

---

## How to Install This
The codebase relies on several heavy-duty computing frameworks for managing high-frequency hardware signals and computer vision pipelines.

### Prerequisites
Your central environment requires Python 3.11 along with the fundamental packages outlined in your `requirements.txt` file, including `google-genai`, `brainflow`, `neurokit2`, `opencv-python`, and `mediapipe`.

### Option 1: Native Installation
You can pull dependencies down locally by running a pip installation at the root of the project:
