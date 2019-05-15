import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def regression():
    """
        构造线性回归模型
    :return:
    """
    # with tf.variable_scope()  变量的作用域
    with tf.variable_scope("Data"):
        # 1.准备数据: x 特征值 [100, 1]  y 目标值 [100]
        x = tf.random_normal([100, 1],
                             mean=1.75, stddev=0.5,
                             name="x_data")
        # 矩阵乘法必须是二维, 构造y值
        y_true = tf.matmul(x, [[0.7]]) + 0.8

    with tf.variable_scope("Model"):
        # 建立线性回归模型，权重+特征+偏置： y = w*x+b
        # 1.随机给定w，b的值，必须定义为变量（需要不断更新）
        # Variable中参数：trainable=bool 指定变量是否跟着梯度下降进行优化
        weight = tf.Variable(tf.random_normal(shape=[1, 1], mean=0.0, stddev=1.0), name="weight")
        bias = tf.Variable(0.0, name="bias")

        y_predict = tf.matmul(x, weight) + bias

    with tf.variable_scope("Loss"):
        # 2.损失函数
        loss = tf.reduce_mean(tf.square(y_true - y_predict))

    with tf.variable_scope("Optimizer"):
        # 3.优化: 梯度下降 learning_rate：0~1 2 3 4 ~ 10
        train = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

    # 增加变量显示
    tf.summary.scalar("losses", loss)
    tf.summary.histogram("weights", weight)
    # 合并op
    merged = tf.summary.merge_all()

    # 定义一个全局变量初始化op
    init_op = tf.global_variables_initializer()

    # 模型op
    saver = tf.train.Saver()

    with tf.Session() as sess:
        sess.run(init_op)

        print("初始化随机weight:%f, 随机bias：%f" % (weight.eval(), bias.eval()))

        # 创建事件文件
        filewriter = tf.summary.FileWriter(logdir="./board", graph=sess.graph)

        # 在训练之前加载模型
        if os.path.exists("./model/checkpoint"):  # 判断模型是否存在
            saver.restore(sess, "./model/model")

        # 训练
        for i in range(100):
            sess.run(train)
            summary = sess.run(merged)
            filewriter.add_summary(summary, i)

            print("优化weight：%f, bias：%f" % (weight.eval(), bias.eval()))

        # 模型的保存
        saver.save(sess, "./model/model")


if __name__ == '__main__':
    regression()



