!/usr/bin/env python
coding: utf-8


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from IPython.core.interactiveshell import InteractiveShell

df_survey_schema = pd.read_csv('survey_results_schema.csv')

df_answers = pd.read_csv('survey_results_public.csv',
                         usecols = ['Respondent', 'Hobbyist', 'Age1stCode', 'YearsCode', 'YearsCodePro', 'CompFreq', 'ConvertedComp', 'WorkWeekHrs', 'Age', 'Student', 'BetterLife'],
                        index_col = ['Respondent'])
pd.options.display.max_columns = None
df_answers.head()

df_answers.shape

pd.unique(df_answers.Age1stCode)

df_answers.Age1stCode.replace(to_replace = {'Younger than 5 years': '4',
                                            'Older than 85': '85'}, inplace=True)

pd.unique(df_answers.Age1stCode)


df_answers.YearsCode.replace(to_replace = {'Less than 1 year': '1',
                                            'More than 50 years': '50'}, inplace=True)
pd.unique(df_answers.YearsCode)

pd.unique(df_answers.YearsCodePro)

df_answers.YearsCodePro.replace(to_replace = {'Less than 1 year': '1',
                                            'More than 50 years': '50'}, inplace=True)

pd.unique(df_answers.YearsCodePro)

pd.unique(df_answers.Age)

df_answers.loc[df_answers['CompFreq']=='Monthly', 'ConvertedComp'] = df_answers['ConvertedComp']*12

df_answers.loc[df_answers['CompFreq']=='Weekly', 'ConvertedComp'] = df_answers['ConvertedComp']*52

df_answers.drop('CompFreq', axis=1, inplace=True)

df_answers.head()

df_answers.dtypes

df_answers[['YearsCode', 'Age1stCode', 'YearsCodePro']] = df_answers[['YearsCode', 'Age1stCode', 'YearsCodePro']].astype('float64', copy=False)

df_answers.dtypes

df_answers.corr()

df_base = df_answers[['YearsCode', 'Age1stCode', 'YearsCodePro', 'ConvertedComp', 'WorkWeekHrs', 'Age']]
df_base.dropna()

df_base.corr()








