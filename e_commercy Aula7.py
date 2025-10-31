e_commerce = {
'livros':{


'ARARI':50.0,
'TALEB':70.0,  


},
'tablets':{
    'SAMSUMG':15000.55,
    'NOKIA':456.5,
},
'fones':{
   'JBL':500.0,
   'APPLE':750.0, 
},
'caixa de som':{
    'jbl':1000.0,
    'jbl plus':1600.0,
}

}



 
minhas_compras = {
'carrinho' : [],
'valores':[]
}



secao1 = input('livros, tablets, fones ou caixa de som ')
prod1 = input(f'{e_commerce[secao1]}')


secao2 = input('livros, tablets, fones ou caixa de som ')
prod2 = input(f'{e_commerce[secao2]}')


secao3 = input('livros, tablets, fones ou caixa de som ')
prod3 = input(f'{e_commerce[secao3]}')

secao4 = input('livros, tablets, fones ou caixa de som ')
prod4 = input(f'{e_commerce[secao4]}')

minhas_compras['carrinho'].append(prod1)
minhas_compras['valores'].append(e_commerce[secao1][prod1])
print(minhas_compras)


minhas_compras['carrinho'].append(prod2)
minhas_compras['valores'].append(e_commerce[secao2][prod2])
print(minhas_compras)


minhas_compras['carrinho'].append(prod3)
minhas_compras['valores'].append(e_commerce[secao3][prod3])
print(minhas_compras)

minhas_compras['carrinho'].append(prod4)
minhas_compras['valores'].append(e_commerce[secao4][prod4])
print(minhas_compras)

soma =  sum(minhas_compras['valores'])