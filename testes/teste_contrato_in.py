import sys
import os
# Add the root directory of your project to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pandas as pd
import numpy as np
import pandera as pa
import pytest

from src.contrato import MetricasFinanceirasBase

def teste_contrato_correto():
    df_teste = pd.DataFrame({
        "setor_da_empresa": ["VND_A1B2C3", "REP_X7Y8Z9", "MNT_4D5E6F"],
        "receita_operacional": [1000, 1000, 1000],
        "data": ["2023-01-01", "2023-01-01", "2023-01-01"],
        "percentual_de_imposto": [0.1, 0.1, 0.1],
        "custos_operacionais": [200, 200, 200]
    })

    MetricasFinanceirasBase.validate(df_teste)

def teste_coluna_adicional():
    df_teste = pd.DataFrame({
        "setor_da_empresa": ["VND_A1B2C3", "REP_X7Y8Z9", "MNT_4D5E6F"],
        "receita_operacional": [1000, 1000, 1000],
        "data": ["2023-01-01", "2023-01-01", "2023-01-01"],
        "percentual_de_imposto": [0.1, 0.1, 0.1],
        "custos_operacionais": [200, 200, 200],
        "coluna_adicional": [0, 0, 0]
    })

    with pytest.raises(pa.errors.SchemaError):
        MetricasFinanceirasBase.validate(df_teste)

def teste_coluna_em_falta():
    df_teste = pd.DataFrame({
        "receita_operacional": [1000, 1000, 1000],
        "data": ["2023-01-01", "2023-01-01", "2023-01-01"],
        "percentual_de_imposto": [0.1, 0.1, 0.1],
        "custos_operacionais": [200, 200, 200],
        "coluna_adicional": [0, 0, 0]
    })

    with pytest.raises(pa.errors.SchemaError):
        MetricasFinanceirasBase.validate(df_teste)

def teste_valor_em_falta():
    df_teste = pd.DataFrame({
        "setor_da_empresa": [np.nan, "REP_X7Y8Z9", "MNT_4D5E6F"],
        "receita_operacional": [1000, 1000, 1000],
        "data": ["2023-01-01", "2023-01-01", "2023-01-01"],
        "percentual_de_imposto": [0.1, 0.1, 0.1],
        "custos_operacionais": [200, 200, 200]
    })

    with pytest.raises(pa.errors.SchemaError):
        MetricasFinanceirasBase.validate(df_teste)

def teste_setor_invalido():
    df_teste = pd.DataFrame({
        "setor_da_empresa": ["AAA_X7Y8Z9", "REP_X7Y8Z9", "MNT_4D5E6F"],
        "receita_operacional": [1000, 1000, 1000],
        "data": ["2023-01-01", "2023-01-01", "2023-01-01"],
        "percentual_de_imposto": [0.1, 0.1, 0.1],
        "custos_operacionais": [200, 200, 200]
    })

    with pytest.raises(pa.errors.SchemaError):
        MetricasFinanceirasBase.validate(df_teste)
    
def teste_receita_negativa():
    df_teste = pd.DataFrame({
        "setor_da_empresa": ["VND_A1B2C3", "REP_X7Y8Z9", "MNT_4D5E6F"],
        "receita_operacional": [-1000, 1000, 1000],
        "data": ["2023-01-01", "2023-01-01", "2023-01-01"],
        "percentual_de_imposto": [0.1, 0.1, 0.1],
        "custos_operacionais": [200, 200, 200]
    })

    with pytest.raises(pa.errors.SchemaError):
        MetricasFinanceirasBase.validate(df_teste)

def teste_data_invalida():
    df_teste = pd.DataFrame({
        "setor_da_empresa": ["VND_A1B2C3", "REP_X7Y8Z9", "MNT_4D5E6F"],
        "receita_operacional": [1000, 1000, 1000],
        "data": ["data invalida", "2023-01-01", "2023-01-01"],
        "percentual_de_imposto": [0.1, 0.1, 0.1],
        "custos_operacionais": [200, 200, 200]
    })

    with pytest.raises(pa.errors.SchemaError):
        MetricasFinanceirasBase.validate(df_teste)

def teste_porcentagem_imposto():
    df_teste = pd.DataFrame({
        "setor_da_empresa": ["VND_A1B2C3", "REP_X7Y8Z9", "MNT_4D5E6F"],
        "receita_operacional": [1000, 1000, 1000],
        "data": ["2023-01-01", "2023-01-01", "2023-01-01"],
        "percentual_de_imposto": [1.1, 0.1, 0.1],
        "custos_operacionais": [200, 200, 200]
    })

    with pytest.raises(pa.errors.SchemaError):
        MetricasFinanceirasBase.validate(df_teste)
        
def teste_custos_negativos():
    df_teste = pd.DataFrame({
        "setor_da_empresa": ["VND_A1B2C3", "REP_X7Y8Z9", "MNT_4D5E6F"],
        "receita_operacional": [1000, 1000, 1000],
        "data": ["2023-01-01", "2023-01-01", "2023-01-01"],
        "percentual_de_imposto": [0.1, 0.1, 0.1],
        "custos_operacionais": [-200, 200, 200]
    })

    with pytest.raises(pa.errors.SchemaError):
        MetricasFinanceirasBase.validate(df_teste)