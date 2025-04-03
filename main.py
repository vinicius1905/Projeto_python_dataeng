import pandas as pd
import sqlite3
from transform import classifica_turno, calc_horas
from data_clean import data_clean

def connect_to_db(db_name):
    """
    Função para conectar ao banco SQLite.
    """
    return sqlite3.connect(db_name)

def insert_df_to_db(df, conn, table_name):
    """
    Função para inserir o DataFrame na tabela do banco de dados.
    """
    df.to_sql(table_name, conn, if_exists='replace', index=False)

def process_data():
    """
    Função principal para orquestrar o processo de limpeza, transformação e inserção dos dados.
    """
    # Conectar ao banco SQLite
    conn = connect_to_db('trabalhofinal.db')

    try:
        # Gera o DataFrame a partir da função de limpeza
        df = data_clean()

        # Aplica as transformações no DataFrame
        df['tempo_voo_minutos'] = calc_horas(df['tempo_voo'])
        df['turno'] = df['data_hora'].apply(classifica_turno)

        # Inserir o DataFrame na tabela
        insert_df_to_db(df, conn, 'table_trabalho_final')

        print("Dados processados e inseridos com sucesso na tabela.")
    
    except Exception as e:
        print(f"Erro ao processar os dados: {e}")
    
    finally:
        # Fechar a conexão
        conn.close()

if __name__ == "__main__":
    process_data()


