## What T3L3PATHY Is About
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
