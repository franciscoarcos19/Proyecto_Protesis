from scipy.signal import lfilter, resample, firwin, hilbert
import numpy as np

##### funcion para calcular envolvente
def get_env(s):
     s_h = hilbert(s)   
     s_en =  np.log10(np.abs(s_h))         
     windowSize = 60;  #30 ms aprox using fs=1khz
     b = (1/windowSize)*np.ones(windowSize);
     a = 1;
     s_en = lfilter(b, a, s_en);
     s_en[0:windowSize+1] =s_en[windowSize+1]
     s_en=(s_en-s_en.min())/np.abs(s_en).max()
     return s_en
