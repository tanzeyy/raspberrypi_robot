import os
import pickle

# Import local modules
import images_classify.label_images as li
import images_classify.capture as cap


def ImageClassify(shelf, side):

    # Get images directory
    images = os.listdir("images_classify/images/%s/%s" % (shelf, side))

    # Get and write results to files
    results = li.LabelImages(shelf, side)
    print results

    if not os.path.exists("images_classify/results"):
        os.makedirs("images_classify/results")

    with open(("images_classify/results/%s" + ".txt") % shelf, 'w') as f:
        f.write(pickle.dumps(results))


def run(shelf, side):
    cap.Capture(shelf, side)
    ImageClassify(shelf, side)


# run('A', 'right')
