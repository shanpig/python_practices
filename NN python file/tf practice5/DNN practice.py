# -*- coding: utf-8 -*-
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
tf.reset_default_graph()

# Load mnist dataset
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

# Define image input 784 = 28 * 28. Note that DNN input is a vector
# [None, 784] mean that there are a batch of data and each of them is 784 dimension vector
x = tf.placeholder(tf.float32, [None, 784])

# Define label. There are totally 10 class (0-9)
y = tf.placeholder(tf.float32, [None, 10])

W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y_predict = tf.matmul(x, W) + b


# Define cost
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=y_predict))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

# Calculate accuracy 
correct_prediction = tf.equal(tf.argmax(y_predict, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(1000):
        batch_xs, batch_ys = mnist.train.next_batch(100)
        
        train_step_, cross_entropy_ = sess.run([train_step, cross_entropy], feed_dict={x: batch_xs, y: batch_ys})
        if step % 50 == 0:
            # print cross_entropy every 50 steps
            print("step {}: cross_entropy is {}".format(step, cross_entropy_))
    # Load test data to validate the model  
    accuracy_ = sess.run(accuracy, feed_dict={x: mnist.test.images, y: mnist.test.labels})
    print('Testing...... accuracy is {}'.format(accuracy_))

