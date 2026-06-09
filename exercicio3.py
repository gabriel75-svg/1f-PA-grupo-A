# Escrever um programa que o usuário digita um número de 1 a 20.
# O programa deverá fazer uma contagem regressiva;
# Não permitir que o usuário digite número maior que 20 ou menor que 1
# Imprimir uma mensagem "acabou a contagem" no final.
# Não permitir digitar letras.

try:
  contador = int (input("Digite um número de 0 a 20: "))

  while contador >= 0:
   print(contador)
   contador -=1
  print("Acabou a contagem!")
except:
  print("digite apenas números!")