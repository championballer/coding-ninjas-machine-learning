import tensorflow as tf
import pandas as pd
import numpy as np
from tensorflow.contrib import rnn
from sklearn.metrics import f1_score, accuracy_score, recall_score, precision_score



#########################################################################
#      https://www.kaggle.com/mlg-ulb/creditcardfraud
########################################################################


def preProcess():

    data = pd.read_csv('creditcard.csv', skiprows=[0], header=None)

    features = data.iloc[:, 1:30]
    labels = data.iloc[:, -1]

    return features, labels

def get_batches(x, y, batch_size=100):
    n_batches = len(x) // batch_size
    x, y = x[:n_batches * batch_size], y[:n_batches * batch_size]
    for ii in range(0, len(x), batch_size):
        yield x[ii:ii + batch_size], y[ii:ii + batch_size]


def train_test_neural_network():

    features, labels, = preProcess()

    split_frac1 = 0.8

    idx1 = int(len(features) * split_frac1)
    train_x, test_x = features[:idx1], features[idx1:]
    train_y, test_y = labels[:idx1], labels[idx1:]


    epochs = 8
    n_classes = 1
    n_units = 200
    n_features = 29
    batch_size = 35

    # Create the graph object
    graph = tf.Graph()
    # Add nodes to the graph
    with graph.as_default():

        # shape of place holder when training (<batch size>, 30)
        xplaceholder = tf.placeholder('float', [None, n_features])
        # shape of place holder when training (<batch size>,)
        yplaceholder = tf.placeholder('float')

        # giving the weights and biases random values
        layer = {'weights': tf.Variable(tf.random_normal([n_units, n_classes])),
                 'bias': tf.Variable(tf.random_normal([n_classes]))}

        x = tf.split(xplaceholder, n_features, 0)

        lstm_cell = rnn.BasicLSTMCell(n_units)

        outputs, states = rnn.static_rnn(lstm_cell, x, dtype=tf.float32)

        output = tf.matmul(outputs[-1], layer['weights']) + layer['bias']

        logit = tf.reshape(output, [-1])

        cost, final_state = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=logit, labels=yplaceholder))

        optimizer = tf.train.AdamOptimizer().minimize(cost)

        predictions = tf.round(tf.nn.sigmoid(logit))

    with tf.Session(graph=graph) as sess:

        tf.set_random_seed(1)

        sess.run(tf.global_variables_initializer())

        iteration = 1
        for e in range(epochs):
            for ii, (x, y) in enumerate(get_batches(np.array(train_x), np.array(train_y), batch_size), 1):

                feed = {xplaceholder: x,
                        yplaceholder: y,
                        }

                loss, states, _ = sess.run([cost, final_state, optimizer], feed_dict=feed)

                if iteration % 5 == 0:
                    print("Epoch: {}/{}".format(e, epochs),
                          "Iteration: {}".format(iteration),
                          "Train loss: {:.3f}".format(loss))
                iteration += 1

    # -----------------testing test set-----------------------------------------
    print("starting testing set")
    prediction_val = []
    y_val = []
    with tf.Session(graph=graph) as sess:

        tf.set_random_seed(1)

        for ii, (x, y) in enumerate(get_batches(np.array(test_x), np.array(test_y), batch_size), 1):

            feed = {xplaceholder: x,
                    yplaceholder: y,
                    }

            prediction = sess.run(predictions, feed_dict=feed)
            prediction = prediction.astype(int)

            for i in range(len(prediction)):
                prediction_val.append(prediction[i][0])
                y_val.append(y[i])

        accuracy = accuracy_score(y_val, prediction_val)
        f1 = f1_score(y_val, prediction_val, average='macro')
        recall = recall_score(y_true=y_val, y_pred=prediction_val, average='macro')
        precision = precision_score(y_val, prediction_val, average='macro')

        print("-----------------testing validation set-----------------------------------------")
        print("Test accuracy: {:.3f}".format(accuracy))
        print("F1 Score: {:.3f}".format(f1))
        print("Recall: {:.3f}".format(recall))
        print("Precision: {:.3f}".format(precision))

if __name__ == '__main__':
train_test_neural_network()
