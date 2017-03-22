# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 16:37:47 2017

@author: Libby
"""

import pandas as pd
import numpy as np

ac79_dat = pd.read_csv("/Users/Libby/Downloads/AC79.pbo.nam08.csv", header = 11, parse_dates = [0], infer_datetime_format=True)


from matplotlib import pyplot as plt

#matplotlib.style.use('ggplot')
#ts.plot(ac79_dat)

#figure1 = plt.figure(figsize(6, 12)) 

f1 = plt.subplot(3, 1, 1)
f1.plot("Date", " North (mm)")
f2 = plt.subplot(3, 1, 2)
f2.plot("Date", " East (mm)")
f3 = plt.subplot(3, 1, 3)
f3.plot("Date", " Vertical (mm)")

#ac79_dat.plot()

