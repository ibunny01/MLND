# Solution is available in the other "solution.py" tab
import tensorflow as tf

# TODO: Convert the following to TensorFlow:
x = 10
y = 2
z = x/y - 1

# TODO: Print z from a session
x = tf.constant(10)
y = tf.constant(2)
z = tf.subtract( tf.divide(x, y), 1)

sess = tf.Session()
print(sess.run(z))
