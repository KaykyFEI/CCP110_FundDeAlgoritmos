def pode_doar(sexo, peso):
    sexo = padronizar_texto(sexo)
    if sexo == "HOMEM" and peso >= 60.0:
        return True
    elif sexo == "MULHER" and peso >= 50.0:
        return True
    else:
        return False
    
def padronizar_texto(texto):
    texto_formatado = texto.strip().upper()
    return texto_formatado

def processar_registro(linha):
    registro_processado = ""
    nome = ""
    sexo = ""
    peso = 0.0
    
    registro_processado = linha.split(";")
    
    nome = registro_processado[0].strip()
    sexo = padronizar_texto(registro_processado[1])
    peso = float(registro_processado[2].strip(" kg"))
    
    resultado = pode_doar(sexo, peso)
    if resultado:
        print("%s: Apto" % (nome) )
    else:
        print("%s: Inapto" % (nome))