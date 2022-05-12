# Regra: A figura deve ter os canais RBG, (X, Y, 3). Algumas figuras, na conversão da linha 10,
# ficam com valores abaixo de 1 em todos os píxels, caso isso aconteça cada ponto deve
# ser multiplicado por 100

import pylab
import matplotlib.pyplot as plt
import numpy as np
#Carrega e converte a Imagem para escala de cinza#
img = pylab.imread("img2.jpg")
img_gray = 0.299 * img[:,:,0] + 0.587 * img[:,:,1] + 0.114 * img[:,:,2]


##Função de Conversão de Quantização##
#essa função faz uma varredura na imagem de acordo com a quantidade de níveis especificados.
#Cada vez que ela detecta que aquele ponto específico está
#no intervalo daquele loop, ela converte  aquele píxel para o novo nível de cinza,
#reduzindo assim os níveis de cinza para o nível especificado.
def convert2gray(niveis,imagem):
    Imagem = np.zeros((len(imagem), int(np.size(imagem) / len(imagem))))
    for k in range(niveis):
        for i in range(len(imagem)):
            for j in range(int(np.size(imagem) / len(imagem))):
                 if imagem[i,j] < 256/niveis * (k+1) and imagem[i,j] >= 256*k/niveis:
                     Imagem[i, j] = 256*k/niveis
    return Imagem


#Criando um tensor para armazenamento das Imagens e aplicando a função#
imgs = np.zeros((len(img_gray), int(np.size(img_gray)/len(img_gray)),3))

imgs[:,:,0] = convert2gray(128,img_gray)
imgs[:,:,1] = convert2gray(32,img_gray)
imgs[:,:,2] = convert2gray(4,img_gray)


#Plota todas as figuras de uma vez#
f, axarr = plt.subplots(2,3)
axarr[0,1].imshow(img_gray,pylab.cm.gray)
axarr[0,1].set_title('256 Tons de Cinza')
axarr[1,0].imshow(imgs[:,:,0],pylab.cm.gray)
axarr[1,0].set_title('128 Tons de Cinza')
axarr[1,1].imshow(imgs[:,:,1],pylab.cm.gray)
axarr[1,1].set_title('32 Tons de Cinza')
axarr[1,2].imshow(imgs[:,:,2],pylab.cm.gray)
axarr[1,2].set_title('4 Tons de Cinza')
f.delaxes(axarr[0,0])
f.delaxes(axarr[0,2])
f.suptitle('Conversão de Quantização')
plt.show()

