from dataclasses import dataclass
import numpy as np
import time

start = time.time()

@dataclass
class Point:
    """
    um ponto é composto por 3 coordenadas (x,y,z)
    """
    x: float = None
    y: float = None
    z: float = None
    maior: bool = False

pArray = [] #empty array
size = 30      #number of loops
cArray = np.empty((size,size))

for i in range(size):  # appending empty objects
    """
    Percorre todo o array, setando ponto a ponto
    """
    p = Point()
    p.x = i*5.3
    p.y = 0.8+i
    p.z = 0.1*i
    p.maior = p.x > p.y
    pArray.append(p)

for i in range(size):
    for j in range(size):
        """
        Preenche o cArray inicialmente, que é um Array combinado
        """
        cArray[i][j] = i*0.3
        assert(print(cArray[i][j])==print(cArray[i][j]))
count1 = 0
count2 = 0
for k in range(size):
    if(pArray[k].maior == False):
        count1 += 1
        for i in range(size):
            for j in range(size):
                cArray[i][j] += k + (pArray[i].y*pArray[i].x)/(j+1)
                assert(print(cArray[i][j])==print(cArray[i][j]))
                """
                Operação de adição ao elemento i,j do array combinado
                """
    else:
        count2 += 1
        for i in range(size):
            for j in range(size):
                cArray[i][j] += k + (pArray[i].y*pArray[i].x)/(j+1)
                assert(print(cArray[i][j])==print(cArray[i][j]))
                """
                Operação de adição ao elemento i,j do array combinado
                """

end = time.time()

print(str(end - start) + "segundos")
