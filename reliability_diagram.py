
import numpy as np
import matplotlib.pyplot as plt
from sklearn.calibration import calibration_curve

# Step 1: Generate Synthetic Data
# Create 1000 perfectly calibrated predictions
n_samples = 1000
true_probs = np.linspace(0, 1, n_samples)
pred_probs = true_probs  # Perfectly calibrated predictions
true_labels = np.random.binomial(1, true_probs)  # Generate true labels

# Step 2: Bin the Predictions
# Use sklearn's calibration_curve function to compute the calibration curve
fraction_of_positives, mean_predicted_value = calibration_curve(true_labels, pred_probs, n_bins=10)

# Step 3: Plot the Reliability Diagram
plt.figure(figsize=(8, 6))
plt.plot(mean_predicted_value, fraction_of_positives, "s-", label="Model")
plt.plot([0, 1], [0, 1], "k--", label="Perfectly calibrated")  # Diagonal line

# Customize the plot
plt.xlabel("Confidence")
plt.ylabel("Accuracy")
plt.title("Reliability Diagram")
plt.legend(loc="best")
plt.grid(True)

# Show the plot
plt.show()

