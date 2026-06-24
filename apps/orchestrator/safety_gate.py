class SafetyCircuitBreaker:
    def check_safety(self, frame: dict) -> bool:
        sai = frame["cardiovascular_physiological"].get("somatic_arousal_index", 0.0)
        if sai > 0.95:
            return False # Immediate system halt
        return True
      
