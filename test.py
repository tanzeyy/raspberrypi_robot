import os
import json

# Import local functions
import images_classify.detectors.label_images as li
import images_classify.preproc.capture as cap
import images_classify.detectors.is_yellow as iy


def ImageClassify(shelf):
    images = os.listdir("images_classify/images/%s" % shelf)

    if shelf == 'A':
        results = json.dumps(iy.FindYellowCube(images))
    else:
        results = json.dumps(li.LabelImages(images, shelf))

    if not os.path.exists("images_classify/results"):
        os.makedirs("images_classify/results")

    with open("images_classify/results/%s.json" % shelf, 'wr') as f:
        f.write(results)


def run(shelf, side):
    cap.Capture(shelf, side)
    if side == "left":
        ImageClassify(shelf)

if __name__ == '__main__':
    import sys
    try:
        shelf, side = sys.argv[1:]
    except:
        shelf, side = 'A', 'right'

    run(shelf, side, )
