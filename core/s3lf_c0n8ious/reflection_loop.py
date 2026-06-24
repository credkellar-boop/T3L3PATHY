import time
import numpy as np

class S3lfC0n8iousEngine:
    def __init__(self, confidence_threshold=0.82):
        self.confidence_threshold = confidence_threshold
        self.last_inference_timestamp = time.time()
        self.historical_latencies = []

    def evaluate_state(self, raw_frame: dict, previous_llm_confidence: float) -> dict:
        current_time = time.time()
        inference_latency = current_time - self.last_inference_timestamp
        self.last_inference_timestamp = current_time
        
        self.historical_latencies.append(inference_latency)
        if len(self.historical_latencies) > 50:
            self.historical_latencies.pop(0)

        somatic_arousal = raw_frame["cardiovascular_physiological"].get("somatic_arousal_index", 0.0)
        
        # Calculate alignment metrics
        latency_penalty = min(1.0, np.mean(self.historical_latencies) / 2.0)
        system_coherence = previous_llm_confidence * (1.0 - (latency_penalty * 0.3))
        cognitive_alignment_factor = system_coherence * (1.0 - (somatic_arousal * 0.4))
        
        execution_permitted = cognitive_alignment_factor >= self.confidence_threshold

        return {
            "inference_latency_ms": round(inference_latency * 1000, 2),
            "system_coherence_score": float(np.clip(system_coherence, 0.0, 1.0)),
            "cognitive_alignment_factor": float(np.clip(cognitive_alignment_factor, 0.0, 1.0)),
            "execution_permitted": execution_permitted,
            "action_gate_status": "CLEAR" if execution_permitted else "SUPPRESSED"
        }
