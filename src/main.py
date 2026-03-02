from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

import threading
import time

from kivy.properties import StringProperty
from kivy.properties import BooleanProperty


class RootWindow(BoxLayout):
    counter_thread = None
    FLAG = False
    time_limit = 5
    

    counter = 0
    cps = StringProperty(str(counter))
    button_text = StringProperty("Press Me")
    slider_timer = StringProperty(f"Timer : {time_limit}")
    button_disabled = BooleanProperty(False)
    final_score = StringProperty('')


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.counter_thread = threading.Thread(target=self.sleep_counter, args=(self.time_limit, ))


    def disable_button(self):
        start_time = time.time()
        end_time = start_time + 5
        self.button_disabled = True

        while time.time() < end_time:
            time_left = int(end_time-time.time())
            self.button_text = f'Button enabling in ... {time_left}'

        self.button_disabled = False
        self.button_text = 'Press Me'

    def sleep_counter(self, t):

        print("Hello")
        start_time = time.time()
        end_time = start_time + t


        #Running a loop for 5s and calculating curr cps
        while time.time() < end_time:

            #total clicks made // time elapsed since first click
            calculated_curr_cps = self.counter // (time.time() - start_time)
            self.cps = str(calculated_curr_cps)

        disable_button_thread = threading.Thread(target=self.disable_button)
        disable_button_thread.start()

        calculated_avg_cps = self.counter//t
        self.final_score = f'FINAL SCORE : {calculated_avg_cps}'
        print(calculated_avg_cps)

        self.counter = 0
        self.button_text = "Press Me"
        self.FLAG = True

    

    def callback(self):
        print("Button Pressed !")


        if self.FLAG:
            self.final_score = ''
            self.counter_thread = threading.Thread(target=self.sleep_counter, args=(self.time_limit, ))
            self.FLAG = False
            
        if self.counter == 0:
            self.counter_thread.start()
            

        self.counter += 1
        self.button_text = str(self.counter)


    def on_slide(self, slider):
        self.time_limit = int(slider.value)
        self.slider_timer = f'Timer : {self.time_limit}'

class CounterApp(App):
    pass
    


if __name__ == '__main__':
    app = CounterApp()
    app.run()
