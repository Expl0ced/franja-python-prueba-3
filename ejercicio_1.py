import numpy as np
import random


def leer():
    numeros=[]
    with open('numeros_prueba.txt','r') as file:
        for linea in file:
            numeros.append(int(linea))

    print(numeros)

def escribir():
    for i in range(0,10):
        numero=random.randint(100,1000)
        with open('numeros_prueba.txt', 'a+', encoding='utf-8') as file:
            file.write(str(numero))
            file.write("\n")

def impares():
    impares=[]
    with open('numeros_prueba.txt', 'r') as file:
        linea=[linea.split() for linea in file]
        # como para cada digito se creo un lista, uso un comodin para poder extraer cada uno de esos de su respectiva lista y asi que solo queden como texto y transformarlos en int
        for comodin in linea:
            for impar in comodin:
                impar=int(impar)
                if impar % 2 != 0:
                    impares.append(impar)
                    
    impares=np.array(impares)
    print(impares)
    print('la dimension de la lista es: '+ str(impares.ndim))


def main():
    escribir()
    leer()
    impares()



if __name__ == '__main__':
    main()