from datetime import datetime
import re

def validar_data(data_str):

    padrao = r'^\d{4}-\d{2}-\d{2}$'

    if not re.match(padrao, data_str):
        print("A data inserida não corresponde ao formato requerido (ano-mês-dia), tente novamente.")
        return None

    try:
        return datetime.strptime(data_str, "%Y-%m-%d").date()
    except ValueError:
        print("Data inválida, tente novamente.")
        return None