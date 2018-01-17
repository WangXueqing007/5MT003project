import numpy as np
from matplotlib import pyplot as plt
##=============================================Definitions.============================================================
def CA(filename):
    load_CA = np.loadtxt(filename)
    rmsd_CA = np.asarray([row[1] for row in load_CA])
    frame_CA = np.asarray([row[0] for row in load_CA])
    return frame_CA,rmsd_CA

def CA_3repli(filename_CA,filename_CA1, filename_CA2):
    load_CA = np.loadtxt(filename_CA)
    rmsd_CA = np.asarray([row[1] for row in load_CA])
    frame_CA = np.asarray([row[0] for row in load_CA])
    load_CA1 = np.loadtxt(filename_CA1)
    rmsd_CA1 = np.asarray([row[1] for row in load_CA1])
    frame_CA1 = np.asarray([row[0] for row in load_CA1])
    load_CA2 = np.loadtxt(filename_CA2)
    rmsd_CA2 = np.asarray([row[1] for row in load_CA2])
    frame_CA2 = np.asarray([row[0] for row in load_CA2])
    ave = []
    stdev = []
    for i in range (0,1000):
        row = rmsd_CA[i]
        row = np.append(row, rmsd_CA1[i])
        row = np.append(row, rmsd_CA2[i])
        ave_row = np.mean (row)
        stdev_row = np.std(row)
        ave = np.append(ave,ave_row)
        stdev = np.append(stdev,stdev_row)
    plus_stdev = ave + stdev
    minus_stdev = ave - stdev
    list=[frame_CA[:1000], ave, plus_stdev, minus_stdev]
    #print (list)
    return list

def res205_5subunits(filenameA, filenameB,filenameC,filenameD,filenameE):
    load_res205a = np.loadtxt(filenameA)
    rmsd_res205a = np.asarray([row[1] for row in load_res205a])
    frame_res205a = np.asarray([row[0] for row in load_res205a])
    load_res205b = np.loadtxt(filenameB)
    rmsd_res205b = np.asarray([row[1] for row in load_res205b])
    frame_res205b = np.asarray([row[0] for row in load_res205b])
    load_res205c = np.loadtxt(filenameC)
    rmsd_res205c = np.asarray([row[1] for row in load_res205c])
    frame_res205c = np.asarray([row[0] for row in load_res205c])
    load_res205d = np.loadtxt(filenameD)
    rmsd_res205d = np.asarray([row[1] for row in load_res205d])
    frame_res205d = np.asarray([row[0] for row in load_res205d])
    load_res205e = np.loadtxt(filenameE)
    rmsd_res205e = np.asarray([row[1] for row in load_res205e])
    frame_res205e = np.asarray([row[0] for row in load_res205e])

    res205_ave = []
    res205_stdev = []
    for i in range(0, 200):
        row = rmsd_res205a[i]
        row = np.append(row, rmsd_res205b[i])
        row = np.append(row, rmsd_res205c[i])
        row = np.append(row, rmsd_res205d[i])
        row = np.append(row, rmsd_res205e[i])
        ave_row = np.mean(row)
        stdev_row = np.std(row)
        res205_ave = np.append(res205_ave, ave_row)
        res205_stdev = np.append(res205_stdev, stdev_row)

    plus_stdev_res205 = res205_ave + res205_stdev
    minus_stdev_res205 = res205_ave - res205_stdev
    return frame_res205a, res205_ave, plus_stdev_res205, minus_stdev_res205


def res205_5subunits_with3repli(filenameA1, filenameB1,filenameC1,filenameD1,filenameE1,filenameA2, filenameB2,filenameC2,filenameD2,filenameE2,filenameA3, filenameB3,filenameC3,filenameD3,filenameE3):
    load_res205a1 = np.loadtxt(filenameA1)
    rmsd_res205a1 = np.asarray([row[1] for row in load_res205a1])
    frame_res205a1 = np.asarray([row[0] for row in load_res205a1])
    load_res205b1 = np.loadtxt(filenameB1)
    rmsd_res205b1 = np.asarray([row[1] for row in load_res205b1])
    load_res205c1 = np.loadtxt(filenameC1)
    rmsd_res205c1 = np.asarray([row[1] for row in load_res205c1])
    load_res205d1 = np.loadtxt(filenameD1)
    rmsd_res205d1 = np.asarray([row[1] for row in load_res205d1])
    load_res205e1 = np.loadtxt(filenameE1)
    rmsd_res205e1 = np.asarray([row[1] for row in load_res205e1])
    load_res205a2 = np.loadtxt(filenameA2, comments='&', skiprows=3)
    rmsd_res205a2 = np.asarray([row[1] for row in load_res205a2])
    load_res205b2 = np.loadtxt(filenameB2, comments='&', skiprows=3)
    rmsd_res205b2 = np.asarray([row[1] for row in load_res205b2])
    load_res205c2 = np.loadtxt(filenameC2, comments='&', skiprows=3)
    rmsd_res205c2 = np.asarray([row[1] for row in load_res205c2])
    load_res205d2 = np.loadtxt(filenameD2, comments='&', skiprows=3)
    rmsd_res205d2 = np.asarray([row[1] for row in load_res205d2])
    load_res205e2 = np.loadtxt(filenameE2, comments='&', skiprows=3)
    rmsd_res205e2 = np.asarray([row[1] for row in load_res205e2])
    load_res205a3 = np.loadtxt(filenameA3, comments='&', skiprows=3)
    rmsd_res205a3 = np.asarray([row[1] for row in load_res205a3])
    load_res205b3 = np.loadtxt(filenameB3, comments='&', skiprows=3)
    rmsd_res205b3 = np.asarray([row[1] for row in load_res205b3])
    load_res205c3 = np.loadtxt(filenameC3, comments='&', skiprows=3)
    rmsd_res205c3 = np.asarray([row[1] for row in load_res205c3])
    load_res205d3 = np.loadtxt(filenameD3, comments='&', skiprows=3)
    rmsd_res205d3 = np.asarray([row[1] for row in load_res205d3])
    load_res205e3 = np.loadtxt(filenameE3, comments='&', skiprows=3)
    rmsd_res205e3 = np.asarray([row[1] for row in load_res205e3])

    res205_ave = []
    res205_stdev = []
    for i in range(0, 1000):
        row = rmsd_res205a1[i]
        row = np.append(row, rmsd_res205b1[i])
        row = np.append(row, rmsd_res205c1[i])
        row = np.append(row, rmsd_res205d1[i])
        row = np.append(row, rmsd_res205e1[i])
        row = np.append(row, rmsd_res205a2[i])
        row = np.append(row, rmsd_res205b2[i])
        row = np.append(row, rmsd_res205c2[i])
        row = np.append(row, rmsd_res205d2[i])
        row = np.append(row, rmsd_res205e2[i])
        row = np.append(row, rmsd_res205a3[i])
        row = np.append(row, rmsd_res205b3[i])
        row = np.append(row, rmsd_res205c3[i])
        row = np.append(row, rmsd_res205d3[i])
        row = np.append(row, rmsd_res205e3[i])
        ave_row = np.mean(row)
        stdev_row = np.std(row)
        res205_ave = np.append(res205_ave, ave_row)
        res205_stdev = np.append(res205_stdev, stdev_row)

    plus_stdev_res205 = res205_ave + res205_stdev
    minus_stdev_res205 = res205_ave - res205_stdev
    return frame_res205a1[0:1000], res205_ave, plus_stdev_res205, minus_stdev_res205

def res205_5subunits_with3repli_2(filenameA1, filenameB1,filenameC1,filenameD1,filenameE1,filenameA2, filenameB2,filenameC2,filenameD2,filenameE2,filenameA3, filenameB3,filenameC3,filenameD3,filenameE3):
    load_res205a1 = np.loadtxt(filenameA1, comments='&', skiprows=3)
    rmsd_res205a1 = np.asarray([row[1] for row in load_res205a1])
    frame_res205a1 = np.asarray([row[0] for row in load_res205a1])
    load_res205b1 = np.loadtxt(filenameB1, comments='&', skiprows=3)
    rmsd_res205b1 = np.asarray([row[1] for row in load_res205b1])
    load_res205c1 = np.loadtxt(filenameC1, comments='&', skiprows=3)
    rmsd_res205c1 = np.asarray([row[1] for row in load_res205c1])
    load_res205d1 = np.loadtxt(filenameD1, comments='&', skiprows=3)
    rmsd_res205d1 = np.asarray([row[1] for row in load_res205d1])
    load_res205e1 = np.loadtxt(filenameE1, comments='&', skiprows=3)
    rmsd_res205e1 = np.asarray([row[1] for row in load_res205e1])
    load_res205a2 = np.loadtxt(filenameA2, comments='&', skiprows=3)
    rmsd_res205a2 = np.asarray([row[1] for row in load_res205a2])
    load_res205b2 = np.loadtxt(filenameB2, comments='&', skiprows=3)
    rmsd_res205b2 = np.asarray([row[1] for row in load_res205b2])
    load_res205c2 = np.loadtxt(filenameC2, comments='&', skiprows=3)
    rmsd_res205c2 = np.asarray([row[1] for row in load_res205c2])
    load_res205d2 = np.loadtxt(filenameD2, comments='&', skiprows=3)
    rmsd_res205d2 = np.asarray([row[1] for row in load_res205d2])
    load_res205e2 = np.loadtxt(filenameE2, comments='&', skiprows=3)
    rmsd_res205e2 = np.asarray([row[1] for row in load_res205e2])
    load_res205a3 = np.loadtxt(filenameA3, comments='&', skiprows=3)
    rmsd_res205a3 = np.asarray([row[1] for row in load_res205a3])
    load_res205b3 = np.loadtxt(filenameB3, comments='&', skiprows=3)
    rmsd_res205b3 = np.asarray([row[1] for row in load_res205b3])
    load_res205c3 = np.loadtxt(filenameC3, comments='&', skiprows=3)
    rmsd_res205c3 = np.asarray([row[1] for row in load_res205c3])
    load_res205d3 = np.loadtxt(filenameD3, comments='&', skiprows=3)
    rmsd_res205d3 = np.asarray([row[1] for row in load_res205d3])
    load_res205e3 = np.loadtxt(filenameE3, comments='&', skiprows=3)
    rmsd_res205e3 = np.asarray([row[1] for row in load_res205e3])

    res205_ave = []
    res205_stdev = []
    for i in range(0, 1000):
        row = rmsd_res205a1[i]
        row = np.append(row, rmsd_res205b1[i])
        row = np.append(row, rmsd_res205c1[i])
        row = np.append(row, rmsd_res205d1[i])
        row = np.append(row, rmsd_res205e1[i])
        row = np.append(row, rmsd_res205a2[i])
        row = np.append(row, rmsd_res205b2[i])
        row = np.append(row, rmsd_res205c2[i])
        row = np.append(row, rmsd_res205d2[i])
        row = np.append(row, rmsd_res205e2[i])
        row = np.append(row, rmsd_res205a3[i])
        row = np.append(row, rmsd_res205b3[i])
        row = np.append(row, rmsd_res205c3[i])
        row = np.append(row, rmsd_res205d3[i])
        row = np.append(row, rmsd_res205e3[i])
        ave_row = np.mean(row)
        stdev_row = np.std(row)
        res205_ave = np.append(res205_ave, ave_row)
        res205_stdev = np.append(res205_stdev, stdev_row)

    plus_stdev_res205 = res205_ave + res205_stdev
    minus_stdev_res205 = res205_ave - res205_stdev
    return frame_res205a1[0:1000], res205_ave, plus_stdev_res205, minus_stdev_res205

def res205_5subunits_with3repli_3(filenameA1, filenameB1,filenameC1,filenameD1,filenameE1,filenameA2, filenameB2,filenameC2,filenameD2,filenameE2,filenameA3, filenameB3,filenameC3,filenameD3,filenameE3):
    load_res205a1 = np.loadtxt(filenameA1)
    rmsd_res205a1 = np.asarray([row[1] for row in load_res205a1])
    frame_res205a1 = np.asarray([row[0] for row in load_res205a1])
    load_res205b1 = np.loadtxt(filenameB1)
    rmsd_res205b1 = np.asarray([row[1] for row in load_res205b1])
    load_res205c1 = np.loadtxt(filenameC1)
    rmsd_res205c1 = np.asarray([row[1] for row in load_res205c1])
    load_res205d1 = np.loadtxt(filenameD1)
    rmsd_res205d1 = np.asarray([row[1] for row in load_res205d1])
    load_res205e1 = np.loadtxt(filenameE1)
    rmsd_res205e1 = np.asarray([row[1] for row in load_res205e1])
    load_res205a2 = np.loadtxt(filenameA2)
    rmsd_res205a2 = np.asarray([row[1] for row in load_res205a2])
    load_res205b2 = np.loadtxt(filenameB2)
    rmsd_res205b2 = np.asarray([row[1] for row in load_res205b2])
    load_res205c2 = np.loadtxt(filenameC2)
    rmsd_res205c2 = np.asarray([row[1] for row in load_res205c2])
    load_res205d2 = np.loadtxt(filenameD2)
    rmsd_res205d2 = np.asarray([row[1] for row in load_res205d2])
    load_res205e2 = np.loadtxt(filenameE2)
    rmsd_res205e2 = np.asarray([row[1] for row in load_res205e2])
    load_res205a3 = np.loadtxt(filenameA3)
    rmsd_res205a3 = np.asarray([row[1] for row in load_res205a3])
    load_res205b3 = np.loadtxt(filenameB3)
    rmsd_res205b3 = np.asarray([row[1] for row in load_res205b3])
    load_res205c3 = np.loadtxt(filenameC3)
    rmsd_res205c3 = np.asarray([row[1] for row in load_res205c3])
    load_res205d3 = np.loadtxt(filenameD3)
    rmsd_res205d3 = np.asarray([row[1] for row in load_res205d3])
    load_res205e3 = np.loadtxt(filenameE3)
    rmsd_res205e3 = np.asarray([row[1] for row in load_res205e3])

    res205_ave = []
    res205_stdev = []
    for i in range(0, 1000):
        row = rmsd_res205a1[i]
        row = np.append(row, rmsd_res205b1[i])
        row = np.append(row, rmsd_res205c1[i])
        row = np.append(row, rmsd_res205d1[i])
        row = np.append(row, rmsd_res205e1[i])
        row = np.append(row, rmsd_res205a2[i])
        row = np.append(row, rmsd_res205b2[i])
        row = np.append(row, rmsd_res205c2[i])
        row = np.append(row, rmsd_res205d2[i])
        row = np.append(row, rmsd_res205e2[i])
        row = np.append(row, rmsd_res205a3[i])
        row = np.append(row, rmsd_res205b3[i])
        row = np.append(row, rmsd_res205c3[i])
        row = np.append(row, rmsd_res205d3[i])
        row = np.append(row, rmsd_res205e3[i])
        ave_row = np.mean(row)
        stdev_row = np.std(row)
        res205_ave = np.append(res205_ave, ave_row)
        res205_stdev = np.append(res205_stdev, stdev_row)

    plus_stdev_res205 = res205_ave + res205_stdev
    minus_stdev_res205 = res205_ave - res205_stdev
    return frame_res205a1[0:1000], res205_ave, plus_stdev_res205, minus_stdev_res205

##=============================================Fit data in.=========================================================
#ax1
M205P_apo_CA=CA('./M205Papo/rmsd_prot_CA_m205p_apo_1219.dat')
M205P_holo_CA=CA('./M205Pholo/rmsd_prot_CA_m205p_holo_1219.dat')
#ax2
M205G_apo_CA=CA('./M205Gapo/RMSD_m205g_apo_prot_and_CA.dat')
M205G_holo_CA=CA('./M205Gholo/RMSD_m205g_holo_prot_and_CA.dat')
#ax3
list_M205W_apo_CA=CA_3repli('./M205WnoPFL/proteinCA.dat','./M205WnoPFL_repli1/proteinCA.dat','./M205WnoPFL_repli2/proteinCA.dat')
list_M205W_holo_CA=CA_3repli('./M205W/proteinCA.dat','./M205W_repli1/proteinCA.dat','./M205W_repli2/proteinCA.dat')
#ax4
list_WT_apo_CA=CA_3repli('./3p50noPFL/proteinCA.dat','./3p50noPFL_repli1/proteinCA.dat','3p50noPFL_repli2/proteinCA.dat')
list_WT_holo_CA=CA_3repli('./3p50/proteinCA.dat','./3p50_repli1/proteinCA.dat','3p50_repli2/proteinCA.dat')
#ax5
M205P_apo_res205=res205_5subunits('./M205Papo/rnsd_resid205_chainA_1220.dat','./M205Papo/rnsd_resid205_chainB_1220.dat','./M205Papo/rnsd_resid205_chainC_1220.dat','./M205Papo/rnsd_resid205_chainD_1220.dat','./M205Papo/rnsd_resid205_chainE_1220.dat')
M205P_holo_res205=res205_5subunits('./M205Pholo/rmsd_resid205_chainA_1220.dat','./M205Pholo/rmsd_resid205_chainC_1220.dat','./M205Pholo/rmsd_resid205_chainE_1220.dat','./M205Pholo/rmsd_resid205_chainG_1220.dat','./M205Pholo/rmsd_resid205_chainI_1220.dat')
#ax6
M205G_apo_res205=res205_5subunits('./M205Gapo/rmsd_resid205_chainA_1220.dat','./M205Gapo/rmsd_resid205_chainB_1220.dat','./M205Gapo/rmsd_resid205_chainC_1220.dat','./M205Gapo/rmsd_resid205_chainD_1220.dat','./M205Gapo/rmsd_resid205_chainE_1220.dat')
M205G_holo_res205=res205_5subunits('./M205Gholo/rmsd_resid205_chainA_1220.dat','./M205Gholo/rmsd_resid205_chainG_1220.dat','./M205Gholo/rmsd_resid205_chainC_1220.dat','./M205Gholo/rmsd_resid205_chainI_1220.dat','./M205Gholo/rmsd_resid205_chainE_1220.dat')
#ax7
M205W_holo_res205=res205_5subunits_with3repli('./M205W/resid205_chainA.dat','./M205W/resid205_chainB.dat','./M205W/resid205_chainC.dat','./M205W/resid205_chainD.dat','./M205W/resid205_chainE.dat','./M205W_repli1/resid205_chainA.agr','./M205W_repli1/resid205_chainB.agr','./M205W_repli1/resid205_chainC.agr','./M205W_repli1/resid205_chainD.agr','./M205W_repli1/resid205_chainE.agr','./M205W_repli2/resid205_chainA.agr','./M205W_repli2/resid205_chainB.agr','./M205W_repli2/resid205_chainC.agr','./M205W_repli2/resid205_chainD.agr','./M205W_repli2/resid205_chainE.agr')
M205W_apo_res205=res205_5subunits_with3repli_2('./M205WnoPFL/resid205_chainA.agr','./M205WnoPFL/resid205_chainB.agr','./M205WnoPFL/resid205_chainC.agr','./M205WnoPFL/resid205_chainD.agr','./M205WnoPFL/resid205_chainE.agr','./M205WnoPFL_repli1/resid205_chainA.agr','./M205WnoPFL_repli1/resid205_chainB.agr','./M205WnoPFL_repli1/resid205_chainC.agr','./M205WnoPFL_repli1/resid205_chainD.agr','./M205WnoPFL_repli1/resid205_chainE.agr','./M205WnoPFL_repli2/resid205_chainA.agr','./M205WnoPFL_repli2/resid205_chainB.agr','./M205WnoPFL_repli2/resid205_chainC.agr','./M205WnoPFL_repli2/resid205_chainD.agr','./M205WnoPFL_repli2/resid205_chainE.agr')
#ax8
WT_apo_res205=res205_5subunits_with3repli_2('./3p50noPFL/resid205_chainA.agr','./3p50noPFL/resid205_chainB.agr','./3p50noPFL/resid205_chainC.agr','./3p50noPFL/resid205_chainD.agr','./3p50noPFL/resid205_chainE.agr','./3p50noPFL_repli1/resid205_chainA.agr','./3p50noPFL_repli1/resid205_chainB.agr','./3p50noPFL_repli1/resid205_chainC.agr','./3p50noPFL_repli1/resid205_chainD.agr','./3p50noPFL_repli1/resid205_chainE.agr','./3p50noPFL_repli2/resid205_chainA.agr','./3p50noPFL_repli2/resid205_chainB.agr','./3p50noPFL_repli2/resid205_chainC.agr','./3p50noPFL_repli2/resid205_chainD.agr','./3p50noPFL_repli2/resid205_chainE.agr')
WT_holo_res205=res205_5subunits_with3repli_2('./3p50/resid205_chainA.agr','./3p50/resid205_chainB.agr','./3p50/resid205_chainC.agr','./3p50/resid205_chainD.agr','./3p50/resid205_chainE.agr','./3p50_repli1/resid205_chainA.agr','./3p50_repli1/resid205_chainB.agr','./3p50_repli1/resid205_chainC.agr','./3p50_repli1/resid205_chainD.agr','./3p50_repli1/resid205_chainE.agr','./3p50_repli2/resid205_chainA.agr','./3p50_repli2/resid205_chainB.agr','./3p50_repli2/resid205_chainC.agr','./3p50_repli2/resid205_chainD.agr','./3p50_repli2/resid205_chainE.agr')
#ax9
M205P_apo_res242=res205_5subunits('./M205Papo/rnsd_resid242_chainA_1221.dat','./M205Papo/rnsd_resid242_chainB_1221.dat','./M205Papo/rnsd_resid242_chainC_1221.dat','./M205Papo/rnsd_resid242_chainD_1221.dat','./M205Papo/rnsd_resid242_chainE_1221.dat')
M205P_holo_res242=res205_5subunits('./M205Pholo/rmsd_resid242_chainA_1221.dat','./M205Pholo/rmsd_resid242_chainG_1221.dat', './M205Pholo/rmsd_resid242_chainC_1221.dat','./M205Pholo/rmsd_resid242_chainI_1221.dat','./M205Pholo/rmsd_resid242_chainE_1221.dat')
#ax10
M205G_apo_res242=res205_5subunits('./M205Gapo/rmsd_resid242_chainA_1221.dat','./M205Gapo/rmsd_resid242_chainB_1221.dat','./M205Gapo/rmsd_resid242_chainC_1221.dat','./M205Gapo/rmsd_resid242_chainD_1221.dat','./M205Gapo/rmsd_resid242_chainE_1221.dat')
M205G_holo_res242=res205_5subunits('./M205Gholo/rmsd_resid242_chainA_1221.dat','./M205Gholo/rmsd_resid242_chainC_1221.dat','./M205Gholo/rmsd_resid242_chainE_1221.dat','./M205Gholo/rmsd_resid242_chainG_1221.dat','./M205Gholo/rmsd_resid242_chainI_1221.dat')
#ax11
M205W_holo_res242=res205_5subunits_with3repli_3('./M205W/resid242_chainA.dat','./M205W/resid242_chainB.dat','./M205W/resid242_chainC.dat','./M205W/resid242_chainD.dat','./M205W/resid242_chainE.dat','./M205W_repli1/resid242_chainA.dat','./M205W_repli1/resid242_chainB.dat','./M205W_repli1/resid242_chainC.dat','./M205W_repli1/resid242_chainD.dat','./M205W_repli1/resid242_chainE.dat','./M205W_repli2/resid242_chainA.dat','./M205W_repli2/resid242_chainB.dat','./M205W_repli2/resid242_chainC.dat','./M205W_repli2/resid242_chainD.dat','./M205W_repli2/resid242_chainE.dat')
M205W_apo_res242=res205_5subunits_with3repli_3('./M205WnoPFL/resid242_chainA.dat','./M205WnoPFL/resid242_chainB.dat','./M205WnoPFL/resid242_chainC.dat','./M205WnoPFL/resid242_chainD.dat','./M205WnoPFL/resid242_chainE.dat','./M205WnoPFL_repli1/resid242_chainA.dat','./M205WnoPFL_repli1/resid242_chainB.dat','./M205WnoPFL_repli1/resid242_chainC.dat','./M205WnoPFL_repli1/resid242_chainD.dat','./M205WnoPFL_repli1/resid242_chainE.dat','./M205WnoPFL_repli2/resid242_chainA.dat','./M205WnoPFL_repli2/resid242_chainB.dat','./M205WnoPFL_repli2/resid242_chainC.dat','./M205WnoPFL_repli2/resid242_chainD.dat','./M205WnoPFL_repli2/resid242_chainE.dat')
#ax12
WT_apo_res242=res205_5subunits_with3repli_3('./3p50noPFL/resid242_chainA.dat','./3p50noPFL/resid242_chainB.dat','./3p50noPFL/resid242_chainC.dat','./3p50noPFL/resid242_chainD.dat','./3p50noPFL/resid242_chainE.dat','./3p50noPFL_repli1/resid242_chainA.dat','./3p50noPFL_repli1/resid242_chainB.dat','./3p50noPFL_repli1/resid242_chainC.dat','./3p50noPFL_repli1/resid242_chainD.dat','./3p50noPFL_repli1/resid242_chainE.dat','./3p50noPFL_repli2/resid242_chainA.dat','./3p50noPFL_repli2/resid242_chainB.dat','./3p50noPFL_repli2/resid242_chainC.dat','./3p50noPFL_repli2/resid242_chainD.dat','./3p50noPFL_repli2/resid242_chainE.dat')
WT_holo_res242=res205_5subunits_with3repli_3('./3p50/resid242_chainA.dat','./3p50/resid242_chainB.dat','./3p50/resid242_chainC.dat','./3p50/resid242_chainD.dat','./3p50/resid242_chainE.dat','./3p50_repli1/resid242_chainA.dat','./3p50_repli1/resid242_chainB.dat','./3p50_repli1/resid242_chainC.dat','./3p50_repli1/resid242_chainD.dat','./3p50_repli1/resid242_chainE.dat','./3p50_repli2/resid242_chainA.dat','./3p50_repli2/resid242_chainB.dat','./3p50_repli2/resid242_chainC.dat','./3p50_repli2/resid242_chainD.dat','./3p50_repli2/resid242_chainE.dat')

##=============================================Make plots.==========================================================
fig, ((ax1,ax2,ax3,ax4),(ax5,ax6,ax7,ax8),(ax9,ax10,ax11,ax12))= plt.subplots(figsize=(108,9),nrows=3,ncols=4)
fig.subplots_adjust(left=0.05, right=0.975, wspace=0, hspace=0.25)#bottom, top
plt.suptitle ('Protein RMSD')

def only_line_with_everything(ax,apo,holo,color_apo,color_holo,title):
    ax.plot(apo[0],apo[1],color=color_apo,label='apo')
    ax.plot(holo[0],holo[1],color=color_holo,label='holo')
    ax.set_xlabel('Time(ns)')
    ax.set_ylabel('RMSD(Å)')
    ax.xaxis.set_label_coords(0.05, -0.1)
    ax.set_xlim([0, 200])
    ax.set_ylim([0, 3.5])
    ax.legend(loc='upper right')
    ax.set_title(title)
    return ax

def only_line_without_xticks(ax,apo,holo,color_apo,color_holo,title):
    ax.plot(apo[0],apo[1],color=color_apo,label='apo')
    ax.plot(holo[0],holo[1],color=color_holo,label='holo')
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_xlim([0, 200])
    ax.set_ylim([0, 3.5])
    ax.legend(loc='upper right')
    ax.set_title(title)
    return ax

#def fill_between_with_everything(ax, list_apo,list_holo,color_apo,color_holo,title):

def fill_between_with_xticks(ax, list_apo,list_holo,color_apo,color_holo,title,xlim):
    ax.fill_between(list_apo[0], list_apo[2], list_apo[3], facecolor=color_apo, alpha=0.2)
    ax.plot(list_apo[0],list_apo[1],color=color_apo,label='apo')
    ax.fill_between(list_holo[0], list_holo[2], list_holo[3], facecolor=color_holo, alpha=0.2)
    ax.plot(list_holo[0], list_holo[1], color=color_holo, label='holo')
    ax.set_yticklabels([])
    ax.set_xlim([0,xlim])
    ax.set_ylim([0,3.5])
    ax.legend(loc='upper right')
    ax.set_title(title)
    return ax

def fill_between_without_xticks(ax, list_apo,list_holo,color_apo,color_holo,title,xlim):
    ax.fill_between(list_apo[0], list_apo[2], list_apo[3], facecolor=color_apo, alpha=0.2)
    ax.plot(list_apo[0],list_apo[1],color=color_apo,label='apo')
    ax.fill_between(list_holo[0], list_holo[2], list_holo[3], facecolor=color_holo, alpha=0.2)
    ax.plot(list_holo[0], list_holo[1], color=color_holo, label='holo')
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_xlim([0,xlim])
    ax.set_ylim([0,3.5])
    ax.legend(loc='upper right')
    ax.set_title(title)
    return ax

#ax5,ax9.
def fill_between_with_everything(ax, list_apo,list_holo,color_apo,color_holo,title):
    ax.fill_between(list_apo[0], list_apo[2], list_apo[3], facecolor=color_apo, alpha=0.2)
    ax.plot(list_apo[0],list_apo[1],color=color_apo,label='apo')
    ax.fill_between(list_holo[0], list_holo[2], list_holo[3], facecolor=color_holo, alpha=0.2)
    ax.plot(list_holo[0], list_holo[1], color=color_holo, label='holo')
    ax.set_xlabel('Time(ns)')
    ax.set_ylabel('RMSD(Å)')
    ax.xaxis.set_label_coords(0.05, -0.1)
    ax.set_xlim([0, 200])
    ax.set_ylim([0, 3.5])
    ax.legend(loc='upper right')
    ax.set_title(title)
    return ax

only_line_with_everything(ax1,M205P_apo_CA,M205P_holo_CA,'#000000','#4162c1','M205P C-alpha')
only_line_without_xticks(ax2,M205G_apo_CA,M205G_holo_CA,'#000000','#1f536a','M205G C-alpha')
fill_between_without_xticks(ax3,list_M205W_apo_CA,list_M205W_holo_CA,'#000000','#008000','M205W C-alpha',200)
fill_between_without_xticks(ax4,list_WT_apo_CA,list_WT_holo_CA,'#000000','#c823c8','WT C-alpha',200)
fill_between_with_everything(ax5,M205P_apo_res205,M205P_holo_res205,'#000000','#4162c1','M205P Residue205')
fill_between_without_xticks(ax6,M205G_apo_res205,M205G_holo_res205,'#000000','#1f536a','M205G Residue205',200)
fill_between_without_xticks(ax7,M205W_apo_res205,M205W_holo_res205,'#000000','#008000','M205W Residue205',200)
fill_between_without_xticks(ax8,WT_apo_res205,WT_holo_res205,'#000000','#c823c8','WT Residue205',200)
fill_between_with_everything(ax9,M205P_apo_res242,M205P_holo_res242,'#000000','#4162c1','M205P Residue242')
fill_between_without_xticks(ax10,M205G_apo_res242,M205G_holo_res242,'#000000','#1f536a','M205G Residue242',200)
fill_between_without_xticks(ax11,M205W_apo_res242,M205W_holo_res242,'#000000','#008000','M205W Residue242',200)
fill_between_without_xticks(ax12,WT_apo_res242,WT_holo_res242,'#000000','#c823c8','WT Residue242',200)

plt.show()
fig.savefig('../PLOTS/RMSD_allinall_0101-4.png')
