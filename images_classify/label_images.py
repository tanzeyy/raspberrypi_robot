import tensorflow as tf
import sys
import os


def LabelImages(shelf, side):

    images = os.listdir("images_classify/images/%s/%s" % (shelf, side))

    results = {}
    # Loads label file, strips off carriage return
    label_lines = [line.rstrip() for line in
                   tf.gfile.GFile("images_classify/tf_files/labels.txt")]

    # Unpersists graph from file
    with tf.gfile.FastGFile("images_classify/tf_files/graph.pb", 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

    # Open a session to label images
    with tf.Session() as sess:
        for image in images:
            print(str(image))
            softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
            image_data = tf.gfile.FastGFile(str("images_classify/images/%s/%s/" +
                                            image) % (shelf, side), 'rb').read()
            predictions = sess.run(softmax_tensor,
                                   {'DecodeJpeg/contents:0': image_data})
            top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

            for node_id in top_k:
                human_string = label_lines[node_id]
                score = predictions[0][node_id]
                if score > 0.45:
                    results[str(image).strip('.jpg')] = str(human_string)

                print('%s (score = %.5f)' % (human_string, score))

    return results
