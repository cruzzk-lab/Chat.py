import tkinter as tk

def responder():
    usuario = entrada.get()
    if usuario.strip() == "":
        return
    
    caixa_texto.insert(tk.END, f"Você: {usuario}\n")
    entrada.delete(0, tk.END)

    resposta = gerar_resposta(usuario)
    caixa_texto.insert(tk.END, f"Bot: {resposta}\n")

def gerar_resposta(mensagem):
    mensagem = mensagem.lower()

    if "oi" in mensagem or "olá" in mensagem:
        return "Oi! ta feliz hoje?"
    elif "não estou feliz" in mensagem:
        return "eita que barra, melhoras 🫂"
    elif "feliz" in mensagem:
        return "que foda"
    elif "tchau" in mensagem:
        return "Tchauzinho! Volta logo, viu? 👋"
    else:
        return "Ainda estou aprendendo, mas quero muito conversar com você!"


janela = tk.Tk()
janela.title("discord")
janela.geometry("400x400")


caixa_texto = tk.Text(janela, height=20, width=50)
caixa_texto.pack(pady=10)


entrada = tk.Entry(janela, width=40)
entrada.pack(side=tk.LEFT, padx=10)


botao = tk.Button(janela, text="Enviar", command=responder)
botao.pack(side=tk.LEFT)

janela.mainloop()
