import os
import re
import cv2
import numpy as np
from imagePreprocessing import edgeDetectCanny
from imagePreprocessing import equalizeImage

# get the all original output filenames
def readInImages(datasetName, folder, do_preprocessing, illum_flag_list = None, curr_labels = None):
    print("reading in images for subset: {}".format(folder))
    image_list = []
    imgRegExp = re.compile(r'.*[.](JPG)$')
    # https://stackoverflow.com/a/3207973
    all_image_filenames = next(os.walk('data/{}/{}'.format(datasetName, folder)),
                         (None, None, []))[2]  # [] if no file
    # filter out file names that are not JPEGs
    all_image_filenames = [i for i in all_image_filenames if imgRegExp.match(i)]
    print('all_image_filenames length: {}'.format(len(all_image_filenames)))
    # walk() outputs unordered, so we need to sort
    all_image_filenames.sort()
    # print("all_image_filenames: {}".format(all_image_filenames))
    # print("illum_flag_list length: {}".format(len(all_image_filenames)))
    # print("curr_labels length: {}".format(len(curr_labels)))

    # if we're not passed an `illum_flag_list` and `curr_label` list, then assume not
    # doing pre-processing (as those lists are required for it) and just read in the
    # image. Still check that the `do_preprocessing` flag is set to false
    if illum_flag_list == None and curr_labels == None and do_preprocessing == False:
        for fn in all_image_filenames:
            im = cv2.imread('data/{}/{}/{}'.format(datasetName, folder, fn))

            new_im = resizeImage(im)
            
            image_list.append(np.asarray(new_im))
    else:
        for fn, illum_flag, curr_label in zip(all_image_filenames, illum_flag_list, curr_labels):
            im = cv2.imread('data/{}/{}/{}'.format(datasetName, folder, fn))

            if do_preprocessing:
                # === do image pre-processing ===
                # equalize the image to boost brightness when the illum flag is set (image was
                # taken in the dark)
                if illum_flag == 'On':
                    im = equalizeImage(im)

                # perform Canny edge detection on non-empty photos
                if curr_label != 'Empty photo':
                    im = edgeDetectCanny(im)

                # === done image pre-processing ===

            
            new_im = resizeImage(im)
            
            image_list.append(np.asarray(new_im))

    return image_list

def resizeImage(im):
    desired_size = 224

    # resize the image to conserve memory, and transform it to be square while
    #   maintaining the aspect ration (give it padding):
    #   https://jdhao.github.io/2017/11/06/resize-image-to-square-with-padding/#using-opencv
    # we don't wrap this in the `do_preprocessing` block, as images will always need
    #   to be appropriately formatted as inputs to the CNN
    old_size = im.shape[:2]
    ratio = float(desired_size)/max(old_size)
    new_size = tuple([int(x*ratio) for x in old_size])
    im = cv2.resize(im, (new_size[1], new_size[0]))

    delta_w = desired_size - new_size[1]
    delta_h = desired_size - new_size[0]
    top, bottom = delta_h//2, delta_h-(delta_h//2)
    left, right = delta_w//2, delta_w-(delta_w//2)

    color = [0, 0, 0]
    new_im = cv2.copyMakeBorder(im, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)

    return new_im