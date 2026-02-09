import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load the dataset

file_path = r"D:\Software\Retail_Data\Retail_Transactions_Dataset.csv"
df = pd.read_csv(file_path)

# Pre-processing

# Select relevant features for ML
features = df[['Total_Items', 'Total_Cost']]

# Remove missing values (if any)
features = features.dropna()

# Standardize the data
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Evaluation - Elbow Method

wcss = []

for i in range(1, 8):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(scaled_features)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(range(1, 8), wcss, marker='o')
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.title("Elbow Method for Optimal Number of Clusters")
plt.show()

# Training - KMeans Clustering

kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(scaled_features)

# Add cluster labels to data
features['Cluster'] = clusters

# Visualisation

plt.figure(figsize=(8, 6))
plt.scatter(
    features['Total_Items'],
    features['Total_Cost'],
    c=features['Cluster']
)
plt.xlabel("Total Items Purchased")
plt.ylabel("Total Cost")
plt.title("Customer Segmentation using K-Means Clustering")
plt.show()
