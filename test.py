import pandas as pd
from lightweight_charts import Chart

if __name__ == '__main__':
    chart = Chart()
    chart.legend(visible=True)

    df = pd.read_csv('data.csv')
    chart.set(df)
    # sma_data1 = calculate_sma(df, period=10)
    # sma_data2 = calculate_sma(df, period=50)
    # result = pd.concat([df, sma_data1.iloc[:,1] , sma_data2.iloc[:,1]], axis=1)
    # result.to_csv('data_edited.csv')


    # line1 = chart.create_line('SMA 10' , color= 'red')
    # line1.set(sma_data1)

    # line2 = chart.create_line('SMA 50' , color= 'green')
    # line2.set(sma_data2)


    chart.show(block=True)