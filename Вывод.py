from kivy.app import  App
from kivy.uix.textinput import  TextInput
from kivy.uix.button import Button
from kivy.config import  Config
from kivy.uix.gridlayout import GridLayout

Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '480')

class MyApp(App):


    def build(self):
        gr_all = GridLayout(size_hint = (1, 1), padding = [5,5,5,5], spacing = [5,5], cols = 2)
        gr1 = GridLayout(size_hint = (.75, 1),padding = [5,5,5,5], spacing = [5,5], cols = 1)
        gr2 = GridLayout(size_hint = (.25, 1),padding = [5,5,5,5], spacing = [10,10], cols = 1)
        gr_text = GridLayout(size_hint = (.75, .2),padding = [5,5,5,5], spacing = [10,5], cols = 1)
        gr123  = GridLayout(size_hint = (.75, .2), padding = [5,5,5,5], spacing = [10,5], cols = 3)
        gr456 = GridLayout(size_hint = (.75, .2), padding = [5,5,5,5], spacing = [10,5], cols = 3)
        gr789 = GridLayout(size_hint = (.75, .2), padding = [5,5,5,5], spacing = [10,5], cols = 3)
        gr0 = GridLayout(size_hint = (.75, .2), padding = [5,5,5,5], spacing = [10,5], cols = 3)


        self.text_input = TextInput( size_hint = (0.67, .25), font_size = 35)
        self.button0 = Button(text='0', on_press=self.click0, size_hint = (.19, .19))
        self.button1 = Button(text='1', on_press=self.click1, size_hint=(.19, .19))
        self.button2 = Button(text='2', on_press=self.click2, size_hint=(.19, .19))
        self.button3 = Button(text='3', on_press=self.click3, size_hint=(.19, .19))
        self.button4 = Button(text='4', on_press=self.click4, size_hint=(.19, .19))
        self.button5 = Button(text='5', on_press=self.click5, size_hint=(.19, .19))
        self.button6 = Button(text='6', on_press=self.click6, size_hint=(.19, .19))
        self.button7 = Button(text='7', on_press=self.click7, size_hint=(.19, .19))
        self.button8 = Button(text='8', on_press=self.click8, size_hint=(.19, .19))
        self.button9 = Button(text='9', on_press=self.click9, size_hint=(.19, .19))

        self.button_is = Button(text='=', on_press=self.click_is, size_hint=(.19, .19))
        self.button_point = Button(text='.', on_press=self.click_point, size_hint=(.19, .19))
        self.button_clean = Button(text='C', on_press=self.click_clean, size_hint=(.19, .19))
        self.button_plus = Button(text='+', on_press=self.click_plus, size_hint=(.19, .19))
        self.button_minus = Button(text='-', on_press=self.click_minus, size_hint=(.19, .19))
        self.button_umn = Button(text='*', on_press=self.click_umn, size_hint=(.19, .19))
        self.button_del = Button(text='/', on_press=self.click_del, size_hint=(.19, .19))

        gr1.add_widget(gr_text)
        gr1.add_widget(gr123)
        gr1.add_widget(gr456)
        gr1.add_widget(gr789)
        gr1.add_widget(gr0)

        gr_all.add_widget(gr1)
        gr_all.add_widget(gr2)


        gr2.add_widget(self.button_is)
        gr2.add_widget(self.button_plus)
        gr2.add_widget(self.button_minus)
        gr2.add_widget(self.button_del)
        gr2.add_widget(self.button_umn)

        gr_text.add_widget(self.text_input)

        gr123.add_widget(self.button1)
        gr123.add_widget(self.button2)
        gr123.add_widget(self.button3)

        gr456.add_widget(self.button4)
        gr456.add_widget(self.button5)
        gr456.add_widget(self.button6)

        gr789.add_widget(self.button7)
        gr789.add_widget(self.button8)
        gr789.add_widget(self.button9)

        gr0.add_widget(self.button0)
        gr0.add_widget(self.button_point)
        gr0.add_widget(self.button_clean)






        return gr_all

    def click0(self, event):
        if self.text_input.text == 'Number?':
           self.text_input.text = ''
        self.text_input.text += self.button0.text

    def click1(self, event):
        if self.text_input.text == 'Number?':
            self.text_input.text = ''
        self.text_input.text += self.button1.text

    def click2(self, event):
        if self.text_input.text == 'Number?':
           self.text_input.text = ''
        self.text_input.text += self.button2.text

    def click3(self, event):
        if self.text_input.text == 'Number?':
           self.text_input.text = ''
        self.text_input.text += self.button3.text

    def click4(self, event):
        if self.text_input.text == 'Number?':
           self.text_input.text = ''
        self.text_input.text += self.button4.text

    def click5(self, event):
        if self.text_input.text == 'Number?':
           self.text_input.text = ''
        self.text_input.text += self.button5.text

    def click6(self, event):
        if self.text_input.text == 'Number?':
           self.text_input.text = ''
        self.text_input.text += self.button6.text

    def click7(self, event):
        if self.text_input.text == 'Number?':
           self.text_input.text = ''
        self.text_input.text += self.button7.text

    def click8(self, event):
        if self.text_input.text == 'Number?':
           self.text_input.text = ''
        self.text_input.text += self.button8.text

    def click9(self, event):
        if self.text_input.text == 'Number?':
           self.text_input.text = ''
        self.text_input.text += self.button9.text

    def click_is(self, event):
        if self.text_input.text == '':
            self.text_input.text = 'Number?'
        else:
            if self.znak == '+':
                self.text_input.text = str(float(self.text_input.text)+ self.n1)
            if self.znak == '-':
                self.text_input.text = str(self.n1 - float(self.text_input.text))
            if self.znak == '*':
                self.text_input.text = str(float(self.text_input.text)*self.n1)
            if self.znak == '/':
                if self.text_input.text != '0':
                    self.text_input.text = str(self.n1/float(self.text_input.text))
                else:
                    self.text_input.text = 'Milana or Alina?'

    def click_point(self, event):
        self.text_input.text += self.button_point.text

    def click_clean(self, event):
        self.text_input.text = ''

    def click_plus(self, event):
        self.n1 = self.text_input.text
        self.znak = '+'
        if self.n1 == '':
            self.text_input.text = 'Number?'
        else:
            self.n1 = float(self.text_input.text)
            self.text_input.text = ''

    def click_minus(self, event):
        self.znak = '-'
        self.n1 = float(self.text_input.text)
        if self.n1 == '':
            self.text_input.text = 'Number?'
        self.text_input.text = ''

    def click_umn(self, event):
        self.znak = '*'
        self.n1 = float(self.text_input.text)
        if self.n1 == '':
            self.text_input.text = 'Number?'
        self.text_input.text = ''

    def click_del(self, event):
        self.znak = '/'
        self.n1 = float(self.text_input.text)
        if self.n1 == '':
            self.text_input.text = 'Number?'
        self.text_input.text = ''

if __name__ == '__main__':
    MyApp().run()

