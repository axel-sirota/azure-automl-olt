import pandas as pd

data = pd.read_csv(filepath_or_buffer='../datasets/energy-pred.csv',
                   names=['Date', 'TZ', 'City', 'Code', 'Load', 'Predicted'], skiprows=1)
accuracy = 100*(1-abs(data['Load'] - data['Predicted'])/data['Load'])
accuracy.dropna(inplace=True)
print(accuracy.describe())

