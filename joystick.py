import pygame
import serial
import time
from networktables import NetworkTables

NetworkTables.initialize()
table = NetworkTables.getTable("joystick")

sit = True
hizBoleni = 1
tolerans = 30

maxdeger = 2000
mindeger = 1000

xAxisVal = yAxisVal = x2AxisVal = y2AxisVal = 0
condition1 = condition2 = condition3 = condition4 = 0

joystickMessage = ""

pygame.init()

while sit:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sit = False

    condition1 = joystick.get_button(0)
    condition2 = joystick.get_button(1)
    condition3 = joystick.get_button(2)
    condition4 = joystick.get_button(3)

    xAxis = joystick.get_axis(0) + 1
    yAxis = joystick.get_axis(1) + 1
    x2Axis = joystick.get_axis(2) + 1
    y2Axis = joystick.get_axis(3) + 1

    xAxis = 512 * xAxis
    yAxis = 512 * yAxis
    x2Axis = 512 * x2Axis
    y2Axis = 512 * y2Axis

    xAxisVal = int(xAxis) + 1000
    yAxisVal = 3000 - (int(yAxis) + 1000)
    x2AxisVal = 3000 - (int(x2Axis) + 1000)
    y2AxisVal = int(y2Axis) + 1000

    xAxisVal = 1500 + (xAxisVal - 1500) / hizBoleni
    yAxisVal = 1500 + (yAxisVal - 1500) / hizBoleni
    x2AxisVal = 1500 + (x2AxisVal - 1500) / hizBoleni
    y2AxisVal = 1500 + (y2AxisVal - 1500) / hizBoleni

    xAxisVal = min(max(xAxisVal, mindeger), maxdeger)
    yAxisVal = min(max(yAxisVal, mindeger), maxdeger)
    x2AxisVal = min(max(x2AxisVal, mindeger), maxdeger)
    y2AxisVal = min(max(y2AxisVal, mindeger), maxdeger)

    if (1500 - tolerans / hizBoleni <= xAxisVal <= 1500 + tolerans / hizBoleni):
        xAxisVal = 1500
    if (1500 - tolerans / hizBoleni <= yAxisVal <= 1500 + tolerans / hizBoleni):
        yAxisVal = 1500
    if (1500 - tolerans / hizBoleni <= x2AxisVal <= 1500 + tolerans / hizBoleni):
        x2AxisVal = 1500
    if (1500 - tolerans / hizBoleni <= y2AxisVal <= 1500 + tolerans / hizBoleni):
        y2AxisVal = 1500

    joystickMessage = (
        str(int(xAxisVal)) + str(int(yAxisVal)) + str(int(x2AxisVal))
        + str(int(y2AxisVal)) + str(condition1) + str(condition2)
        + str(condition3) + str(condition4)
    )
    
    print(joystickMessage)
    table.putString("value", joystickMessage)