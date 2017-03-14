# Solution is available in the other "solution.py" tab
import tensorflow as tf


def run():
    output = None
    x = tf.placeholder(tf.int32)

    tf.Print(x, [x])

    with tf.Session() as sess:
        # TODO: Feed the x tensor 123
        output = sess.run(x,
                          feed_dict={x:123})

    return output


def main():
    print(run())


if __name__ == '__main__':
    main()
