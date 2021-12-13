from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu

class DropDownException(Exception):
    '''DropDownException class.'''
    pass

class DownDrop(MDDropdownMenu):
    def __init__(self, **kwargs):
        super(MDDropdownMenu).__init__(**kwargs)

    def open(self, widget):
        # ensure we are not already attached
        if self.attach_to is not None:
            self.dismiss()

        # we will attach ourself to the main window, so ensure the
        # widget we are looking for have a window
        self._win = widget.get_parent_window()
        if self._win is None:
            raise DropDownException(
                'Cannot open a dropdown list on a hidden widget')

        self.attach_to = widget
        widget.bind(pos=self._reposition, size=self._reposition)
        self._reposition()

        # attach ourself to the main window
        self._win.add_widget(self)

if __name__ == "__main__":
    pass

