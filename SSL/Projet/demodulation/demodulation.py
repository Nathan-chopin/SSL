import numpy as np
import pandas as pd
import plotly.express as px
import msicpe.ssl as msi
import scipy.io as io

nu_p = 21000

def porte(t):
    y=(abs(t)<0.5)
    return np.float16(y)


rdic = io.loadmat('signal_multiplex.mat')
signal_multiplex = rdic['melange'].squeeze()

t = np.arange(0, 5, 1 / len(signal_multiplex))

cos = np.cos(2 * np.pi * nu_p * t)
signal_multiplex *= cos

tf_multiplex, nu = msi.TransFourier(signal_multiplex,t)
tf_filtre =tf_multiplex * porte(t/2*nu_p)
signal,t = msi.TransFourierInv(tf_filtre, nu)

# I) Creer sa structure de données
df = pd.DataFrame({'temps':t, 'signal': s, 'frequence' : nu, 'tf_real' : tf.real, 'tf_imag' : tf.imag})

# II) Creer sa figure
fig = px.line(df, x='temps', y='signal')

# III) Creer son layout
fig.update_layout(yaxis_title='Argument 1', xaxis_title='temps(s)',
#xaxis_range=..., yaxis_range=..., # if needed
title = 'Tracé de gamma',
template='plotly_white', width=500, height=300)

# IV) Afficher
fig.show()
