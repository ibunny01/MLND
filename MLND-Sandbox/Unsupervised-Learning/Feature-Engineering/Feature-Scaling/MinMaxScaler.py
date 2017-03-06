from sklearn.preprocessing import MinMaxScaler
import numpy as np

weights = np.array([[140],[175],[115]]).astype(float)
scaler = MinMaxScaler()
scaled_weight = scaler.fit_transform(weights)

print weights
print scaled_weight
