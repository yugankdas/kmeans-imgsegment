import matplotlib.pyplot as plt
from matplotlib import image as mpimg  # Changed import for image reading
from sklearn.cluster import KMeans

# Read the image
image = mpimg.imread('imagea.jpg')
print(image.shape)  # Optional :prints the shape of the image

# Flatten the image for clustering
x = image.reshape(-1, 3)

# Perform KMeans clustering
kmeans = KMeans(n_clusters=10, n_init=10)
kmeans.fit(x)
segmented_img = kmeans.cluster_centers_[kmeans.labels_]
segmented_img = segmented_img.reshape(image.shape)  # Use parentheses, not brackets

# Plot the segmented image
plt.imshow(segmented_img / 255)  # Divide by 255 if image is uint8 (0-255)
plt.axis('off')                  # Optional: hides axis
plt.show()                       # Shows the plot