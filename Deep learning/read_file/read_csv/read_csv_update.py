import tensorflow as tf
import numpy as np
import pandas as pd
import re
from tensorflow.python.data import Dataset

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


data = pd.read_csv("./data/A.csv", sep=",", header=None, names=["name", "target"])

print(data)

#
# def my_input_fn(features, targets, batch_size=1, shuffle=True, num_epochs=None):
#     """Trains a linear regression model of one feature.
#
#     Args:
#       features: pandas DataFrame of features
#       targets: pandas DataFrame of targets
#       batch_size: Size of batches to be passed to the model
#       shuffle: True or False. Whether to shuffle the data.
#       num_epochs: Number of epochs for which data should be repeated. None = repeat indefinitely
#     Returns:
#       Tuple of (features, labels) for next data batch
#     """
#     #
#     pd.read_csv("./")
#
#     # Convert pandas data into a dict of np arrays.
#     features = {key: np.array(value) for key, value in dict(features).items()}
#
#     # Construct a dataset, and configure batching/repeating.
#     ds = Dataset.from_tensor_slices((features, targets))  # warning: 2GB limit
#     ds = ds.batch(batch_size).repeat(num_epochs)
#
#     # Shuffle the data, if specified.
#     if shuffle:
#         ds = ds.shuffle(buffer_size=10000)
#
#     # Return the next batch of data.
#     features, labels = ds.make_one_shot_iterator().get_next()
#     return features, labels
#
#
#
#
# def csvread(filelist):
#     """
#         读取csv文件
#     :param filelist:  文件路径+ 名字列表
#     :return:
#     """
#     # 构建文件路径队列
#     #
#     file_queue = tf.train.string_input_producer(file_list, num_epochs=2)
#     # file_queue = tf.constant(file_list)
#     print(file_queue)
#     # 构造csv文件的阅读器
#     # reader = tf.data.TextLineDataset(filenames=file_queue)
#     reader = tf.TextLineReader()
#     key, value = reader.read(file_queue)
#
#     # 对每行内容进行解码
#     # record_defaults: 指定每一个样本的每一列的类型，指定默认值
#     records = [["None"], ["None"]]
#     example, label = tf.decode_csv(value, record_defaults=records)
#
#     # 文件批处理
#     # batch_size : 表示一次取多少数据
#     # capacity : 表示批处理容器存多少数据
#     example_batch, example_label = tf.train.batch([example, label], batch_size=9, num_threads=1, capacity=9)
#     return example_batch, example_label
#
#
# if __name__ == '__main__':
#     # 构造需要读取文件的路径： 路径+文件名，如['./data/A.csv', './data/B.csv', './data/C.csv']
#     file_name = os.listdir("./data")  # 获取path下的文件列表
#     file_list = [os.path.join("./data/", file) for file in file_name]  # 组合文件列表下文件的路径
#
#     example_batch, label_batch = csvread(file_list)
#
#     # 开启会话运行结果
#     with tf.Session() as sess:
#         # 定义一个线程协调器
#         coord = tf.train.Coordinator()
#
#         # 开启读取文件的线程(文件填充队列的线程)
#         tf.train.start_queue_runners(sess, coord=coord)
#
#         # 打印读取内容
#         print(sess.run(example_batch), sess.run(label_batch))
#
#         # 关闭子线程
#         coord.request_stop()  # 子线程关闭，请求
#         coord.join()  # 等待子线程关闭
#
#


