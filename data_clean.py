import pandas as pd
import datetime
import numpy as np
import re

def padroniza_str(obs):
    return re.sub('[^A-Za-z0-9]+', '', obs.upper())


def data_clean():


    df = pd.read_csv(
        "https://raw.githubusercontent.com/JackyP/testing/master/datasets/nycflights.csv",
        index_col=0
        )
    df.head()


    usecols=["year", "month",  "day", "hour", "minute","arr_delay","carrier","flight","air_time","distance", "origin", "dest"]

    df_raw = df.loc[
        (~df["carrier"].isna()) \
        & (~df["flight"].isna()) \
        & (~df["year"].isna()) \
        & (~df["hour"].isna()) \
        & (~df["minute"].isna()) \
        & (~df["month"].isna()) \
        & (~df["day"].isna()) \
        & (df["air_time"] > 0)
    ].loc[:, usecols]


    df_raw.drop_duplicates(inplace=True)


    df_raw = df_raw.astype("object")


    tmp = df.loc[:, usecols].copy()
    tmp = tmp[tmp["air_time"]>0]
    for col in ["carrier","flight", "year", "month", "day" ,"hour", "minute"]:
        tmp_df = tmp.loc[~df[col].isna()]
        tmp = tmp_df.copy()


    tmp.drop_duplicates(inplace=True)   

    tmp.shape[0] == df_raw.shape[0]


    df_raw["date_time"] =  pd.to_datetime(df_raw[["year", "month", "day", "hour", "minute"]],  dayfirst=True)


    usecols2 =["date_time", "arr_delay","carrier","flight","air_time","distance", "origin", "dest" ]


    new_columns = ["data_hora", "atraso_chegada", "companhia", "id_voo","tempo_voo", "distancia", "origem", "destino"]


    columns_map = {usecols2[i]: new_columns[i] for i in range(len(usecols2))}
    columns_map


    df_work = df_raw.loc[:, usecols2].copy()
    df_work.rename(columns=columns_map, inplace=True)
    df_work.head()


    df_work["distancia"] = df_work.loc[:,"distancia"].astype(float)
    df_work["companhia"] = df_work.loc[:,"companhia"].astype(str)
    df_work["id_voo"] = df_work.loc[:,"id_voo"].astype(str)
    df_work["atraso_chegada"] = df_work.loc[:,"atraso_chegada"].astype(str)
    df_work["origem"] = df_work.loc[:,"origem"].astype(str)
    df_work["destino"] = df_work.loc[:,"destino"].astype(str)
   


    df_work["companhia"] = df_work.loc[:,"companhia"].apply(lambda x: padroniza_str(x))
    df_work["id_voo"] = df_work.loc[:,"id_voo"].apply(lambda x: padroniza_str(x))
    df_work["origem"] = df_work.loc[:,"origem"].apply(lambda x: padroniza_str(x))
    df_work["destino"] = df_work.loc[:,"destino"].apply(lambda x: padroniza_str(x))

    # df_work.to_csv("base_tratada.csv", index=False)

    return df_work