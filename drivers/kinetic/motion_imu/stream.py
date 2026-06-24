import math


class KineticIMUDriver:
    def __init__(self):
        self.velocity = [0.0, 0.0, 0.0]

    def read_six_dof_sensor(self) -> dict:
        """Simulates reading from an I2C connected MPU6050/BNO085."""
        # Mocking accelerometer (G) and gyroscope (rad/s) data
        accel = [0.01, 0.02, 0.98]
        gyro = [0.0, 0.0, 0.01]

        # Calculate absolute vector magnitude
        kinetic_magnitude = math.sqrt(accel[0] ** 2 + accel[1] ** 2 + accel[2] ** 2)

        return {
            "linear_acceleration_g": accel,
            "angular_velocity_rad_s": gyro,
            "kinetic_magnitude": round(kinetic_magnitude, 3),
            "postural_shift_detected": kinetic_magnitude
            > 1.2,  # > 1G implies sudden movement
        }
