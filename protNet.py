dirproteins = {}

def checkYesNo(prompt):
    answer = input(prompt)
    if(answer.upper() == 'Y' or answer.upper() == 'YES'):
        return True
    elif(answer.upper() == 'N' or answer.upper() == 'NO'):
        return False
    else:
        print('Your answer didn\'t match Y or N. Try again.')
        checkYesNo(prompt)

def createProt(name=''):
    if(name == ''):
        prot = input('What is the name of this protein? ')
    else:
        proteins['IP3']
        prot = name

    if(checkYesNo('Does ' + prot + ' have any downstream targets? (Y/N) ')):
        targets = addTargets(prot)
    else:
        string = input('What do you want printed when ' + prot + ' is activated? ')
        targets = { 'results': string }
    proteins[prot] = Protein(True, targets)
    if(checkYesNo('Would you like to add another protein? (Y/N) ')):
        createProt()
    else:
        prompt()

def addTargets(prot):
    loopBool = True
    targets = {}
    while(loopBool):
        target = input('What is the name of ' + prot + '\'s target? ')
        effect = input('Does ' + prot + ' activate ' + target + '? (Y/N) ')
        if(checkYesNo('Does ' + prot + '\'s effect on ' + target + ' depend on any upstream effectors? (Y/N) ')):
            effectors = addEffectors(prot, target, effect)
            targets[target] = [effect, effectors]
        else:
            targets[target] = [effect, {}]
        moreTargets = checkYesNo('Does ' + prot + ' have more targets? (Y/N) ')
        if(not moreTargets):
            loopBool = False

    return targets

def addEffectors(prot, target, effect):
    loopBool = True
    effectors = {}
    while(loopBool):
        effector = input('What is the name of this effector? ')
        upstreamEffect = checkYesNo('Does ' + effector + ' activate ' + prot +'? (Y/N) ')
        effectors[effector] = upstreamEffect
        moreEffectors = checkYesNo('Are there more upstream effectors for ' + prot + '\'s effect on ' + target + '? (Y/N) ')
        if(moreEffectors == False):
            loopBool = False

    return effectors

class Protein:
    #proteins have a name, current_state (active or inactive), and a dictionary of
    #targets
    def __init__(self, current_state, targets):
        self.__current_state = current_state
        self.__targets = targets

    def getState(self):
        return self.__current_state

    def getTargets(self):
        return  self.__targets

def prompt():
    command = input('What command would you like to run? ')

#createProt()
