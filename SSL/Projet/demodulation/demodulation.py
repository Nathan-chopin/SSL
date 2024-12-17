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


rdic = io.loadmat('demodulation/groupe_1_Melange-17-Dec-2024.mat')
signal_multiplex = rdic['melange'].squeeze()

t = np.arange(0, 5, 5 * ( 1 / len(signal_multiplex) ))
Fe = 96000 #Hz

tf_multiplex_ini, nu = msi.TransFourier(signal_multiplex,t) # visualisation du signal fréquentiel avant démodulation


cos = np.cos(2 * np.pi * nu_p * t)*150000 
signal_multiplex *= cos # démodulation plus augmentation de l'amplitude car signal inaudible

tf_multiplex_cos, nu = msi.TransFourier(signal_multiplex,t) # visualisation du signal fréquentiel post démodulation


signal_multiplex = msi.PasseBas(signal_multiplex, Fe, 3000) # fc = 3000 car intervalle de 6kHz


tf_multiplex_fin, nu = msi.TransFourier(signal_multiplex,t) # visualisation du signal fréquentiel post filtrage

# tracé du signal
df = pd.DataFrame({'temps':nu, 'signal1': np.abs(tf_multiplex_ini), 'signal2': np.abs(tf_multiplex_cos), 'signal3': np.abs(tf_multiplex_fin)})
fig = px.line(df, x='temps', y='signal1')
fig.update_layout(yaxis_title='tf du Signal (ini)', xaxis_title='fréquence(Hz)',
title = 'Tracé du signal fréquentiel initial',
template='plotly_white', width=500, height=300)

# IV) Afficher
fig.show()

fig = px.line(df, x='temps', y='signal2')
fig.update_layout(yaxis_title='tf du Signal (cos)', xaxis_title='fréquence(Hz)',
title = 'Tracé du signal fréquentiel post-démodulation',
template='plotly_white', width=500, height=300)

# IV) Afficher
fig.show()

fig = px.line(df, x='temps', y='signal3')
fig.update_layout(yaxis_title='tf du Signal (fin)', xaxis_title='fréquence(Hz)',
title = 'Tracé du signal fréquentiel post-filtrage',
template='plotly_white', width=500, height=300)

# IV) Afficher
fig.show()

sf.write('signal.wav', np.int16(signal_multiplex), Fe) #création du signal démodulé
msi.audioread('signal.wav',True)# lecture du signal démodulé