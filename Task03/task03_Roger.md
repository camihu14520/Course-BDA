import pandas as pd


### 1.最常發文的集團有哪些?
# 載入ddt0
df1 = pd.read_csv("C:/Users/user/Desktop/bda-class/ddt_dataset/0_ddt_content.csv")

# 計算GROUP
group_counts = df1['GROUP'].value_counts()
most_frequent_group = group_counts.idxmax()
most_frequent_groupcount = group_counts.max()

print(most_frequent_group, most_frequent_groupcount)


### 2.平台是方案多還是博文多?
# 計算TYPE
type_counts = df1['TYPE'].value_counts()
most_frequent_type = type_counts.idxmax()
most_frequent_typecount = type_counts.max()

print(most_frequent_type, most_frequent_typecount)


### 3.都是那些文章比較熱門?
# 載入ddt1
df2 = pd.read_csv("C:/Users/user/Desktop/bda-class/ddt_dataset/1_ddt_content_tags.csv")

# 計算CAT1
cat1_counts = df2['CAT1'].value_counts()
most_frequent_cat1 = cat1_counts.idxmax()
most_frequent_cat1count = cat1_counts.max()

print(most_frequent_cat1, most_frequent_cat1count)


### 4.在第二層分類中，那些熱門?
# 計算CAT2
cat2_counts = df2['CAT2'].value_counts()
most_frequent_cat2 = cat2_counts.idxmax()
most_frequent_cat2count = cat2_counts.max()

print(most_frequent_cat2, most_frequent_cat2count)


### 5.外部用戶與內部用戶的數量比例?
# 載入ddt5
df3 = pd.read_csv("C:/Users/user/Desktop/bda-class/ddt_dataset/5_ddt_log.csv")

# 計算USER_TYPE
user_type_counts = df3['USER_TYPE'].value_counts()
user_type_totalcounts = user_type_counts.sum()
external_ratio = user_type_counts['external_user'] / user_type_totalcounts
internal_ratio = user_type_counts['internal_user'] / user_type_totalcounts

print("外部用戶比例:" ,external_ratio)
print("內部用戶比例:" ,internal_ratio)
