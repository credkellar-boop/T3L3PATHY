import neurokit2 as nk
import numpy as np


class AutonomicDriver:
    def __init__(self, sampling_rate=250):
        self.sampling_rate = sampling_rate

    def extract_cardio_metrics(
        self, raw_ecg_array: np.ndarray, raw_eda_array: np.ndarray
    ) -> dict:
        """Processes raw physiological voltage into polygraph metrics."""
        try:
            # 1. Process Electrocardiogram (ECG)
            ecg_signals, info = nk.ecg_process(
                raw_ecg_array, sampling_rate=self.sampling_rate
            )
            hrv_metrics = nk.hrv_time(
                info["ECG_R_Peaks"], sampling_rate=self.sampling_rate
            )

            # 2. Process Electrodermal Activity (EDA)
            eda_signals, eda_info = nk.eda_process(
                raw_eda_array, sampling_rate=self.sampling_rate
            )

            # Extract latest values for the frame
            current_hr = ecg_signals["ECG_Rate"].iloc[-1]
            rmssd = hrv_metrics["HRV_RMSSD"].iloc[0]
            phasic_scr = eda_signals["EDA_Phasic"].iloc[-1]

            return {
                "heart_rate_bpm": float(current_hr),
                "hrv_rmssd_ms": float(rmssd),
                "phasic_scr_amplitude_us": float(max(0, phasic_scr)),
                "expiration_suppression_ratio": 0.9,  # Placeholder for respiratory belt integration
            }
        except Exception as e:
            # Fallback if ring buffer is corrupted
            return {
                "heart_rate_bpm": 70.0,
                "hrv_rmssd_ms": 50.0,
                "phasic_scr_amplitude_us": 0.0,
                "expiration_suppression_ratio": 1.0,
            }
