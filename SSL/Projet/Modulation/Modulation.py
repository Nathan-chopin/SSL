import numpy as np
import pandas as pd
import plotly.express as px
import msicpe.ssl as msi
import soundfile as sf
import scipy.io as io

def porte(t,T):
    y=(abs(t)<T/2)
    return np.float16(y)

rdic = io.loadmat('signal_multiplex.mat')
signal_multiplex = rdic['melange'].squeeze()
Fs = 96000
Ts = 1/Fs
t=[]
for i in range(len(f)):
    t.append(0+i*Ts)

df = pd.DataFrame({'temps':t, 'signal':f})
fig = px.line(df, x='temps', y='signal')
fig.update_layout(xaxis_title='temps', yaxis_title='signal',
title = 'Tracé du signal',
template='plotly_white', width=500, height=300)
fig.show()