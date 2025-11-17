from PIL import ImageGrab
def take_screenshot(filename="mal.png"):
    img = ImageGrab.grab()
    img.save(filename)
    print(f"Screenshot saved as {filename}")
if __name__ == "__main__":
    take_screenshot()
import os
os.system("start chrome --new-window https://www.google.com/search?q=whats+my+current+location&rlz=1C1ONGR_enUS1185US1185&oq=whats+my+cur&gs_lcrp=EgZjaHJvbWUqBwgAEAAYgAQyBwgAEAAYgAQyBwgBEAAYgAQyBwgCEAAYgAQyCQgDEAAYChiABDIGCAQQRRg5MgkIBRAAGAoYgAQyBwgGEAAYgAQyCQgHEAAYChiABDIJCAgQABgKGIAEMgkICRAAGAoYgASoAgCwAgA&sourceid=chrome&ie=UTF-8&safe=active&ssui=on")
#pyautogui.moveTo(1300, 750, duration = 1)
#pyautogui.click()

take_screenshot()