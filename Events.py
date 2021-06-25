import pygame

def testEvent():
    print("test")

def closeProgram():
    pygame.quit()


def LinkToEvent(event : int):
    if event == 0:
        testEvent()

    if event == 1:
        closeProgram()