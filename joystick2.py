# ANTALYA ISAS
# ------------
# Joystick Controller for Logitech G310

import pygame
import serial
import time
from networktables import NetworkTables

# NetworkTables for Orange Pi 
NetworkTables.initialize()
table = NetworkTables.getTable("joystick")

logo = pygame.image.load("logo.png")
logo = pygame.transform.scale(logo, (50, 50))

running = True
joystick_module = 1 # 1 for Logitech, 2 for Arduino Leonardo

hizBoleni = 1
tolerans = 30

maxdeger = 1940
mindeger = 1060

# Pygame Window
pygame.init()
screen = pygame.display.set_mode((800, 290))
pygame.display.set_caption("Antalya ISAS Joystick Kontrol")

font = pygame.font.Font(None, 36)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Reading Joystick 
    if (pygame.joystick.get_count() > 0):
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        joystick_module = joystick.get_name()
        if (joystick_module == "Arduino Leonardo"):
            condition1 = joystick.get_button(0)
            condition2 = joystick.get_button(1)
            condition3 = joystick.get_button(2)
            condition4 = joystick.get_button(3)

            xAxis = (joystick.get_axis(0) + 1) * 500
            yAxis = (joystick.get_axis(1) + 1) * 500
            x2Axis = (joystick.get_axis(2) + 1) * 500
            y2Axis = (joystick.get_axis(3) + 1) * 500
        
        elif (joystick_module == "Controller (Gamepad F310)"):
            condition1 = joystick.get_button(0)
            condition2 = joystick.get_button(1)
            condition3 = joystick.get_button(2)
            condition4 = joystick.get_button(3)

            xAxis = (joystick.get_axis(0) + 1) * 500
            yAxis = (joystick.get_axis(1) + 1) * 500
            x2Axis = (joystick.get_axis(2) + 1) * 500
            y2Axis = (joystick.get_axis(3) + 1) * 500

    else:
        joystick_module = "None"
        condition1 = 0
        condition2 = 0
        condition3 = 0
        condition4 = 0

        xAxis = 500
        yAxis = 500
        x2Axis = 500
        y2Axis = 500

    # Reverse
    xAxisVal = int(xAxis) + 1000
    yAxisVal = int(xAxis) + 1000 # yAxisVal = 3000 - (int(yAxis) + 1000)
    x2AxisVal = int(x2Axis) + 1000 # x2AxisVal = 3000 - (int(x2Axis) + 1000)
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

    # Pygame Part
    xAxis_text = f"X  Axis: {int(xAxisVal)}"
    yAxis_text = f"Y  Axis: {int(yAxisVal)}"
    x2Axis_text = f"X2 Axis: {int(x2AxisVal)}"
    y2Axis_text = f"Y2 Axis: {int(y2AxisVal)}"
    condition_text = f"Condition 1: {int(condition1)}" f" Condition 2: {int(condition2)}" f" Condition 3: {int(condition3)}" f" Condition 4: {int(condition4)}"
    joystick_status = f"Joystick: {(joystick_module)}"    

    text_x = 10
    text_y = 50
    text_spacing = 40

    # Pygame: Joystick Visualization
    screen.fill((250, 250, 255))
    text = font.render(f"Antalya ISAS Joystick Kontrol", True, (0, 0, 0))
    screen.blit(text, (200, 15))

    text = font.render(xAxis_text, True, (0, 0, 0))
    screen.blit(text, (text_x, text_y))

    text = font.render(yAxis_text, True, (0, 0, 0))
    text_y += text_spacing
    screen.blit(text, (text_x, text_y))

    text = font.render(x2Axis_text, True, (0, 0, 0))
    text_y += text_spacing
    screen.blit(text, (text_x, text_y))

    text = font.render(y2Axis_text, True, (0, 0, 0))
    text_y += text_spacing
    screen.blit(text, (text_x, text_y))

    text = font.render(condition_text, True, (0, 0, 0))
    text_y += text_spacing
    screen.blit(text, (text_x, text_y))

    text = font.render(joystick_status, True, (0, 0, 0))
    text_y += text_spacing
    screen.blit(text, (text_x, text_y))

    pygame.draw.rect(screen, (0, 0, 255), (200, 52, ((xAxis) / 460) * 270, 18))
    pygame.draw.rect(screen, (25, 75, 255), (200, 90, ((yAxis) / 460) * 270, 18))
    pygame.draw.rect(screen, (50, 150, 255), (200, 132, ((x2Axis) / 460) * 270, 18))
    pygame.draw.rect(screen, (75, 225, 255), (200, 172, ((y2Axis) / 460) * 270, 18))

    screen.blit(logo, (560, 0))
    pygame.display.flip()
    print(joystickMessage)
    # table.putString("value", joystickMessage)
    time.sleep(0.02)

   
