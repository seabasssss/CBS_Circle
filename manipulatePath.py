import IP3_Pathway
from protNet import *

#proteins[protName] = Protein(active/inactive, {Name of target:[Activate/Deactivate (T/F), { Upstream Effector: Effect }]})
proteins['GenericInhibitorA'] = Protein(True, {'GenericInhibitorA': [False, {}]})
proteins['GenericInhibitorB'] = Protein(True, {'GPCR': [False, {'GenericInhibitorB': False}]})
proteins['Hormone'] = Protein(True, {'GPCR': [True, {}]})
proteins['GPCR'] = Protein(True, {'Ga': [True, {'GenericInhibitorB': False, 'Hormone': True}]})
proteins['Ga'] = Protein(True, {'IP3': [True, {'GPCR': True}]})
#for a protein with no downstream effectors we instead have [active message,
#inactive message, upstream effectors and their effects]
proteins['IP3'] = Protein(True, {'results': ['IP3 is active', 'IP3 is inactive', {'Ga': True}]})
#takes the upstream protein and the downstream protein

def setDownstream(upProt):
    if('results' in upProt._Protein__targets):
        if(upProt._Protein__current_state == True):
            print(upProt._Protein__current_state['results'],upProt._Protein__current_state['results'][0])
        else:
            print(upProt._Protein__current_state['results'],upProt._Protein__current_state['results'][1])
    else:
        for target in upProt._Protein__targets:
            print(upProt._Protein__targets[target],upProt._Protein__targets[target][0])
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

setDownstream(proteins['GenericInhibitorA'])
