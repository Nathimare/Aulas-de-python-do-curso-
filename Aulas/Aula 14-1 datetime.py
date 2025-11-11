import datetime

data_hora_atual = datetime.datetime.now()
print("Data e Hora Atual:", data_hora_atual)
print("-------------------------------------------------------")

#Calculando a diferença entre datas:
data1 = datetime.date(2023, 7, 1)
data2 = datetime.date(2023, 7, 15)
diferenca = data2 - data1
print("Diferença de Dias:", diferenca.days)
print("-------------------------------------------------------")

#como formatar uma data e hora de forma legível:
data_hora_atual2 = datetime.datetime.now()
formato = "%d/%m/%Y %H:%M:%S"
data_hora_formatada = data_hora_atual2.strftime(formato)
print("Data e Hora Formatada:", data_hora_formatada)
print("-------------------------------------------------------")

#Como somar um periodo de tempo a uma data:
data_atual = datetime.date.today()
um_ano = datetime.timedelta(days=365)
data_futura = data_atual + um_ano
print("Data daqui a um ano:", data_futura)
print("-------------------------------------------------------")

#Como extrair informações específicas de uma data:
data_hora_atual3 = datetime.datetime.now()
ano = data_hora_atual3.year
mes = data_hora_atual3.month
dia = data_hora_atual3.day
print(f"Ano: {ano}, Mês: {mes}, Dia: {dia}")