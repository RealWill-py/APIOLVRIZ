import tkinter as tk

def say_hello():
    label["text"] = "Hello, World!"

# Criação da janela
window = tk.Tk()
window.title("Hello, World!")

# Criação do rótulo
label = tk.Label(window, text="Clique no botão para exibir a mensagem.")
label.pack(pady=10)

# Criação do botão
button = tk.Button(window, text="Clique aqui!", command=say_hello)
button.pack(pady=5)

# Execução da janela
window.mainloop()
