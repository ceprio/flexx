"""
Example that demonstrates three ways to react to changes in properties.

All reaction functions get called once when ``foo`` changes. In the first
reaction, we have no information other than the current value of foo.
In the other reactions we have more information about how `foo` changed.
"""

from flexx import event
from flexx import flx

class Test(flx.Widget):

    foo1 = event.IntProp(0, settable=True)
    foo = event.ListProp([], settable=True,)
    
    def init(self):
        self.b1 = flx.Button(text='apple')

    @event.reaction
    def react_to_foo_a(self):
        print(f'A: foo changed to {self.foo}')

    @event.reaction('foo')
    def react_to_foo_b(self, *events):
        # This function
        print(f'B: foo changed from {events[0].old_value} to {events[-1].new_value}')

    @event.reaction('foo')
    def react_to_foo_c(self, *events):
        print('C: foo changed:')
        for ev in events:
            print(f'    from {events[0].old_value} to {events[-1].new_value}')
            
    @flx.reaction('b1.pointer_click')
    def _button_clicked(self, *events):
        ev = events[-1]
        self.set_foo([5])
        self.set_foo([5,7])

flx.launch(Test, "default-browser")
flx.run()
