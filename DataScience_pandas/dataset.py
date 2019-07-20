import pandas
from pandas.plotting import scatter_matrix  # For scatter plot matrix

import matplotlib.pyplot as plt  # For plotting the graphs

# LOAD DATA SET

# Path to data file
file_name = 'iris.data'  # It's a .csv
# Can also be a url
# url = \
#     'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# Field (column) names
names = [
    'sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class'
]
# Loading the csv file
dataset = pandas.read_csv(file_name, names=names)

# Shape of array
print('Shape is:', dataset.shape)

print('=' * 30)

# Values
values = dataset.values  # Array
print(values[:10])

print('=' * 30)

# Retrieves the first @n records
print(dataset.head(20))

print('=' * 30)

# Statistical descriptions - includes count, mean, min, max...
print(dataset.describe())

print('=' * 30)

# Distribution - absolute count by @column_name
print(dataset.groupby('class').size())

# UNIVARIATE PLOTS
# Box and whisker plots
dataset.plot(
    kind='box', subplots=True, layout=(2, 2), sharex=False, sharey=False
)
plt.show()

# Histograms
dataset.hist()
plt.show()

# MULTIVARIATE PLOTS
# Scatter plot matrix
scatter_matrix(dataset)
plt.show()
