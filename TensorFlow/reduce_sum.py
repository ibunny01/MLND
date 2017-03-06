import tensorflow as tf

x = tf.constant(
    [[1, 1, 1],
     [1, 1, 1]], dtype=tf.float32
)


sum = tf.reduce_sum(x)
sum = tf.reduce_sum(x, 0)
sum = tf.reduce_sum(x, 1)
sum = tf.reduce_sum(x, 1, keep_dims=True)

sess = tf.Session()
result = sess.run(sum)

print result

if __name__ == '__main__':
    main()
