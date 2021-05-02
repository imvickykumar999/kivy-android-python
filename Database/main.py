# Kernel -> Restart -> Run Cell

from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class Fejkbiljett(App):

    def build(self):
        self.gen_btn = Button(text='Generera',
                         size_hint=(.90, .10),
                         pos=(5, 5),
                         font_size=21)
        self.gen_btn.bind(on_press=self.getMessageFejkbiljett)
        l = BoxLayout()
        l.add_widget(self.gen_btn)
        return l

    def getMessageFejkbiljett(self, *args):
        st = StockholmTicket()
        st.getMessage(self)


class StockholmTicket():

    def getMessage(self, source):
        from firebase import firebase
        fb_app = firebase.FirebaseApplication('https://led-blink-wifi-default-rtdb.firebaseio.com', None)
        fb_app.put('/','led1', 0)
        result = fb_app.get('/led1', None)
        source.gen_btn.text = str(result)


# def start():
#     Fejkbiljett().run()

if __name__ == "__main__":
    Fejkbiljett().run()

# Press ESC (top left on keyboard) to exit screen....
