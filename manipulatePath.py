import IP3_Pathway
from protNet import *

#takes the upstream protein and the downstream protein
def setDownstream(upProt):
    if('results' in upProt._Protein__targets):
        if(upProt._Protein__current_state == True):
            print(upProt._Protein__current_state['results'][0])
        else:
            print(upProt._Protein__current_state['results'][1])
    else:
        for target in upProt._Protein__targets:
            print(upProt._Protein__targets[target][0])
            oldstate = proteins[target]._Protein__current_state
            #set the current state of the downstream target according to the upstream effector
            proteins[target]._Protein__current_state = upProt._Protein__targets[target][0]
            #if the current_state of the downstream protein changed
            if(oldstate != proteins[target]._Protein__current_state):
                #Continue the cascade!!!
                setDownstream(proteins[target])

def setUpstream(upProt, downProt):
    print()

def prompt():
    print()

setDownstream(proteins['CH'])
