from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from direct.task import Task
from panda3d.core import Vec3, WindowProperties, ClockObject
from math import sin, cos, pi

class MyApp(ShowBase):
    def __init__(self):
        super().__init__()

        self.scene = self.loader.loadModel("models/environment")
        self.scene.reparentTo(self.render)
        self.scene.setScale(0.25)
        self.scene.setPos(-8, 42, 0)

        self.pandaActor = Actor("models/panda-model", {"walk": "models/panda-walk4"})
        self.pandaActor.reparentTo(self.render)
        self.pandaActor.setScale(0.0055)
        self.pandaActor.loop("walk")
        self.pandaActor.setH(180)

        self.isJumping = False
        self.canJump = True
        self.jumpVelocity = 0
        self.gravity = -9.8
        self.groundZ = self.pandaActor.getZ()

        self.keys = {"space": False, "w": False, "a": False, "s": False, "d": False}
        for key in self.keys:
            self.accept(key, self.updateKey, [key, True])
            self.accept(key + "-up", self.updateKey, [key, False])

        self.accept("escape", self.unlockMouse)
        self.accept("c", self.toggleCameraMode)
        self.accept("mouse1", self.lockMouse)

        self.mouseLocked = True
        self.firstPerson = False
        self.pitch = 0

        props = WindowProperties()
        props.setCursorHidden(True)
        props.setSize(800, 600)
        self.win.requestProperties(props)
        self.centerX = self.win.getXSize() // 2
        self.centerY = self.win.getYSize() // 2
        self.win.movePointer(0, self.centerX, self.centerY)
        
        self.camLens.setFov(60)

        self.taskMgr.add(self.jumpTask, "JumpTask")
        self.taskMgr.add(self.movementTask, "MovementTask")
        self.taskMgr.add(self.camFollowTask, "CameraFollowTask")
        self.taskMgr.add(self.mouseTurnTask, "MouseTurnTask")

    def updateKey(self, key, value):
        self.keys[key] = value

    def unlockMouse(self):
        props = WindowProperties()
        props.setCursorHidden(False)
        self.win.requestProperties(props)
        self.mouseLocked = False

    def lockMouse(self):
        if not self.mouseLocked:
            props = WindowProperties()
            props.setCursorHidden(True)
            self.win.requestProperties(props)
            self.mouseLocked = True
            self.win.movePointer(0, self.centerX, self.centerY)

    def toggleCameraMode(self):
        self.firstPerson = not self.firstPerson
        if self.firstPerson:
           self.pandaActor.hide()
        else:
            self.pandaActor.show()


    def jumpTask(self, task):
        dt = ClockObject.getGlobalClock().getDt()
        if self.keys["space"] and not self.isJumping and self.canJump:
            self.isJumping = True
            self.jumpVelocity = 5
            self.canJump = False
        if not self.keys["space"]:
            self.canJump = True
        if self.isJumping:
            self.jumpVelocity += self.gravity * dt
            newZ = self.pandaActor.getZ() + self.jumpVelocity * dt
            if newZ <= self.groundZ:
                newZ = self.groundZ
                self.isJumping = False
                self.jumpVelocity = 0
            self.pandaActor.setZ(newZ)
        return Task.cont

    def movementTask(self, task):
        dt = ClockObject.getGlobalClock().getDt()
        speed = 5
        pos = self.pandaActor.getPos()
        heading_rad = self.pandaActor.getH() * (pi / 180)

        forward = Vec3(sin(heading_rad), cos(heading_rad), 0)
        right = Vec3(forward.y, -forward.x, 0)

        if self.keys["w"]:
            pos += forward * speed * dt
        if self.keys["s"]:
            pos -= forward * speed * dt
        if self.keys["a"]:
            pos -= right * speed * dt
        if self.keys["d"]:
            pos += right * speed * dt

        self.pandaActor.setPos(pos)
        return Task.cont

    def camFollowTask(self, task):
        pandaPos = self.pandaActor.getPos()
        heading_rad = self.pandaActor.getH() * (pi / 180)
        pitch_rad = self.pitch * (pi / 180)

        if self.firstPerson:
            forward_offset = 1.5
            offset = Vec3(sin(heading_rad) * forward_offset, cos(heading_rad) * forward_offset, 1.8)
            self.camera.setPos(pandaPos + offset)
            self.camera.setHpr(self.pandaActor.getH(), self.pitch, 0)
        else:
            horizontal_dist = 13 * cos(pitch_rad)
            vertical_offset = 4 - 13 * sin(pitch_rad)
            offset = Vec3(-sin(heading_rad) * horizontal_dist, 
                         -cos(heading_rad) * horizontal_dist, 
                         vertical_offset)
            self.camera.setPos(pandaPos + offset)
            self.camera.lookAt(pandaPos + Vec3(0, 0, 2))
        return Task.cont


    def mouseTurnTask(self, task):
        if not self.mouseLocked:
            return Task.cont
        if self.mouseWatcherNode.hasMouse():
            mp = self.win.getPointer(0)
            dx = mp.getX() - self.centerX
            dy = mp.getY() - self.centerY

            if self.firstPerson:
                self.pandaActor.setH(self.pandaActor.getH() - dx * 0.2)
            else:
                self.pandaActor.setH(self.pandaActor.getH() + dx * 0.2)
            
            self.pitch = max(-45, min(45, self.pitch - dy * 0.2))

            self.win.movePointer(0, self.centerX, self.centerY)
        return Task.cont

app = MyApp()
app.run()