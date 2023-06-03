from kivy.app import App
from kivy.uix.button import Button
from kivy.utils import platform
from jnius import autoclass
from location import get_disposal_point_location


class OpenBrowserApp(App):
    def open_browser(self, url):
        pythonActivity = autoclass('org.kivy.android.PythonActivity')
        intent = autoclass('android.content.Intent')
        uri = autoclass('android.net.Uri')
        intent = intent()
        intent.setAction(intent.ACTION_VIEW)
        intent.setData(uri.parse(url))
        current_activity = pythonActivity.mActivity
        current_activity.startActivity(intent)

    def build(self):
        url = get_disposal_point_location("AIzaSyDmBgSA-GRX0vva8DgID438EvCBzycUwS4", "PSZOK")
        button = Button(text='Open Browser', on_release=lambda x: self.open_browser(url))
        return button


OpenBrowserApp().run()
