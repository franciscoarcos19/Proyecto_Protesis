# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 12:16:53 2021

@author: Usuario
"""
import numpy as np

#signal must be a array
def f_aac(signal):
    n = len(signal) - 1
    sum = 0
    for i in range(n):
        a = abs(signal[i+1] - signal[i])
        sum = sum + a
    return sum/n


def f_dasdv(signal):
    n = len(signal) - 1
    sum = 0
    for i in range(n):
        a = (signal[i+1] - signal[i])**2
        sum = sum + a
    return np.sqrt(sum/(n-1))


def f_log(signal):
    n = len(signal)
    return np.exp((np.sum(np.log10(abs(signal))))/n)


def f_mav(signal):
    signal = signal/(np.max(abs(signal)))
    return np.mean(abs(signal))


def f_ssi(signal):
    sum = 0
    n = len(signal)
    for i in range(n):
        a = (signal[i])**2
        sum = sum + a
    return sum


def f_wl(signal):
    n = len(signal) - 1
    sum = 0
    for i in range(n):
        sum = sum + abs(signal[i+1] - signal[i])
    return sum


def f_rms(signal):
    sum = 0
    n = len(signal)
    y = 0
    for i in range(n):
        sum = sum + (signal[i])**2
    y = sum/n    
    return np.sqrt(y)

