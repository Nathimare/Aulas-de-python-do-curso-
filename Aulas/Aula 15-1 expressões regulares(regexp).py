import re

def validar_email(email):
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$' #verifica se o email corresponde ao padrão
    if re.match(padrao,email):
        return True
    else:
        return False

email1 = "usuario@dominio.com"
email2 = "invalido@com"
print(validar_email(email1))
print(validar_email(email2))

print("-------------------------------------------------------")

texto = "Meu número de telefone é (123) 456-7890 e o outro é (987) 654-3210."
padrao2 = r'\(\d{3}\) \d{3}-\d{4}' #Essa expressão procura números entre aspas "(ddd) ddd-dddd"
numeros = re.findall(padrao2, texto) #Retorna todos os padrões correspondentes encontrados
print(numeros)

print("-------------------------------------------------------")

texto2 = "Python é uma linguagem de programação popular para desenvolvimento web."
padrao3 = r'Python'
novo_texto = re.sub(padrao3, 'JavaScript', texto2)
print(novo_texto)

print("-------------------------------------------------------")

texto3 = "Hoje é 19/07/2023 e amanhã será 20/07/2023"
padrao4 = r'\d{2}/\d{2}/\d{4}'
datas = re.findall(padrao4, texto3)
print(datas)