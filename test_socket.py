import socket
import vgamepad as vg


HOST = '192.168.199.1'

PORT = 62222
gamepad = vg.VX360Gamepad()
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))

    print("Listening")

    while True:
        # get the wheel
        wheel, addr = s.recvfrom(1024)
        # get the throttle
        throttle, addr = s.recvfrom(1024)
        # get the break
        breaking, addr = s.recvfrom(1024)

        Wheel = int.from_bytes(wheel, 'little', signed = True) 
        Throttle = int.from_bytes(throttle, 'little', signed = False) 
        Breaking = int.from_bytes(breaking, 'little', signed = True) 
        gamepad.left_joystick(x_value = Wheel, y_value = 2048)
        print(Wheel)
        gamepad.right_trigger(Throttle)
        gamepad.left_trigger(Breaking)
        gamepad.update()