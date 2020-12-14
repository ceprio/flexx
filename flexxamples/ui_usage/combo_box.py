"""
Simple use of a dropdown,
"""


from flexx import app, event, ui, flx


class Example(ui.Widget):

    def init(self):
        # A combobox
        self.combo = ui.ComboBox(editable=True,
                                 options=('foo', 'bar', 'spaaam', 'eggs', 'bacon'))
        self.label = ui.Label()
        self.button = ui.Button(text='change list')

    @event.reaction('combo.text')  
    def on_combobox_text(self, *events):
        text = f'"{self.combo.text}" (index {self.combo.selected_index})'
        self.label.set_text(text)
        
    @event.reaction('button.pointer_click') 
    def on_button_press(self, *events): 
        self.combo.set_selected_index(-1)
        self.combo.set_options((1,2,3))

if __name__ == '__main__':
     m = flx.launch(Example, 'default-browser')
     flx.run()
