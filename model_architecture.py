from basic_model import BasicModel
import tensorflow as tf
from config import *

model = BasicModel()


def generate_model(images_ph, number_of_classes):
    # First layer of convolution
    network = model.conv_layer(images_ph, 5, 3, 16, 1)
    network = model.pooling_layer(network, 5, 2)
    network = model.activation_layer(network)
    print(network)

    # Second layer of convolution
    network = model.conv_layer(network, 4, 16, 32, 1)
    network = model.pooling_layer(network, 4, 2)
    network = model.activation_layer(network)
    print(network)

    # Third layer of convolution
    network = model.conv_layer(network, 3, 32, 64, 1)
    network = model.pooling_layer(network, 3, 2)
    network = model.activation_layer(network)
    print(network)

    network, features = model.flattening_layer(network)
    print(network)

    # Fully connected layer
    network = model.fully_connected_layer(network, features, 1024)
    network = model.activation_layer(network)
    print(network)

    # output layer
    network = model.fully_connected_layer(network, 1024, number_of_classes)
    print(network)
    return network


if __name__ == '__main__':
    images_ph = tf.placeholder(tf.float32, shape=[None, 100, 100, 3])
    generate_model(images_ph, number_of_classes)
