#Manutenção Corretiva

from kivy.app import App
from kivy.uix.button import Button



class TesteApp(App):
    def build(self):
        # Antes causava erro porque chamava função inexistente
        # return Button(text="Clique aqui", on_press=self.funcao)

        # Correção: agora chama uma função válida
        return Button(text="Clique aqui", on_press=self.mostrar_msg)#Aqui estava o erro, onde a funcao chamada não era encontrada

    def mostrar_msg(self, instance):
        print("Botão clicado!")

TesteApp().run()
