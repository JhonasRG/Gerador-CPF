
import random

nove_digitos = ''

for i in range(9):
   nove_digitos += str(random.randint(0, 9))

contador = 10
resultado_multiplicação = 0

for numero in nove_digitos:
   while contador >= 2:
      numero = int(numero)
      resultado_multiplicação += (numero * contador)
      contador -= 1
      break

digito = (resultado_multiplicação * 10) % 11
digito = digito if digito <= 9 else 0

resultado_mult_segundo_digito = 0
segundo_contador = 11
dez_digitos = nove_digitos + str(digito)

for numero2 in dez_digitos:
   while segundo_contador >= 2:
      numero2 = int(numero2)
      resultado_mult_segundo_digito += (numero2 * segundo_contador)
      segundo_contador -= 1
      break

segundo_digito = (resultado_mult_segundo_digito * 10) % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

CPF_Validado = f'{nove_digitos}{digito}{segundo_digito}'

print(CPF_Validado)