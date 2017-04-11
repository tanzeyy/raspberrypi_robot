import os
import json

# Import local functions
import images_classify.label_images as li
import images_classify.capture as cap


def ImageClassify(shelf):

    # Get images directory
    images = os.listdir("images_classify/images/%s" % shelf)

    # Get and write results to files
    results = json.dumps(li.LabelImages(images, shelf))

    if not os.path.exists("images_classify/results"):
        os.makedirs("images_classify/results")

    with open(("images_classify/results/%s" + ".json") % shelf, 'w') as f:
        f.write(results)


def run(shelf, side):
    cap.Capture(shelf, side)
    ImageClassify(shelf)
run("A", "right")
