#Manutenção Perfectiva
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


#Adiciona um feddback quando clicar no botão, melhorando a usabilidade
class PerfectivaApp(App):
    def build(self):
        self.lbl = Label(text="Clique no botão")
        botao = Button(text="clique aqui", on_press=self.feedback)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.lbl)
        layout.add_widget(botao)
        return layout

    def feedback(self, instance):
        self.lbl.text = "Você clicou no botão"

PerfectivaApp().run()
