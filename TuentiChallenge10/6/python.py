import sys
import socket
import time
import random
import numpy as np
import matplotlib.pyplot as plt

hostname = "52.49.91.111"
port = 2003

#explorado = np.zeros((211,211))
explorado = np.load('mapa.npy')
pos = np.array([105,105])

val = {
    '1u2l' : np.array([-2,1]),
    '2u1l' : np.array([-1,2]),
    '2u1r' : np.array([1,2]),
    '1u2r' : np.array([2,1]),
    '1d2r' : np.array([2,-1]),
    '2d1r' : np.array([1,-2]),
    '2d1l' : np.array([-1,-2]),
    '1d2l' : np.array([-2,-1])
}
mov = ['4','7','9','6','3','.','0','1']

def movimientoPosible(i):
    if i not in list(val.keys()):
        return False
    global explorado
    global pos
    x = pos[0] + val[i][0]
    y = pos[1] + val[i][1]
    return explorado[x][y] !=1

def netcat(hn, p):
    global explorado
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((hn,p))
    time.sleep(0.5)
    data = sock.recv(1024)
    handleResponse(data,"")
    while True:
        i = getNCMessage()
        if i=='q':
            break
        elif i =='p' or i=='':
            plt.imshow(explorado.T)
            plt.gca().invert_yaxis()
            plt.show()
        elif movimientoPosible(i):
            print(f"Envia {i}")
            sock.sendall(i.encode())
            data = sock.recv(1024)
            if not data:
                break;
            handleResponse(data,i)

    sock.shutdown(socket.SHUT_WR)
    sock.close()
    np.save('mapa',explorado)


def getNCMessage():
    inp = input()
    if inp in mov:
        m = mov.index(inp)
        return list(val.keys())[m]
    else:
        return inp

#Devuelve False cuando error
def handleResponse(res,inp):
    global pos
    print(res.decode())
    lineas = list(filter(None,res.decode().split('\n')))
    #Comando no valido
    if len(lineas[0])>15:
        return False
    #Si hay input mueve la posicion
    if inp != "":
        pos+=val[inp]
    x, y = pos[0], pos[1]
    print(f"Posicion actual::{pos}")
    #Lo usa para calcular la posicion del primer simbolo
    yOffset = [2,1,0,-1,-2]
    for i in range(5):
        procesarLinea(np.array((x-2,y+yOffset[i])),lineas[i])


#posicion mas a la izquierda de la linea ->#####
def procesarLinea(pos,linea):
    global explorado
    x,y = pos[0],pos[1]
    for c in linea:
        if c=='#':
            explorado[x][y] = 1
        else:
            explorado[x][y] = 2
        x+=1

netcat(hostname, port)
