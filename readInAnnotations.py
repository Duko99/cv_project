import csv

def readInAnnotations(datasetName, folder, do_preprocessing):
    print("reading in labels for subset: {}".format(folder))
    # print('path: data/{}/{}/{}.csv'.format(datasetName, folder, folder))

    if do_preprocessing:
        labelList, illum_flag_list = readCsv(
            datasetName, folder, do_preprocessing)
        print("returning labelList of length: {}".format(len(labelList)))
        return labelList, illum_flag_list
    else:
        labelList = readCsv(datasetName, folder, do_preprocessing)
        print("returning labelList of length: {}".format(len(labelList)))
        return labelList


def readCsv(datasetName, folder, do_preprocessing):
    labelList = []
    illum_flag_list = []

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
                # FIXME handle when hitlist contains more than one item
                # (e.g., BB06 IMG_512 has 'kangaroo' and 'empty photo') - sort of
                # handled, need to make more dynamic
                hit_list = row[22]
                # print("hit_list: {}".format(hit_list))
                if hit_list == '':
                    labelList.append("Empty photo")
                elif hit_list == 'Empty photo\nHuman Presense/Deployment':
                    labelList.append("Human Presense/Deployment")
                elif hit_list == 'Kangaroo\nEmpty photo':
                    labelList.append("Kangaroo")
                else:
                    # FIXME: redundant case?
                    labelList.append(hit_list.replace("\n", ", "))

                if do_preprocessing:
                    illum_flag_list.append(row[7])

                line_count += 1
    
    if do_preprocessing:
        return labelList, illum_flag_list
    else:
        return labelList
