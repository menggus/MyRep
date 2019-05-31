import pandas as pd
from matplotlib import pyplot as plt



# 读取本地数据
file_path = "./starbucks_store_worldwide.csv"
data = pd.read_csv(file_path)
# print(data.info())
# print(data.head(1))

# 按国家进行分类，并对店铺进行计数
country_cato = data["Brand"].groupby(by=data["Country"]).count()
# 排序,取前10
head_data = country_cato.sort_values(ascending=False).head(10)

# 准备画图数据
x = head_data.index
y = head_data.values

plt.figure(figsize=(20, 8), dpi=60)

plt.bar(x, y, color="orange")

plt.show()

