class Protein:
    def __init__(self, name, current_state=True):
        self.__name=name
        self.__current_state=current_state

    # Current state notation: False = inactive/inhibited and True = active/uninhibited
    # All proteins contain domains which enact their functions
    
    def display(self):
        if self.__current_state == True:
            state="inactive"
        else:
            state="active"
##        if self.__modification == 'p':
##            modification = 'phosphorylated'
##        elif self.__modification == '':
##            modification = unphosphorylated
        print("Name: ",self.__name, "\n"
              "Currently ",state)##, "and", modification)

    def getName(self):
        return str(self.__name)
        
    def getCurrent_state(self):
        return str(self.__current_state)

##    def getFunctions(self):
##        return str(self.__functions)
##
##    def getFunctions_inputs(self):
##        return str(self.__current_state)
##
##    def getFunctions_outputs(self):
##        return str(self.__current_state)

    def change_state(self):
        if self.__current_state == False:
           self.__current_state = True
        else:
            self.__current_state == True

##    def phosphorylate(self):  # we can later add ubiquitin, glycosylation etc
##        self.__modification = 'p'
##
##    def dephosphorylate(self):
##        self.__modification = ''
##
##    def getModification(self):
##        return (self.__modification)


class stimuli(Protein):
    def __init__(self, name):
        super().__init__(name)

    def stimulus(self, stimulus):  # DNA damage, stress, ROS, etc.
        self.__stimulus = stimulus

    def getStimulus(self):
        return str(self.__stimulus)

class protein_protein(Protein):
    def __init__(self, name):
        super().__init__(name)

    def bind(self, Protein):
        self.__binding = Protein # when two proteins are bound

    def unbind(self):
        self.__binding = ''

    def getBinding(self):
        return(self.__binding)

class response(Protein):
    def __init__(self, name):
        super().__init__(name)

    def response(self, response): # apoptosis, gene regulation/expression etc.
        self.___response = response

    def getResponse(self):
        return str(self.__response)



