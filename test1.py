import vgamepad as vg
import time

gamepad = vg.VX360Gamepad()
gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
gamepad.update()
time.sleep(0.5)
gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
gamepad.update()
time.sleep(0.5)

while True:
    gamepad.left_joystick(x_value=0, y_value=25535)
    gamepad.update()
    time.sleep(0.5)
    gamepad.left_joystick(x_value=0, y_value=-25535)
    gamepad.update()
    time.sleep(0.5)