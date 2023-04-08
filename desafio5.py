#DIGITAR PARA INVERTER A STRING
string1 = input("Digite uma string para inverter: ")

#CRIA UMA STRING VAZIA, PARA GUARDAR A STRING INVERTIDA
string2_invertida = ''

#PEGANDO PELOS CARACTERES DA STRING1 DE TRAS PARA FRENTE, ADD CADA UM NA NOVA STRING
for i in range(len(string1)-1, -1,-1):
    string2_invertida += string1[i]

#AQUI SERA O RESULTADO DA STRING INVERTIDA
print("String invertida é", string2_invertida)
