from flexx import flx, xui, event

class Example(flx.Widget):
     
    def init(self):
        self.tag = flx.Tag("div",{})
        #self._mutate("container", [self.tag], 'insert', len(self.container))
#         with flx.HBox() as self._container:
#             self.but = flx.Button(text='add')
#             flx.Widget(minsize=10)  # seperator

#     @flx.reaction("but.pointer_click")
#     def add_widgets(self, *events):
#         with self:
#             self.but2 = flx.Button(text="Other")
#         self.but2.set_parent(self._container)
#         self.set_test_list([])

flx.launch(Example, "default-browser")
flx.start()