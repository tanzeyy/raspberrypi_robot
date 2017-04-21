import os
import pickle

# Import local modules
from images_classify.label_images import LabelImages
from images_classify.capture import Capture
from images_classify.yellow_color import is_yellow


def ImageClassify(shelf, side):

    # Get images directory
    images = os.listdir("images_classify/images/%s/%s" % (shelf, side))

    # Get and write results to files
    if shelf == 'A':
        results = is_yellow()
    else:
        results = LabelImages(shelf, side)
    print results

    if not os.path.exists("images_classify/results"):
        os.makedirs("images_classify/results")

    with open(("images_classify/results/%s" + ".txt") % shelf, 'w') as f:
        f.write(pickle.dumps(results))


def run(shelf, side):
    if shelf == 'A':
        if side == 'right':
            Capture(shelf, side)
        else:
            Capture(shelf, side)
            ImageClassify(shelf, side)
    else:
        Capture(shelf, side)
        ImageClassify(shelf, side)


# run('A', 'right')
