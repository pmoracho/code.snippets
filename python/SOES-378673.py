import pandas as pd
import numpy as np
import os

os.system("clear")

df1 = pd.read_csv('~/Descargas/QuestionBank.csv', low_memory=False)
df2 = pd.read_csv('~/Descargas/QuestionBank_31072020_1220.csv', low_memory=False)

A = df1[ ['Questions', 'QID', 'URL']].astype(str)
B = df2[['Questions', 'QID']].astype(str)
A['Questions'] = A['Questions'].str.strip()
B['Questions'] = B['Questions'].str.strip()

# Dividimos el QID de las subpreguntas en QID y número de subpregunta
B[['QID_B','nr']] = pd.DataFrame(B.QID.str.split('_',1).tolist(),columns = ['QID_B','nr'])


# 1. Preguntas en A que no están en B
A1 = A[~A.Questions.isin(B.Questions)].dropna()
A1 = A1[["Questions", "QID"]]
A1.columns = ["Questions", "QID_A"]
A1["QID_B"] = pd.NA
A1["QID_PADRE"] = pd.NA


# 2. Preguntas en A que están en B y no se repiten
A2 = A[A.Questions.isin(B.Questions)].dropna().groupby('Questions').filter(lambda x: len(x) == 1)
A2 = A2.merge(B, on = 'Questions', how='inner')[["Questions", "QID_x", "QID_y"]]
A2["QID_PADRE"] = pd.NA
A2.columns = ["Questions", "QID_A", "QID_B", "QID_PADRE"]

print(A2[7:10].QID_A.astype(int).max())
exit()

# 3. Preguntas en A que están en B y no se repiten y tienen subpreguntas
A3 = A2.merge(B[B["QID"].str.contains("_")], on = 'QID_B', how='inner')[["Questions_y", "QID_A", "QID_B", "QID"]]
A3["QID_A"] = pd.NA
A3 = A3[["Questions_y", "QID_A", "QID", "QID_B"]]
A3.columns = ["Questions", "QID_A", "QID_B", "QID_PADRE"]

# 4. Preguntas que se repiten las relacionamos si se puede de manera secuencial
A4 = pd.DataFrame(data=None, columns=A3.columns)
TMP = A[A.Questions.isin(B.Questions)].dropna().groupby('Questions').filter(lambda x: len(x) > 1)
batches = []
for _, r in TMP.iterrows():
    q = r.Questions

    a = A[A.Questions == q].reset_index()
    b = B[B.Questions == q].reset_index()

    rows_a, rows_b = a.shape[0], b.shape[0]
    if rows_a == rows_b:
        c = pd.merge(a, b, left_index=True, right_index=True)[["Questions_x", "QID_x", "QID_y"]]
        c["QID_PADRE"] = pd.NA
        c.columns = ["Questions", "QID_A", "QID_B", "QID_PADRE"]
        batches.append(c)

A4 = pd.concat(batches)


# Unimos los tres lotes
FINAL = pd.concat([A1, A2, A3, A4])
FINAL.to_csv("Salida.csv", sep=',')


UNION = FINAL.merge(df1.dropna(subset=['QID']), how="left", left_on="QID_A", right_on="QID")
UNION = UNION.merge(df2.dropna(subset=['QID']), how="left", left_on="QID_B", right_on="QID")
UNION.to_csv("Union.csv", sep=',')


