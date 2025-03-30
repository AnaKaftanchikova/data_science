from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score

silhouette_scores = []
davies_bouldin_scores = []
inertia_scores = []
calinski_harabasz_scores = []


for n_clusters in range(2,21):
  kmeans = KMeans(n_clusters=n_clusters, random_state=42)
  kmeans_labels = kmeans.fit_predict(data)

  kmeans_silhouette = silhouette_score(data, kmeans_labels)
  kmeans_davies = davies_bouldin_score(data, kmeans_labels)
  kmeans_inertia = kmeans.inertia_
  kmeans_calinski = calinski_harabasz_score(data, kmeans_labels)

  silhouette_scores.append(kmeans_silhouette)
  davies_bouldin_scores.append(kmeans_davies)
  inertia_scores.append(kmeans_inertia)
  calinski_harabasz_scores.append(kmeans_calinski)

  print(f'Number of clusters: {n_clusters}, Silhouette Score: {kmeans_silhouette:.2f}, Davies-Bouldin Score: {kmeans_davies:.2f}, Inertia: {kmeans_inertia:.2f}, Calinski-Harabasz Score: {kmeans_calinski:.2f}')

  plt.figure(figsize=(10,8))
  plt.scatter(data.iloc[:, -1], data.iloc[:, 3], c=kmeans_labels, s = 50, cmap='Set2')

  centers = kmeans.cluster_centers_
  plt.scatter(centers[:, -1], centers[:, 3], c='red', s=200, alpha=0.75, marker='x')

  plt.title(f'K-Means Clustering (n_clusters = {n_clusters})')
  plt.xlabel('IMT')
  plt.ylabel('Weight')
  plt.show()


plt.figure(figsize=(10,8))

plt.subplot(2,2,1)
plt.plot(range(2,21), silhouette_scores, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Silhouette Score')
plt.title('Silhouette Score for Different Numbers of Clusters')

plt.subplot(2,2,2)
plt.plot(range(2,21), davies_bouldin_scores, marker='o')
plt.xlabel('Number of Clusters')
plt.ylabel('Davies-Bouldin Score')
plt.title('Davies-Bouldin Score for Different Numbers of Clusters')

plt.subplot(2,2,3)
plt.plot(range(2,21), inertia_scores, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.title('Inertia for Different Numbers of Clusters')

plt.subplot(2, 2, 4)
plt.plot(range(2, 21), calinski_harabasz_scores, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Calinski-Harabasz Score')
plt.title('Calinski-Harabasz Score for Different Numbers of Clusters')

plt.tight_layout()
plt.show()