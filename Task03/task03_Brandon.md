1.WPIG

# Group by 'GROUP' column and count the occurrences to find the most frequent posting group
group_post_count = file_content.groupby('GROUP').size().reset_index(name='Post_Count')

# Sort the groups by the count of posts in descending order
group_post_count_sorted = group_post_count.sort_values(by='Post_Count', ascending=False)

import ace_tools as tools; tools.display_dataframe_to_user(name="Group Post Count", dataframe=group_post_count_sorted)

2.方案

# Check the 'TYPE' column in file_content to determine the count of different content types
content_type_count = file_content['TYPE'].value_counts().reset_index(name='Count')
content_type_count.columns = ['Content_Type', 'Count']

tools.display_dataframe_to_user(name="Content Type Count", dataframe=content_type_count)

3.物聯網最熱門，第二電源，第三車聯網

# Filter content tags to identify popular articles in different categories like '車聯網' and '電源'
# Count occurrences for each CAT1 category to see which one has more popular content
popular_categories_count = file_tags['CAT1'].value_counts().reset_index(name='Count')
popular_categories_count.columns = ['Category', 'Count']

tools.display_dataframe_to_user(name="Popular Categories Count", dataframe=popular_categories_count)

4.智能家居和智慧城市

# Count occurrences for each CAT2 category to see which one is more popular at the second level
popular_categories_count_cat2 = file_tags['CAT2'].value_counts().reset_index(name='Count')
popular_categories_count_cat2.columns = ['Category_Level_2', 'Count']

tools.display_dataframe_to_user(name="Popular Second-Level Categories Count", dataframe=popular_categories_count_cat2)

5.外部用戶佔比11.9%，內部用戶佔比9.3%

# Calculate the ratio (as a fraction) of each user type
total_users = user_type_count['Count'].sum()
user_type_count['Ratio'] = user_type_count['Count'] / total_users

tools.display_dataframe_to_user(name="User Type Ratio", dataframe=user_type_count)





結論:
平台上由WPIG集團發佈的文章數量最多，且內容主要以方案為主。最受歡迎的內容是物聯網，在第二層分類中智能家居和智慧城市
最受關注。用戶類型方面，未登錄用戶佔大多數，外部用戶和內部用戶分別佔約12%和9%。