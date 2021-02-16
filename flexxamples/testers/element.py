"""
Test element functionnalities
"""

from flex import Element

class ElementDemo(Element):
    def init(self):  # at this point a self.container as been initialized
        tag, text, line, widget, stag = self.container.ttlws()  # syntax borrowed from yattag
        fill_my_container(self.container)  # call a sub to fill a fist part
        with tag("div") as d:
            self.button_container = d     # keep a reference on the container
            self.button1 = widget(e.Button(text='swap'))  # keep a reference on the button
            widget(e.Button(text='bar'))
        with tag("div") as d:
            with widget(flx.GroupWidget()):
                 with tag("span") as s:
                     self.span = s
                     text("My video:")
                     widget(ui.YoutubeWidget(source='RG1P8MQS1cU'))

    @flx.reaction('button1.pointer_click')
    def _button_clicked(self, *events):
        ev = events[-1]
        old_container = self.button_container.container
        self.button_container.container = e.Container()
        tag, text, line, widget, stag = self.button_container.container.ttlws() 
        for elem in reverse(old_container):
            self.button_container.container.append(elem)
        text("Buttons have swapped")
            
    @flx.reaction("but.pointer_click")
    def add_widgets(self, *events):
        container = self.span.container
        container.insert(0, container.Widget(flx.Button(text="Added button"))
        self.span.sync_container() # don't know if this would be needed but the span container needs to be synced with the dom

if __name__ == '__main__':
    flx.launch(ElementDemo, 'default-browser')
    # flx.run() # runs once
    flx.start()
