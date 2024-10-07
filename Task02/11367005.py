import numpy as np
import pandas as pd
from collections import Counter

# 讀取資料
df1 = pd.read_csv("C:\\Users\\Peter\\Desktop\\all-cancelled-flights.csv")
df2 = pd.read_csv("C:\\Users\\Peter\\Desktop\\cancellation-codes.csv")

# 合併資料集
merged_df = pd.merge(df1, df2, left_on='CANCELLATION_CODE', right_on='Code', how='left')
merged_df.to_csv('Merged_Files.csv', index=False)

# 取消代碼字元比例統計
merged_df['counts'] = merged_df['CANCELLATION_CODE'].apply(lambda x: Counter(x))
merged_df['總長度'] = merged_df['CANCELLATION_CODE'].apply(len)
counts_sum = merged_df['counts'].sum()
proportions = {k: v / merged_df['總長度'].sum() for k, v in counts_sum.items()}
print("取消代碼字元比例：", proportions)

# 航班取消次數與比例
flight_cancellations = merged_df['OP_CARRIER_FL_NUM'].value_counts()
max_cancelled_flight = flight_cancellations.idxmax()
max_cancellations = flight_cancellations.max()
cancel_percentage = (max_cancellations / flight_cancellations.sum()) * 100
print(f"取消最多的航班號是：{max_cancelled_flight}")
print(f"取消次數：{max_cancellations}")
print(f"佔三年的百分比：{cancel_percentage:.2f}%")

# OGG 機場取消原因按年統計
merged_df['FLIGHT_DATE'] = pd.to_datetime(merged_df['FLIGHT_DATE'])
ogg_flights = merged_df[merged_df['ORIGIN'] == 'OGG']
ogg_flights['year'] = ogg_flights['FLIGHT_DATE'].dt.year
cancellation_by_year = ogg_flights.groupby(['year', 'CANCELLATION_CODE']).size().unstack(fill_value=0)
cancellation_percentage = cancellation_by_year.div(cancellation_by_year.sum(axis=1), axis=0) * 100
print("OGG 機場取消原因按年統計：")
print(cancellation_percentage)

# IAD 機場航班與取消原因統計
iad_flights = merged_df[merged_df['ORIGIN'] == 'IAD']
top_carrier = iad_flights.groupby(['OP_CARRIER', 'CARRIER_NAME']).size().idxmax()
cancellation_reasons = iad_flights['CANCELLATION_CODE'].value_counts()
top_cancellation_reason = cancellation_reasons.idxmax()
print(f"從IAD起飛架次最多的航空公司是: {top_carrier}")
print(f"從IAD起飛航班遭取消的最常見原因是: {top_cancellation_reason}")
