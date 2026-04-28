import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.font_manager as font_manager
font_path = '/Library/Fonts/Arial Unicode.ttf'
font_prop = font_manager.FontProperties(fname = font_path)
matplotlib.rcParams['font.family'] = font_prop.get_name()

def true_function():
    x = np.linspace(-1, 1, 100) 
    y = np.sin(np.pi * x * 0.8) * 10
    return x,y

x, y = true_function()

plt.plot(x, y, label="y = sin(pi * x * 0.8) * 10")
plt.legend()

plt.savefig("ex1.1.png")
plt.show()