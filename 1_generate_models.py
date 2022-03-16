import sys
import os
for i in [2,4,8,16]:
    for act in ['sigmoid','tanh','relu','elu']:
#     for act in ['step1','step2','step3']:
        print(i,act)
        os.system('python encoder.py {} {}'.format(i,act))
