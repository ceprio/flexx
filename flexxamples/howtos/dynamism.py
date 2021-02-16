from flexx import flx

class Example(flx.Widget):

    def init(self):
        super().init()
        with flx.VBox():
            with flx.HBox():
                self.but = flx.Button(text='add')
                self.label = flx.Label(flex=1)
            with flx.HBox() as self.box:
                flx.Button(text='x')

    @flx.reaction('but.pointer_click')
    def add_widget(self, *events):
        flx.Button(parent=self.box, text='x')

    @flx.reaction('box.children*.pointer_click')
    def a_button_was_pressed(self, *events):
        ev = events[-1]  # only care about last event
        self.label.set_text(ev.source.id + ' was pressed')
        

m = flx.launch(Example)
flx.run()