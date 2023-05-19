# Alunos participantes (Julio Cesar Orso, Julinna Orso e Felipe Matheus da Rosa)

# Instalação do SQLite
pip install sqlite3

# Importações
import sqlite3
from tkinter import *
from tkinter import messagebox

# Criação da conexão com o banco de dados
conn = sqlite3.connect('funcionarios.db')
cursor = conn.cursor()

# Verifica se a tabela já existe
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='funcionarios'")
tableExists = cursor.fetchall()

# Cria a tabela funcionarios caso não exista
if not tableExists:
    cursor.execute('''CREATE TABLE funcionarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
                        data_nascimento TEXT,
                        salario REAL
                    )''')

# Função para inserir um novo funcionário
def inserir_funcionario():
    nome = nome_entry.get()
    data_nascimento = data_entry.get()
    salario = salario_entry.get()

    if nome == '' or data_nascimento == '' or salario == '':
        messagebox.showerror("Erro", "Preencha todos os campos")
        return

    try:
        salario = float(salario)
    except ValueError:
        messagebox.showerror("Erro", "Salário inválido")
        return

    cursor.execute("INSERT INTO funcionarios (nome, data_nascimento, salario) VALUES (?, ?, ?)",
                   (nome, data_nascimento, salario))
    conn.commit()
    messagebox.showinfo("Sucesso", "Funcionário inserido com sucesso")

    nome_entry.delete(0, END)
    data_entry.delete(0, END)
    salario_entry.delete(0, END)

# Função para atualizar um funcionário
def atualizar_funcionario():
    codigo = codigo_entry.get()
    nome = nome_entry.get()
    data_nascimento = data_entry.get()
    salario = salario_entry.get()

    if codigo == '' or nome == '' or data_nascimento == '' or salario == '':
        messagebox.showerror("Erro", "Preencha todos os campos")
        return

    try:
        codigo = int(codigo)
        salario = float(salario)
    except ValueError:
        messagebox.showerror("Erro", "Código ou salário inválido")
        return

    cursor.execute("UPDATE funcionarios SET nome=?, data_nascimento=?, salario=? WHERE id=?",
                   (nome, data_nascimento, salario, codigo))
    conn.commit()
    messagebox.showinfo("Sucesso", "Funcionário atualizado com sucesso")

    codigo_entry.delete(0, END)
    nome_entry.delete(0, END)
    data_entry.delete(0, END)
    salario_entry.delete(0, END)

# Função para excluir um funcionário
def excluir_funcionario():
    codigo = codigo_entry.get()

    if codigo == '':
        messagebox.showerror("Erro", "Digite o código do funcionário")
        return

    try:
        codigo = int(codigo)
    except ValueError:
        messagebox.showerror("Erro", "Código inválido")
        return

    cursor.execute("DELETE FROM funcionarios WHERE id=?", (codigo,))
    conn.commit()
    messagebox.showinfo("Sucesso", "Funcionário excluído com sucesso")

    codigo_entry.delete(0, END)

# Função para listar os funcionários
def listar_funcionarios():
    cursor.execute("SELECT * FROM funcionarios")
    funcionarios = cursor.fetchall()

    listagem_text.delete('1.0', END)

    for funcionario in funcionarios:
        listagem_text.insert(END, f"ID: {funcionario[0]}, Nome: {funcionario[1]}, Data de Nascimento: {funcionario[2]}, Salário: {funcionario[3]}\n")

# Função para consultar os funcionários
def consultar_funcionarios():
    codigo = codigo_entry.get()
    nome = nome_entry.get()
    data_nascimento = data_entry.get()
    salario = salario_entry.get()

    query = "SELECT * FROM funcionarios WHERE 1=1"

    if codigo != '':
        try:
            codigo = int(codigo)
            query += f" AND id={codigo}"
        except ValueError:
            messagebox.showerror("Erro", "Código inválido")
            return

    if nome != '':
        query += f" AND nome LIKE '%{nome}%'"

    if data_nascimento != '':
        query += f" AND data_nascimento='{data_nascimento}'"

    if salario != '':
        try:
            salario = float(salario)
            query += f" AND salario={salario}"
        except ValueError:
            messagebox.showerror("Erro", "Salário inválido")
            return

    cursor.execute(query)
    funcionarios = cursor.fetchall()

    listagem_text.delete('1.0', END)

    for funcionario in funcionarios:
        listagem_text.insert(END, f"ID: {funcionario[0]}, Nome: {funcionario[1]}, Data de Nascimento: {funcionario[2]}, Salário: {funcionario[3]}\n")

# Função para fechar a conexão com o banco de dados
def fechar_conexao():
    conn.close()
    root.destroy()

# Configuração da interface
root = Tk()
root.title("CRUD de Funcionários")

# Labels
Label(root, text="Código:").grid(row=0, column=0, sticky=W)
Label(root, text="Nome:").grid(row=1, column=0, sticky=W)
Label(root, text="Data de Nascimento:").grid(row=2, column=0, sticky=W)
Label(root, text="Salário:").grid(row=3, column=0, sticky=W)

# Campos de entrada
codigo_entry = Entry(root, width=30)
codigo_entry.grid(row=0, column=1, padx=10, pady=5)

nome_entry = Entry(root, width=30)
nome_entry.grid(row=1, column=1, padx=10, pady=5)

data_entry = Entry(root, width=30)
data_entry.grid(row=2, column=1, padx=10, pady=5)

salario_entry = Entry(root, width=30)
salario_entry.grid(row=3, column=1, padx=10, pady=5)

# Botões
Button(root, text="Inserir", command=inserir_funcionario).grid(row=4, column=0, padx=10, pady=5)
Button(root, text="Atualizar", command=atualizar_funcionario).grid(row=4, column=1, padx=10, pady=5)
Button(root, text="Excluir", command=excluir_funcionario).grid(row=4, column=2, padx=10, pady=5)
Button(root, text="Listar", command=listar_funcionarios).grid(row=5, column=0, padx=10, pady=5)
Button(root, text="Consultar", command=consultar_funcionarios).grid(row=5, column=1, padx=10, pady=5)
Button(root, text="Fechar", command=fechar_conexao).grid(row=5, column=2, padx=10, pady=5)

# Área de listagem
listagem_text = Text(root, width=40, height=10)
listagem_text.grid(row=6, column=0, columnspan=3, padx=10, pady=5)

root.mainloop()
