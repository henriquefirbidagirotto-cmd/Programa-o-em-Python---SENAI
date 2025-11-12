import statistics as st

def estatistica(lista_notas):


    moda  =  st.mode(lista_notas)
    print(moda)

    media  =  st.mean(lista_notas)
    print(media) 

    desvio = st.stdev(lista_notas)
    print(desvio)

    