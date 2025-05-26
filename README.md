K-Means Image Segmentation

Image Compression via Unsupervised Clustering in Python

This project demonstrates how K-Means clustering can be applied to segment and compress an image by reducing the number of distinct colors. A 640x960 image is processed and its color palette is reduced to just 10 clusters, significantly reducing complexity while preserving visual structure.


---

Features

Image segmentation using K-Means clustering

Reduces image colors to a specified number of clusters (default: 10)

Simple and customizable implementation in Python

Visualization of original vs. segmented images



---

How It Works

1. Load the image using matplotlib.


2. Reshape the image array to a 2D array of RGB values.


3. Apply K-Means clustering from sklearn.cluster.


4. Replace each pixel with the color of its cluster center.


5. Reshape and visualize the segmented image.




---

Requirements

Python 3.7+

scikit-learn

matplotlib


Install dependencies using:

pip install -r requirements.txt


---

Usage

python segment.py

You can modify parameters in segment.py such as:

k = 10  # number of color clusters
image_path = 'path/to/image.jpg'


---

File Structure

kmeans-image-segmentation/
│
├── segment.py                 # Main script
├── requirements.txt           # Dependencies
├── samples/                   # Folder for input/output image examples
│   ├── original_image.png
│   └── segmented_image.png
└── README.md


---

TODO

Add support for batch image processing

Enable dynamic cluster selection via CLI

Integrate PSNR/SSIM for quality evaluation



---

License

This project is licensed under the MIT License.


---

Author

Yugank Das
https://github.com/yugankdas


---
