import tensorflow as tf

sess = tf.Session()

n = tf.argmax(
    [[0.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
     [1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.]], 0)

sess.run(n)

n = tf.argmax(
    [[0.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
     [1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.]], 1)

sess.run(n)

sess.close()
