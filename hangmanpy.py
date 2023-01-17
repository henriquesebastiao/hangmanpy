from random import random
import modules.random as random

tentaivas = 3
palavra = random.sorteiaPalavra()
palavraOculta = '_' * len(palavra)
print(palavraOculta)

while True:
    while True:
        letra = input('Informe uma letra: ')
        if len(letra) > 1:
            print('Ah espertinho. Voce não pode inserir mais de uma letra por vez.')
            print('Tente novamente.')
            print()
        else:
            break
    
    letra = letra.upper
    contador = 0
    for l in palavra:
        if l == letra:
            palavraOculta.replace(palavraOculta[contador], l)
        contador += 1
    
    print(palavraOculta)
    print()
    
    if '_' not in palavraOculta:
        break

print('Você conseguiu desvendar a palavra!')
print(palavraOculta)