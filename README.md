##  Deep learning 

### Image classification with CNN Model


CNNs are a cornerstone of modern AI, excelling in tasks like image classification, object detection, and facial recognition. This article explores CNN basics, practical applications, and how to implement them using popular datasets and frameworks, providing a comprehensive guide to mastering this essential deep learning technology

### Dataset 
##### Content
This Data contains around 25k images of size 150x150 distributed under 6 categories. {'buildings' -> 0, 'forest' -> 1, 'glacier' -> 2, 'mountain' -> 3, 'sea' -> 4, 'street' -> 5 }

The Train, Test and Prediction data is separated in each zip files. There are around 14k images in Train, 3k in Test and 7k in Prediction.

### Model evaluation

Model 1
![download (1)](https://github.com/user-attachments/assets/f194c3d8-21b8-4735-85a0-a08074e5c138)

187/187 ━━━━━━━━━━━━━━━━━━━━ 24s 130ms/step - accuracy: 0.7943 - loss: 0.6225
Test Loss: 0.49921363592147827
Test Accuracy: 0.831885039806366

Model 2
![download (3)](https://github.com/user-attachments/assets/36fad340-00f3-4253-bb87-59b8928d3c54)


878/878 ━━━━━━━━━━━━━━━━━━━━ 559s 636ms/step - accuracy: 0.9106 - loss: 0.2504
Train accuracy: 90.59%

Results:
The first model achieved a test accuracy of approximately 83.19%.
The second model, which included early stopping, achieved a higher train accuracy of approximately 90.59%.
Conclusion:
The CNN models demonstrated good performance in classifying images into the specified categories. The use of data augmentation, early stopping, and learning rate reduction contributed to the models' effectiveness. The confusion matrix provided insights into the specific areas where the models performed well and where there was room for improvement. Future work could involve further tuning of hyperparameters, experimenting with different architectures, and increasing the dataset size to enhance model performance.
