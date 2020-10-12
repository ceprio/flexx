from flexx import flx




class Example(flx.Widget):
    def init(self):
        with flx.HBox() as self._container:
            self.but = flx.Button(text='add')
            flx.Widget(minsize=10)  # seperator

    @flx.reaction("but.pointer_click")
    def add_widgets(self, *events):
        # This would be better - create the widget exactly in the
        # context (parent widget) where you want it
        # with self._container:
        #     flx.Button("stub")
        # For sake of example, you can create a new widget under *any* context,
        # and then move it somewhere else.
        with self:
            c=Calculate()
            self.but2 = flx.Button(text=c[9])
        self.but2.set_parent(self._container)

print(Calculate())

flx.launch(Example, "default-browser")
flx.run()