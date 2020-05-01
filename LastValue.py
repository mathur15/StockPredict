#predicting adj close price using LastValue Method
    #-set current obs adj value to last observed value
    #-Baseline model

#import dataset

import pandas as pd
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

#import dataset 
df = pd.read_csv('VTI.csv')
df_adj_close = df['Adj Close']

df_adj_close_date = df[["Date",'Adj Close']]

length = len(df_adj_close)

#split up data to build model and validate
split_point = length -60
test,validate = df_adj_close[0:split_point],df_adj_close[split_point:]
test.to_csv('test.csv',header=False)
validate.to_csv('validate.csv',header=False)

history = [x for x in test]
predicted = list()
for item in test:
    y_hat = history[-1]
    predicted.append(y_hat)
    observed = item
    history.append(observed)
    print(">Predicted=%.3f   Expected=%.3f" %(y_hat,observed))
    
print("\n")
print("Evaluating performance using mean squared error \n")

print(mean_squared_error(test.values,predicted))

ax = df_adj_close_date.plot(x='Date',grid=True,style='b-')
plt.show()
df_predicted = pd.DataFrame(predicted)
ax1 = df_predicted.plot(grid=True,style='r-')
plt.show()

