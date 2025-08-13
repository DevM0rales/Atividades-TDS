from kivy.uix.accordion import StringProperty
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class MeuWidget(BoxLayout):
    """
    MyWidget é um widget simples que ecibe uma saudacao usando uma StringProperty
    A interface do usuario é definida no arquivo kv associado.
    """
    
    #Declara uma StringProperty chamada 'saudacao com um valor inicial.
    #StringProperty é usada para armazenar e gerenciar strings que podem 
    #observadas por outros elementos da UI ou lógica do aplicativo.
    saudacao = StringProperty("Ola, Kivy!")
    
    def __init__(self, **kwargs):
        """
        Contrutor para MyWidget.
        """
    
        super().__init__(**kwargs)
        
        #nenhuma lógica de UI é definida diretamente aqui, pois o layout 
        #Seráo feitos no arquivo kv(String_Prop_app.kv)
        #
        
class StringProApp(App):
    
    
    def build(self):
        return MeuWidget()
    
    
StringProApp().run()
