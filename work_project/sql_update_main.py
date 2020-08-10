import sql_update_one
import datetime
import time
import pandas as pd
import margin_daily_update
data_log = pd.DataFrame([])
DAY = 1
while True:
    if DAY ==1 :

        d1 = datetime.datetime.now()
        d2 = datetime.datetime(2020, 7, 7)# 啟動隔天日期
        time.sleep((d2 - d1).seconds-600) # 前一天10中前抓取 11.50

        #time.sleep(60)
        #date_1 = datetime.datetime.now().strftime('%Y%m%d')
        #debug
        date_1 = '20200706'
        #..............
        start_time = datetime.datetime.now()
        a = sql_update_one.sql_update(date_1)
        b = margin_daily_update.get_margin_daily(date_1)
        #b=date_1
        DAY = DAY+1
        data_log = pd.concat([data_log, pd.DataFrame([[a,b,c]])], axis=0)
        data_log.to_csv("C:/Users/Big data/Desktop/sql_log.csv")
        end_time = datetime.datetime.now()
        dif_time = (end_time - start_time).seconds
        print(datetime.datetime.now())
    else:
        time.sleep(86400-dif_time)
        start_time = datetime.datetime.now()
        #time.sleep(60)
        date_1 = datetime.datetime.now().strftime('%Y%m%d')
        a = sql_update_one.sql_update(date_1)
        b = margin_daily_update.get_margin_daily(date_1)
        end_time = datetime.datetime.now()
        dif_time = (end_time-start_time).seconds
        #b = date_1
        DAY = DAY + 1
        data_log = pd.concat([data_log, pd.DataFrame([[a,b]])], axis=0)
        data_log.to_csv("C:/Users/Big data/Desktop/sql_log.csv")
    print(DAY)
    print(datetime.datetime.now())


