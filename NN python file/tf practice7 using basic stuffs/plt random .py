from __future__ import print_function
import tensorflow as tf 
import matplotlib.pyplot as plt
import numpy as np

#1 create data 

x_data = np.random.rand(1000).astype(np.float32)
noise = np.random.normal(0.0, 0.05, x_data.shape)
y_data = x_data*2.0 + noise



#2 create tensorflow network

weight1 = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
weight2 = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
bias1 = tf.Variable(tf.zeros([1]))
bias2 = tf.Variable(tf.zeros([1]))

lay1 = tf.add(tf.multiply(weight1, x_data), bias1, name = 'layer1')
lay2 = tf.add(tf.multiply(weight2, lay1), bias2, name = 'layer2')

loss = tf.reduce_mean(tf.square(lay2-y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()

#3 session run 

sess = tf.Session()
sess.run(init)

for step in range(2001):
    sess.run(train)
    if step%200 == 0:
        print ('\nstep = ', step, 'loss = ', sess.run(loss), 
               '\nweight1 = ', sess.run(weight1), 
               '\nbias1 = ', sess.run(bias1), 
               '\nweight2 = ', sess.run(weight2), 
               '\nbias2 = ', sess.run(bias2), '\n',
               '\nw = ', sess.run(weight1*weight2), '\nb = ', sess.run(weight2*bias1+bias2),
               '--------------')

#4 draw input scattered figure for reference
        
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(x_data, y_data)
plt.ion()
plt.show()
