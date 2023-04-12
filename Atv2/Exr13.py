string = input("Digite uma string: ")
vogais = "aeiou"
string_sem_vogais = ""

for letra in string:
    if letra not in vogais:
        string_sem_vogais += letra

print(string_sem_vogais)
