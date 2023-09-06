# Implementation of numpy function
import numpy as np

scores = np.nan
if np.any(np.isnan(scores)):
  crash_indicator = np.float('nan')
  print(crash_indicator)
