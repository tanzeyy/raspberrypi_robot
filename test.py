import os
import json

# Import local functions
import images_classify.label_images as li
import images_classify.capture as cap


<<<<<<< HEAD
def run(cap_src=0):
    cap.Capture(cap_src)
    images = os.listdir("images_classify/images")
=======
def ImageClassify(shelf):
    images = os.listdir("images_classify/images/%s" % shelf)
>>>>>>> half_shelf

    results = json.dumps(li.LabelImages(images))

    if not os.path.exists("images_classify/results"):
        os.makedirs("images_classify/results")

    with open("images_classify/results/results.json", 'w') as f:
        f.write(results)


def run(shelf, side):
    cap.Capture(shelf, side)
    if side == "left":
        ImageClassify(shelf)

if __name__ == '__main__':
    import sys
    try:
<<<<<<< HEAD
        cap_src = sys.argv[1]
    except:
        cap_src = 0

    run(cap_src)
=======
        shelf, side = sys.argv[1:]
    except:
        shelf, side = 'A', 'right'

    run(shelf, side, )
>>>>>>> half_shelf
