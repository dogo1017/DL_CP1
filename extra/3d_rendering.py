import os
import keyboard
import time


wall1 = str("########                           ########################################################################################################################################")
wall2 = """########                           ########################################################################################################################################"""
wall3 = """########                           ########################################################################################################################################"""
wall4 = """########                           ########################################################################################################################################"""
wall5 = """########                           ########################################################################################################################################"""
wall6 = """########                           ########################################################################################################################################"""


pos = 50
neg_pos = 1

while True:
    time.sleep(0.1)
    os.system('cls')
    if neg_pos < 1:
        print(wall1[neg_pos + len(wall1):len(wall1)], wall1[1:pos])
        print(wall2[neg_pos + len(wall2):len(wall2)], wall2[1:pos])
        print(wall3[neg_pos + len(wall3):len(wall3)], wall3[1:pos])
        print(wall4[neg_pos + len(wall4):len(wall4)], wall4[1:pos])
        print(wall5[neg_pos + len(wall5):len(wall5)], wall5[1:pos])
        print(wall6[neg_pos + len(wall6):len(wall6)], wall6[1:pos])
    else:
        print(wall1[neg_pos:pos])
        print(wall2[neg_pos:pos])
        print(wall3[neg_pos:pos])
        print(wall4[neg_pos:pos])
        print(wall5[neg_pos:pos])
        print(wall6[neg_pos:pos])
    if keyboard.is_pressed('d'):
        pos += 1
        neg_pos += 1
    if keyboard.is_pressed('a'):
        pos -= 1
        neg_pos -= 1

