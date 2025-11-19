import tkinter as tk

def nome_1_nome():
    nome_ = nome.get()
    print(nome_)


    idade_ = idade.get()
    print(idade_)


    email_ = email.get()
    print(email_)


    Endereço_ = Endereço.get()
    print(Endereço_)


    Celular_ = Celular.get()
    print(Celular_)


    Cep_ = Cep.get()
    print(Cep_)


    Cidade_ = Cidade.get()
    print(Cidade_)


    Cursos_ = Cursos.get()
    print(Cursos_)
root = tk.Tk()
root.geometry('560x750')

nome_label = tk.Label(root, text='Nome', font=('arial',12))
nome_label.grid(pady=5, column=1, row =1 )

nome =  tk.Entry(root, font=('arial',12))
nome.grid(row=1, column=2, padx=5)

idade_label = tk.Label(root, text='Idade', font=('arial',12))
idade_label.grid(pady=5, column=1, row =10 )

idade =  tk.Entry(root, font=('arial',12))
idade.grid(row=10, column=2, padx=5)

email_label = tk.Label(root, text='Email', font=('arial',12))
email_label.grid(pady=5, column=1, row =15 )

email =  tk.Entry(root, font=('arial',12))
email.grid(row=15, column=2, padx=5)

Endereço_label = tk.Label(root, text='Endereço', font=('arial',12))
Endereço_label.grid(pady=5, column=1, row =20 )

Endereço =  tk.Entry(root, font=('arial',12))
Endereço.grid(row=20, column=2, padx=5)

Celular_label = tk.Label(root, text='Celular', font=('arial',12))
Celular_label.grid(pady=5, column=60, row =1 )

Celular =  tk.Entry(root, font=('arial',12))
Celular.grid(row=1, column=80, padx=5)

Cep_label = tk.Label(root, text='Cep', font=('arial',12))
Cep_label.grid(pady=5, column=60, row =10 )

Cep =  tk.Entry(root, font=('arial',12))
Cep.grid(row=10, column=80, padx=5)

Cidade_label = tk.Label(root, text='Cidade', font=('arial',12))
Cidade_label.grid(pady=5, column=60, row =15 )

Cidade =  tk.Entry(root, font=('arial',12))
Cidade.grid(row=15, column=80, padx=5)

Cursos_label = tk.Label(root, text='Cursos', font=('arial',12))
Cursos_label.grid(pady=5, column=60, row =20 )

Cursos =  tk.Entry(root, font=('arial',12))
Cursos.grid(row=20, column=80, padx=5)

btn_idade =  tk.Button(root, text= 'Enviar', font=('arial',15), command=nome_1_nome)
btn_idade.grid(row=90, column= 3, pady=5)

resultado =  tk.Label(root, text = '', font=('arial',12))
resultado.grid(row = 100, column=3)

root.mainloop()