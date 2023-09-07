import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


data = [['steve',25,56],['linus',28,29],['elon ',25]]
df = pd.DataFrame(data=data,columns=['Name','Age','weight'])
print(df)

from sklearn.preprocessing import StandardScaler
std = StandardScaler();
X = std.fit_transform(df[['Age','weight']])
                                        