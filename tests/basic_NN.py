import tensorflow as tf

import matplotlib
from matplotlib import pyplot as plt

matplotlib.rcParams['figure.figsize'] = [9, 6]

x = tf.linspace(-2, 2, 201)
x = tf.cast(x, tf.float32)

def f(x):
  y = x**2 + 2*x - 5
  return y

y = f(x) + tf.random.normal(shape=[201])

plt.plot(x.numpy(), y.numpy(), '.', label='Data')
plt.plot(x, f(x),  label='Ground truth')
plt.legend()

class Model(tf.keras.Model):
  def __init__(self, units):
    super().__init__()
    self.inputlayer = tf.keras.layers.InputLayer(input_shape=(1,))
    self.dense1 = tf.keras.layers.Dense(units=units,
                                        activation=tf.nn.selu,
                                        kernel_initializer=tf.random.normal,
                                        bias_initializer=tf.random.normal)
    self.dense2 = tf.keras.layers.Dense(units=units, activation=tf.nn.selu,
                                        kernel_initializer=tf.random.normal,
                                        bias_initializer=tf.random.normal)
    self.dense3 = tf.keras.layers.Dense(units=units, activation=tf.nn.selu,
                                        kernel_initializer=tf.random.normal,
                                        bias_initializer=tf.random.normal)
    self.dense4 = tf.keras.layers.Dense(1)

  def call(self, x, training=True):
    # For Keras layers/models, implement `call` instead of `__call__`.
    x = x[:, tf.newaxis]
    x = self.inputlayer(x)
    x = self.dense1(x)
    x = self.dense2(x)
    x = self.dense3(x)
    x = self.dense4(x)
    return tf.squeeze(x, axis=1)
    # return x
  
model = Model(6)
plt.plot(x, model(x), label='Untrained predictions')
plt.title('Training')

variables = model.variables

optimizer = tf.optimizers.Adam(learning_rate=0.01)

for step in range(1000):
  with tf.GradientTape() as tape:
    prediction = model(x)
    error = (y-prediction)**2
    mean_error = tf.reduce_mean(error)
  gradient = tape.gradient(mean_error, variables)
  optimizer.apply_gradients(zip(gradient, variables))

  if step % 100 == 0:
    print(f'Mean squared error: {mean_error.numpy():0.3f}')



plt.plot(x, model(x), label='Trained predictions')
plt.legend()