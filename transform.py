import pandas as pd

def calc_horas(coluna_tempo_voo):
    """"
    
    Função para criar coluna_tempo_voo em minutos
    
    """
    return coluna_tempo_voo * 60


def classifica_turno(coluna_data_hora):
    hora = coluna_data_hora.hour  
    """
    Classificação com base nas faixas horárias
    """
    
    if 6 <= hora < 12:
        return "MANHÃ"
    elif 12 <= hora < 18:
        return "TARDE"
    elif 18 <= hora < 24:
        return "NOITE"
    else:
        return "MADRUGADA"
