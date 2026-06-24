import numpy as np

class SomaticPolygraphEvaluator:
    def __init__(self, baseline_hr=72.0, baseline_hrv=50.0):
        self.baseline_hr = baseline_hr
        self.baseline_hrv = baseline_hrv

    def compute_somatic_arousal_index(self, frame_data: dict) -> float:
        cardio = frame_data["cardiovascular_physiological"]
        
        # Calculate physiological deviations
        hr_delta = max(0.0, cardio["heart_rate_bpm"] - self.baseline_hr) / self.baseline_hr
        hrv_drop = max(0.0, (self.baseline_hrv - cardio["hrv_rmssd_ms"]) / self.baseline_hrv)
        eda_spike = cardio["phasic_scr_amplitude_us"]
        resp_suppression = 1.0 - cardio["expiration_suppression_ratio"]

        # Weighted calculation of sympathetic nervous system activation
        sai = (hr_delta * 0.3) + (hrv_drop * 0.25) + (eda_spike * 0.35) + (resp_suppression * 0.1)
        
        # Inject back into the frame
        frame_data["cardiovascular_physiological"]["somatic_arousal_index"] = float(np.clip(sai, 0.0, 1.0))
        return frame_data["cardiovascular_physiological"]["somatic_arousal_index"]
      
