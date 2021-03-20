import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('Kim', 'Natalia', 'Jagruti', 'Srini', 'Robert')
y_pos = np.arange(len(objects))
performance = [22,23,15,10,12]

plt.bar(y_pos, performance, align='center', alpha=0.5, color=['red', 'black', 'purple', 'green', 'blue'])
plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.title('Number of Years With the Company')

plt.show()






