import datetime

aniversario = datetime.date(2000, 5, 15)
print("Aniversário:", aniversario.strftime("%d/%m/%Y"))
horario_atual = datetime.datetime.now().time()
print("Horário atual:", horario_atual.strftime("%H:%M:%S"))
hoje = datetime.date.today()
diferenca = aniversario - hoje
print("Dias até o próximo aniversário:", diferenca.days)
data_hora_atual = datetime.datetime.now()
print("Data e hora atual:", data_hora_atual.strftime("%d/%m/%Y %H:%M:%S"))