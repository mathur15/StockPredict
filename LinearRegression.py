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
#lt.xlabel("Date (YYYY-MM-DD)")
plt.ylabel("Prices(USD)")

#sharp incline towards later dates
#plt.plot(df['Date'],df['Volume'])
#plt.xlabel('Date (YYYY-MM-DD)')
#plt.ylabel('Volume')

#print(df.shape)
#print(df.describe())
#print(df.corr(method='pearson'))

#using the pearson correaltion coefficient strong pos relation with Open
#High,Low,Close and -ve correlation with Volume(Moderate)

y = df['Adj Close']
x = df[['Volume']]

#split the data in 60% train and 40% test
X_train,X_test,Y_train,Y_test = train_test_split(x,y,test_size=0.6,
                                                 random_state=123)
regressor = LinearRegression()
regressor.fit(X_train,Y_train)
#print(regressor.coef_)

Y_predict = regressor.predict(X_test)

#compare prediction and test
df1 = pd.DataFrame({'Actual': Y_test,"Predicted":Y_predict})
df1_plot = df.head(10)
df1.plot(kind='bar',figsize=(16,10))
plt.show()

#print(df)

#evaluate performance of LinearRegression
print(mean_squared_error(Y_test, Y_predict))
print(r2_score(Y_test, Y_predict))

#save LinearRegression Model
joblib.dump(regressor,'Linregress.pkl')

















