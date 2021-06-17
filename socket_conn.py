import socket
import vgamepad as vg
import threading


HOST = '192.168.199.1'

PORT1 = 62221
PORT2 = 62222
gamepad = vg.VX360Gamepad()

def receive_wheel():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT1))
        print("Listening Wheel")
        while True:
            wheel, addr = s.recvfrom(128)
            Wheel = int.from_bytes(wheel, 'little', signed = True) 
            print(Wheel)
            gamepad.left_joystick(x_value = Wheel, y_value = 2048)
            gamepad.update()

def receive_pad():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT2))
        print("Listening Pad")

        while True:
            # get the throttle
            throttle, addr = s.recvfrom(128)
            # get the break
            breaking, addr = s.recvfrom(128)
            Throttle = int.from_bytes(throttle, 'little', signed = False) 
            Breaking = int.from_bytes(breaking, 'little', signed = True) 
            print(Throttle)
            print(Breaking)
            gamepad.right_trigger(Throttle)
            gamepad.left_trigger(Breaking)
            gamepad.update()


if __name__ == '__main__':
    threading.Thread(target = receive_pad).start()
    threading.Thread(target = receive_wheel).start()
