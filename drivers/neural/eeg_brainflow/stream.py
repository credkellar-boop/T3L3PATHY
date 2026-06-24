# Author: Infinite-zer0
import time
import numpy as np
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds
from brainflow.data_filter import DataFilter, FilterTypes, DetrendOperations


class EEGDriver:
    def __init__(self, serial_port="/dev/ttyUSB0"):
        params = BrainFlowInputParams()
        params.serial_port = serial_port
        # Using OpenBCI Cyton 8-channel as the baseline hardware
        self.board_id = BoardIds.CYTON_BOARD.value
        self.board = BoardShim(self.board_id, params)
        self.sampling_rate = BoardShim.get_sampling_rate(self.board_id)
        self.eeg_channels = BoardShim.get_eeg_channels(self.board_id)

    def start_stream(self):
        self.board.prepare_session()
        self.board.start_stream(45000)  # Ring buffer size
        print("[EEG] Neural stream active.")

    def get_band_powers(self) -> dict:
        """Pulls the latest chunk of EEG data and calculates band power."""
        data = self.board.get_current_board_data(256)  # Fetch last second of data
        if data.shape[1] < 256:
            return {
                "alpha_relaxation": 0.0,
                "beta_cognitive_load": 0.0,
                "gamma_binding": 0.0,
            }

        # Apply bandpass filter to remove DC offset and 60Hz powerline noise
        for channel in self.eeg_channels:
            DataFilter.remove_environmental_noise(data[channel], self.sampling_rate, 0)
            DataFilter.perform_bandpass(
                data[channel],
                self.sampling_rate,
                1.0,
                50.0,
                4,
                FilterTypes.BUTTERWORTH.value,
                0,
            )

        # Calculate average band powers across all channels
        bands = DataFilter.get_avg_band_powers(
            data, self.eeg_channels, self.sampling_rate, True
        )

        return {
            "alpha_relaxation": round(bands[0][1], 3),  # 8-13 Hz
            "beta_cognitive_load": round(bands[0][2], 3),  # 14-30 Hz
            "gamma_binding": round(bands[0][3], 3),  # 30-50 Hz
        }
