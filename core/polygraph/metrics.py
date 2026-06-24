class RollingMetricTracker:
    def __init__(self, window_size=100):
        self.history = []
        self.window_size = window_size

    def update_and_score(self, new_val: float) -> float:
        self.history.append(new_val)
        if len(self.history) > self.window_size:
            self.history.pop(0)

        # Calculate Z-score to determine how anomalous the current arousal level is
        mean = sum(self.history) / len(self.history)
        std = (sum([(x - mean) ** 2 for x in self.history]) / len(self.history)) ** 0.5
        return (new_val - mean) / (std + 1e-6)
