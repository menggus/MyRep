import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties


# 读取本地数据
file_path = "./starbucks_store_worldwide.csv"
data = pd.read_csv(file_path)

# 按国家，按城市分类
country_city_cato = data["Brand"].groupby(by=[data["Country"], data["City"]]).count()

# 获取中国数据
china_data = country_city_cato["CN"]

# 排序
# head_data = china_data.sort_values(ascending=False).head(10)
head_data = china_data.sort_values().tail(10)

# 准备
x = head_data.index
y = head_data.values

# 设置图像，加载中文字体
my_font = FontProperties(fname=r"C:\WINDOWS\FONTS\MSYH.TTC")
plt.figure(figsize=(20, 8), dpi=60)

plt.yticks(range(len(x)), x, fontproperties=my_font)

plt.barh(x, y, height=0.5, color="orange")
plt.show()



