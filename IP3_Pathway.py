import protNet
#proteins[protName] = Protein(active/inactive, {Name of target:[Activate/Deactivate (T/F), { Upstream Effector: Effect }]})
proteins['CS'] = Protein(True, {'CS': [False, {}]})
proteins['CH'] = Protein(True, {'GPCR': [False, {'CS': False}]})
proteins['Hormone'] = Protein(True, {'GPCR': [True, {}]})
proteins['GPCR'] = Protein(True, {'Ga': [True, {'CH': False, 'Hormone': True}]})
proteins['Ga'] = Protein(True, {'IP3': [True, {'GPCR': True}]})
