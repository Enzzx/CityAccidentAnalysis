import pandas as pd
import os
import glob

def join_csvs(files):
    dfs = []
    for f in files:
        df = pd.read_csv(f, sep=";", encoding="latin1")
        dfs.append(df)

    return pd.concat(dfs, ignore_index=True, sort=False)

pessoas = join_csvs(["data/pessoas_2015-2021.csv", "data/pessoas_2022-2025.csv"])
pessoas.to_csv("data/pessoas_completo.csv", index=False)

sinistros = join_csvs(["data/sinistros_2015-2021.csv", "data/sinistros_2022-2025.csv"])
sinistros.to_csv("data/sinistros_completo.csv", index=False)

veiculos = join_csvs(["data/veiculos_2015-2021.csv", "data/veiculos_2022-2025.csv"])
veiculos.to_csv("data/veiculos_completo.csv", index=False)