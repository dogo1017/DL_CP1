import os
import sys
import select
from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFileData, Filename, LVector3
from PIL import Image
import math

# -------------------------------
# CONFIGURATION
# -------------------------------
FORCE_OFFSCREEN = False
NUM_FRAMES = 60
SCREENSHOT_FOLDER = os.path.join("extra", "screenshots")
GIF_FILENAME = "animation.gif"
FRAME_DELAY_MS = 100
CAM_SPEED = 5
ROT_SPEED = 60

if FORCE_OFFSCREEN or not os.environ.get("DISPLAY"):
    OFFSCREEN_MODE = True
    loadPrcFileData("", "window-type offscreen")
    loadPrcFileData("", "win-size 1024 768")
else:
    OFFSCREEN_MODE = False

# -------------------------------
# GAME CLASS
# -------------------------------
class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.disableMouse()

        # Static environment (optional)
        self.environment = self.loader.loadModel("models/environment")
        self.environment.reparentTo(self.render)
        self.environment.setScale(0.25)
        self.environment.setPos(0, 10, -1)

        # Reference panda at the center
        self.panda = self.loader.loadModel("models/panda")
        self.panda.reparentTo(self.render)
        self.panda.setScale(0.005)
        self.panda.setPos(0, 10, 0)

        # Camera initial position (offset from panda)
        self.cam_distance = 10
        self.cam_angle_h = 0  # Horizontal rotation
        self.cam_angle_v = 15  # Vertical tilt
        self.update_camera_position()

        # Offscreen input handling
        self.offscreen_commands = []

        if OFFSCREEN_MODE:
            os.makedirs(SCREENSHOT_FOLDER, exist_ok=True)
            self.frame_count = 0
            self.taskMgr.add(self.save_frame_task, "SaveFrameTask")
            self.taskMgr.add(self.terminal_input_task, "TerminalInputTask")
        else:
            # Normal keyboard controls
            self.accept("w", self.move_cam, ["forward"])
            self.accept("s", self.move_cam, ["back"])
            self.accept("a", self.move_cam, ["left"])
            self.accept("d", self.move_cam, ["right"])
            self.accept("i", self.rotate_cam, ["up"])
            self.accept("k", self.rotate_cam, ["down"])
            self.accept("j", self.rotate_cam, ["left"])
            self.accept("l", self.rotate_cam, ["right"])

    # -------------------------------
    # CAMERA CONTROL
    # -------------------------------
    def update_camera_position(self):
        # Convert spherical coordinates to cartesian for smooth orbit around panda
        rad_h = math.radians(self.cam_angle_h)
        rad_v = math.radians(self.cam_angle_v)
        x = self.cam_distance * math.cos(rad_v) * math.sin(rad_h)
        y = self.cam_distance * math.cos(rad_v) * math.cos(rad_h)
        z = self.cam_distance * math.sin(rad_v)
        self.cam.setPos(self.panda.getPos() + LVector3(x, y, z))
        self.cam.lookAt(self.panda)

    def move_cam(self, direction, dt=1/60):
        # Move the camera around the panda in orbit-like fashion
        if direction == "forward":
            self.cam_distance = max(2, self.cam_distance - CAM_SPEED * dt)
        elif direction == "back":
            self.cam_distance += CAM_SPEED * dt
        elif direction == "left":
            self.cam_angle_h += ROT_SPEED * dt
        elif direction == "right":
            self.cam_angle_h -= ROT_SPEED * dt
        self.update_camera_position()

    def rotate_cam(self, direction, dt=1/60):
        if direction == "up":
            self.cam_angle_v = min(89, self.cam_angle_v + ROT_SPEED * dt)
        elif direction == "down":
            self.cam_angle_v = max(-10, self.cam_angle_v - ROT_SPEED * dt)
        elif direction == "left":
            self.cam_angle_h += ROT_SPEED * dt
        elif direction == "right":
            self.cam_angle_h -= ROT_SPEED * dt
        self.update_camera_position()

    # -------------------------------
    # OFFSCREEN TERMINAL INPUT
    # -------------------------------
    def terminal_input_task(self, task):
        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            line = sys.stdin.readline().strip().lower()
            for cmd in line:
                if cmd in "wasdijkl":
                    self.offscreen_commands.append(cmd)

        if self.offscreen_commands:
            cmd = self.offscreen_commands.pop(0)
            self.process_offscreen_command(cmd)
        return task.cont

    def process_offscreen_command(self, cmd):
        dt = 1/60
        if cmd == "w": self.move_cam("forward", dt)
        elif cmd == "s": self.move_cam("back", dt)
        elif cmd == "a": self.move_cam("left", dt)
        elif cmd == "d": self.move_cam("right", dt)
        elif cmd == "i": self.rotate_cam("up", dt)
        elif cmd == "k": self.rotate_cam("down", dt)
        elif cmd == "j": self.rotate_cam("left", dt)
        elif cmd == "l": self.rotate_cam("right", dt)

    # -------------------------------
    # SCREENSHOT / GIF
    # -------------------------------
    def save_frame_task(self, task):
        filename = os.path.join(SCREENSHOT_FOLDER, f"screenshot_{self.frame_count:03}.png")
        self.win.saveScreenshot(Filename(filename))
        print(f"Saved {filename}")
        self.frame_count += 1

        if self.frame_count >= NUM_FRAMES:
            print("Finished capturing frames. Creating GIF...")
            self.create_gif()
            self.cleanup_screenshots()
            self.userExit()
        return task.cont

    def create_gif(self):
        frames = []
        for i in range(NUM_FRAMES):
            path = os.path.join(SCREENSHOT_FOLDER, f"screenshot_{i:03}.png")
            img = Image.open(path)
            frames.append(img)

        gif_path = os.path.join(SCREENSHOT_FOLDER, GIF_FILENAME)
        frames[0].save(
            gif_path,
            save_all=True,
            append_images=frames[1:],
            duration=FRAME_DELAY_MS,
            loop=0
        )
        print(f"GIF saved as {gif_path}")

    def cleanup_screenshots(self):
        for file in os.listdir(SCREENSHOT_FOLDER):
            if file.endswith(".png"):
                os.remove(os.path.join(SCREENSHOT_FOLDER, file))
        print("Deleted individual screenshot files, kept the GIF.")

# -------------------------------
# RUN
# -------------------------------
if __name__ == "__main__":
    app = MyApp()
    app.run()
