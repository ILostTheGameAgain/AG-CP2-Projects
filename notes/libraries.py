#Alec George libraries notes

#start with pip install library name

#always import at top, they can be accessed by any page if they are imported in main.py
import matplotlib.pyplot as plt
import numpy as np
from faker import Faker

#x = np.linspace(-10,10)
#y = x

#fig, ax = plt.subplots()
#ax.plot(x, y)
#plt.show()


fake = Faker()

print(fake.name())
