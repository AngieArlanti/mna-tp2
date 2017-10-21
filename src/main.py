'''
Camera Example
==============

This example demonstrates a simple use of the camera. It shows a window with
a buttoned labelled 'play' to turn the camera on and off. Note that
not finding a camera, perhaps because gstreamer is not installed, will
throw an exception during the kv language processing.

'''

# Uncomment these lines to see all the messages
# from kivy.logger import Logger
# import logging
# Logger.setLevel(logging.TRACE)

from kivy.app import App
from kivy.clock import mainthread
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from fft_transformer import transform
import threading


import time
Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    counter: counter
    Label:
        id: counter
        font_size: 30
        color: 0.6, 0.6, 0.6, 1
        text_size: self.width, None
        halign: 'center'
        text: '0'
    ToggleButton:
        text: 'Play'
        on_press: 
        size_hint_y: None
        height: '48dp'
    Button:
        text: 'Capture'
        size_hint_y: None
        height: '48dp'
        on_press: root.button_press()
''')


class CameraClick(BoxLayout):

    def button_press(self):
        threading.Thread(target=self.start_fft).start()

    def start_fft(self):
        self.update_label(str(transform()))

    @mainthread
    def update_label(self, new_counter):
        self.counter.text = new_counter

    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        # camera = self.ids['camera']
        # timestr = time.strftime("%Y%m%d_%H%M%S")
        # camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")


class TestCamera(App):

    def build(self):
        return CameraClick()


TestCamera().run()