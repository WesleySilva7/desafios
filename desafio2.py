# AQUI VAMOS SOLICITAR QUE DIGITE UM NUMERO

numero = int(input("Digite um número: "))

#DOIS PRIMEIROS VALORES DA SEQUENCIA FIBONACCI
a, b = 0, 1

#LOOP PARA CALCULAR A SEQUENCIA FIBONACCI
while b < numero:
    a, b = b, a + b

# AQUI IRA VERIFICAR SE O NUMERO PERTENCE OU NAO A SEQUENCIA FIBONACCI

if b == numero:
    print(f'O número {numero} pertence a sequencia fibonacci!!')
else:
    print(f'O número {numero} não pertence a sequencia fibonacci!!')