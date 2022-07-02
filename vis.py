import warnings
warnings.filterwarnings('ignore')

####################
# 读取数据
####################

import scipy.io as scio

data = scio.loadmat('0_55.bin4N.mat')
data = data['data']

print('data.shape =', data.shape)
# print(data[0,:,:])

####################
# 可视化
####################

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

frame = 575
multi = 50

fig = plt.figure()
ax = Axes3D(fig)
img = ax.scatter( data[frame:frame+multi,:,0],
                  data[frame:frame+multi,:,1],
                  data[frame:frame+multi,:,2],
                  c=data[frame:frame+multi,:,3], cmap='autumn_r', alpha=0.5, marker='.' ) # afmhot_r

# 颜色条
plt.colorbar(img, ax=ax)

ax.set_xlabel('X', fontsize=14)
ax.set_ylabel('Y', fontsize=14)
ax.set_zlabel('Z', fontsize=14)

plt.show()
