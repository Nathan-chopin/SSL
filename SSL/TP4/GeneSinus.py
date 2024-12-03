import numpy as np

def porte(t):
    y=(abs(t)<0.5)
    return np.float16(y)

def GeneSin(A,nu0,phi0,D,Fe,T):
    Te = 1 / Fe
    if T < D:
        return [],[]
    else :
        t = np.arange(0,T,Te)
        s = A * np.sin(2 * np.pi * nu0 * t + phi0) * porte(t - D / 2)
        return t ,s

