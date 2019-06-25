import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv("./friends.csv", header=None, names=["nickname", "name", "gender", "province", "city", "signature", "attrStatus"])

# print(data.head())

gender_data = data.groupby("gender", axis=0).count()  # axis=0表示根据行来分组

x = gender_data["nickname"].index
y = gender_data["nickname"].values

print(x)
print(y)

plt.figure(figsize=(20,20), dpi=80)

plt.bar(x,y)
plt.show()