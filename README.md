AI Tools and Frameworks - Laboratory Assignments

This repository contains laboratory exercises completed for the AI Tools and Frameworks course. 
Each lab demonstrates practical implementation of machine learning or AI-related workflows, focusing on framework usage, data handling, model development, and tool creation. 
The work emphasizes clear methodology, reproducibility, and correctness.

Lab 1: CIFAR-10 Neural Network Classification

File: Lab1.ipynb
1. Objective:
The purpose of this lab was to design and implement a simple feed-forward neural network for image classification using the CIFAR-10 dataset.
CIFAR-10 is a widely used benchmark dataset consisting of 60,000 color images (32×32 resolution), categorized into 10 classes.
The goal was to load the dataset, preprocess it, construct a neural network model, train it, visualize learning curves, and evaluate its predictive performance.

3. Dataset and Preprocessing:
The dataset is accessed directly from TensorFlow Keras, which provides built-in utilities for downloading and loading CIFAR-10.
The training and testing partitions are loaded automatically, eliminating the need for external files.
All images are normalized by scaling pixel values from the range [0, 255] to [0, 1].
Labels are flattened to remove unnecessary dimensions and enable compatibility with dense layers.
This step ensures numerical stability during training and allows the model to converge more effectively.

5. Model Architecture:
The model is implemented using Keras Sequential API. The structure contains:
A Flatten layer to convert the 32×32×3 tensor into a one-dimensional vector.
A fully connected (Dense) hidden layer with 128 units and ReLU activation.
A final Dense layer with 10 units and a softmax activation for multiclass classification.
Although this is not a convolutional network, it serves as an introductory demonstration of classification using dense neural networks. 
Expected accuracy for this architecture is around 40–45%.

4. Training Procedure:
The model is compiled using:-
Optimizer: Adam
Loss function: sparse categorical crossentropy
Metrics: accuracy
The network is trained for 10 epochs with validation on the test set.
This enables monitoring of overfitting and generalization behavior.
Training and validation accuracy/loss curves are visualized to assess model behavior and convergence patterns.

6. Evaluation:
Final evaluation is done using the test partition.
Sample predictions are generated and compared with ground truth labels.
The observed performance aligns with expectations for a dense-only model on CIFAR-10, confirming correctness of the implementation and preprocessing pipeline.

7. Tools Used: Python, TensorFlow/Keras, NumPy, Matplotlib, Jupyter Notebook


Lab 2: Simpsons Image Labeling Tool (Tkinter Application)

Files:
Lab2_labeler.py, Lab2_labels.csv, Lab2_images.zip

1. Objective:
The aim of this lab was to create an interactive tool for annotating an image dataset.
Instead of manually labeling images in a spreadsheet, the task was to build a custom Python application capable of displaying images sequentially and recording annotations provided by the user.
This lab emphasizes building a simple GUI, handling image rendering, and automating dataset labeling.

3. System Design:
The tool is developed using Tkinter, Python’s standard GUI library.
It programmatically loads image files from a designated directory, displays them to the user, and collects label information through interface components.
The GUI contains: A dynamically updated image display panel.
Two sets of radio-button controls:
Character identification (Homer, Marge, Bart, Lisa, Maggie, Abe)
Environment type (indoor or outdoor)
A "Save & Next" button, which records the chosen labels and loads the next image.
The program continues iterating through all files and terminates once the dataset is fully labeled.

3. Image Processing:
Images are loaded using the Pillow (PIL) library.
Each image is resized to ensure consistent display dimensions in the GUI, independent of original resolution.
The use of PIL allows efficient handling of JPEG and PNG formats and ensures compatibility across systems.

5. Data Recording:
For each labeled image, a row is appended to the CSV file Lab2_labels.csv.
Each row follows the structure: filename, character_label, environment_label
This creates a machine-readable dataset that can be used for future machine learning tasks, such as training a classifier.
The application handles indexing and ensures that each image is labeled exactly once.

5. Dataset Packaging:
The original image dataset provided by the instructor contains a large number of individual files.
Uploading hundreds of loose images to GitHub is not practical, so the dataset is included in this repository as a compressed file: Lab2_images.zip
Users can extract the contents and run the labeling tool locally.

7. Tools Used:
Python, Tkinter GUI Framework, Pillow (PIL) for image handling.

Execution Instructions:

Running Lab 1:
Open Lab1.ipynb in Jupyter Notebook or Google Colab.
Execute the notebook cells in order.
CIFAR-10 will be automatically downloaded and processed.
Model results and visualizations will appear in the notebook.

Running Lab 2:
Extract Lab2_images.zip into a folder named images.
Ensure Lab2_labeler.py and Lab2_labels.csv are in the same directory.
Run the program using: python Lab2_labeler.py
Label the images using the graphical interface.
The output CSV file will update automatically.
