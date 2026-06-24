import asyncio
import os
import json
from google import genai
from core.pipeline.validator import SecurityEnclave
from core.pipeline.multiplexer import SensorMultiplexer
from core.polygraph.polygraph_eval import SomaticPolygraphEvaluator
from core.s3lf_c0n8ious.reflection_loop import S3lfC0n8iousEngine


class T3l3pathyOrchestrator:
    def __init__(self):
        # Initialize Google GenAI Client (Requires GEMINI_API_KEY environment variable)
        self.client = genai.Client()
        self.security = SecurityEnclave()
        self.multiplexer = SensorMultiplexer(self.security.session_id)
        self.polygraph = SomaticPolygraphEvaluator()
        self.s3lf_c0n8ious = S3lfC0n8iousEngine()
        self.is_running = True
        self.last_confidence = 0.95

    async def runtime_loop(self):
        if not await self.security.verify_operator():
            return

        print(
            "[T3L3PATHY] Core online. Streaming multimodal context to Gemini 3.1 Pro..."
        )

        while self.is_running:
            # 1. Fetch synchronous data array
            frame = await self.multiplexer.get_synchronized_frame()

            # 2. Append Autonomic Polygraph Score
            self.polygraph.compute_somatic_arousal_index(frame)

            # 3. Append Metacognitive State
            frame["s3lf_c0n8ious"] = self.s3lf_c0n8ious.evaluate_state(
                frame, self.last_confidence
            )

            # 4. Gate Execution
            if not frame["s3lf_c0n8ious"]["execution_permitted"]:
                print("[WARNING] s3lf-c0n8ious Suppressed Execution. Re-calibrating...")
                prompt = f"SYSTEM DRIFT DETECTED. Analyze telemetry and stabilize: {json.dumps(frame)}"
            else:
                prompt = f"Evaluate operator intent and execute logic based on telemetry: {json.dumps(frame)}"

            # 5. Model Inference (Using async text generation)
            try:
                response = await self.client.models.generate_content_async(
                    model="gemini-3.1-pro", contents=prompt
                )
                print(
                    f"[GEMINI] {response.text[:100]}..."
                )  # Print first 100 chars of output

                # Mock updating internal confidence for next loop
                self.last_confidence = 0.96
            except Exception as e:
                print(f"[API ERROR] {e}")

            await asyncio.sleep(0.5)  # Throttle loop for API rate limits


if __name__ == "__main__":
    orchestrator = T3l3pathyOrchestrator()
    asyncio.run(orchestrator.runtime_loop())


# snippet in main.py
async def runtime_loop(self):
    # 1. Fetch current frame
    frame = await self.multiplexer.get_synchronized_frame()

    # 2. Recall previous context from AWS
    embedding = self.client.embed_content(
        model="text-embedding-004", contents=str(frame)
    )
    relevant_history = self.aws_memory.recall_memory(embedding.vector)

    # 3. Prime Gemini with history + current frame
    prompt = (
        f"Previous context: {relevant_history}. Current telemetry: {frame}. Action?"
    )
    # ... (rest of orchestration)
