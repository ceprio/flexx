from flexx import flx


class CustomPyWidget(flx.PyWidget):
    frame = None

    def dispose(self):
        self.frame.dispose()
        self.frame = None
        super().dispose()

    def init(self, additional_style="border: 3px solid red"):
        with flx.VFix(flex=1, style=additional_style) as self.frame:
            pass

class Example(flx.PyWidget):
    def init(self):
        with flx.VFix(flex=1) as self.frame_layout:
            self.custom = CustomPyWidget(
                "width: 100%; height: 100%; border: 5px solid black;", flex=1
            )
            self.but = flx.Button(text="swap it")

    @flx.reaction("but.pointer_click")
    def delete_function(self, *events):
        self.custom.dispose()
        self.custom._jswidget.dispose()  # <-- added
        self.custom = None
        with self.frame_layout:
            self.custom = CustomPyWidget(
                "width: 100%; height: 100%; border: 5px solid green;", flex=1
            )

m = flx.launch(Example)
flx.run()