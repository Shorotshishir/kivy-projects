from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

from os import listdir

kv_path = './kv/'
for kv in listdir(kv_path):
    Builder.load_file(kv_path + kv)


class Container(GridLayout):
    dp = ObjectProperty()

    def add_one(self):
        value = int(self.dp.text)
        self.dp.text = str(value + 1)

    def subtract_one(self):
        value = int(self.dp.text)
        self.dp.text = str(value - 1)

    def multiply(self):
        value = (int(self.dp.text) - 1) * (int(self.dp.text) + 1)
        self.dp.text = str(value)


class AddButton(Button):
    pass


class MultiplyButton(Button):
    pass


class SubtractButton(Button):
    pass


class MainApp(App):
    def build(self):
        self.title = "My Test APP"
        return Container()


if __name__ == '__main__':
    app = MainApp()
    app.run()
