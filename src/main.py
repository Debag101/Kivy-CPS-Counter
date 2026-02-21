from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

from kivy.uix.button import Button

import threading

import time

#like 5 secs er jonno count korbo
#ha oita korbo kikore bhabchi like last all entries er opor avg nebo?
#ouhh is ts my goat


class MainButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) 

    
    # def disable_button(self, t):

    #     print("disabling button")
    #     self.avg_cps = 'DISABLED'
    #     self.disabled = True
    #     time.sleep(t)
    #     self.disabled = False

    


class RootWindow(BoxLayout):
    counter_thread = None
    FLAG = False

    counter = 0
    cps = StringProperty(str(counter))
    avg_cps = StringProperty("Press Me")

    time_limit = 5

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.counter_thread = threading.Thread(target=self.sleep_counter, args=(self.time_limit, ))
        #self.disable_button_thread = threading.Thread(target=MainButton().disable_button, args=(self.time_limit, ))
        

    def sleep_counter(self, t):

        print("Hello")
        start_time = time.time()
        end_time = start_time + t


        #Running a loop for 5s and calculating curr cps
        while time.time() < end_time:

            #total clicks made // time elapsed since first click
            calculated_curr_cps = self.counter // (time.time() - start_time)
            self.cps = str(calculated_curr_cps)


        calculated_avg_cps = self.counter//t
        print(calculated_avg_cps)
        #self.disable_button_thread.start()
        self.counter = 0
        self.avg_cps = "Press Me"
        self.FLAG = True

    

    def callback(self):
        print("Button Pressed !")


        if self.FLAG:
            self.counter_thread = threading.Thread(target=self.sleep_counter, args=(self.time_limit, ))
            #self.disable_button_thread = threading.Thread(target=MainButton().disable_button, args=(self.time_limit, ))
            self.FLAG = False
            
        if self.counter == 0:
            self.counter_thread.start()
            

        self.counter += 1
        self.avg_cps = str(self.counter)


class CounterApp(App):
    pass
    


if __name__ == '__main__':
    app = CounterApp()
    app.run()
