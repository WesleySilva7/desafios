#DISTANCIA ENTRE RIBERÃO PRETO E FRANCA
distancia = 100 #km

#VELOCIDADE DO CARRO E CAMINHÃO EM KM
carro_velo = 110 #km
caminhao_velo = 80 #km

#TEMPO DO PEDAGIO 
tempo_pedagio = 5 #minutos

#CONVERTE O TEMPO DO PEDAGIO DE MINUTOS PARA HORAS, PARA SOMAR A VELOCIDADE DO CAMINHÃO
caminhao_velo_pedagio = caminhao_velo * (60 /(60 - tempo_pedagio))

#CALCULA O TEMPO QUE LEVARÃO PARA SE ENCONTRAREM
tempo_encontro = distancia / (carro_velo + caminhao_velo_pedagio)

#CALCULA A DISTANCIA QUE CADA VEICULO PERCORRERÁ ATÉ O ENCONTRO
carro_dist_encontro = tempo_encontro * carro_velo
caminhao_dist_encontro = tempo_encontro * caminhao_velo

#VERIFICA QUAL VEICULO ESTARÁ MAIS PROXIMO DE R. PRETO
if carro_dist_encontro > caminhao_dist_encontro:
    print('O Caminhão estará mais proximo de riberão preto no momento do encontro!')
else:
    print('O carro estará mais proximo de riberão preto no momento do encontro!')


#c) Explique como chegou no resultado.
#Chegamos nesse resultado atráves da fórmula de tempo = distancia/velocidade (V = v0 + a )
#a distancia entre as duas cidades é de 100km e os dois veiculos estão se aproximando em direções opostas
#podemos somar as velocidades do carro e do caminhão para ter a velocidade relativa dos dois

# velocidade relativa = velocidade do carro + velocidade do caminhão
# velocidade relativa = 110 + 80
# velocidade relativa = 190km
# atraves disso podemos calcular quanto tempo os dois veiculos levará para se encontrarem

# tempo = distancia / velocidade relativa
# tempo = 100 / 190
# tempo = 31,58 minutos

# o caminhão levara 10 minutos para passar os pedagio (5minutos cada)

# tempo total do caminhão = tempo + 10minutos 
# tempo total do caminhão = 31,58 + 0,1667
# tempo total do caminhão = 31,75 minutos

# O CAMINHÃO ESTÁ MAIS PROXIMO DE RIBERÃO PRETO






