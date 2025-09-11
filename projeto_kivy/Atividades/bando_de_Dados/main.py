import sqlite3
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

Window.clearcolor = (0.7, 0.7, 0.7, 1)


# --- BANCO ---
class DB:
    def __init__(self):
        self.run("""CREATE TABLE IF NOT EXISTS filmes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT, genero TEXT, ano INTEGER)""")

    def run(self, q, p=(), fetch=False):
        con = sqlite3.connect("filmes.db"); cur = con.cursor()
        cur.execute(q, p); data = cur.fetchall() if fetch else None
        con.commit(); con.close(); return data

    def add(self, titulo, genero, ano): self.run("INSERT INTO filmes (titulo,genero,ano) VALUES (?,?,?)",(titulo,genero,ano))
    
    def all(self): return self.run("SELECT * FROM filmes ORDER BY id DESC", fetch=True)
    
    def get(self, id): return self.run("SELECT * FROM filmes WHERE id=?", (id,), True)[0]
    
    def upd(self, id, titulo, genero, ano): self.run("UPDATE filmes SET titulo=?,genero=?,ano=? WHERE id=?", (titulo, genero, ano, id))
    
    def del_(self, id): self.run("DELETE FROM filmes WHERE id=?", (id,))


def campo(lbl, widget):
    layout = BoxLayout(orientation='vertical')
    layout.add_widget(Label(text=lbl))
    layout.add_widget(widget)
    return layout


# --- TELAS ---
class Cadastro(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.t, self.g, self.a = TextInput(), TextInput(), TextInput(input_filter="int")
        layout = BoxLayout(orientation="vertical")
        layout.add_widget(Label(text="Novo Filme"))
        
        
        for lbl, campo_w in [("Título:", self.t), ("Gênero:", self.g), ("Ano:", self.a)]:
            layout.add_widget(campo(lbl, campo_w))
        bts = BoxLayout(orientation='vertical')
        
        
        bts.add_widget(Button(text="Salvar", on_release=lambda x:self.salvar(), color=(0.5, 1, 0.5, 1)))
        bts.add_widget(Button(text="Cancelar", on_release=lambda x:self.cancelar(), color=(1, 0.5, 0.5, 1)))
        layout.add_widget(bts)
        self.add_widget(layout)

    def salvar(self):
        if self.t.text and self.g.text:
            App.get_running_app().db.add(self.t.text, self.g.text, int(self.a.text) if self.a.text else None)
            self.cancelar()

    def cancelar(self):
        self.t.text=self.g.text=self.a.text=""
        self.manager.get_screen("lista").carregar()
        self.manager.current="lista"


class Lista(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.box = BoxLayout(orientation="vertical")
        self.box.bind(minimum_height=self.box.setter("height"))
        layout = BoxLayout(orientation="vertical")
        cabecalho = BoxLayout(orientation='vertical')
        
        cabecalho.add_widget(Label(text="Filmes", font_size=24, color=(0.5, 1, 0.5, 1), font_name='Roboto-Bold.ttf'))
        cabecalho.add_widget(Button(text="Novo", on_release=lambda x:self.novo()))
        layout.add_widget(cabecalho)
        s = ScrollView()
        s.add_widget(self.box)
        layout.add_widget(s)
        self.add_widget(layout)

    def on_enter(self): self.carregar()

    def carregar(self):
        self.box.clear_widgets()
        for id,t,g,a in App.get_running_app().db.all():
            layout = BoxLayout()
            layout.add_widget(Label(text=f"{t} ({a or '?'}) - {g}"))
            layout.add_widget(Button(text="Editar", on_release=lambda x,i=id:self.editar(i)))
            layout.add_widget(Button(text="Excluir", on_release=lambda x,i=id:self.excluir(i)))
            self.box.add_widget(layout)

    def novo(self): self.manager.current="cadastro"
    def editar(self, id): App.get_running_app().abrir_edicao(id)
    def excluir(self, id): App.get_running_app().db.del_(id); self.carregar()


class Edicao(Cadastro):
    def carregar(self, id):
        self.id, t, g, a = App.get_running_app().db.get(id)
        self.t.text, self.g.text, self.a.text = t, g, str(a) if a else ""

    def salvar(self):
        App.get_running_app().db.upd(self.id, self.t.text, self.g.text, int(self.a.text) if self.a.text else None)
        self.cancelar()


class FilmesApp(App):
    def build(self):
        self.db = DB()
        sm = ScreenManager()
        sm.add_widget(Lista(name="lista"))
        sm.add_widget(Cadastro(name="cadastro"))
        sm.add_widget(Edicao(name="edicao"))
        return sm

    def abrir_edicao(self, id):
        tela = self.root.get_screen("edicao")
        tela.carregar(id)
        self.root.current="edicao"


FilmesApp().run()

