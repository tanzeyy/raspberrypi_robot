#!/usr/bin/env python

# Python 2/3 compatibility
from __future__ import print_function

import tensorflow as tf
import sys
import os


def label_images():
    images = os.listdir('images/BCD')
    results = {}
    final_results = {}

    # Loads label file, strips off carriage return
    label_lines = [line.rstrip() for line in
                   tf.gfile.GFile('tf_files/labels.txt')]

    # Initial the results
    for line in label_lines:
        results[line] = ('no', 0)

    # Unpersists graph from file
    with tf.gfile.FastGFile('tf_files/graph.pb', 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

    # Open a session to label images
    with tf.Session() as sess:
        for image in images:
            softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
            image_data = tf.gfile.FastGFile(str('images/BCD/' +
                                                image), 'rb').read()
            predictions = sess.run(softmax_tensor,
                                   {'DecodeJpeg/contents:0': image_data})
            top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

            node_id = top_k[0]
            human_string = label_lines[node_id]
            score = predictions[0][node_id]
            print(image.strip('.jpg'), ': %s  %.5f' % (human_string, score))

            if score > results[human_string][1]:
                results[human_string] = (image.strip('.jpg'), score)

    for obj, result in results.items():
        final_results[result[0]] = obj

    if final_results.get('no'):
        final_results.pop('no')

    return final_results


if __name__ == '__main__':
    label_images()
