import tensorflow as tf


class BasicModel:

    def add_weights(self, shape):
        # To create all weight connections
        return tf.Variable(tf.truncated_normal(shape=shape, stddev=0.05))

    def add_biases(self, shape):
        # To add biases
        return tf.Variable(tf.constant(0.05, shape=shape))

    def conv_layer(self, layer, kernel, input_shape, output_shape, stride_size):
        # convolution starts here
        weights = self.add_weights([kernel, kernel, input_shape, output_shape])
        biases = self.add_biases([output_shape])
        stride = [1, stride_size, stride_size, 1]
        layer = tf.nn.conv2d(layer, weights, strides=stride, padding='SAME') + biases
        return layer

    def pooling_layer(self, layer, kernel_size, stride_size):
        # It reduces the complexity
        kernel = [1, kernel_size, kernel_size, 1]
        stride = [1, stride_size, stride_size, 1]
        return tf.nn.max_pool(layer, ksize=kernel, strides=stride, padding='SAME')

    def flattening_layer(self, layer):
        input_size = layer.get_shape().as_list()
        new_size = input_size[-1] * input_size[-2] * input_size[-3]
        return tf.reshape(layer, [-1, new_size]),new_size

    def fully_connected_layer(self, layer, input_shape, output_shape):
        weights = self.add_weights([input_shape, output_shape])
        biases = self.add_biases([output_shape])
        layer = tf.matmul(layer, weights) + biases
        return layer

    def activation_layer(self, layer):
        return tf.nn.relu(layer)
