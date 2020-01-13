from __future__ import print_function
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# add layer and return output
def add_layer(inputs, inSize, outSize, activation_function = None):
    weights = tf.Variable(tf.random_normal([inSize, outSize]))
    biases = tf.Variable(tf.zeros([1, outSize]) + 0.1 )
    
    Wx_plus_b = tf.matmul(inputs, weights) + biases
    
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
        
    return outputs

###
    
#1 make real data

x_data = np.linspace(-1, 1, 300)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape)
y_data = np.sin(np.multiply(x_data, 10))-0.5 + noise


#2 define placeholder for inputs to network
xs = tf.placeholder(tf.float32, [None, 1])
ys = tf.placeholder(tf.float32, [None, 1])

#3 add hidden layer
L1 = add_layer(xs, 1, 10, tf.nn.relu)

#4 add output layer
prediction = add_layer(L1, 10, 1)


#5 the error between prediction and real data
loss = tf.reduce_mean(tf.square(ys-prediction), reduction_indices=[1])
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

#6 plot real data 
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(x_data, y_data)
plt.ion()
plt.show()

for i in range(1000):
    #training
    sess.run(train_step, feed_dict={xs:x_data, ys:y_data})
    if i%50 == 0:
        #print stepwise result
        try:
            ax.lines.remove(lines[0])
        except Exception:
            pass
        prediction_value = sess.run(prediction, feed_dict={xs:x_data})
        #plot prediction
        lines = ax.plot(x_data, prediction_value, markersize = 10)
        plt.pause(0.1)
  
        