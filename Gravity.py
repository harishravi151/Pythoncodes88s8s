r=1.5e11
import numpy as np
G=6.67e-11
M=2e30
T=2*np.pi*r**1.5/(G*M)**.5
Tdays=T/24/3600
print(Tdays)
