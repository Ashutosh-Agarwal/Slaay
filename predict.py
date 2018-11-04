import cv2
import numpy as np
import tensorflow as tf

from config import *


def prediction(image):
    # Get the image from path and reshape it
    img = cv2.imread(image)
    session = tf.Session()
    img = cv2.resize(img, (100, 100))
    img = img.reshape(1, 100, 100, 3)
    labels = np.zeros((1, number_of_classes))

    # Create an object to save the graph
    saver = tf.train.import_meta_graph(os.path.join(model_path, 'model.meta'))

    # For restore the model
    saver.restore(session, tf.train.latest_checkpoint('./checkpoints'))

    # Create graph object for getting the same network architecture
    graph = tf.get_default_graph()

    # Get the last layer of the network by it's name which includes all the previous layers too
    network = graph.get_tensor_by_name('add_4:0')

    # Create placeholders to pass the image and get output labels
    im_ph = graph.get_tensor_by_name('Placeholder:0')
    label_ph = graph.get_tensor_by_name('Placeholder_1:0')

    # In order to make the output to be either 0 or 1.
    network = tf.nn.sigmoid(network)

    # Creating the feed_dict that is required to be fed to calculate y_pred
    feed_dict_testing = {im_ph: img, label_ph: labels}
    result = session.run(network, feed_dict=feed_dict_testing)
    return result


if __name__ == '__main__':
    tst = 'test/test_11.jpg'
    print(prediction(tst))
    index = prediction(tst).flatten().argmax()
    p_dict = {0: 'Fastrack', 1: 'MVMT', 2: 'TIMEX'}
    print(p_dict[index])
            



