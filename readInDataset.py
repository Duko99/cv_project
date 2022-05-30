import sys
import os
import re
import cv2
import numpy as np
import csv
from sklearn.model_selection import train_test_split
import collections
from sklearn.preprocessing import LabelEncoder

args = sys.argv
print("args: {}".format(args))
dataset_names = args[1:len(args)]
print("dataset_names: {}".format(dataset_names))

# === read in dataset and labels ===

# get the all original output filenames
def readInImages(datasetName, folder):
    print("reading in images for subset: {}".format(folder))
    desired_size = 224
    image_list = []
    imgRegExp = re.compile(r'.*[.](JPG)$')
    # https://stackoverflow.com/a/3207973
    all_image_filenames = next(os.walk('data/{}/{}'.format(datasetName, folder)),
                         (None, None, []))[2]  # [] if no file
    # filter out file names that are not JPEGs
    all_image_filenames = [i for i in all_image_filenames if imgRegExp.match(i)]
    # walk() outputs unordered, so we need to sort
    all_image_filenames.sort()
    # print("all_image_filenames: {}".format(all_image_filenames))
    # print("all_image_filenames length: {}".format(len(all_image_filenames)))
    for fn in all_image_filenames:
        # im = Image.open('data/{}/{}'.format(datasetName, fn))
        im = cv2.imread('data/{}/{}/{}'.format(datasetName, folder, fn))
        # resize the image to conserve memory, and transform it to be square while
        # maintaining the aspect ration (give it padding):
        # https://jdhao.github.io/2017/11/06/resize-image-to-square-with-padding/#using-opencv
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

        
        image_list.append(np.asarray(new_im))

    return image_list

def readInAnnotations(datasetName, folder):
    print("reading in labels for subset: {}".format(folder))
    labelList = []
    # print('path: data/{}/{}/{}.csv'.format(datasetName, folder, folder))
    # https://realpython.com/python-csv/#reading-csv-files-with-csv
    with open('data/{}/{}/{}.csv'.format(datasetName, folder, folder)) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            # print("row: {}".format(row))
            # first row always contains this string, so ignore it
            if "RECONYX - MapView Professional" in row:
                continue
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                # print("Image Name: {}. Hit List: {}".format(row[0], row[22].replace("\n", ", ")))
                # FIXME handle when hitlist contains more than one item (e.g., BB06 IMG_512 has 'kangaroo' and 'empty photo') - sort of handled, need to make more dynamic
                hit_list = row[22]
                # print("hit_list: {}".format(hit_list))
                if hit_list == '':
                    labelList.append("Empty photo")
                elif hit_list == 'Empty photo\nHuman Presense/Deployment':
                    labelList.append("Human Presense/Deployment")
                elif hit_list == 'Kangaroo\nEmpty photo':
                    labelList.append("Kangaroo")
                else:
                    # FIXME: rendundant case?
                    labelList.append(hit_list.replace("\n", ", "))
                line_count += 1
    # print("returning labelList (length: {}): {}".format(len(labelList), labelList))
    # print("returning labelList of length: {}".format(len(labelList)))
    return labelList

def splitDataset(all_images, all_image_labels):
    training_images, test_images, training_labels, test_labels = train_test_split(all_images, all_image_labels, test_size=0.2)
    print("training_labels length: {}".format(len(training_labels)))
    print("test_labels length: {}".format(len(test_labels)))    

    training_classes = []
    for label in training_labels:
        if label not in training_classes:
            training_classes.append(label)
    test_classes = []
    for label in test_labels:
        if label not in test_classes:
            test_classes.append(label)

    print("training_classes (length={}): {}".format(len(training_classes), training_classes))
    print("test_classes (length={}): {}".format(len(test_classes), test_classes))
    return training_images, test_images, training_labels, test_labels, training_classes, test_classes

all_images = []
all_image_labels = []
for fn in dataset_names:
    # get all the folders in the current dataset - e.g., BB01, BB02, ..., BBXY
    # https://stackoverflow.com/a/973488
    all_folders_for_curr_dataset = next(os.walk('data/{}'.format(fn)))[1]
    all_folders_for_curr_dataset = sorted(all_folders_for_curr_dataset)
    print("reading in images and labels for dataset: {}".format(fn))
    print("all_folders_for_curr_dataset: {}".format(all_folders_for_curr_dataset))
    
    for folder in all_folders_for_curr_dataset:   
        all_images = [*all_images, *readInImages(fn, folder)]
        all_image_labels = [*all_image_labels, *readInAnnotations(fn, folder)]
        print("done current subset")

classes = set(all_image_labels)
print("all classes (length={}): {}".format(len(classes), classes))

print("all_images size: {}".format(len(all_images)))
# print("all_image_labels size: {}".format(len(all_image_labels)))

# === split the dataset ===
training_images, test_images, training_labels, test_labels, training_classes, test_classes = splitDataset(all_images, all_image_labels)

timeout_counter = 0
while len(training_classes) != len(test_classes):
    # keep re-spltting until we have equal classes for train/test sets
    training_images, test_images, training_labels, test_labels, training_classes, test_classes = splitDataset(all_images, all_image_labels)
    timeout_counter+=1
    if timeout_counter >= 100:
        raise Exception('Too many attempts to re-split the dataset. This happens when the train and test datasets cannot be properly split with even number of classes. Consider adding more of each class. Exiting...')
print('final training_classes: {}'.format(training_classes))
print('final test_classes: {}'.format(test_classes))
counter = collections.Counter(test_labels)
print("classes count: {}".format(all_image_labels))

# integer-encode labels so they can be one-hot-encoded
# https://stackoverflow.com/a/56227965/6476994
label_encoder = LabelEncoder()
training_labels = np.array(training_labels)
training_labels = label_encoder.fit_transform(training_labels)
test_labels = np.array(test_labels)
test_labels = label_encoder.fit_transform(test_labels)


# convert list of numpy arrays to numpy array of numpy arrays
# https://stackoverflow.com/a/27516930/6476994
training_images = np.stack(training_images, axis = 0)
test_images = np.stack(test_images, axis = 0)

print("done stacking")
print("training_images shape: {}".format(training_images.shape))
print("test_images shape: {}".format(test_images.shape))