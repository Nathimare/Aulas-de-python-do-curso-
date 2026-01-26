#Desafio 04
#Criar um script que leia algo pelo teclado o seu tipo primitivo e todas as informações possíveis sobre ele.
print("===== DESAFIO 04 =====")
p = input("Digite algo: ")
print("Sua palavra:", p)
print("É do tipo:",type(p))

print("É alfabético?",p.isalpha())
print("É númerico?",p.isnumeric())
print("É alfanúmerico?",p.isalnum())
print("Esta em minúsculo?",p.islower())
print("Esta em maiúsculo?",p.isupper())
print("Ésta capitalizada?",p.istitle())