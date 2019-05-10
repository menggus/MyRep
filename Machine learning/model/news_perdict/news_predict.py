#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report


# #### 获取数据 
#     new.DESCR:数据描述
#     news.data:数据  
#     news.filesname: 文件名  
#     news.target: 目标值   
#     news.target_names: 目标分类

# In[2]:


news = fetch_20newsgroups(subset="all")  # 获取数据


# In[3]:


x_train, x_test, y_train, y_test = train_test_split(news.data, news.target, test_size=0.25)  # 分割


# #### 特征工程 

# In[4]:


tf = TfidfVectorizer()  # 特征值提取，以重要性方法 


# In[5]:


x_train_trans = tf.fit_transform(x_train)  # 


# In[6]:


x_test_trans = tf.transform(x_test) 


# #### 朴素贝叶斯进行训练，预测

# In[7]:


bayes = MultinomialNB(alpha=1.0)  # 实例化 alpha 拉普拉斯平滑系数 1.0


# In[8]:


bayes.fit(x_train_trans, y_train)  # 传入数据训练数据


# In[9]:


result = bayes.predict(x_test_trans)  # 预测


# In[10]:


print(result)  # 预测结果


# In[11]:


print(bayes.score(x_test_trans, y_test))  # 输入测试集，得出准确率


# #### 查看精确率，召回率
#     classification_report(真实值， 预测值， 目标分类名称)

# In[12]:


print(classification_report(y_test, result, target_names=news.target_names))

