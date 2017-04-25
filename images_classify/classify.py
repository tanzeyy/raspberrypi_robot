import os
import pickle

# Import local modules
from label_images import label_images
from yellow_color import is_yellow


def image_classify(shelf):
    # Get and write results to files
    if shelf == 'A':
        results = is_yellow()
    else:
        results = label_images()
    print results

    with open("results.txt", 'w') as f:
        f.write(pickle.dumps(results))

    return results

if __name__ == '__main__':
    image_classify("B")
