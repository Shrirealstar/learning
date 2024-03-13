import React, { useState } from 'react';
import axios from 'axios';
import Plotly from 'plotly.js';
import createPlotlyComponent from 'react-plotly.js/factory';

const Plot = createPlotlyComponent(Plotly);

function App() {
  const [kMeansClusters, setKMeansClusters] = useState([]);
  const [dbscanClusters, setDBSCANClusters] = useState([]);

  // Function to handle K-means clustering
  const handleKMeans = async () => {
    try {
      const response = await axios.post('/kmeans', { num_clusters: 3 }); // Change 3 to desired number of clusters
      const clusters = response.data.clusters;
      setKMeansClusters(clusters);
    } catch (error) {
      console.error('Error performing K-means clustering:', error);
    }
  };

  // Function to handle DBSCAN clustering
  const handleDBSCAN = async () => {
    try {
      const response = await axios.post('/dbscan', { eps: 0.5, min_samples: 5 }); // Change parameters as needed
      const clusters = response.data.clusters;
      setDBSCANClusters(clusters);
    } catch (error) {
      console.error('Error performing DBSCAN clustering:', error);
    }
  };

  return (
    <div>
      <h1>Clustering Analysis</h1>
      <button onClick={handleKMeans}>Run K-means Clustering</button>
      <button onClick={handleDBSCAN}>Run DBSCAN Clustering</button>

      {/* Plotly visualization for k-means clusters */}
      {kMeansClusters.length > 0 && (
        <div>
          <h2>K-means Clusters</h2>
          <Plot
            data={[
              {
                type: 'scatter',
                mode: 'markers',
                x: kMeansClusters.map(cluster => cluster.reclong),
                y: kMeansClusters.map(cluster => cluster.reclat),
                marker: { color: kMeansClusters.map(cluster => cluster.cluster) }
              }
            ]}
            layout={{ width: 800, height: 600, title: 'K-means Clustering' }}
          />
        </div>
      )}

      {/* Plotly visualization for DBSCAN clusters */}
      {dbscanClusters.length > 0 && (
        <div>
          <h2>DBSCAN Clusters</h2>
          <Plot
            data={[
              {
                type: 'scatter',
                mode: 'markers',
                x: dbscanClusters.map(cluster => cluster.reclong),
                y: dbscanClusters.map(cluster => cluster.reclat),
                marker: { color: dbscanClusters.map(cluster => cluster.cluster) }
              }
            ]}
            layout={{ width: 800, height: 600, title: 'DBSCAN Clustering' }}
          />
        </div>
      )}
    </div>
  );
}

export default App;
