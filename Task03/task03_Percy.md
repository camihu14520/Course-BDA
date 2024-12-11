# 1連結雲端
from google.colab import drive
drive.mount('/content/drive')

# 2套件讀取
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 3資料讀取
df_blogcomment = pd.read_csv("/content/drive/My Drive/碩士課程/大數據實務/DDT/8_ddt_blog_comment.csv")
df_content = pd.read_csv("/content/drive/My Drive/碩士課程/大數據實務/DDT/0_ddt_content.csv")

# 4原始資料檢視
# 4-1blogcomment檢視資料屬性
df_blogcomment.info()

BlogComment資料介紹
COMMENT_ID=評論編號
BLOG_ID=執行動作類型(ACTION_OBJECT_MAPPING)
USER_ID=評論人
COMMENT_TEXT=評論內容
COMMENT_STATUS=評論狀態
VOTE_UP_CNT=按讚數
CREATION_DATE=評論日期
LAST_UPDATE=評論更新日期

# 4-2content檢視資料屬性
df_content.info()

Content資料介紹
AUTHOR_ID=作者ID
GROUP_ID=所屬集團
CONTENT_ID=NEWS_ID/BLOG_ID
CONTENT_CODE=BLOG_CODE
PUBLISG_DATE=發布日期
TITLE=標題
TYPE=方案/博文

# 5資料前處理
# 5-1BlogComment
#轉換COMMENT_ID BLOG_ID USER_ID資料屬性 int64到object
df_blogcomment[['COMMENT_ID', 'BLOG_ID', 'USER_ID']] = df_blogcomment[['COMMENT_ID', 'BLOG_ID', 'USER_ID']].astype('object')

#轉換CREATION_DATE資料屬性 object到datetime
df_blogcomment['CREATION_DATE'] = pd.to_datetime(df_blogcomment['CREATION_DATE'])
df_blogcomment['LAST_UPDATE_DATE'] = pd.to_datetime(df_blogcomment['LAST_UPDATE_DATE'])

df_blogcomment.info()

清理後BlogComment 概述
行數：有 329 條數據記錄（從 0 到 328）。
列數：總共有 8 列。
df_blogcomment中所有資料皆無空值
數據列詳細信息
COMMENT_ID, BLOG_ID, USER_ID, COMMENT_TEXT, COMMENT_STATUS 皆為object屬性
VOTE_UP_CNT為int屬性
CREATION_DATE, LAST_UPDATE為datetime屬性

# 5-2Content
#轉換COMMENT_ID BLOG_ID USER_ID資料屬性 int64到object
df_content[['CONTENT_ID', 'AUTHOR_ID']] = df_content[['CONTENT_ID', 'AUTHOR_ID']].astype('object')

df_content.info()
清理後Content 概述
行數：有 1637 條數據記錄（從 0 到 1636）。
列數：總共有 7 列。
df_content中所有資料皆無空值
所有數據皆為object屬性

# 5-3提供數值列的摘要統計
numeric_summary = df_blogcomment.describe()
print(numeric_summary)
數據摘要解釋 VOTE_UP_CNT: 按讚數

count: 總共有 329 項按讚資料
mean: 平均按讚數為 0.59
std: 標準差為 0.93
min: 最少按讚數為0
max: 最多按讚數為6

# 6資料的摘要統計
# 6-1BlogComment
#包括所有列（數值和非數值）的摘要統計
all_summary_blogcomment = df_blogcomment.describe(include='all')
print(all_summary_blogcomment)

COMMENT_ID評論編號
unique=329　等於COMMENT_ID的總數代表沒有重複的資料

USER_ID評論人
top=62206　編號62206的評論人出現最多次 freq=28　出現最多次的評論人次數為28次

COMMENT_TEXT評論內容
top=很不错的分享，谢谢！　"很不错的分享，谢谢！"這項評論出現最多次
freq=5　出現最多次數為28次

# 7資料分析
# 7-1繪製各集團發文數占比圓餅圖
計算 "GROUP" 欄位中每個值的出現次數
group_counts = df_content['GROUP'].value_counts()

繪製各集團發文數占比圓餅圖
plt.figure(figsize=(8, 8))  # 設置圖表大小
plt.pie(
    group_counts,
    labels=group_counts.index,  # 使用 GROUP 的值作為標籤
    autopct='%1.2f%%',  # 顯示百分比，保留兩位小數
    startangle=140,  # 起始角度設置為 140 度，使圖表更美觀
    textprops={'fontsize': 12}  # 設置文字大小
)
plt.title("Proportion of Posts by Each Group", fontsize=16)  # 設置圖表標題
plt.show()  # 顯示圖表

# 7-2繪製各集團發文類型長條圖
按 "GROUP" 和 "TYPE" 分組，並計算每組的發文數
type_group_counts = df_content.groupby(['GROUP', 'TYPE']).size().unstack(fill_value=0)

繪製長條圖
plt.figure(figsize=(10, 6))
type_group_counts.plot(kind='bar', stacked=False, color=['#1f77b4', '#ff7f0e'], figsize=(10, 6))

圖表標題和軸標籤（英文）
plt.title("Post Types by Group", fontsize=16)  # 標題
plt.xlabel("Group", fontsize=12)  # X 軸標籤
plt.ylabel("Count", fontsize=12)  # Y 軸標籤

圖例翻譯
plt.legend(title="TYPE", labels=["Proposal", "Blog Post"], fontsize=10)

美化
plt.xticks(rotation=0)  # X 軸標籤角度設為水平
plt.grid(axis='y', linestyle='--', alpha=0.7)  # 添加水平網格線
plt.tight_layout()  # 調整圖表佈局以防止重疊

顯示圖表
plt.show()

# 7-3繪製使用者的評論數量排行
計算每個使用者的評論數量
user_comment_counts = df_blogcomment['USER_ID'].value_counts()

排序並選擇評論數最多的前 30 名使用者
top_users = user_comment_counts.head(30)  # 選取前 30 名使用者

繪製水平條形圖
plt.figure(figsize=(8, 10))  # 設定圖表大小
top_users.plot(kind='barh', color='skyblue', edgecolor='black')  # 條形圖，設置顏色和邊框
plt.title("User Comment Counts Ranking", fontsize=16)  # 設置圖表標題
plt.xlabel("Comment Count", fontsize=12)  # X 軸標籤
plt.ylabel("User ID", fontsize=12)  # Y 軸標籤
plt.gca().invert_yaxis()  # 反轉 Y 軸，讓排行從上到下
plt.grid(axis='x', linestyle='--', alpha=0.7)  # 添加水平網格線
plt.tight_layout()  # 調整圖表佈局以防止重疊
plt.show()  # 顯示圖表