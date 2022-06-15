import xlsxwriter

workbook = xlsxwriter.Workbook('epoch_data.xlsx')
worksheet = workbook.add_worksheet()

data = []

str = """
Epoch 1/90
89/89 [==============================] - 9s 85ms/step - loss: 44.9683 - accuracy: 0.6174 - top_k_categorical_accuracy: 0.9712 - val_loss: 0.9676 - val_accuracy: 0.6963 - val_top_k_categorical_accuracy: 0.9824
Epoch 2/90
89/89 [==============================] - 7s 83ms/step - loss: 0.8701 - accuracy: 0.7222 - top_k_categorical_accuracy: 0.9840 - val_loss: 0.8198 - val_accuracy: 0.7490 - val_top_k_categorical_accuracy: 0.9835
Epoch 3/90
89/89 [==============================] - 7s 80ms/step - loss: 0.7641 - accuracy: 0.7551 - top_k_categorical_accuracy: 0.9884 - val_loss: 0.7564 - val_accuracy: 0.7712 - val_top_k_categorical_accuracy: 0.9877
Epoch 4/90
89/89 [==============================] - 7s 82ms/step - loss: 0.7116 - accuracy: 0.7713 - top_k_categorical_accuracy: 0.9917 - val_loss: 0.7629 - val_accuracy: 0.7599 - val_top_k_categorical_accuracy: 0.9866
Epoch 5/90
89/89 [==============================] - 7s 82ms/step - loss: 0.6774 - accuracy: 0.7813 - top_k_categorical_accuracy: 0.9916 - val_loss: 0.7024 - val_accuracy: 0.7740 - val_top_k_categorical_accuracy: 0.9870
Epoch 6/90
89/89 [==============================] - 7s 82ms/step - loss: 0.6429 - accuracy: 0.7933 - top_k_categorical_accuracy: 0.9923 - val_loss: 0.6589 - val_accuracy: 0.7961 - val_top_k_categorical_accuracy: 0.9884
Epoch 7/90
89/89 [==============================] - 7s 82ms/step - loss: 0.6240 - accuracy: 0.7943 - top_k_categorical_accuracy: 0.9930 - val_loss: 0.6466 - val_accuracy: 0.7954 - val_top_k_categorical_accuracy: 0.9898
Epoch 8/90
89/89 [==============================] - 8s 85ms/step - loss: 0.5901 - accuracy: 0.8041 - top_k_categorical_accuracy: 0.9933 - val_loss: 0.6218 - val_accuracy: 0.8011 - val_top_k_categorical_accuracy: 0.9898
Epoch 9/90
89/89 [==============================] - 7s 81ms/step - loss: 0.5737 - accuracy: 0.8041 - top_k_categorical_accuracy: 0.9938 - val_loss: 0.6039 - val_accuracy: 0.8060 - val_top_k_categorical_accuracy: 0.9926
Epoch 10/90
89/89 [==============================] - 7s 79ms/step - loss: 0.5458 - accuracy: 0.8138 - top_k_categorical_accuracy: 0.9960 - val_loss: 0.5857 - val_accuracy: 0.8098 - val_top_k_categorical_accuracy: 0.9933
Epoch 11/90
89/89 [==============================] - 7s 79ms/step - loss: 0.5279 - accuracy: 0.8206 - top_k_categorical_accuracy: 0.9961 - val_loss: 0.5658 - val_accuracy: 0.8116 - val_top_k_categorical_accuracy: 0.9933
Epoch 12/90
89/89 [==============================] - 7s 81ms/step - loss: 0.5159 - accuracy: 0.8220 - top_k_categorical_accuracy: 0.9967 - val_loss: 0.5520 - val_accuracy: 0.8250 - val_top_k_categorical_accuracy: 0.9951
Epoch 13/90
89/89 [==============================] - 7s 81ms/step - loss: 0.4927 - accuracy: 0.8277 - top_k_categorical_accuracy: 0.9969 - val_loss: 0.5771 - val_accuracy: 0.8109 - val_top_k_categorical_accuracy: 0.9937
Epoch 14/90
89/89 [==============================] - 8s 86ms/step - loss: 0.4798 - accuracy: 0.8309 - top_k_categorical_accuracy: 0.9976 - val_loss: 0.5269 - val_accuracy: 0.8306 - val_top_k_categorical_accuracy: 0.9951
Epoch 15/90
89/89 [==============================] - 7s 84ms/step - loss: 0.4576 - accuracy: 0.8391 - top_k_categorical_accuracy: 0.9972 - val_loss: 0.5725 - val_accuracy: 0.8190 - val_top_k_categorical_accuracy: 0.9944
Epoch 16/90
89/89 [==============================] - 7s 82ms/step - loss: 0.4453 - accuracy: 0.8425 - top_k_categorical_accuracy: 0.9983 - val_loss: 0.5023 - val_accuracy: 0.8359 - val_top_k_categorical_accuracy: 0.9947
Epoch 17/90
89/89 [==============================] - 7s 84ms/step - loss: 0.4205 - accuracy: 0.8518 - top_k_categorical_accuracy: 0.9982 - val_loss: 0.5031 - val_accuracy: 0.8337 - val_top_k_categorical_accuracy: 0.9968
Epoch 18/90
89/89 [==============================] - 7s 82ms/step - loss: 0.4140 - accuracy: 0.8499 - top_k_categorical_accuracy: 0.9989 - val_loss: 0.5136 - val_accuracy: 0.8299 - val_top_k_categorical_accuracy: 0.9972
Epoch 19/90
89/89 [==============================] - 7s 81ms/step - loss: 0.4002 - accuracy: 0.8561 - top_k_categorical_accuracy: 0.9989 - val_loss: 0.4743 - val_accuracy: 0.8432 - val_top_k_categorical_accuracy: 0.9965
Epoch 20/90
89/89 [==============================] - 7s 80ms/step - loss: 0.4018 - accuracy: 0.8550 - top_k_categorical_accuracy: 0.9987 - val_loss: 0.4513 - val_accuracy: 0.8464 - val_top_k_categorical_accuracy: 0.9968
Epoch 21/90
89/89 [==============================] - 7s 80ms/step - loss: 0.3696 - accuracy: 0.8652 - top_k_categorical_accuracy: 0.9993 - val_loss: 0.5051 - val_accuracy: 0.8306 - val_top_k_categorical_accuracy: 0.9968
Epoch 22/90
89/89 [==============================] - 7s 83ms/step - loss: 0.3623 - accuracy: 0.8675 - top_k_categorical_accuracy: 0.9992 - val_loss: 0.4273 - val_accuracy: 0.8562 - val_top_k_categorical_accuracy: 0.9968
Epoch 23/90
89/89 [==============================] - 7s 83ms/step - loss: 0.3452 - accuracy: 0.8744 - top_k_categorical_accuracy: 0.9995 - val_loss: 0.4539 - val_accuracy: 0.8513 - val_top_k_categorical_accuracy: 0.9975
Epoch 24/90
89/89 [==============================] - 7s 82ms/step - loss: 0.3349 - accuracy: 0.8776 - top_k_categorical_accuracy: 0.9992 - val_loss: 0.4481 - val_accuracy: 0.8408 - val_top_k_categorical_accuracy: 0.9979
Epoch 25/90
89/89 [==============================] - 7s 81ms/step - loss: 0.3206 - accuracy: 0.8834 - top_k_categorical_accuracy: 0.9992 - val_loss: 0.4374 - val_accuracy: 0.8555 - val_top_k_categorical_accuracy: 0.9975
Epoch 26/90
89/89 [==============================] - 7s 83ms/step - loss: 0.3212 - accuracy: 0.8838 - top_k_categorical_accuracy: 0.9996 - val_loss: 0.4451 - val_accuracy: 0.8566 - val_top_k_categorical_accuracy: 0.9979
Epoch 27/90
89/89 [==============================] - 8s 85ms/step - loss: 0.3140 - accuracy: 0.8885 - top_k_categorical_accuracy: 0.9996 - val_loss: 0.4082 - val_accuracy: 0.8636 - val_top_k_categorical_accuracy: 0.9965
Epoch 28/90
89/89 [==============================] - 7s 80ms/step - loss: 0.3062 - accuracy: 0.8868 - top_k_categorical_accuracy: 0.9999 - val_loss: 0.4602 - val_accuracy: 0.8534 - val_top_k_categorical_accuracy: 0.9972
Epoch 29/90
89/89 [==============================] - 7s 80ms/step - loss: 0.2844 - accuracy: 0.8964 - top_k_categorical_accuracy: 0.9995 - val_loss: 0.4038 - val_accuracy: 0.8717 - val_top_k_categorical_accuracy: 0.9979
Epoch 30/90
89/89 [==============================] - 7s 80ms/step - loss: 0.2834 - accuracy: 0.8962 - top_k_categorical_accuracy: 0.9999 - val_loss: 0.4121 - val_accuracy: 0.8640 - val_top_k_categorical_accuracy: 0.9982
Epoch 31/90
89/89 [==============================] - 7s 80ms/step - loss: 0.2645 - accuracy: 0.9047 - top_k_categorical_accuracy: 0.9996 - val_loss: 0.4072 - val_accuracy: 0.8619 - val_top_k_categorical_accuracy: 0.9979
Epoch 32/90
89/89 [==============================] - 7s 81ms/step - loss: 0.2535 - accuracy: 0.9069 - top_k_categorical_accuracy: 0.9999 - val_loss: 0.4385 - val_accuracy: 0.8710 - val_top_k_categorical_accuracy: 0.9979
Epoch 33/90
89/89 [==============================] - 7s 82ms/step - loss: 0.2477 - accuracy: 0.9060 - top_k_categorical_accuracy: 0.9999 - val_loss: 0.4405 - val_accuracy: 0.8471 - val_top_k_categorical_accuracy: 0.9982
Epoch 34/90
89/89 [==============================] - 7s 83ms/step - loss: 0.2462 - accuracy: 0.9066 - top_k_categorical_accuracy: 0.9999 - val_loss: 0.4118 - val_accuracy: 0.8605 - val_top_k_categorical_accuracy: 0.9986
Epoch 35/90
89/89 [==============================] - 7s 82ms/step - loss: 0.2365 - accuracy: 0.9124 - top_k_categorical_accuracy: 0.9999 - val_loss: 0.4024 - val_accuracy: 0.8707 - val_top_k_categorical_accuracy: 0.9979
Epoch 36/90
89/89 [==============================] - 7s 82ms/step - loss: 0.2532 - accuracy: 0.9043 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.4179 - val_accuracy: 0.8559 - val_top_k_categorical_accuracy: 0.9982
Epoch 37/90
89/89 [==============================] - 7s 82ms/step - loss: 0.2316 - accuracy: 0.9145 - top_k_categorical_accuracy: 0.9999 - val_loss: 0.4477 - val_accuracy: 0.8619 - val_top_k_categorical_accuracy: 0.9968
Epoch 38/90
89/89 [==============================] - 7s 84ms/step - loss: 0.2445 - accuracy: 0.9090 - top_k_categorical_accuracy: 0.9999 - val_loss: 0.4417 - val_accuracy: 0.8717 - val_top_k_categorical_accuracy: 0.9979
Epoch 39/90
89/89 [==============================] - 7s 83ms/step - loss: 0.2104 - accuracy: 0.9204 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.3975 - val_accuracy: 0.8749 - val_top_k_categorical_accuracy: 0.9982
Epoch 40/90
89/89 [==============================] - 7s 82ms/step - loss: 0.2037 - accuracy: 0.9254 - top_k_categorical_accuracy: 0.9999 - val_loss: 0.3819 - val_accuracy: 0.8830 - val_top_k_categorical_accuracy: 0.9979
Epoch 41/90
89/89 [==============================] - 7s 80ms/step - loss: 0.1910 - accuracy: 0.9289 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.3900 - val_accuracy: 0.8858 - val_top_k_categorical_accuracy: 0.9975
Epoch 42/90
89/89 [==============================] - 7s 81ms/step - loss: 0.1972 - accuracy: 0.9257 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.4459 - val_accuracy: 0.8671 - val_top_k_categorical_accuracy: 0.9979
Epoch 43/90
89/89 [==============================] - 7s 82ms/step - loss: 0.1931 - accuracy: 0.9279 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.4136 - val_accuracy: 0.8773 - val_top_k_categorical_accuracy: 0.9975
Epoch 44/90
89/89 [==============================] - 7s 83ms/step - loss: 0.1708 - accuracy: 0.9387 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.4267 - val_accuracy: 0.8749 - val_top_k_categorical_accuracy: 0.9975
Epoch 45/90
89/89 [==============================] - 7s 83ms/step - loss: 0.1832 - accuracy: 0.9302 - top_k_categorical_accuracy: 0.9999 - val_loss: 0.4748 - val_accuracy: 0.8446 - val_top_k_categorical_accuracy: 0.9982
Epoch 46/90
89/89 [==============================] - 7s 83ms/step - loss: 0.1711 - accuracy: 0.9366 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.4037 - val_accuracy: 0.8777 - val_top_k_categorical_accuracy: 0.9972
Epoch 47/90
89/89 [==============================] - 7s 82ms/step - loss: 0.1806 - accuracy: 0.9315 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.3831 - val_accuracy: 0.8805 - val_top_k_categorical_accuracy: 0.9968
Epoch 48/90
89/89 [==============================] - 7s 83ms/step - loss: 0.1870 - accuracy: 0.9318 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.4107 - val_accuracy: 0.8798 - val_top_k_categorical_accuracy: 0.9975
Epoch 49/90
89/89 [==============================] - 7s 82ms/step - loss: 0.1675 - accuracy: 0.9392 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.4012 - val_accuracy: 0.8805 - val_top_k_categorical_accuracy: 0.9975
Epoch 50/90
89/89 [==============================] - 7s 83ms/step - loss: 0.1606 - accuracy: 0.9401 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.4541 - val_accuracy: 0.8696 - val_top_k_categorical_accuracy: 0.9975
Epoch 51/90
89/89 [==============================] - 7s 83ms/step - loss: 0.1546 - accuracy: 0.9415 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.4218 - val_accuracy: 0.8770 - val_top_k_categorical_accuracy: 0.9979
Epoch 52/90
89/89 [==============================] - 7s 82ms/step - loss: 0.1630 - accuracy: 0.9373 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.4324 - val_accuracy: 0.8728 - val_top_k_categorical_accuracy: 0.9975
Epoch 53/90
89/89 [==============================] - 7s 82ms/step - loss: 0.1496 - accuracy: 0.9425 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.4170 - val_accuracy: 0.8791 - val_top_k_categorical_accuracy: 0.9975
Epoch 54/90
89/89 [==============================] - 7s 82ms/step - loss: 0.1482 - accuracy: 0.9448 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.4156 - val_accuracy: 0.8830 - val_top_k_categorical_accuracy: 0.9968
Epoch 55/90
89/89 [==============================] - 7s 82ms/step - loss: 0.1351 - accuracy: 0.9484 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.4617 - val_accuracy: 0.8756 - val_top_k_categorical_accuracy: 0.9979
Epoch 56/90
89/89 [==============================] - 7s 83ms/step - loss: 0.1386 - accuracy: 0.9483 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.4730 - val_accuracy: 0.8742 - val_top_k_categorical_accuracy: 0.9979
Epoch 57/90
89/89 [==============================] - 7s 83ms/step - loss: 0.1375 - accuracy: 0.9480 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.4498 - val_accuracy: 0.8773 - val_top_k_categorical_accuracy: 0.9972
Epoch 58/90
89/89 [==============================] - 7s 84ms/step - loss: 0.1251 - accuracy: 0.9531 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.4376 - val_accuracy: 0.8879 - val_top_k_categorical_accuracy: 0.9975
Epoch 59/90
89/89 [==============================] - 7s 84ms/step - loss: 0.1370 - accuracy: 0.9480 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.4408 - val_accuracy: 0.8900 - val_top_k_categorical_accuracy: 0.9975
Epoch 60/90
89/89 [==============================] - 7s 83ms/step - loss: 0.1267 - accuracy: 0.9517 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.4632 - val_accuracy: 0.8777 - val_top_k_categorical_accuracy: 0.9979
Epoch 61/90
89/89 [==============================] - 7s 82ms/step - loss: 0.1154 - accuracy: 0.9584 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.4340 - val_accuracy: 0.8910 - val_top_k_categorical_accuracy: 0.9979
Epoch 62/90
89/89 [==============================] - 7s 82ms/step - loss: 0.1187 - accuracy: 0.9546 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.4542 - val_accuracy: 0.8808 - val_top_k_categorical_accuracy: 0.9982
Epoch 63/90
89/89 [==============================] - 7s 83ms/step - loss: 0.1095 - accuracy: 0.9590 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.4678 - val_accuracy: 0.8879 - val_top_k_categorical_accuracy: 0.9965
Epoch 64/90
89/89 [==============================] - 8s 85ms/step - loss: 0.1107 - accuracy: 0.9574 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.5180 - val_accuracy: 0.8636 - val_top_k_categorical_accuracy: 0.9972
Epoch 65/90
89/89 [==============================] - 7s 83ms/step - loss: 0.1157 - accuracy: 0.9567 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.4782 - val_accuracy: 0.8812 - val_top_k_categorical_accuracy: 0.9972
Epoch 66/90
89/89 [==============================] - 7s 84ms/step - loss: 0.1054 - accuracy: 0.9621 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.4931 - val_accuracy: 0.8714 - val_top_k_categorical_accuracy: 0.9979
Epoch 67/90
89/89 [==============================] - 8s 85ms/step - loss: 0.1212 - accuracy: 0.9531 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.5752 - val_accuracy: 0.8773 - val_top_k_categorical_accuracy: 0.9965
Epoch 68/90
89/89 [==============================] - 8s 84ms/step - loss: 0.1278 - accuracy: 0.9551 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.4839 - val_accuracy: 0.8812 - val_top_k_categorical_accuracy: 0.9979
Epoch 69/90
89/89 [==============================] - 8s 90ms/step - loss: 0.1072 - accuracy: 0.9603 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.5048 - val_accuracy: 0.8910 - val_top_k_categorical_accuracy: 0.9972
Epoch 70/90
89/89 [==============================] - 8s 85ms/step - loss: 0.1088 - accuracy: 0.9602 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.5312 - val_accuracy: 0.8805 - val_top_k_categorical_accuracy: 0.9975
Epoch 71/90
89/89 [==============================] - 7s 83ms/step - loss: 0.1342 - accuracy: 0.9541 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.5400 - val_accuracy: 0.8833 - val_top_k_categorical_accuracy: 0.9982
Epoch 72/90
89/89 [==============================] - 7s 83ms/step - loss: 0.0990 - accuracy: 0.9634 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.6128 - val_accuracy: 0.8854 - val_top_k_categorical_accuracy: 0.9975
Epoch 73/90
89/89 [==============================] - 7s 84ms/step - loss: 0.0891 - accuracy: 0.9692 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.5474 - val_accuracy: 0.8886 - val_top_k_categorical_accuracy: 0.9975
Epoch 74/90
89/89 [==============================] - 7s 83ms/step - loss: 0.0905 - accuracy: 0.9654 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.5669 - val_accuracy: 0.8861 - val_top_k_categorical_accuracy: 0.9975
Epoch 75/90
89/89 [==============================] - 7s 81ms/step - loss: 0.0761 - accuracy: 0.9714 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.6140 - val_accuracy: 0.8896 - val_top_k_categorical_accuracy: 0.9975
Epoch 76/90
89/89 [==============================] - 7s 82ms/step - loss: 0.0888 - accuracy: 0.9692 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.5817 - val_accuracy: 0.8928 - val_top_k_categorical_accuracy: 0.9975
Epoch 77/90
89/89 [==============================] - 7s 83ms/step - loss: 0.0798 - accuracy: 0.9715 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.5862 - val_accuracy: 0.8931 - val_top_k_categorical_accuracy: 0.9972
Epoch 78/90
89/89 [==============================] - 7s 82ms/step - loss: 0.0809 - accuracy: 0.9688 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.5694 - val_accuracy: 0.8801 - val_top_k_categorical_accuracy: 0.9975
Epoch 79/90
89/89 [==============================] - 7s 82ms/step - loss: 0.0995 - accuracy: 0.9649 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.6521 - val_accuracy: 0.8854 - val_top_k_categorical_accuracy: 0.9958
Epoch 80/90
89/89 [==============================] - 7s 83ms/step - loss: 0.0947 - accuracy: 0.9647 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.6112 - val_accuracy: 0.8777 - val_top_k_categorical_accuracy: 0.9968
Epoch 81/90
89/89 [==============================] - 7s 83ms/step - loss: 0.0915 - accuracy: 0.9667 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.5551 - val_accuracy: 0.8830 - val_top_k_categorical_accuracy: 0.9982
Epoch 82/90
89/89 [==============================] - 7s 81ms/step - loss: 0.0767 - accuracy: 0.9708 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.5987 - val_accuracy: 0.8868 - val_top_k_categorical_accuracy: 0.9975
Epoch 83/90
89/89 [==============================] - 7s 80ms/step - loss: 0.0974 - accuracy: 0.9676 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.6925 - val_accuracy: 0.8773 - val_top_k_categorical_accuracy: 0.9965
Epoch 84/90
89/89 [==============================] - 7s 83ms/step - loss: 0.1161 - accuracy: 0.9580 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.6225 - val_accuracy: 0.8784 - val_top_k_categorical_accuracy: 0.9979
Epoch 85/90
89/89 [==============================] - 7s 83ms/step - loss: 0.0854 - accuracy: 0.9675 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.5665 - val_accuracy: 0.8879 - val_top_k_categorical_accuracy: 0.9975
Epoch 86/90
89/89 [==============================] - 7s 83ms/step - loss: 0.0808 - accuracy: 0.9721 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.6287 - val_accuracy: 0.8851 - val_top_k_categorical_accuracy: 0.9979
Epoch 87/90
89/89 [==============================] - 7s 82ms/step - loss: 0.0602 - accuracy: 0.9775 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.7062 - val_accuracy: 0.8917 - val_top_k_categorical_accuracy: 0.9979
Epoch 88/90
89/89 [==============================] - 7s 84ms/step - loss: 0.0730 - accuracy: 0.9761 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.7357 - val_accuracy: 0.8833 - val_top_k_categorical_accuracy: 0.9968
Epoch 89/90
89/89 [==============================] - 7s 80ms/step - loss: 0.1086 - accuracy: 0.9625 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.7518 - val_accuracy: 0.8640 - val_top_k_categorical_accuracy: 0.9972
Epoch 90/90
89/89 [==============================] - 7s 83ms/step - loss: 0.0944 - accuracy: 0.9671 - top_k_categorical_accuracy: 1.0000 - val_loss: 0.6687 - val_accuracy: 0.8738 - val_top_k_categorical_accuracy: 0.9982
"""

lines = str.split("\n")

curr_epoch_num = None
curr_row = dict()
for line in lines:
    if line == '': continue    
    # print('line: {}'.format(line))
    if "Epoch" in line:
        epoch_number = line.split("Epoch ")[1].split("/")[0]
        curr_epoch_num = epoch_number
        curr_row['Epoch'] = curr_epoch_num
    elif "[==============================]" in line:
        # print('data for epoch {}: '.format(curr_epoch_num))
        data_line = line
        metrics = data_line.split(" - ")

        loss = metrics[2].split(": ")[1]
        # print('loss: {}'.format(loss))
        curr_row['Loss'] = loss

        # for Inception Model, as I forgot to collect other metrics (comment out below
        # code for accuracy, validation loss, and validation accuracy)

        # validation_loss =  metrics[3].split(": ")[1]
        # # print('validation_loss: {}'.format(validation_loss))
        # curr_row['Validation Loss'] = validation_loss

        accuracy = metrics[3].split(": ")[1]
        # print('accuracy: {}'.format(accuracy))
        curr_row['Accuracy'] = accuracy

        validation_loss =  metrics[5].split(": ")[1]
        # print('validation_loss: {}'.format(validation_loss))
        curr_row['Validation Loss'] = validation_loss

        validation_accuracy =  metrics[6].split(": ")[1]
        # print('validation_accuracy: {}'.format(validation_accuracy))
        curr_row['Validation Accuracy'] = validation_accuracy

        data.append(curr_row)
        curr_row = dict()

print('data:\n{}'.format(data))

worksheet.write(0, 0, "Epoch")
worksheet.write(0, 1, "Loss")

# for Inception Model, as I forgot to collect other metrics (comment out below
# code for accuracy, validation loss, and validation accuracy)
# worksheet.write(0, 2, "Validation Loss")

worksheet.write(0, 2, "Accuracy")
worksheet.write(0, 3, "Validation Loss")
worksheet.write(0, 4, "Validation Accuracy")
row_num = 1
for row in data:
    col_num = 0
    for col_key in row:
        cast_col = -1
        try:
            cast_col = int(row[col_key])
        except:
            cast_col = float(row[col_key])

        worksheet.write(row_num, col_num, cast_col)
        col_num+=1
    row_num+=1

workbook.close()