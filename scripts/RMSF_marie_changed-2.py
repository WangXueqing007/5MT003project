#!/usr/bin/python

#calculating average hydrophobicity score

#Imports libraries
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

load = np.loadtxt('rmsf_m205p_holo.xvg', skiprows=17)
rmsf = np.asarray([row[1] for row in load])
residue = np.asarray([row[0] for row in load])

print residue[0]
print residue[309]
print residue[310]
print residue[311]

A_rmsf = rmsf[0:311]
A_residue = residue[0:311]
end = A_residue.shape[0]
print A_residue[0]
print A_residue[(end - 1)]
print A_residue[253]
print A_rmsf[253]

B_rmsf = rmsf[311:622]
B_residue = residue[311:622]
end = B_residue.shape[0]
print B_residue[0]
print B_residue[(end - 1)]

C_rmsf = rmsf[622:933]
C_residue = residue[622:933]
end = C_residue.shape[0]
print C_residue[0]
print C_residue[(end - 1)]

D_rmsf = rmsf[933:1244]
D_residue = residue[933:1244]
end = D_residue.shape[0]
print D_residue[0]
print D_residue[(end - 1)]

E_rmsf = rmsf[1244:1555]
E_residue = residue[1244:1555]
end = E_residue.shape[0]
print E_residue[0]
print E_residue[(end - 1)]

A_M1_rmsf = A_rmsf[192:200]
A_M1_residue = A_rmsf[192:200]
A_M3_rmsf = A_rmsf[249:253]
A_M3_residue = A_rmsf[249:253]

M1_x1 = [197, 197]
M1_x2 = [205, 205]
M_y = [0, 0.3]
M3_x1 = [254, 254]
M3_x2 = [262, 262]

fig, ax = plt.subplots()

#ax.plot(A_M1_residue, A_M1_rmsf, color='k')
#ax.plot(A_M3_residue, A_M3_rmsf, color='k')
ax.plot(A_residue, A_rmsf, 'g')
ax.plot(B_residue, B_rmsf, 'b')
ax.plot(C_residue, C_rmsf, 'm')
ax.plot(D_residue, D_rmsf, 'y')
ax.plot(E_residue, E_rmsf, 'r')
ax.plot(M1_x1, M_y,'k--')
ax.plot(M1_x2, M_y,'k--')
ax.plot(M3_x1, M_y,'k--')
ax.plot(M3_x2, M_y,'k--')

#t1=[50,120,150,200]
#t2=[0,0.1,0.2,0.3]
#ax.plot(t1,t2,'k--')
#ax.plot((6,0.1),(200,0.3),'k--')

ax.set_xlabel('Residue')
ax.set_ylabel('RMSF (nm)')
ax.set_xlim([5,315])
ax.set_ylim([0,0.3])
ax.set_title('M205P C-alpha RMSF without PFL')
ax.legend#(loc='upper left')

plt.show()
#fig.savefig("rmsf_M1-5_m205p_Ca_holo1.png")
