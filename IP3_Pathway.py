from protNet import *
proteins={}
#proteins[protName] = Protein(active/inactive, {Name of target:[Activate/Deactivate (T/F), { Upstream Effector: Effect }]})
proteins['GenericInhibitorA'] = Protein(True, {'GenericInhibitorA': [False, {}]})
proteins['GenericInhibitorB'] = Protein(True, {'GPCR': [False, {'GenericInhibitorB': False}]})
proteins['Hormone'] = Protein(True, {'GPCR': [True, {}]})
proteins['GPCR'] = Protein(True, {'Ga': [True, {'GenericInhibitorB': False, 'Hormone': True}]})
proteins['Ga'] = Protein(True, {'IP3': [True, {'GPCR': True}]})
#for a protein with no downstream effectors we instead have [active message,
#inactive message, upstream effectors and their effects]
proteins['IP3'] = Protein(True, {'results': ['IP3 is active', 'IP3 is inactive', {'Ga': True}]})

print(proteins)
print(proteins['Ga'])
proteins['Ga'].getState()
