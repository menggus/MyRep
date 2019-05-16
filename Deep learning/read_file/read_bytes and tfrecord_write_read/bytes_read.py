import tensorflow as tf
import os

# 删除更新警告 和 使用 CPU支持警告
# Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX AVX2
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
old_v = tf.logging.get_verbosity()
tf.logging.set_verbosity(tf.logging.ERROR)


class CIFARManager:

    def __init__(self, path_list):
        self.path_list = path_list

    def read(self):

        # 1、构造文件列表队列
        file_list_queue = tf.train.string_input_producer(self.path_list)

        # 2、构造文件读取器
        # 参数：3072   数据为：图片标签（1字节）+图片（32*32*3） 所以一个样本的大小：1+32x32x3=3073字节
        reader = tf.FixedLengthRecordReader(3073)  # 这里字节数，已经限制了读取字节数，也就是一个样本
        key, value = reader.read(file_list_queue)
        # print("read: ", value)

        # 3、解码内容
        content = tf.decode_raw(value, out_type=tf.uint8)
        # print("decode_raw: ", content)  #

        # 4、切分解码内容，获取label image
        # [0], [1]: 前者为起始位置，后者为切分的个数
        # label = tf.slice(content, [0], [1]), tf.uint8
        label = tf.cast(tf.slice(content, [0], [1]), tf.int32)
        image = tf.slice(content, [1], [3072])

        # 对image进行特征数据形状改变
        image_resize = tf.reshape(image, [32, 32, 3])
        # print("image: ", image_resize)

        # 批处理
        label_batch, image_batch = tf.train.batch([label, image_resize], batch_size=10, num_threads=1, capacity=10)
        # print("label,image: ", label, image)

        return label_batch, image_batch

    def write_tfrecord(self, label_batch, image_batch):
        """
            写入数据以tfrecord格式
        :param label:
        :param image:
        :return:
        """
        # 构建文件存储器
        writer = tf.python_io.TFRecordWriter("./data/data.tfrecords")

        # 对样本，循环存储，每一个样本都要构建example
        for i in range(10):
            # pass
            label = label_batch[i].eval()[0]

            image = image_batch[i].eval().tostring()

            example = tf.train.Example(features=tf.train.Features(feature={
                "label": tf.train.Feature(int64_list=tf.train.Int64List(value=[label])),
                "image": tf.train.Feature(bytes_list=tf.train.BytesList(value=[image]))
            }))
            # 写入单独样本
            writer.write(example.SerializeToString())

        # 关闭
        writer.close()

        print("写入完成…………………………")

    def read_fr_tfrecord(self):
        """
            从tfrecord读取数据
        :param path:
        :return:
        """
        # 创建文件队列
        file_queue = tf.train.string_input_producer(["./data/data.tfrecords"])

        # 构造tfrecord文件阅读器
        reader = tf.TFRecordReader()
        key, value = reader.read(file_queue)

        # 解析example
        example = tf.parse_single_example(value, features={
            "label": tf.FixedLenFeature([], tf.int64),
            "image": tf.FixedLenFeature([], tf.string)
        })

        # 解码, 读取内容是string时需要解码，如果是int64，float不需要
        image = tf.decode_raw(example.get("image"), tf.uint8)

        # 固定图片形状，方便批处理
        image_resize = tf.reshape(image, [32, 32, 3])

        label = tf.cast(example.get("label"), tf.int64)

        # 批处理
        label_batch, image_batch = tf.train.batch([label, image_resize], batch_size=10, num_threads=1, capacity=10)

        return label_batch, image_batch


if __name__ == '__main__':
    file_names = os.listdir("./data")
    file_path_list = [os.path.join("./data/", i) for i in file_names if i[-3:] == "bin"]

    cifar = CIFARManager(file_path_list)
    # label_batch, image_batch = cifar.read() # 从CIFAR-10中读取数据
    label_batch, image_batch = cifar.read_fr_tfrecord()  # 从tfrecord中读取数据

    with tf.Session() as sess:
        # 构建线程协调器
        coord = tf.train.Coordinator()
        # 子线程
        threads = tf.train.start_queue_runners(coord=coord, sess=sess)

        print(sess.run(label_batch))
        # print(label_batch[0].eval()[0])
        print(sess.run(image_batch))

        # 存储数据以tfrecord格式
        # cifar.write_tfrecord(label_batch, image_batch)

        # 子线程结束
        coord.request_stop()
        coord.join(threads)
