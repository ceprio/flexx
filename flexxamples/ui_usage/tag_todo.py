# doc-export: Main
"""
Simple use of a TagWidget,
"""

from flexx import app, event, ui, flx

class Example(ui.PyWidget):

    def init(self):
#        super().init()
#        ui.TagWidget("h1",{}, "123456") # {'dir':"rtl"}, 
#        ui.TagWidget("p", {}, ["this is some ", ui.TagWidget("b", {}, "bold text 1")])
#        ui.TagWidget("p", {}, ["this is some ", ui.Label(text="allo")])
#        with ui.TagWidget("p", {'dir':"ltr"}, None):
#        ui.TagWidget("span", {}, "This is other ")
#        ui.TagWidget("div", {'innerHTML':"<b>bold text</b>"}, [])  # This cannot work as it is meant for create_element()
        ui.TagWidget("span", {'contenteditable':'true'}, content=["<b>bold text 2</b>"])

if __name__ == '__main__':
#     m = flx.launch(Example)
#     flx.run()
    
    m = flx.launch(Example, 'default-browser')
    flx.start()
