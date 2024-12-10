import numpy as np
import pandas as pd
import plotly.express as px
import msicpe.ssl as msi
import scipy.io as io


def porte(t):
    y=(abs(t)<0.5)
    return np.float16(y)


rdic = io.loadmat('signal_multiplex.mat')
signal_multiplex = rdic['melange'].squeeze()

t = np.arange(0, 5, 1 / len(signal_multiplex))

tf_multiplex = msi.TransFourier(signal_multiplex,t)

