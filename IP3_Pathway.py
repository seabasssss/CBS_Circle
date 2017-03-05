from protNet import *
#proteins[protName] = Protein(active/inactive, {Name of target:[Activate/Deactivate (T/F), { Upstream Effector: Effect }]})
proteins['CS'] = Protein(True, {'CS': [False, {}]})
proteins['CH'] = Protein(True, {'GPCR': [False, {'CS': False}]})
proteins['Hormone'] = Protein(True, {'GPCR': [True, {}]})
proteins['GPCR'] = Protein(True, {'Ga': [True, {'CH': False, 'Hormone': True}]})
proteins['Ga'] = Protein(True, {'IP3': [True, {'GPCR': True}]})
#for a protein with no downstream effectors we instead have [active message,
#inactive message, upstream effectors and their effects]
proteins['IP3'] = Protein(True, {'results': ['IP3 is active', 'IP3 is inactive', {'Ga': True}]})
