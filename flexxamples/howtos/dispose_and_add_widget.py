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
        super().init()
        with flx.VFix(flex=1) as self.frame_layout:
            self.custom = CustomPyWidget(
                "width: 100%; height: 100%; border: 5px solid black;", flex=1
            )
            self.but1 = flx.Button(text="swap it")

    @flx.reaction("but1.pointer_click")
    def delete_function(self, *events):
        self.custom.dispose()
        self.but1.dispose()
        self.custom._jswidget.dispose()  # <-- added
        self.custom = None
        self.but1 = None
        with self.frame_layout:
            self.but2 = flx.Button(text="swap it")
            self.custom = CustomPyWidget(
                "width: 100%; height: 100%; border: 5px solid green;", flex=1
            )

#     @flx.reaction('frame_layout.children*.pointer_click')
#     def a_button_was_pressed(self, *events):
#         ev = events[-1]  # only care about last event
#         self.label.set_text(ev.source.id + ' was pressed')


m = flx.launch(Example)
flx.run()