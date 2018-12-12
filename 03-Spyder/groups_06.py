# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 07:27:09 2018

@author: USRSIG
"""

import pandas as pd
import os
import numpy as np
import math

data_frame_guardado = pd.read_pickle('C://Users//USRSIG//Documents//GitHub//eguez-sarzosa-vicente-adrian//03-Spyder//data//artwork_data_frame.pickle')

seccion_df = data_frame_guardado.iloc[49980:50019,:].copy()

## group by

df_agrupado = seccion_df.groupby('acquisitionYear')

type(df_agrupado)

for anio, data_frame_agrupado_de_artista in df_agrupado:
    print('Anio:{}'.format(anio))
    print(data_frame_agrupado_de_artista)
    # anio_minimo = data_frame_agrupado_de_artista['acquisitionYear'].min()
    # print(type(data_frame_agrupado_de_artista))
    # print("{}:{}".format(nombre_de_artista,anio_minimo))


def llenar_valores_vacios(series):
    valores_contados = series.value_counts()
    if valores_contados.empty:
        return series
    """   
    # 1) iterar y sumar los valores
    sumatoria = 0
    numero_nans = 0
    for valor in series:
        print(valor)
        print(type(valor))
        if type(valor) == str:
            sumatoria = sumatoria + int(valor)
        if type(valor) == float:
            numero_nans = numero_nans + 1
    print(sumatoria)
    
    # 2) Dividir para el numero de valores
    division = series.size - numero_nans
    valor_mas_utilizado = sumatoria / division
    print(valor_mas_utilizado)
    """
    print(valores_contados)
    print(valores_contados.index[0])
    nuevo_valor = series.fillna(valores_contados.index[0])
    return nuevo_valor

def transformar_df_por_artista(df):
    agrupado_por_artista = df.groupby('artist')
    arreglo_dataframes_por_grupo = []
    for nombre_artista, grupo in agrupado_por_artista:
        df_llenado = grupo.copy()
        # print(grupo['height'])  # Devuelve una serie
        # print(grupo['width'])
        df_llenado.loc[:,'medium'] = llenar_valores_vacios(grupo['medium'])
        # print(df_llenado)
        arreglo_dataframes_por_grupo.append(df_llenado)
    nuevo_df_lleno = pd.concat(arreglo_dataframes_por_grupo)
    return nuevo_df_lleno
        
    

seccion_df_transformada = transformar_df_por_artista(seccion_df)



df_agrupado_por_titulo = data_frame_guardado.groupby('title')


print(df_agrupado_por_titulo.size())
print(type(df_agrupado_por_titulo.size()))
titulos_contados = df_agrupado_por_titulo.size().sort_values(ascending = False)
print(titulos_contados)

condicion = lambda x: len(x.index)>1


dup_titles_df = df_agrupado_por_titulo.filter(condicion)

# print(dup_titles_df)
# print(type(dup_titles_df))

dup_titles_df.sort_values('title', inplace=True)
print(dup_titles_df.sort_values('title', inplace=True))













