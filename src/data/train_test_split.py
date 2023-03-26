import pandas as pd
import numpy as np

df = pd.read_csv("data/processed/current_data.csv", sep=",", header=0)

stevilo = df.shape[0]
stTest = int(stevilo*0.10)
stTrain = stevilo-stTest

dfTest = df.head(stTest)
dfTrain = df.tail(stTrain)

dfTest.to_csv('data/processed/test.csv')
dfTrain.to_csv('data/processed/train.csv')