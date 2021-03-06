#! /usr/bin/env python3
import numpy as np

""" common maths functions that are not provided by default"""

def gaussian(x, mu, sig):
	""" return a Gaussian distribution over x"""
	return 1/(sig * np.sqrt(2*np.pi)) * np.exp((-1/2) * ((x - mu)/sig)**2)


def pink_power(f, alpha=1, scale=1):
	""" power spectral density for pink noise """
	return scale / f**alpha
