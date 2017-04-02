import os
import json

# Import local functions
import images_classify.detectors.label_images as li
import images_classify.preproc.capture as cap


def run(cap_src=0):
    cap.Capture(cap_src)
    images = os.listdir("images_classify/images")

    results = json.dumps(li.LabelImages(images))

    if not os.path.exists('images_classify/results'):
        os.makedirs('images_classify/results')

    with open("images_classify/results/results.json", 'w') as f:
        f.write(results)

if __name__ == '__main__':
    import sys
    try:
        cap_src = sys.argv[1]
    except:
        cap_src = 0

    run(cap_src)
