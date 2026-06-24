import cv2
import numpy as np
import glfw
from OpenGL.GL import *


class DisplayServer:
    def __init__(self, width=3840, height=2160):
        self.width = width
        self.height = height
        self._init_window()

    def _init_window(self):
        if not glfw.init():
            raise Exception("GLFW failed to initialize")
        # Create a fullscreen 4K window for the projector output
        self.window = glfw.create_window(
            self.width,
            self.height,
            "T3L3PATHY_Display",
            glfw.get_primary_monitor(),
            None,
        )
        glfw.make_context_current(self.window)

    def composite_ar_frame(self, ar_elements: list):
        """
        Composites AR elements (UI, telemetry, maps) into the 4K buffer.
        ar_elements: list of dicts containing coordinate/rendering data.
        """
        # Create blank 4K frame (RGBA)
        frame = np.zeros((self.height, self.width, 4), dtype=np.uint8)

        for element in ar_elements:
            # Logic: Map normalized AR coordinates to 4K pixel space
            x, y = int(element["x"] * self.width), int(element["y"] * self.height)
            # Render UI/Text overlay
            cv2.putText(
                frame,
                element["text"],
                (x, y),
                cv2.FONT_HERSHEY_SIMPLEX,
                2,
                (255, 255, 255, 255),
                3,
            )

        return frame

    def push_to_projector(self, frame):
        """Pushes the frame buffer to the HDMI output via OpenGL."""
        glClear(GL_COLOR_BUFFER_BIT)
        # Texture upload logic for high-performance projection
        glDrawPixels(self.width, self.height, GL_RGBA, GL_UNSIGNED_BYTE, frame)
        glfw.swap_buffers(self.window)
        glfw.poll_events()

    def run(self):
        while not glfw.window_should_close(self.window):
            # In production, receive AR elements from the orchestrator via Queue/Pipe
            frame = self.composite_ar_frame(
                [{"x": 0.1, "y": 0.1, "text": "SYSTEM READY"}]
            )
            self.push_to_projector(frame)


if __name__ == "__main__":
    server = DisplayServer()
    server.run()
