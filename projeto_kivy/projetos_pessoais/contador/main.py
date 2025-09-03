from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager


class tela_principal(Screen):
    
    def __init__(self, **kw):
        super().__init__(**kw)
    
        layout = BoxLayout(orientation='vertical', padding=10)
        
        texto = Label(
            text='Seja Bem vindo ao Contador'
        )
        layout.add_widget(texto)
        
        botao = Button(
            text='Ir para contador',
            size_hint=(1, 0.3)
        )
        
        botao.bind(on_press=self.ir_para_contador)
        
        layout.add_widget(botao)
        
        
        self.add_widget(layout)
        
    def ir_para_contador(self, instance):
        self.manager.current = 'contador'
        
    
    
    
class Tela_contador(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        
        layout = BoxLayout(orientation='vertical')
        self.texto = Label(
            text='0'
        )
        layout.add_widget(self.texto)
    
        botao_voltar = Button(
            text='voltar',
            size_hint=(1, 0.3)
            
        )
        botao_voltar.bind(on_press=self.voltar)
        
        
        
        layout2 = BoxLayout()
        botao_somar = Button(
            text='Adicionar',
            on_release=self.adicionar
        )
        
        botao_subtrair = Button(
            text='subtrair',
            on_release=self.subtrair
        )
        
        
        
        
        #adidionando os widgets no layout.
        layout2.add_widget(botao_somar)
        layout2.add_widget(botao_subtrair)
        layout.add_widget(botao_voltar)
        
        
        layout.add_widget(layout2)
        self.add_widget(layout)
    
    
    def voltar(self, instance):
        self.manager.current = 'principal'
        
    def adicionar(self, insance):
        
        self.texto.text = str(int(self.texto.text)+1)
    
    def subtrair(self, instance):
        self.texto.text = str(int(self.texto.text)-1)
        
        



class MeuApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(tela_principal(name='principal'))
        sm.add_widget(Tela_contador(name='contador'))
        
        return sm
    
MeuApp().run()