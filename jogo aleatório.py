import random
import numpy as np
import emoji

sorte = int (input ("digite o seu número da sorte:"))
x = np.random.randint(1,9,(1,))
if sorte == x :
    print(emoji.emojize("você ganhou :\U0001f929: "))
    print("número sorteado foi:",x)
else:
    print(emoji.emojize("Você perdeu :\U0001f92c:",))
    print("número sorteado foi:",x)
    