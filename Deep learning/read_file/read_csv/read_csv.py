import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def csvread(filelist):
    """
        读取csv文件
    :param filelist:  文件路径 + 名字列表
    :return: example_batch, example_label
    """
    # 构建文件路径队列
    file_queue = tf.train.string_input_producer(file_list)

    # 构造csv文件的阅读器
    reader = tf.TextLineReader()
    key, value = reader.read(file_queue)

    # 对每行内容进行解码
    # record_defaults: 指定每一个样本的每一列的类型，指定默认值
    records = [["None"], ["None"]]
    example, label = tf.decode_csv(value, record_defaults=records)

    # 文件批处理
    # batch_size : 表示一次取多少数据
    # capacity : 表示批处理容器存多少数据
    example_batch, example_label = tf.train.batch([example, label], batch_size=9, num_threads=1, capacity=9)
    return example_batch, example_label


if __name__ == '__main__':
    # 构造需要读取文件的路径： 路径+文件名，如['./data/A.csv', './data/B.csv', './data/C.csv']
    file_name = os.listdir("./data")  # 获取path下的文件列表
    file_list = [os.path.join("./data/", file) for file in file_name]  # 组合文件列表下文件的路径

    example_batch, label_batch = csvread(file_list)

    # 开启会话运行结果
    with tf.Session() as sess:
        # 定义一个线程协调器
        coord = tf.train.Coordinator()

        # 开启读取文件的线程
        tf.train.start_queue_runners(sess, coord=coord)

        # 打印读取内容
        print(sess.run(example_batch), sess.run(label_batch))

        # 关闭子线程
        coord.request_stop()  # 子线程关闭，请求
        coord.join()  # 等待子线程关闭




