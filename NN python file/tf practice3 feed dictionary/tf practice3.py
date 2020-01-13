from __future__ import print_function
import tensorflow as tf

input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)
output = tf.multiply(input1, input2)

a = [[2, 1], [3, 3]]


sess = tf.Session()
print(sess.run(output, feed_dict={input1:[[7.], [2.]], input2:[[3.], [8.]]}))
print(a)
print(sess.run(tf.transpose(a)))