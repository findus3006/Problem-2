import numpy as np
import matplotlib as plt

#Problem a: Phasefactor matrix

def P(ni,Di,k0):
    Phasetransfer = np.zeros((2,2),dtype = 'complex');
    Phasetransfer[0,0] = np.exp(1j*k0*Di*ni)
    Phasetransfer[1,1] = np.exp(-1j*k0*Di*ni)
    return Phasetransfer

print(P(1,1,1))

