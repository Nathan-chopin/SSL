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

