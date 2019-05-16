import tensorflow as tf
import os

# 删除更新警告 和 使用 CPU支持警告
# Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX AVX2
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
old_v = tf.logging.get_verbosity()
tf.logging.set_verbosity(tf.logging.ERROR)


def read_image(file_path_list):
    """
        读取image学习数据
    :param file_path_list: 文件路径
    :return:
    """
    # 1.构建文件队列
    file_queue = tf.train.string_input_producer(file_path_list)

    # 2.构造image阅读器
    reader = tf.WholeFileReader()
    # 读取图片数据key：b'./data/8.jpg'    value：图片-2进制数据
    key, value = reader.read(file_queue)
    # out: Tensor("ReaderReadV2:1", shape=(), dtype=string)
    print(value)

    # 3.对图片2进制数据进行解码
    image = tf.image.decode_jpeg(value)
    # out: Tensor("DecodeJpeg:0", shape=(?, ?, ?), dtype=uint8)
    print(image)
    image1 = image

    # 4.同一图片的尺寸大小, 尺寸大小： 200 x 200
    image_size = tf.image.resize_images(image, [200, 200])
    # out: Tensor("resize/Squeeze:0", shape=(200, 200, ?), dtype=float32)
    print(image_size)

    # 5.重点：所有图片必须固定shape，尺寸+通道数，才能确定一张图片
    image_size.set_shape([200, 200, 3])
    # out:  Tensor("resize/Squeeze:0", shape=(200, 200, 3), dtype=float32)
    print(image_size)

    # 6.批处理
    image_batch = tf.train.batch([image_size, key], batch_size=5, num_threads=1, capacity=5)
    # out: Tensor("batch:0", shape=(5, 200, 200, 3), dtype=float32)
    print(image_batch)


    return image_batch, key, image1


if __name__ == '__main__':
    file_names = os.listdir("./data")  # 获取文件列表
    file_path_list = [os.path.join("./data/", i) for i in file_names]

    image_batch, key, im1 = read_image(file_path_list)

    with tf.Session() as sess:
        # 定义一个线程协调器
        coord = tf.train.Coordinator()

        # 开启读取文件的线程
        threads = tf.train.start_queue_runners(sess, coord=coord)

        # 打印读取内容
        print(sess.run(image_batch), sess.run(key))
        print("-"*100)
        print(sess.run(im1))


        # 关闭子线程
        coord.request_stop()
        coord.join(threads)
