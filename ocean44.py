#import numpy library as np
import numpy as np
#import matplotlib.pyplot library as plt
import matplotlib.pyplot as plt
#loading the data from the file
data=np.loadtxt('data.csv',skiprows=1)
#taking height data
H=data[::,1]
#taking weight data
W=data[::,2]
plt.plot(H,W,'0')
#fitting the data into line
coeffs=np.polyfit(H,W,1)
#equating the polynomia;l with the coeffecients
Y=np.polyval(coeffs,H)
#plotting the line
plt.plot(H,Y)
#showing the line
plt.show()
