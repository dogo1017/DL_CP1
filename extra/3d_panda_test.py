# Import necessary classes and modules from the direct and panda3d libraries
# xvfb-run -a python your_game_file.py

from direct.showbase.ShowBase import ShowBase #
from panda3d.core import loadPrcFileData

# Use loadPrcFileData to set initial window properties like title and size
# loadPrcFileData: Function to load configuration data (prc) from a string at runtime.
# "": An empty string placeholder for a potential configuration name.
# "window-title Your FPS Game": The configuration key and value to set the window title.
# "win-size 1024 768": Sets the window's width and height.
loadPrcFileData("", "window-title Your FPS Game")
loadPrcFileData("", "win-size 1024 768")

# Define a class for your game, inheriting from ShowBase
class MyApp(ShowBase): #
    # class: Keyword to define a new class.
    # MyApp: The name of your game class.
    # (ShowBase): Parent class from which MyApp inherits all its methods and properties.
    def __init__(self): #
        # def: Keyword to define a method (function inside a class).
        # __init__: The special "constructor" method, called when a new instance of the class is created.
        # self: A reference to the current instance of the class, used to access variables and methods within the class.
        ShowBase.__init__(self) #
        # Calls the constructor of the parent class (ShowBase) to initialize the engine's core functionalities.

        # Basic FPS setup includes disabling the default camera control
        # base: A global variable pointing to the ShowBase instance (self in this context).
        # disableMouse(): Method to stop Panda3D from using the mouse for default camera movement.
        self.disableMouse()

        # Load a basic environment model (you will need a model file like "models/environment" in your project folder)
        # self.loader: The object responsible for loading assets (models, textures, sounds).
        # loadModel("models/environment"): Method to load a 3D model file (e.g., a .bam or .gltf file).
        self.environment = self.loader.loadModel("models/environment")
        # self.environment: Stores a reference to the loaded model in the class instance.

        # Reparent the model to the render scene graph
        # self.environment.reparentTo(): Method to attach the model to the main 3D scene (the render node).
        # self.render: The root node of the 3D scene graph; anything attached here gets rendered.
        self.environment.reparentTo(self.render)

        # Apply a scale and position transform to the model
        # setScale(2): Method to uniformly scale the environment model by a factor of 2.
        # setPos(0, 0, -2): Method to set the model's position in 3D space (X, Y, Z coordinates).
        self.environment.setScale(2)
        self.environment.setPos(0, 0, -2)

# Create an instance of your game class and run the application
app = MyApp()
# app: A variable storing the new instance of the MyApp class.
app.run()
# app.run(): Method that starts the main Panda3D game loop, which continuously renders frames and handles events.
