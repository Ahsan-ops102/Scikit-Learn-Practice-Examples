from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

real_scores = np.array([90,60,80,100])
predicted_scores = np.array([85,70,70,95])

mae = mean_absolute_error(real_scores, predicted_scores)
mse = mean_squared_error(real_scores, predicted_scores)
rmse = np.sqrt(mse)

print(f"Mean Absolute Error (MAE): {mae}")
print(f"Mean Squared Error (MSE): {mse}")
print(f"Root Mean Squared Error (RMSE): {rmse}")