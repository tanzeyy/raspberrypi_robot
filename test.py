import os
import json

# Import local functions
import images_classify.detectors.label_images as li
import images_classify.preproc.capture as cap
import images_classify.detectors.is_yellow as iy


def run(shelf):
    cap.Capture(shelf)
    images = os.listdir("images_classify/images/%s" % shelf)
    if shelf == 'A':
        results = json.dumps(iy.FindYellowCube(images))
    else:
        results = json.dumps(li.LabelImages(images, shelf))

    with open("images_classify/results/%s.json" % shelf, 'wr') as f:
        f.write(results)

if __name__ == '__main__':
    import sys
    try:
        shelf = sys.argv[1]
    except:
        shelf = 'A'

    run(shelf)
