import numpy as np
import pandas as pd
import plotly.express as px
import msicpe.ssl as msi

def porte(t, T):
    y=(abs(t)<T/2)
    return np.float16(y)