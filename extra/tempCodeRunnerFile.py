import os
from math import sin, cos, radians
from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFileData, Filename, Vec3
from direct.task import Task
from PIL import Image


FORCE_OFFSCREEN = False  # True to always use offscreen
NUM_FRAMES = 60
SCREENSHOT_FOLDER = os.path.join("extra", "screenshots")
GIF_FILENAME = "animation.gif"
FRAME_DELAY_MS = 100  # Delay between frames in the GIF

CAM_SPEED = 10        # Camera move speed
ROT_SPEED = 60        # Degrees per second

# Automatically enable offscreen if no display exists
if FORCE_OFFSCREEN or not os.environ.get("DISPLAY"):
    OFFSCREEN_MODE = True
    loadPrcFileData("", "window-type offscreen")
    loadPrcFileData("", "win-size 1024 768")
else:
    OFFSCREEN_MODE = False

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Load Panda model as reference
        self.panda = self.loader.loadModel("models/panda")
        self.panda.reparentTo(self.render)
        self.panda.setScale(0.5)
        self.panda.setPos(0, 0, 0)

        if OFFSCREEN_MODE:
            # Prepare screenshot folder
            os.makedirs(SCREENSHOT_FOLDER, exist_ok=True)
            self.frame_count = 0
            self.taskMgr.add(self.save_frame_task, "SaveFrameTask")
            # For terminal movement in offscreen, simple WASD text input
            self.keys = {"w":0, "a":0, "s":0, "d":0, "i":0, "j":0, "k":0, "l":0}
            self.cam.setPos(0, -20, 5)
            self.cam.lookAt(self.panda)
            self.taskMgr.add(self.offscreen_camera_task, "OffscreenCameraTask")
        else:
            # Live window controls
            self.disableMouse()
            self.keys = {"w":0, "a":0, "s":0, "d":0, "i":0, "j":0, "k":0, "l":0}
            for key in self.keys:
                self.accept(key, self.update_key, [key, 1])
                self.accept(key + "-up", self.update_key, [key, 0])
            self.cam.setPos(0, -20, 5)
            self.cam.lookAt(self.panda)
            self.taskMgr.add(self.live_camera_task, "LiveCameraTask")



    def update_key(self, key, value):
        self.keys[key] = value


    def offscreen_camera_task(self, task):
        # For simplicity, move camera based on current key states (from terminal input)
        # (Could be expanded to read input() periodically in a separate thread)
        dt = globalClock.getDt()
        hpr = self.cam.getHpr()
        pos = self.cam.getPos()

        # Rotate
        if self.keys["j"]: hpr.x += ROT_SPEED * dt
        if self.keys["l"]: hpr.x -= ROT_SPEED * dt
        if self.keys["i"]: hpr.z += ROT_SPEED * dt
        if self.keys["k"]: hpr.z -= ROT_SPEED * dt
        self.cam.setHpr(hpr)

        # Movement
        forward = Vec3(cos(radians(hpr.x)), sin(radians(hpr.x)), 0)
        right = Vec3(-forward.y, forward.x, 0)
        move = Vec3(0,0,0)
        if self.keys["w"]: move += forward
        if self.keys["s"]: move -= forward
        if self.keys["a"]: move -= right
        if self.keys["d"]: move += right

        self.cam.setPos(pos + move * CAM_SPEED * dt)
        self.cam.lookAt(self.panda)
        return Task.cont

    # -------------------------------
    # Live window camera task
    # -------------------------------
    def live_camera_task(self, task):
        dt = globalClock.getDt()
        hpr = self.cam.getHpr()
        pos = self.cam.getPos()

        # Rotate
        if self.keys["j"]: hpr.x += ROT_SPEED * dt
        if self.keys["l"]: hpr.x -= ROT_SPEED * dt
        if self.keys["i"]: hpr.z += ROT_SPEED * dt
        if self.keys["k"]: hpr.z -= ROT_SPEED * dt
        self.cam.setHpr(hpr)

        # Movement
        forward = Vec3(cos(radians(hpr.x)), sin(radians(hpr.x)), 0)
        right = Vec3(-forward.y, forward.x, 0)
        move = Vec3(0,0,0)
        if self.keys["w"]: move += forward
        if self.keys["s"]: move -= forward
        if self.keys["a"]: move -= right
        if self.keys["d"]: move += right

        self.cam.setPos(pos + move * CAM_SPEED * dt)
        self.cam.lookAt(self.panda)
        return Task.cont

    # -------------------------------
    # Screenshot task
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

    # -------------------------------
    # GIF creation
    # -------------------------------
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

    # -------------------------------
    # Cleanup
    # -------------------------------
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
