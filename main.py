import serial
import time
from networktables import NetworkTables
import board

i2c = board.I2C()  # uses board.SCL and board.SDA

NetworkTables.initialize("10.76.72.31")
table = NetworkTables.getTable("joystick")

xAxisVal = yAxisVal = x2AxisVal = y2AxisVal = 0
condition1 = condition2 = condition3 = condition4 = 0

frri_val = frle_val = reri_val = rele_val = frriup_val = frleup_val = reriup_val = releup_val = 1500

joystickMessage = "" # Incoming message from Joystick
serialMessage = "" # Data that we send to Arduino

mode = 0  # There are three mods: Teleop (0), Autonomus (1) and Security (2)

arduino = serial.Serial(port="/dev/ttyUSB0", baudrate=115200, timeout=0.1)

maxValue = 1940
minValue = 1060
baseValue = "15001500150015000000"

time.sleep(3)

def write(serial_com, message):
    serial_com.write(bytes(message, "utf-8"))
    time.sleep(0.05)

def read(serial_com):
    data = serial_com.readline().decode(encoding="ascii")
    return data

def fix_motor_direction(value):
    return 3000 - value

def limit_value(value, min_val, max_val):
    return min(max(value, min_val), max_val)

for x in range(20):
    write(arduino, baseValue)
    print("Calibration")

while True:

    joystickMessage = table.getString("value", baseValue)

    # print(joystickMessage)

    xAxisVal = int(joystickMessage[:4])
    yAxisVal = int(joystickMessage[4:8])
    x2AxisVal = int(joystickMessage[8:12])
    y2AxisVal = int(joystickMessage[12:16])

    # print(yAxisVal, xAxisVal, x2AxisVal, y2AxisVal)

    condition1 = int(joystickMessage[16])
    condition2 = int(joystickMessage[17])
    condition3 = int(joystickMessage[18])
    condition4 = int(joystickMessage[19])

    #front-right-up // rear-right-up
    frriup_val = frleup_val = reriup_val = releup_val = 3000 - xAxisVal

    frri_val = 1500 + (x2AxisVal - 1500) - (y2AxisVal - 1500) - (yAxisVal - 1500)
    frle_val = 1500 + (x2AxisVal - 1500) + (y2AxisVal - 1500) + (yAxisVal - 1500)
    reri_val = 1500 + (x2AxisVal - 1500) + (y2AxisVal - 1500) - (yAxisVal - 1500)
    rele_val = 1500 + (x2AxisVal - 1500) - (y2AxisVal - 1500) + (yAxisVal - 1500)

    ### Fixing reversed motors:
    frri_val = fix_motor_direction(frri_val)
    frle_val = fix_motor_direction(frle_val)
    reri_val = fix_motor_direction(reri_val)
    rele_val = fix_motor_direction(rele_val)
    frriup_val = fix_motor_direction(frriup_val)
    #frleup_val = fix_motor_direction(frleup_val)
    reriup_val = fix_motor_direction(reriup_val)
    #releup_val = fix_motor_direction(releup_val)

    frri_val = limit_value(frri_val, minValue, maxValue)
    frle_val = limit_value(frle_val, minValue, maxValue)
    reri_val = limit_value(reri_val, minValue, maxValue)
    rele_val = limit_value(rele_val, minValue, maxValue)
    frriup_val = limit_value(frriup_val, minValue, maxValue)
    frleup_val = limit_value(frleup_val, minValue, maxValue)
    reriup_val = limit_value(reriup_val, minValue, maxValue)
    releup_val = limit_value(releup_val, minValue, maxValue)

    serialMessage = (
        str(int(frri_val))
        + str(int(frle_val))
        + str(int(reri_val))
        + str(int(rele_val))
        + str(frriup_val)
        + str(frleup_val)
        + str(reriup_val)
        + str(releup_val)
    )

    write(arduino, serialMessage)
    print(serialMessage)
    print(read(arduino))