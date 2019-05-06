import pandas as pd
from matplotlib import pyplot as plt



# data
file_path = "./books.csv"
data = pd.read_csv(file_path)
# print(data.info())
# print(data.loc[:, "average_rating"].head(1))

# 不同年份书的平均评分,对于公元前数据，书大多数只有1本，对于评分没什么参考价值，去掉
books_rate_years_data = data["average_rating"].groupby(by=data["original_publication_year"]).mean()
books_rate_years_data = books_rate_years_data[1800:]
print(books_rate_years_data)
# 准备数据
x = books_rate_years_data.index
y = books_rate_years_data.values

# 图形设置
plt.figure(figsize=(20, 8), dpi=80)
plt.xticks(x[::5], rotation=45)

plt.plot(x, y)
plt.show()
