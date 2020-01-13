from __future__ import print_function
import tensorflow as tf
import numpy as np

#1 create data

x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*np.pi + 0.3

print("#1 finished")
      
#2 Create tensorflow network (one layer/ one neuron)

weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
biases = tf.Variable(tf.zeros([1]))

y = weights*x_data + biases

loss = tf.reduce_mean(tf.square(y-y_data))
optimizer = tf.train.GradientDescentOptimizer(0.6)
train = optimizer.minimize(loss) #run this then the training begins

init = tf.global_variables_initializer()

print("#2 finished")
      
#3 session run

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(2001):
    sess.run(train)
    if step%200 == 0:
        print ('step = ', step, '\nweights = ', sess.run(weights), '\nbiases = ', sess.run(biases), '\nloss = ', sess.run(loss), '\n')









