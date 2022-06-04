import sys
import os
import numpy as np
from sklearn.model_selection import train_test_split
import collections
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf
from readInImages import readInImages
from readInAnnotations import readInAnnotations

args = sys.argv
print("args: {}".format(args))
using_batch_generator = args[1] == 'true'
print('using_batch_generator? {}'.format(using_batch_generator))
do_preprocessing = args[2] == 'true'
print('doing pre-processing? {}'.format(do_preprocessing))
dataset_names = args[3:len(args)]
print("dataset_names: {}".format(dataset_names))

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
        curr_labels, illum_flag_list = readInAnnotations(fn, folder, do_preprocessing)
        all_image_labels = [*all_image_labels, *curr_labels]
        all_images = [*all_images, *readInImages(fn, folder, do_preprocessing, illum_flag_list, curr_labels)]
        print("done current subset")

classes = set(all_image_labels)
print("all classes (length={}): {}".format(len(classes), classes))

# print('all_images: {}'.format(all_images))
print("all_images size: {}".format(len(all_images)))
print("all_image_labels size: {}".format(len(all_image_labels)))

# === split the dataset ===
training_images, test_images, training_labels, test_labels, training_classes, test_classes = splitDataset(all_images, all_image_labels)

timeout_counter = 0
while len(training_classes) != len(test_classes):
    # keep re-splitting until we have equal classes for train/test sets
    training_images, test_images, training_labels, test_labels, training_classes, test_classes = splitDataset(all_images, all_image_labels)
    timeout_counter+=1
    if timeout_counter >= 100:
        raise Exception('Too many attempts to re-split the dataset. This happens when the train and test datasets cannot be properly split with even number of classes. Consider adding more of each class. Exiting...')
print('final training_classes: {}'.format(training_classes))
print('final test_classes: {}'.format(test_classes))

counter_all = collections.Counter(all_image_labels)
print("all classes count: {}".format(counter_all))

counter_train = collections.Counter(training_labels)
print("train classes count: {}".format(counter_train))

counter_test = collections.Counter(test_labels)
print("test classes count: {}".format(counter_test))

# integer-encode labels so they can be one-hot-encoded
# https://stackoverflow.com/a/56227965/6476994
label_encoder = LabelEncoder()
training_labels = np.array(training_labels)
training_labels = label_encoder.fit_transform(training_labels)
test_labels = np.array(test_labels)
test_labels = label_encoder.fit_transform(test_labels)

# one-hot encode labels
training_labels = tf.keras.utils.to_categorical(training_labels, num_classes=len(training_classes))
test_labels = tf.keras.utils.to_categorical(test_labels, num_classes=len(test_classes))

# convert list of numpy arrays to numpy array of numpy arrays
# https://stackoverflow.com/a/27516930/6476994
training_images = np.stack(training_images, axis = 0)
test_images = np.stack(test_images, axis = 0)

print("done stacking")
print("training_images shape: {}".format(training_images.shape))
print("test_images shape: {}".format(test_images.shape))

if using_batch_generator:
    print('saving image filenames and labels in separate train/test files')
    # `all_images` will be the filenames if the `using_batch_generator` is passed
    np.save('train_image.npy', training_images)
    np.save('test_image.npy', test_images)

    np.save('train_labels.npy', training_labels)
    np.save('test_labels.npy', test_labels)