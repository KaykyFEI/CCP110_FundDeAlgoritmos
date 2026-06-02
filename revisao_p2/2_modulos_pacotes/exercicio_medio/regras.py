def pode_doar(sexo, peso):
    if sexo == "HOMEM" and peso >= 60.0:
        return True
    elif sexo == "MULHER" and peso >= 50.0:
        return True
    else:
        return False
    
def padronizar_texto(texto):
    texto_formatado = texto.strip().upper()
    return texto_formatado