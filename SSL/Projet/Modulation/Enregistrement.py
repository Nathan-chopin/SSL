import msicpe.ssl as msi
import soundfile as sf
import scipy.io as io

#Permet d'enregistrer le son (au format .wave et .mat)

nom, sig, t = msi.RecordModulation(96000)

mdic = {"signal": sig}
io.savemat('signal.mat', mdict=mdic)

