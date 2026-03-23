def validar_hora(hora):
    try:
        h, m = map(int, hora.split(":"))
        return 0 <= h < 24 and 0 <= m < 60
    except:
        return False