# UNQ_C1
# GRADED FUNCTION: find_closest_centroids

def find_closest_centroids(X, centroids):
    """
    Computes the centroid memberships for every example
    """
    K = centroids.shape[0]
    idx = np.zeros(X.shape[0], dtype=int)

    for i in range(X.shape[0]):
        distances = []
        for j in range(K):
            dist = np.linalg.norm(X[i] - centroids[j])
            distances.append(dist)
        idx[i] = np.argmin(distances)

    return idx
