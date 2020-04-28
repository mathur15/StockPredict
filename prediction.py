import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
#family of model - RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.externals import joblib
import matplotlib.pyplot as plt

#the goal is to build a model to predict adj close prices based on data from
#the last year

#import and clean data-252 samples and 7 features
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
df = pd.read_csv('VTI.csv')

#Data exploration
print(df.head(5))
print(df.isnull().values.any())

#sharp drop observed towards later dates
plt.plot(df['Date'],df['Adj Close'])
plt.xlabel("Date (YYYY-MM-DD)")
plt.ylabel("Prices(USD)")

#sharp incline towards later dates
plt.plot(df['Date'],df['Volume'])
plt.xlabel('Date (YYYY-MM-DD)')
plt.ylabel('Volume')
#print(df.shape)
print(df.describe())
print(df.corr(method='pearson'))
#using the pearson correaltion coefficient strong pos relation with Open
#High,Low,Close and -ve correlation with Volume(Moderate)



