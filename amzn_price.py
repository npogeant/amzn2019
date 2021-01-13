#Yahoo Finance Library
!pip install yfinance

import pandas as pd
import yfinance as yf

import plotly.express as px

#Getting AMZN 2019 stock evolution
amzn_df = yf.download('AMZN', 
                      start='2019-01-01', 
                      end='2019-12-31', 
                      progress=False)

#Calculating the daily & monthly returns from the pct change function
amzn_df['Daily Returns'] = amzn_df['Adj Close'].pct_change()
amzn_monthly_returns = amzn_df['Adj Close'].resample('M').ffill().pct_change()
amzn_df.reset_index(level=0, inplace=True)
amzn_df.tail()

#Processing the Date values
amzn_df['Date'] = pd.to_datetime(amzn_df['Date']).dt.to_period('D')
amzn_df['Month'] = amzn_df['Date'].dt.strftime('%b')
amzn_df['Month_digit'] = amzn_df['Date'].dt.month
amzn_df['Date'] = amzn_df['Date'].astype(str)

#AMZN Adj Close evolution for 2019
fig = px.line(amzn_df, x='Date', y='Adj Close', title='Close Price of $AMZN in 2019', width=800, height=400)
fig.update(layout=dict(title=dict(x=0.5)))
fig.show()

#month evolution (last day - first day) / first day
jan = ((1718.72998 - 1539.130005) / 1539.130005) 
feb = ((1639.829956 - 1626.22998)/ 1626.22998)
mar = ((1780.75 - 1671.72998)/ 1671.72998)
apr = ((1926.52002 - 1814.189941)/ 1814.189941)
may = ((1775.069946 - 1911.52002)/ 1911.52002)
jun = ((1893.630005 - 1692.689941)/ 1692.689941) 
jul = ((1866.780029 - 1922.189941)/ 1922.189941)
aug = ((1776.290039 - 1855.319946)/ 1855.319946)
sept = ((1735.910034 - 1789.839966)/ 1789.839966) 
oct = ((1776.660034 - 1735.650024)/ 1735.650024) 
nov = ((1800.800049 - 1791.439941)/ 1791.439941) 
dec = ((1846.890015 - 1781.599976)/ 1781.599976)

#Creating the dataframe from the previous values
amzn_rmonthly = pd.DataFrame([jan, feb, mar, apr, may, jun, jul, aug, sept, oct, nov, dec],
                             ['2019-01', '2019-02', '2019-03', '2019-04', '2019-05', '2019-06', '2019-07', '2019-08', '2019-09', '2019-10', '2019-11', '2019-12'])
amzn_rmonthly.reset_index(level=0, inplace=True)
amzn_rmonthly.columns = ["Month","Monthly Pourcentage Change"]
amzn_rmonthly["Color"] = np.where(amzn_rmonthly["Monthly Pourcentage Change"]<0, 'red', 'blue')
amzn_rmonthly["Pct"] = ['11.67%', '0.84%', '6.52%', '6.19%', '-7.14%', '11.87%', '-2.88%', '-4.26%', '-3.01%', '2.36%', '0.52%', '3.66%']

#AMZN Monthly evolution by color (positive or negative)
fig = px.bar(amzn_rmonthly, x='Month', color='Color', y='Pct', title='Monthly Pourcentage Change of $AMZN in 2019', text='Pct', width=800, height=400)
fig.update_layout(showlegend=False, plot_bgcolor='white', yaxis=dict(title=''), margin=dict(autoexpand=False, l=100, r=20, t=110,))
fig.update(layout=dict(title=dict(x=0.5)))
fig.update_yaxes(visible=False)
fig.show()

