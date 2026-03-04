
pontuacao = 0

ligacao = input("Telefonou para a vítima? (S(im) / N(ão))")
local = input("Esteve no local do crime? S(im) / N(ão)")
distancia = input("Mora perto da vítima? S(im) / N(ão)")
divida = input("Devia para a vítmia? S(im) / N(ão)")
trabalho = input("Já trabalhou com a vítima? S(im) / N(ão)")

if ligacao == "S" or ligacao =="Sim" or ligacao == "s" or ligacao == "sim":
    pontuacao = pontuacao + 1
else:
    pontuacao = pontuacao - 1

if local == "S" or local == "Sim" or local == "s" or local == "sim":
    pontuacao = pontuacao + 1
else:
    pontuacao = pontuacao - 1

if distancia == "S" or distancia == "Sim" or distancia == "s" or distancia == "sim":
    pontuacao = pontuacao + 1
else:
    pontuacao = pontuacao + 1