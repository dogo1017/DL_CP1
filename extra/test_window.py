from direct.showbase.ShowBase import ShowBase

class TestApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.setBackgroundColor(0.5, 0.7, 1)

app = TestApp()
app.run()
