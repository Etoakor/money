# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


fig = plt.figure(figsize=(10,8))
pd.Series(np.random.normal(loc=1500,scale=200,size=120)).map(lambda x: round(x,2)).hist(bins=30)
plt.savefig('./bonus正太分布1500,200.png',dpi=400)
plt.show()


fig = plt.figure(figsize=(10,8))
pd.Series(np.random.randint(3000,3501,size=120)).hist(bins=30)
plt.savefig('./general_expense均匀分布3000,3500.png',dpi=400)
plt.show()

fig = plt.figure(figsize=(10,8))
pd.Series(np.random.normal(loc=5000,scale=500,size=120)).map(lambda x: round(x,2)).hist(bins=30)
plt.savefig('./shopping正太分布5000,500.png',dpi=400)
plt.show()

fig = plt.figure(figsize=(10,8))
pd.Series(np.random.randint(400,1200,size=120)).hist(bins=30)
plt.savefig('./happy400,1200均匀分布.png',dpi=400)
plt.show()

fig = plt.figure(figsize=(10,8))
pd.Series(np.random.randint(100,500,size=120)).hist(bins=30)
plt.savefig('./study100,500均匀分布.png',dpi=400)
plt.show()

fig = plt.figure(figsize=(10,8))
pd.Series(np.random.normal(loc=500,scale=40,size=120)).map(lambda x: round(x,2)).hist(bins=30)
plt.savefig('./other正太分布500,40.png',dpi=400)
plt.show()