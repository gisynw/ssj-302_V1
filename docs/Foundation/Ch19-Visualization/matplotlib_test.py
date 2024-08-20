import matplotlib.pyplot as plt
import numpy as np

x_data = ['2011','2012','2013','2014','2015','2016','2017']
y_data = [58000,60200,63000,71000,84000,90500,107000]
y_data2 = [52000,54200,51500,58300,56800,59500,62700]

bar_width = 0.4
plt.barh(y = range(len(x_data)),width = y_data, label = 'Crazy Python', color = 'steelblue',alpha = 0.8, height = bar_width)
plt.barh(y = np.arange(len(x_data)) + bar_width,
        width = y_data2, label = 'Crazy Java', color = 'indianred',alpha = 0.8, height = bar_width)
for x,y in enumerate(y_data):
    plt.text(x + 5000, y-bar_width/2 ,'%s'%x, ha = 'center', va = 'bottom')
for x,y in enumerate(y_data2):
    plt.text(x + 5000, y+bar_width/2, '%s'%x, ha = 'center', va = 'bottom')

plt.yticks(np.arange(len(x_data)) + bar_width/2, x_data)
plt.title('Comparison between Java and Python')
plt.xlabel('Sales')
plt.ylabel('Year')

plt.legend(loc = 'best')
plt.show()