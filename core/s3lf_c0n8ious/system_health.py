import psutil

class HostTelemetry:
    def __init__(self):
        self.process = psutil.Process()

    def get_system_vitals(self) -> dict:
        cpu_usage = psutil.cpu_percent(interval=None)
        ram_usage = psutil.virtual_memory().percent
        
        # Simulate GPU VRAM check (requires pynvml in production)
        vram_usage = 45.2 

        return {
            "host_cpu_percent": cpu_usage,
            "host_ram_percent": ram_usage,
            "gpu_vram_percent": vram_usage,
            "hardware_throttling": cpu_usage > 95.0 or vram_usage > 95.0
        }
      
