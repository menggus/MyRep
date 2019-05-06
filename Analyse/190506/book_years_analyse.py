import pandas as pd
from matplotlib import pyplot as plt


# data
file_path = "./books.csv"
data = pd.read_csv(file_path)
# print(data.info())
# print(data.head(1))

# 不同年份书的数量
year_book_data = data["title"].groupby(by=data["original_publication_year"]).count()

# print(year_book_data)
# 数据处理，由于数据，许多为每年就1本书，本身无多大意义，所以这里去除
year_book_data = year_book_data[1800:]
# print(year_book_data)

# 准备画图数据
x = year_book_data.index
y = year_book_data.values

# 设置图形
plt.figure(figsize=(25, 8), dpi=60)

plt.bar(x, y, width=0.5)
plt.show()

