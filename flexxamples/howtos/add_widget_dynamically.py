from flexx import flx

class Example(flx.Widget):

    def init(self):
        with flx.HBox() as self._container:
            self.but = flx.Button(text='add')
            flx.Widget(minsize=10)  # seperator
        self.but2 = None

    @flx.reaction("but.pointer_click")
    def add_widgets(self, *events):
        # This would be better - create the widget exactly in the
        # context (parent widget) where you want it
        # with self._container:
        #     flx.Button("stub")
        # For sake of example, you can create a new widget under *any* context,
        # and then move it somewhere else.
        if self.but2 is not None:
            with self:
                self.but2 = flx.Button(text="remove")
            self.but2.set_parent(self._container)

    @flx.reaction("!but2.pointer_click")  ### use create reaction instead
    def remove_widget(self, *events):
        self.but2.set_parent(None)
        self.but2.dispose()
        self.but2 = None
        
flx.launch(Example)
flx.run()