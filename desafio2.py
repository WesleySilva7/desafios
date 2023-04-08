# VAMOS CALCULAR FIBONACCI

def fibonacci(n):
fib_sequence = [a,b]

while b < n:
  a, b = b, a + b
  fib_sequence.append(b)
  
 return fib_sequence

# AQUI IRA PEDIR PARA O USUARIO DIGITAR UM NUMERO
numero = int(input("digite um número: "))

# AQUU IRÁ CALCULAR A SENQUENCIA DE FIBONACCI

sequencia_fibonacci = fibonacci(numero)

#AQUI IRA VERIFICAR SE O NUMERO PERTENCE OU NÃO A SEQUENCIA FIBONACCI

if numero in sequencia_fibonacci: 
  print(f'O numero {numero} pertence a sequencia fibonacci!')
 else:
  print(f' O numero {numero} não pertence a sequencia fibonacci!')

