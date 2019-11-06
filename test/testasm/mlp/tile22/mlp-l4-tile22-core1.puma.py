
import sys, os
import numpy as np
import math
sys.path.insert (0, '/home/plinio/puma-simulator/include/')
sys.path.insert (0, '/home/plinio/puma-simulator/src/')
sys.path.insert (0, '/home/plinio/puma-simulator/')
from data_convert import *
from instrn_proto import *
from tile_instrn_proto import *
dict_temp = {}
dict_list = []
i_temp = i_set(d1=513, imm=286, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=513, r1=513, load_width=16, vec=8)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=641, imm=414, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=641, r1=641, load_width=16, vec=8)
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=0, r1=513, vec=128, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=128, r1=641, vec=128, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_mvm(['11'])
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=513, r1=256, vec=10, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=523, r1=384, vec=10, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=533, imm=0, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=533, r1=533, load_width=10, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_alu('add', d1=513, r1=513, r2=533, vec=10)
dict_list.append(i_temp.copy())
i_temp = i_alu('add', d1=513, r1=523, r2=513, vec=10)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=523, imm=10, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=523, r1=513, counter=1, store_width=10, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_hlt()
dict_list.append(i_temp.copy())
filename = 'mlp/tile22/core_imem1.npy'
np.save(filename, dict_list)
