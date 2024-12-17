import msicpe.ssl as msi
import soundfile as sf
import scipy.io as io



nom, sig, t = msi.RecordModulation(96000)

mdic = {"signal": sig}
io.savemat('signal.mat', mdict=mdic)

