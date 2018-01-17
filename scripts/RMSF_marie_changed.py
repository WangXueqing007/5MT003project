#!/usr/bin/python

#calculating average hydrophobicity score

#Imports libraries
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
#fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(18, 6))
count_num=0

#def plotting_rmsf (file_xvg):
load = np.loadtxt('xueqing1221-3_rmsf_m205p_apo.xvg', skiprows=17)
rmsf = np.asarray([row[1] for row in load])
residue = np.asarray([row[0] for row in load])

A_rmsf = rmsf[0:311]
A_residue = residue[0:311]
B_rmsf = rmsf[311:622]
B_residue = residue[311:622]
C_rmsf = rmsf[622:933]
C_residue = residue[622:933]
D_rmsf = rmsf[933:1244]
D_residue = residue[933:1244]
E_rmsf = rmsf[1244:1555]
E_residue = residue[1244:1555]

protCA_ave_rmsf = []
protCA_stdev_rmsf = []
for i in range (0,311):
    row = A_rmsf[i]
    row = np.append(row, B_rmsf[i])
    row = np.append(row, C_rmsf[i])
    row = np.append(row, D_rmsf[i])
    row = np.append(row, E_rmsf[i])
    average_rmsf = np.mean (row)
    stdev_rmsf = np.std(row)
    protCA_ave_rmsf = np.append(protCA_ave_rmsf,average_rmsf)
    protCA_stdev_rmsf = np.append(protCA_stdev_rmsf,stdev_rmsf)

plus_stdev_rmsf = protCA_ave_rmsf + protCA_stdev_rmsf
minus_stdev_rmsf = protCA_ave_rmsf - protCA_stdev_rmsf
#print protCA_ave_rmsf


load = np.loadtxt('xueqing1221-4_rmsf_m205p_holo.xvg', skiprows=17)
rmsf = np.asarray([row[1] for row in load])
residue = np.asarray([row[0] for row in load])

A_rmsf2 = rmsf[0:311]
A_residue2 = residue[0:311]
B_rmsf2 = rmsf[311:622]
B_residue2 = residue[311:622]
C_rmsf2 = rmsf[622:933]
C_residue2 = residue[622:933]
D_rmsf2 = rmsf[933:1244]
D_residue2 = residue[933:1244]
E_rmsf2 = rmsf[1244:1555]
E_residue2 = residue[1244:1555]


protCA_ave_rmsf2 = []
protCA_stdev_rmsf2 = []
for i in range (0,311):
    row = A_rmsf2[i]
    row = np.append(row, B_rmsf2[i])
    row = np.append(row, C_rmsf2[i])
    row = np.append(row, D_rmsf2[i])
    row = np.append(row, E_rmsf2[i])
    average_rmsf2 = np.mean (row)
    stdev_rmsf2 = np.std(row)
    protCA_ave_rmsf2 = np.append(protCA_ave_rmsf2,average_rmsf2)
    protCA_stdev_rmsf2 = np.append(protCA_stdev_rmsf2,stdev_rmsf2)

plus_stdev_rmsf2 = protCA_ave_rmsf2 + protCA_stdev_rmsf2
minus_stdev_rmsf2 = protCA_ave_rmsf2 - protCA_stdev_rmsf2


M1_x1 = [197, 197]
M1_x2 = [205, 205]
M_y_holo = [0, 0.3]
M_y_apo = [0,3.5]
M3_x1 = [254, 254]
M3_x2 = [262, 262]

fig, ax = plt.subplots()
#fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(18, 6))

#ax.plot(A_M1_residue, A_M1_rmsf, color='k')
#ax.plot(A_M3_residue, A_M3_rmsf, color='k')
ax.fill_between(A_residue, plus_stdev_rmsf, minus_stdev_rmsf, facecolor='#000000', alpha=0.2)
ax.plot(A_residue, protCA_ave_rmsf, label='apo', color='#000000')
ax.fill_between(A_residue2, plus_stdev_rmsf2, minus_stdev_rmsf2, facecolor='#1f536a', alpha=0.2)
ax.plot(A_residue2, protCA_ave_rmsf2, label='holo', color='#4162c1')
#ax.plot(A_residue, A_rmsf, 'g')
#ax.plot(B_residue, B_rmsf, 'b')
#ax.plot(C_residue, C_rmsf, 'm')
#ax.plot(D_residue, D_rmsf, 'y')
#ax.plot(E_residue, E_rmsf, 'r')
ax.plot(M1_x1, M_y_apo,'k--')
ax.plot(M1_x2, M_y_apo,'k--')
ax.plot(M3_x1, M_y_apo,'k--')
ax.plot(M3_x2, M_y_apo,'k--')

#t1=[50,120,150,200]
#t2=[0,0.1,0.2,0.3]
#ax.plot(t1,t2,'k--')
#ax.plot((6,0.1),(200,0.3),'k--')

ax.set_xlabel('Residue')
ax.set_ylabel('RMSF (nm)')
ax.set_xlim([190,315])
ax.set_ylim([0,0.3])
ax.set_title('M205P C-alpha RMSF')
plt.legend(loc='upper right')

plt.show()
fig.savefig("rmsf_average_m205p_Ca_0113_1.png")
