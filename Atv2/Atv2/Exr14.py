palavra = input("Digite uma palavra: ")

num_vogais = 0
for letra in palavra:
    if letra in "aeiouAEIOU":
        num_vogais += 1

caractere_substituto = input("Digite um caractere (vogal ou consoante) para substituir as vogais: ")

palavra_sem_vogais = palavra.replace('a,e,i,o,u')

print(f"A palavra '{palavra}' tem {num_vogais} vogais.")
print(f"A palavra '{palavra}' sem vogais é '{palavra_sem_vogais}'.")
