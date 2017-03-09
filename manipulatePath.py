#import IP3_Pathway
from protNet import *

proteins={}
#proteins[protName] = Protein(Name, active/inactive, {Name of target:[Activate/Deactivate (T/F), { Upstream Effector: Effect }]})
proteins['GenericInhibitorA'] = Protein('GenericInhibitorA',True, {'GenericInhibitorB': [False, {}]})
proteins['GenericInhibitorB'] = Protein('GenericInhibitorB',True, {'GPCR': [False, {'GenericInhibitorB': False}]})
proteins['Hormone'] = Protein('Hormone',True, {'GPCR': [True, {}]})
proteins['GPCR'] = Protein('GPCR',True, {'Ga': [True, {'GenericInhibitorB': False, 'Hormone': True}]})
proteins['Ga'] = Protein('Ga',False, {'IP3': [True, {'GPCR': True}]})
#for a protein with no downstream effectors we instead have [active message,
#inactive message, upstream effectors and their effects]
proteins['IP3'] = Protein('IP3',False, {'results': ['IP3 is active', 'IP3 is inactive', {'Ga': True}]})
#takes the upstream protein and the downstream protein

def setDownstream(upProt,counter=1):
    print("entering step number",counter)
    if 'results' in upProt._Protein__targets:
        if upProt._Protein__current_state == True:
            print("final result is",upProt._Protein__targets['results'][0])
        else:
            print("final result is",upProt._Protein__targets['results'][1])
    else:
        print("protein targets of",upProt._Protein__name,"include",upProt._Protein__targets)
        for target in upProt._Protein__targets:
            if upProt._Protein__targets[target][0] == False:
                action="deactivates"
            else:
                action="activates"
            print(upProt._Protein__name,action,target)
            oldstate = proteins[target]._Protein__current_state
            #set the current state of the downstream target according to the upstream effector
            proteins[target]._Protein__current_state = upProt._Protein__targets[target][0]
            #if the current_state of the downstream protein changed
            if oldstate != proteins[target]._Protein__current_state:
                #Continue the cascade!!!
                setDownstream(proteins[target],counter+1)

def setUpstream(upProt, downProt):
    print()

def prompt():
    print()

setDownstream(proteins['GenericInhibitorA'])
