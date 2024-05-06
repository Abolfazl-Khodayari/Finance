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


    line_min = chart.create_line('min' , color= '#073763')
    line_min.set(df[['time',"min"]])

    line_max = chart.create_line('max' , color= '#073763')
    line_max.set(df[['time',"max"]])

    line_mid = chart.create_line('mid' , color= '#0b5394', style= 'dashed')
    line_mid.set(df[['time',"mid"]])

    chart.show(block=True)