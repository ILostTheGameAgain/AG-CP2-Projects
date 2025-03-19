import pandas as pd

df = pd.read_csv('test_folder/file.csv')

print(df.to_string())


import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# make data
y = [1,2,3,4,5,6]

# plot
fig, ax = plt.subplots()

ax.stairs(y, linewidth=2.5)

ax.set(xlim=(0, 6), xticks=np.arange(1, 6),
       ylim=(0, 20), yticks=np.arange(1, 20))

plt.show()

print(np.arange(0,9))