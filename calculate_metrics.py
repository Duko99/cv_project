# perform all necessary calculations to retrieve mean average precision

# import sys
import numpy as np
from sklearn.metrics import f1_score
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import average_precision_score
from sklearn.metrics import PrecisionRecallDisplay
import matplotlib.pyplot as plt
from itertools import cycle

def calc_metrics(classes, test_labels, predictions_prob, predictions):
    # For each class, get precisions and recalls based on the probabilities (using confidence intervals)
    precision = dict()
    recall = dict()
    average_precision = dict()
    for i in range(len(classes)):
        precision[i], recall[i], _ = precision_recall_curve(test_labels[:, i], predictions_prob[:, i])
        average_precision[i] = average_precision_score(test_labels[:, i], predictions_prob[:, i])

    # A "micro-average": quantifying score on all classes jointly
    precision["micro"], recall["micro"], _ = precision_recall_curve(
        test_labels.ravel(), predictions_prob.ravel()
    )
    average_precision["micro"] = average_precision_score(test_labels, predictions_prob, average="micro")

    # get f-1 score for each class
    f_scores = f1_score(test_labels, predictions, average=None)

    return precision, recall, average_precision, f_scores

def plot_pr_curves(classes, sorted_test_classes, precision, recall, average_precision, f_scores):
    # setup plot details
    colors = cycle(["navy", "turquoise", "darkorange", "cornflowerblue", "teal", "magenta", "red", "darkmagenta", "lawngreen", "chocolate", "black"])

    _, ax = plt.subplots(figsize=(15, 12))

    lines, labels = [], []
    for f_score in f_scores:
        x = np.linspace(0.01, 1)
        y = f_score * x / (2 * x - f_score)
        (l,) = plt.plot(x[y >= 0], y[y >= 0], color="gray", alpha=0.2)
        plt.annotate("f1={0:0.1f}".format(f_score), xy=(0.9, y[45] + 0.02))

    display = PrecisionRecallDisplay(
        recall=recall["micro"],
        precision=precision["micro"],
        average_precision=average_precision["micro"],
    )
    display.plot(ax=ax, name="Micro-average precision-recall", color="gold")

    for i, class_label, f_score, color in zip(range(len(classes)), sorted_test_classes, f_scores, colors):
        display = PrecisionRecallDisplay(
            recall=recall[i],
            precision=precision[i],
            average_precision=average_precision[i],
        )
        display.plot(ax=ax, name=f"{class_label}: (f1={np.format_float_positional(f_score, precision=3)})", color=color)

    # add the legend for the iso-f1 curves
    handles, labels = display.ax_.get_legend_handles_labels()
    handles.extend([l])
    labels.extend(["iso-f1 curves with f1 scores annotated"])
    # set the legend and the axes
    ax.set_xlim([0.0, 1.0])
    ax.set_ylim([0.0, 1.05])

    # make the legend show outside the plot: https://stackoverflow.com/a/4701285
    # Shrink current axis by 20%
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    # Put a legend to the right of the current axis
    ax.legend(handles=handles, labels=labels, loc='center left', bbox_to_anchor=(1, 0.5))

    ax.set_title("Precision-Recall curve for all class, and micro-average over all classes")

    plt.show()

def calculate_map(average_precision):
    # remove the elements pertaining to 'totals', i.e., 'micro', etc.
    del average_precision['micro']

    aps = average_precision.values()
    sum = 0
    for ap in aps:
        sum += ap
    return sum / len(aps)

def do_map(classes, test_labels, predictions_prob, predictions, sorted_test_classes):
    precision, recall, average_precision, f_scores = calc_metrics(classes, test_labels, predictions_prob, predictions)

    plot_pr_curves(classes, sorted_test_classes, precision, recall, average_precision, f_scores)

    map = calculate_map(average_precision)
    print('Mean average precision: {}'.format(map))