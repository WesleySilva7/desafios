# PRIMEIRA QUESTÃO a) 1, 3, 5, 7, ___
questao_a = [1,3,5,7]
proximo_elemento_a = questao_a [-1] + 2
print(f'O proximo número da questão a): {proximo_elemento_a}')

#SEGUNDA QUESTÃO b) 2, 4, 8, 16, 32, 64, __
questao_b = [2,4,8,16,32,64]
proximo_elemento_b = questao_b [-1] * 2
print(f'O proximo número da questão b): {proximo_elemento_b}')

#TERCEIRA QUESTÃO c) 0, 1, 4, 9, 16, 25, 36, __
questao_c = [0,1,4,9,16,25,36]
indice_c = len(questao_c) + 1
proximo_elemento_c = indice_c ** 2
print(f'O proximo número da questão c): {proximo_elemento_c}')

#QUARTA QUESTÃO d) 4, 16, 36, 64, __
questao_d = [4,16,36,64]
ultimo_elemente_d = questao_d [-1]
proximo_elemento_d = ultimo_elemente_d + (len(questao_d) *4)
print(f'O proximo número da questão d): {proximo_elemento_d}')

#QUINTA QUESTÃO e) 1, 1, 2, 3, 5, 8, __
questao_e = [1,1,2,3,5,8]
proximo_elemento_e = questao_e [-1] + questao_e [-2]
print(f'O proximo número da questão e): {proximo_elemento_e}')

#SEXTA QUESTÃO f) 2,10, 12, 16, 17, 18, 19, __
questao_f = [2,10,12,16,17,18,19]
proximo_elemento_f = questao_f [-1] + 1
if len(questao_f) %3 == 0:
    proximo_elemento_f += 4
elif len(questao_f) %3 == 1:
    proximo_elemento_f += 2
else:
    proximo_elemento_f += 1
print(f'O proximo número da questão f): {proximo_elemento_f}')

