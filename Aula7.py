# **Exercício 1:** Crie uma lista chamada numeros que contenha os números inteiros de 1 a 10 e imprima-a na tela.
lista_numeros = [1,2,3,4,5,6,7,8,9,10]
print(lista_numeros)
# **Exercício 2:** Acesse e imprima o terceiro elemento da lista `numeros`.
print (lista_numeros [2])
# **Exercício 3:** Adicione o número 9 à lista `numeros` e imprima a lista atualizada.
lista_numeros.append(9)
print(lista_numeros)
# **Exercício 4:** Remova o número 5 da lista `numeros` e imprima a lista resultante.
lista_numeros.remove(5)
print(lista_numeros)
# **Exercício 5:** Crie uma lista chamada carros contendo três nomes de carros diferentes. Em seguida, concatene essa lista com a lista `numeros` e imprima o resultado.  
lista_carros = ['x1','x2','x3']
print(lista_carros + lista_numeros)