from flask import Flask, request, jsonify
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load the dataset
data = pd.read_csv('/home/shri123/learning/Gadjoy/POC/meteorite_landings_clean-top.csv')

# Define API endpoints
@app.route('/kmeans', methods=['POST'])
def perform_kmeans():
    # Extracting required parameters from the request
    num_clusters = request.json.get('num_clusters')
    
    # Perform K-means clustering
    X = data[['reclong', 'reclat', 'mass (g)']]  # Features for clustering
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(X)
    labels = kmeans.labels_.tolist()
    
    # Return cluster labels
    return jsonify({'clusters': labels})

@app.route('/dbscan', methods=['POST'])
def perform_dbscan():
    # Extracting required parameters from the request
    eps = request.json.get('eps')
    min_samples = request.json.get('min_samples')
    
    # Perform DBSCAN clustering
    X = data[['reclong', 'reclat', 'mass (g)']]  # Features for clustering
    X = StandardScaler().fit_transform(X)  # Standardize features
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    labels = dbscan.fit_predict(X).tolist()
    
    # Return cluster labels
    return jsonify({'clusters': labels})

if __name__ == '__main__':
    app.run(debug=True)
