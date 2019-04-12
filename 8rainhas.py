import numpy as np

a = 0

def diagonais(tab, x, y, i):
    if x+i < 8 and y+i < 8:
        if tab[x+i, y+i] == 1:
            return 1
    if x-i >= 0 and y+i < 8:
        if tab[x-i, y+i] == 1:
            return 1
    if x-i >= 0 and y-i >= 0:
        if tab[x-i, y-i] == 1:
            return 1
    if x+i < 8 and y-i >= 0:
        if tab[x+i, y-i] == 1:
            return 1
    return 0

def rainhas(x,y,tab):
    aux = 0
    if x == 8:
        global a
        a +=1
        print(a)
        print(tab)
        return 0
    for y in range(8):
        for i in range(8):
            if tab[x,i] == 1 or tab[i,y] == 1 or diagonais(tab, x, y, i) == 1:
                aux = 1
                break
        if aux == 0:
            tab[x,y] = 1
            if rainhas(x+1,0,tab) == 0:
                tab[x,y] = 0
            else:
                return 1
        aux = 0
    return 0

def rainhasEsquerda(x,y,tab):
    aux = 0
    if y == -1:
        global a
        a +=1
        print(a)
        print(tab)
        return 0
    for x in range(8):
        for i in range(8):
            if tab[x,i] == 1 or tab[i,y] == 1 or diagonais(tab, x, y, i) == 1:
                aux = 1
                break
        if aux == 0:
            tab[x,y] = 1
            if rainhasEsquerda(0,y-1,tab) == 0:
                tab[x,y] = 0
            else:
                return 1
        aux = 0
    return 0
def main():
    tab = np.zeros( (8,8) )
    
    x = 0
    y = 0
    rainhas(x,y,tab)

    tab = np.zeros( (8,8) )
    
    x = 0
    y = 7
    global a
    a = 0
    rainhasEsquerda(x,y,tab)        

if __name__ == "__main__":
    main()