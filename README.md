# StockPredict
AppliedML Project 2 - Predict Adjusted closing prices for stocks
In this example I have chosen to analyze the Vanguard ETF. 

#### Methods applied
* Linear Regression 
    * The two variables considered were Volume and Adj Closeing price
* Last value - Set the predicted value to the previously observed value 
* Moving Averages- Set the predicted value to the mean of the previous N days. Need to tune for N
    * Optimal value was N=2 according to lowest mean squared error
* Extreme Gradient Boosting
* Long Short Term Memory

