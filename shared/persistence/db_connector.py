import aiofiles
import json

class FrameLogger:
    async def log_frame(self, frame: dict):
        async with aiofiles.open("logs/session_telemetry.jsonl", "a") as f:
            await f.write(json.dumps(frame) + "\n")
          
