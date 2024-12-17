import numpy as np
import pandas as pd
import plotly.express as px
import msicpe.ssl as msi
import soundfile as sf
import scipy.io as io
import scipy.signal as sig

rdic = io.loadmat('Modulation/signal.mat') 
signal = rdic['signal'].squeeze() 

Fs = 96000
Ts = 1/Fs

#Création du vecteur temporel t
t=[]
for i in range(len(signal)):
    t.append(0+i*Ts)
"""
#Tracé du signal temporel
df = pd.DataFrame({'temps':t, 'signal':signal})
fig = px.line(df, x='temps', y='signal')
fig.update_layout(xaxis_title='temps', yaxis_title='signal',
title = 'Tracé du signal',
template='plotly_white', width=500, height=300)
fig.show()
"""
#Calcul et tracé de la transformé de Fourrier du signal
Trans, Nu = msi.TransFourier(signal, t)
"""
df = pd.DataFrame({'fréquence':Nu, 'transformée':np.real(Trans)})
fig = px.line(df, x='fréquence', y='transformée')
fig.update_layout(xaxis_title='fréquence', yaxis_title='transfomée',
title = 'Tracé de la transformée de Fourier du signal',
template='plotly_white', width=500, height=300)
fig.show()
"""
#Filtrage du signal et tracé du signal temporel filtré
sig_filtre= msi.PasseBas(signal, 96000, 3000)
"""
df = pd.DataFrame({'temps':t, 'signal':sig_filtre})
fig = px.line(df, x='temps', y='signal')
fig.update_layout(xaxis_title='temps', yaxis_title='signal',
title = 'Tracé du signal filtré',
template='plotly_white', width=500, height=300)
fig.show()
"""
#Calcul et tracé de la transofrmé de Fourrier du signal filtré
Trans_f, Nu = msi.TransFourier(sig_filtre, t)
"""
df = pd.DataFrame({'fréquence':Nu, 'transformée':np.real(Trans_f)})
fig = px.line(df, x='fréquence', y='transformée')
fig.update_layout(xaxis_title='fréquence', yaxis_title='transfomée',
title = 'Tracé de la transformée de Fourier du signal filtré',
template='plotly_white', width=500, height=300)
fig.show()
"""
#Modulation du signal et tracé du signal modulé
sig_mod = []
for i in range(len(t)):
    sig_mod.append(sig_filtre[i]*np.cos(2 * np.pi * 21000 * t[i])-np.imag(sig.hilbert(sig_filtre)[i])*np.sin(2 * np.pi * 21000 * t[i]))

df = pd.DataFrame({'temps':t, 'signal':np.real(sig_mod)})
fig = px.line(df, x='temps', y='signal')
fig.update_layout(xaxis_title='temps', yaxis_title='signal',
title = 'Tracé du signal modulé',
template='plotly_white', width=500, height=300)
fig.show()

#Calcul et tracé de la transformé de Fourrier du signal modulé
Trans_mod, Nu = msi.TransFourier(sig_mod, t)

df = pd.DataFrame({'fréquence':Nu, 'transformée':np.real(Trans_mod)})
fig = px.line(df, x='fréquence', y='transformée')
fig.update_layout(xaxis_title='fréquence', yaxis_title='transfomée',
title = 'Tracé de la transformée de Fourier du signal modulé',
template='plotly_white', width=500, height=300)
fig.show()

#Enregistrement du signal modulé (au format .mat)
mdic = {"sig_mod_fp_21kHz": sig_mod}

io.savemat('groupe_c1_phrase_24.mat', mdict=mdic)