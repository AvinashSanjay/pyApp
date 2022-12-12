import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

kivy.require("1.9.0")


class layoutLogin(BoxLayout):
    def __init__(self):
        super(layoutLogin, self).__init__()

    def login(self):
        if self.email.text == "abc@gmail.com":
            if self.passwd.text == "123123":
                self.tit.text = "Logged IN Successfully..."
        else:
            self.tit.text = "Incorrect Username or Password...."


class Snap(App):
    def build(self):
        return layoutLogin()


snap = Snap()
snap.run()
