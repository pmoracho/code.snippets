import pandas as pd
import numpy as np
import os


def find_row_from_question(df, start, end, questions):
    """find_row_from_question: Busca una pregunta entre un rango de filas
    """
    for i in range(start, end):
        row = df.loc[i]
        print("      *{0}* == *{1}*".format(row.Questions, questions))

        if row.Questions == questions:
            return i
    return  None

os.system("clear")

df1 = pd.read_csv('~/Descargas/QuestionBank.csv', low_memory=False)
df2 = pd.read_csv('~/Descargas/QuestionBank_31072020_1220.csv', low_memory=False)

#
A = df1[ ['Questions', 'QID', 'URL']].astype(str)
B = df2[['Questions', 'QID']].astype(str)
A['Questions'] = A['Questions'].str.strip()
B['Questions'] = B['Questions'].str.strip()

# Dividimos el QID de las subpreguntas en QID y número de subpregunta
B[['QID_N','nr']] = pd.DataFrame(B.QID.str.split('_',1).tolist(),columns = ['QID_N','nr'])

# N sera nuestro DF final consolidado
N = pd.DataFrame({'QID': pd.Series([], dtype='str'),
                  'QID_NEW': pd.Series([], dtype='str'),
                  'Questions': pd.Series([], dtype='str'),
                  'URL': pd.Series([], dtype='str'),
                  'A_row': pd.Series([], dtype='int'),
                  'B_row': pd.Series([], dtype='int')})
i, j = 0, 0
rows_A, rows_B = A.shape[0], B.shape[0]
rows_list = []
while (i < rows_A):

    #print("{0}/{1} --> *{2}* == *{3}*".format(i,j,row_A.Questions, row_B.Questions))

    row_A = A.loc[i]
    if not row_A.URL == 'nan' and not row_A.Questions == 'nan'  :
        print("---> {0}".format(row_A.Questions))
        index = find_row_from_question(B, j, rows_B, row_A.Questions)
        if index:
            row_B = B.loc[index]
            j = index
            # Preguntas coincidentes en ambas tablas
            # Preguntas coinicdentes que además tienen subpreguntas
            if "_" in row_B.QID:
                for _, row in B[B.QID == row_B.QID].iterrows():
                    d = {'QID': row_A.QID, 'QID_NEW': row.QID_N, 'Questions': row_B.Questions, 'URL': row_A.URL, 'A_row': i, 'B_row': j}
                    rows_list.append(d)
                    j = j + 1
            else:
                d = {'QID': row_A.QID, 'QID_NEW': row_B.QID_N, 'Questions': row_B.Questions, 'URL': row_A.URL, 'A_row': i, 'B_row': j}
                rows_list.append(d)
                j = j + 1

        else:
            # Preguntas en A que no existen en B
            d = {'QID': row_A.QID, 'QID_NEW': pd.NA, 'Questions': row_A.Questions, 'URL': row_A.URL, 'A_row': i, 'B_row': pd.NA}
            rows_list.append(d)
    else:
        # Preguntas con URL vacia que no existen en B
        d = {'QID': row_A.QID, 'QID_NEW': pd.NA, 'Questions': row_A.Questions, 'URL': pd.NA, 'A_row': i, 'B_row': pd.NA}
        rows_list.append(d)
    i += 1

    # if i >= 226:
    #     _ = input()


N = pd.DataFrame(rows_list)
N.to_csv("Salida.csv", sep=',')

# print(N.B_row == 'nan')
