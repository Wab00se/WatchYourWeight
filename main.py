import kivy 
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen


#Screen Functions
class WelcomeView(Screen):
    pass

class RegistrationView(Screen):
    pass

class DashboardView(Screen):
    pass

class ViewManager(ScreenManager):
   pass
   

# Load .kv Files
Builder.load_file('view/welcome.kv')
Builder.load_file('view/registration.kv')

# Create MainApp
class WatchYourWeightApp(App):
   def build (self):

      vm = ScreenManager()
      vm.add_widget(WelcomeView(name='welcome'))
      vm.add_widget(RegistrationView(name='registration'))

      return vm
   


if __name__== '__main__':
   WatchYourWeightApp().run()
