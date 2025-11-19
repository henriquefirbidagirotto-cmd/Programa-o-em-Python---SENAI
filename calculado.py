import tkinter as tk


def mostrar_resultado_soma():
    n1_ = float(n1.get())
    n2_ = float(n2.get())
    soma  = n1_ +  n2_
    resultado.config(text=soma) 

def mostrar_resultado_sub():
    n1_ = float(n1.get())
    n2_ = float(n2.get())
    sub  = n1_ -  n2_
    resultado.config(text=sub) 

def mostrar_resultado_mult():
    n1_ = float(n1.get())
    n2_ = float(n2.get())
    mult = n1_ *  n2_
    resultado.config(text=mult) 

def mostrar_resultado_div():
    n1_ = float(n1.get())
    n2_ = float(n2.get())
    div  = n1_ /  n2_
    resultado.config(text=div) 

def mostrar_resultado_por():
    n1_ = float(n1.get())
    n2_ = float(n2.get())
    por = n1_ %  n2_
    resultado.config(text=por) 

def mostrar_resultado_ele():
    n1_ = float(n1.get())
    n2_ = float(n2.get())
    ele = n1_ **  n2_
    resultado.config(text=ele) 
root = tk.Tk()
root.geometry('250x370')


n1_label =  tk.Label(root, text='N1', font=('arial',12))
n1_label.grid(pady=5, column=1, row =1 )

n1 =  tk.Entry(root, font=('arial',12))
n1.grid(row=1, column=2, padx=5)

n2_label =  tk.Label(root, text='N2', font=('arial',12))
n2_label.grid(pady=5, column=1, row =3 )

n2 =  tk.Entry(root, font=('arial',12))
n2.grid(row=3, column=2, padx=5)

btn_soma =  tk.Button(root, text= '+', font=('arial',10), command=mostrar_resultado_soma)
btn_soma.grid(row=5, column= 1, pady=5)

resultado =  tk.Label(root, text = '=', font=('arial',12))
resultado.grid(row = 7, column=2)

btn_soma =  tk.Button(root, text= '-', font=('arial',10), command=mostrar_resultado_sub)
btn_soma.grid(row=5, column= 2, pady=5)

resultado =  tk.Label(root, text = '=', font=('arial',12))
resultado.grid(row = 7, column=2)

btn_soma =  tk.Button(root, text= '*', font=('arial',10), command=mostrar_resultado_mult)
btn_soma.grid(row=5, column= 3, pady=5)

resultado =  tk.Label(root, text = '=', font=('arial',12))
resultado.grid(row = 7, column=2)

btn_soma =  tk.Button(root, text= '/', font=('arial',10), command=mostrar_resultado_div)
btn_soma.grid(row=6, column= 1, pady=5)

resultado =  tk.Label(root, text = '=', font=('arial',12))
resultado.grid(row = 7, column=2)

btn_soma =  tk.Button(root, text= '%', font=('arial',10), command=mostrar_resultado_por)
btn_soma.grid(row=6, column= 2, pady=5)

resultado =  tk.Label(root, text = '=', font=('arial',12))
resultado.grid(row = 7, column=2)

btn_soma =  tk.Button(root, text= '**', font=('arial',10), command=mostrar_resultado_ele)
btn_soma.grid(row=6, column= 3, pady=5)

resultado =  tk.Label(root, text = '=', font=('arial',12))
resultado.grid(row = 7, column=2)

root.mainloop()
