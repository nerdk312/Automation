import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Example NumPy array
data = np.random.randn(1000)

# Create a histogram with Seaborn
sns.histplot(data, bins=30, kde=True)  # kde=True adds a Kernel Density Estimate line




'''
north_data_flattened = north_data.data.reshape((-1,north_data.shape[-1]))
south_data_flattened = south_data.data.reshape((-1,south_data.shape[-1]))
west_data_flattened = west_data.data.reshape((-1,west_data.shape[-1]))
east_data_flattened = east_data.data.reshape((-1,east_data.shape[-1]))

north_data_full_flattened = north_data.data.reshape((-1))
south_data_full_flattened = south_data.data.reshape((-1))
west_data_full_flattened = west_data.data.reshape((-1))
east_data_full_flattened = east_data.data.reshape((-1))

sns.histplot(data=north_data_full_flattened, bins=30,kde=True)
plt.title('North')
plt.show()
sns.histplot(data=south_data_full_flattened, bins=30,kde=True)
plt.title('South')
plt.show()
sns.histplot(data=west_data_full_flattened, bins=30,kde=True)
plt.title('West')
plt.show()
sns.histplot(data=east_data_full_flattened, bins=30,kde=True)
plt.title('East')
plt.show()
'''