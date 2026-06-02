def pode_doar(sexo, peso):
    if sexo == "Homem" and peso >= 60.0:
        return True
    elif sexo == "Mulher" and peso >= 50.0:
        return True
    else:
        return False