import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib

link = '/Dannye_Zadanie.csv'
usd_eur_df = pd.read_csv('Dannye_Zadanie.csv', sep =';')
#print('Размер таблицы', usd_eur_df.shape)

new_columns_name = ['TICKER', 'PER',  'DATE', 'TIME', 'OPEN', 'HIGH', 'LOW', 'CLOSE']
usd_eur_df.set_axis(new_columns_name, axis='columns', inplace=True)
#print(usd_eur_df.head())

df_numeric = usd_eur_df.select_dtypes(include=[np.number])
#print(df_numeric)
#print(usd_eur_df.info())

#print('Всего дубликатов:', usd_eur_df.duplicated().sum())
#print(usd_eur_df.duplicated())

#print(usd_eur_df[usd_eur_df.duplicated()])

usd_eur_df = usd_eur_df.drop_duplicates()
#print(usd_eur_df[usd_eur_df.duplicated()])
#print(usd_eur_df.info())

usd_eur_df.loc[:, 'OPEN'] = pd.to_numeric(usd_eur_df.loc[:, 'OPEN'], errors = 'coerce')
#print(usd_eur_df.info())

#print(usd_eur_df.isnull().sum())

#print(usd_eur_df[usd_eur_df.isnull().any(axis=1)])

usd_eur_df = usd_eur_df.fillna(method = 'bfill')
#print(usd_eur_df.info())

#print(usd_eur_df.describe())

usd_eur_df.boxplot(column=['OPEN','HIGH','LOW','CLOSE'])
#plt.show()
#df_new  -----------------------------------------------------------------------

#print(df_new.info())

columns_int64 = df_new.select_dtypes(include=['int64'])
#print(columns_int64.dtypes)

columns_float64 = df_new.select_dtypes(include=['float64'])
#print(columns_int64.dtypes)

convert_columns_int64 = columns_int64.apply(pd.to_numeric, downcat = 'integer')
#print(convert_columns_int64.dtypes, '\n')

convert_columns_float64 = columns_float64.apply(pd.to_numeric, downcat = 'float')
#print(convert_columns_float64.dtypes, '\n')

columns_obj = df_new.select_dtypes(include=['object'])
#print(columns_obj.describe())

columns_ctg = columns_obj.astype('category')
#print(columns_ctg.info())

df_optim = df_new.copy()
df_optim[columns_ctg.columns] = columns_ctg
df_optim[convert_columns_int64.columns] = convert_columns_int64
df_optim[convert_columns_float64] = convert_columns_float64
#print(df_optim.head())

df_new = df_optim
#print(df_new.info())

df_date = df_new['DATE'].copy()
df_date = pd.to_datetime(df_date, format = '%y%m%d%', utc=False)
#print(type(df_date))
#print(df_date)

df_new['DATE'] = df_date
print(df_new.info())

df_new.to_csv('Clean data.csv', sep=';', index=False)