import sqlite3


con = sqlite3.connect("meu_banco.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS alunos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    idade INT,
    curso TEXT
);
""")


cur.execute("INSERT INTO alunos (nome, idade, curso) VALUES (?, ?, ?)", ("Maria", 20, "Informática"))
cur.execute("INSERT INTO alunos (nome, idade, curso) VALUES (?, ?, ?)", ("João", 22, "Redes"))


con.commit()


cur.execute("SELECT * FROM alunos")
dados = cur.fetchall()
for linha in dados:
    print(linha)


