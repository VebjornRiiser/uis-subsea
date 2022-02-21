import unittest
from main import check_camera_command, build_manipulator_byte
from controller import Controller


class TestController(unittest.TestCase):
    def test_camera_lock(self):
        data: dict = {"camera_to_control": 1}

        camera_should_lock = [
            [[200+data["camera_to_control"], {"on": True, "bildebehandlingsmodus": 1}]],
            [[200, {"on": True, "bildebehandlingsmodus": 1, "tilt": 30}]],
            [[200, {"on": False, "bildebehandlingsmodus": 3, "tilt": 40}]]
         ]

        camera_should_lock_expected = [
            [False, True],
            [True, False],
            [True, False]
        ]

        camera_should_not_lock = [
            [[200, {"on": True, "bildebehandlingsmodus": 0}]],
            [[200+data["camera_to_control"], {"on": False, "bildebehandlingsmodus": 0}]]
            ]

        camera_should_not_lock_expected = [[False, False]] * len(camera_should_not_lock)
        for index, command in enumerate(camera_should_lock):
            result = check_camera_command(command)
            self.assertEqual(result, camera_should_lock_expected[index])

        for index, command in enumerate(camera_should_not_lock):
            result = check_camera_command(command)
            self.assertEqual(result, camera_should_not_lock_expected[index])

        # BUTTON_GRAB = 4
    # BUTTON_RELEASE = 5
    # Dpad_in_out = 1
    # Dpad_rotate = 0
    def test_build_manipulator_byte(self):
        dpad = (-1, 0)
        buttons = [0, 0, 0, 0, 0, 0]
        enabled = False

        # rotate ccw
        self.assertEqual(build_manipulator_byte(dpad, buttons, enabled), 8)

        dpad = (1, 0)
        self.assertEqual(build_manipulator_byte(dpad, buttons, enabled), 4)

        dpad = (-1, 0)
        enabled = True
        # send add enable bit
        self.assertEqual(build_manipulator_byte(dpad, buttons, enabled), 72)

        # Forward, rotate left and enable bit
        dpad = (1, 1)
        self.assertEqual(build_manipulator_byte(dpad, buttons, enabled), 70)

    def test_controller_pack_values(self):
        mocked_controller = Mocked_controller()

        expected = {'joysticks': [0, 0, 0, 0, 0, 0, 0], 'camera_movement': 0, 'buttons': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'dpad': (0, 0), 'camera_to_control': 0, 'time_between_updates': 50}  # noqa
        print("sadsad")
        self.assertEquals(Controller.pack_controller_values(mocked_controller), expected)  # noqa

    def test_camera_tilt_update(self):
        pass


class Mocked_controller:
    def __init__(self) -> None:
        self.joysticks = [0, 0, 0, 0, 0, 0, 0]
        self.joysticks[3] = 0
        self.buttons = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.dpad = (0, 0)
        self.camera_motor = 0
        self.duration = 50


if __name__ == "__main":
    unittest.main()
