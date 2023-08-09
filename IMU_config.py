import numpy as np


class IMU_config:
    def __init__(self) -> None:
        self.addr=0x50
        self.i2cbus=0
        self.GRAVITY = 9.8
        self.buffer = {"acceleration":0x34, "angular velocity":0x37, 
                       "RollPitchYaw":0x3d, "Quaterions":0x51}
        self.data_range = {"acceleration":16 * self.GRAVITY, "angular velocity":2000, 
                           "RollPitchYaw":180, "Quaterions":1}
        # data structure from IMU
        # 0x34 - 0x36 : xyz_accelerations
        # 0x37 - 0x39 : xyz_angular_velocity
        # 0x3d - 0x3f : Roll_Pitch_Yaw_xyz
        # 0x51 - 0x54 : Quaterions Q0-Q3
