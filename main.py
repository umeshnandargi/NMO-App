from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Canvas,RoundedRectangle,Rectangle, Color
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from math import sin, cos, tan, cosh, sinh, tanh, exp, pi
from kivy.lang import Builder
from kivy.core.window import Window

# Window.size = (1920,1080)


class P(FloatLayout):
    pass


class MainWindow(Screen):
    def btn(self):
        I = f"Planning To Add More\nFeatures Like:\nLagrange's Interpolation\nNewton Raphson method, etc"
        show_popup(I)


class GaussTwoWindow(Screen):
    func = ObjectProperty(None)
    ul = ObjectProperty(None)
    ll = ObjectProperty(None)


    def button(self):
        try:
            function = lambda x: eval(self.func.text)
            # print(f"Function: {self.func.text}\nUpper Limit: {self.ul.text}\nLower Limit: {self.ll.text}")
            a, b = (float(eval(self.ul.text)) - float(eval(self.ll.text))) / 2, (float(eval(self.ul.text))
                                                                                 + float(eval(self.ll.text))) / 2
            # print(a,b)
            u1, u2 = -a / (3 ** 0.5) + b, a / (3 ** 0.5) + b
            # print(u1,u2)
            I = f"Integration of {self.func.text}\nwithin limits {self.ll.text} to {self.ul.text}\n" \
                f"using Gl2p Formula is:\n{a * (function(u1) + function(u2))}"

            self.func.text = ""
            self.ul.text = ""
            self.ll.text = ""
            show_popup(I)
        except:
            invalid_popup()


class GaussThreeWindow(Screen):
    func = ObjectProperty(None)
    ul = ObjectProperty(None)
    ll = ObjectProperty(None)

    def button(self):
        try:
            function = lambda x: eval(self.func.text)
            # print(f"Function: {self.func.text}\nUpperLimit: {self.ul.text}\nLower Limit: {self.ll.text}")
            a, b = (float(eval(self.ul.text)) - float(eval(self.ll.text))) / 2, (float(eval(self.ul.text))
                                                                                 + float(eval(self.ll.text))) / 2
            # print(a,b)
            u1, u2, u3 = a * (3 / 5) ** 0.5 + b, b, -a * (3 / 5) ** 0.5 + b
            # print(u1,u2)
            ans = ((5 / 9) * (function(u1)) + (8 / 9) * (function(u2)) + (5 / 9) * (function(u3))) * a
            I = f"Integration of {self.func.text}\nwithin limits {self.ll.text} to {self.ul.text}\nusing Gl3p" \
                f" Formula is:\n{ans}"
            self.func.text = ""
            self.ul.text = ""
            self.ll.text = ""
            show_popup(I)
        except:
            invalid_popup()


class TrapWindow(Screen):
    func = ObjectProperty(None)
    ul = ObjectProperty(None)
    ll = ObjectProperty(None)
    n = ObjectProperty(None)

    def button(self):
        try:
            function = lambda x: eval(self.func.text)
            # print(f"Function: {self.func.text}\nUpperLimit: {self.ul.text}\nLower Limit: {self.ll.text}\n"
            #       f"No. of Strips(n): {self.n.text}")
            sum = 0
            x1 = float(eval(self.ll.text))
            xn = float(eval(self.ul.text))
            n = int(self.n.text)
            h = (xn - x1) / n
            for i in range(1, n + 1):
                sum = sum + (h / 2) * (function(x1) + function(x1 + h))
                x1 += h
            I = f"Integration of {self.func.text}\nwithin limits {self.ll.text} to {self.ul.text}\nwith {n}" \
                f" no. of strips\nusing Trapezoidal Rule is:\n{sum}"
            self.func.text = ""
            self.ll.text = ""
            self.ul.text = ""
            self.n.text = ""
            show_popup(I)
        except:
            invalid_popup()


class SimpsonOneWindow(Screen):
    func = ObjectProperty(None)
    ul = ObjectProperty(None)
    ll = ObjectProperty(None)
    n = ObjectProperty(None)

    def button(self):
        try:
            function = lambda x: eval(self.func.text)
            # print(f"Function: {self.func.text}\nUpperLimit: {self.ul.text}\nLower Limit: {self.ll.text}\n"
            #       f"No. of Strips(n): {self.n.text}")
            sum = 0
            x1 = float(eval(self.ll.text))
            xn = float(eval(self.ul.text))
            n = int(self.n.text)
            h = (xn - x1) / n
            for i in range(1, n + 1, 2):
                sum = sum + function(x1) + 4 * function(x1 + h) + function(x1 + 2 * h)
                x1 += 2 * h
            I = f"Integration of {self.func.text}\nwithin limits {self.ll.text} to {self.ul.text}\nwith {n}" \
                f" no. of strips\nusing Simpson's 1/3rd Rule is:\n{sum * h / 3}"
            self.func.text = ""
            self.ll.text = ""
            self.ul.text = ""
            self.n.text = ""
            show_popup(I)
        except:
            invalid_popup()


class SimpsonThreeWindow(Screen):
    func = ObjectProperty(None)
    ul = ObjectProperty(None)
    ll = ObjectProperty(None)
    n = ObjectProperty(None)

    def button(self):
        try:
            function = lambda x: eval(self.func.text)
            sum = 0
            x1 = float(eval(self.ll.text))
            xn = float(eval(self.ul.text))
            n = int(self.n.text)
            h = (xn - x1) / n
            for i in range(1, n + 1, 3):
                sum = sum + function(x1) + 3 * function(x1 + h) + 3 * function(x1 + 2 * h) + function(x1 + 3 * h)
                x1 += 3 * h
            I = f"Integration of {self.func.text}\nwithin limits {self.ll.text} to {self.ul.text}\nwith {n}" \
                f" no. of strips\nusing Simpson's 3/8 Rule is:\n{sum * h * 3 / 8}"
            self.func.text = ""
            self.ll.text = ""
            self.ul.text = ""
            self.n.text = ""
            show_popup(I)
        except:
            invalid_popup()


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("main.kv")


class NmoApp(App):
    def build(self):
        self.icon = "./assets/icon.png"
        return kv


# def show_popup(I):
#     Popup(title="", content=Label(text=I, font_size = 15,size_hint=(None, None), size=(400,400)), size_hint=(None, None), size=(400, 400)).open()


def show_popup(I):
    # content = BoxLayout(orientation="vertical")
    content = GridLayout(cols = 1)
    label = Label(text=I, font_size=55, size_hint=(1, 1))
    content.add_widget(label)
    mybutton_cancel = CustomButton()
    content.add_widget(mybutton_cancel)

    mypopup = Popup(content = content,
        title = "Hello There!",
        auto_dismiss = False,
        size_hint = (0.8,0.8),
        background = 'atlas://data/images/defaulttheme/bubble')
    mybutton_cancel.bind(on_release=mypopup.dismiss)
    mypopup.open()


class CustomButton(Button):
    pass

def invalid_popup():
    t = "INVALID INPUT\nPLEASE TRY AGAIN"
    content = BoxLayout(orientation="vertical")
    content.add_widget(Label(text=t, font_size=55))
    mybutton_cancel = CustomButton()
    content.add_widget(mybutton_cancel)

    mypopup = Popup(content=content,
                    title="Oops!",
                    auto_dismiss=False,
                    size_hint=(0.8, 0.8),
                    background='atlas://data/images/defaulttheme/bubble')
    mybutton_cancel.bind(on_release=mypopup.dismiss)
    mypopup.open()


if __name__ == "__main__":
    NmoApp().run()
