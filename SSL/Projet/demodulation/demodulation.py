import numpy as np
import pandas as pd
import plotly.express as px
import msicpe.ssl as msi
import scipy.io as io
import soundfile as sf

nu_p = 21000

def porte(t):
    y=(abs(t)<0.5)
    return np.float16(y)


rdic = io.loadmat('SSL/Projet/demodulation/sig_mod_fp_21kHz.mat')
signal_multiplex = rdic['sig_mod_fp_21kHz'].squeeze()

t = np.arange(0, 5, 5 * ( 1 / len(signal_multiplex) ))
Fe = 96000 #Hz

cos = np.cos(2 * np.pi * nu_p * t)
signal_multiplex *= cos

tf_multiplex, nu = msi.TransFourier(signal_multiplex,t) #
tf_filtre =tf_multiplex * porte(t/2*nu_p)               # a changer
signal,t = msi.TransFourierInv(tf_filtre, nu)           #

# tracé du signal
df = pd.DataFrame({'temps':t, 'signal': signal})
fig = px.line(df, x='temps', y='signal')
fig.update_layout(yaxis_title='Signal', xaxis_title='temps(s)',
title = 'Tracé du signal',
template='plotly_white', width=500, height=300)

# IV) Afficher
fig.show()

sf.write('signal.wav', np.int16(signal), Fe)
msi.audioread('signal.wav',True)