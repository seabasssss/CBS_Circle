pka = {'A': 'null', 'F':'null', 'G':'null', 'S':'null', 'I':'null', 'L':'null', 'M':'null', 'N':'null', 'P':'null', 'Q':'null', 'T':'null','W':'null', 'V':'null','H':6.0, 'D':3.7, 'E':4.2, 'Y':10.5, 'C':8.2, 'K':10.5, 'R':12.5}
acidic = ['D', 'E', 'Y', 'C']
basic = ['K', 'R', 'H']
protein = str((input('Enter amino acid sequence:')).upper())
freq = {}
a = ''

def aaFreq():
    for x in range(len(protein)):
        a = protein[x]
        if a in freq:
            freq[a] += 1
        else:
            freq[a] = 1
    return freq

def charge():
    charge = 0.0
    ph = float(input('Enter pH of solution:'))
    for key in freq:
        try:
            if ph > pka[key] and key in acidic: #deprotonated
                if abs(ph - pka[key]) < 1.05 and abs(ph - pka[key]) > 0.85:
                    charge -= (1 * freq[key] * 0.9)
                elif abs(ph - pka[key]) < 0.85 and abs(ph - pka[key]) > 0.6:
                    charge -= (1 * freq[key] * 0.875)
                elif abs(ph - pka[key]) < 0.6 and abs(ph - pka[key]) > 0.35:
                    charge -= (1 * freq[key] * 0.75)
                elif abs(ph - pka[key]) < 0.35 and abs(ph - pka[key]) > 0.15:
                    charge -= (1 * freq[key] * 0.67)
                elif abs(ph - pka[key]) < 0.15:
                    charge -= (1 * freq[key] * 0.5)
                else:
                    charge -= (1 * freq[key])
            if ph < pka[key] and key in basic: #protonated
                if abs(ph - pka[key])< 1.05 and abs(ph - pka[key]) > 0.85:
                    charge += (1 * freq[key] * 0.9)
                elif abs(ph - pka[key]) < 0.85 and abs(ph - pka[key]) > 0.6:
                    charge += (1 * freq[key] * 0.875)
                elif abs(ph - pka[key]) < 0.6 and abs(ph - pka[key]) > 0.35:
                    charge += (1 * freq[key] * 0.75)
                elif abs(ph - pka[key]) < 0.35 and abs(ph - pka[key]) > 0.15:
                    charge += (1 * freq[key] * 0.67)
                elif abs(ph - pka[key]) < 0.15:
                    charge += (1 * freq[key] * 0.5)
                else:
                    charge += (1 * freq[key])
            if ph > pka[key] and key in basic: #partial
                if abs(ph - pka[key]) < 1.05 and abs(ph - pka[key]) > 0.85:
                    charge += (1 * freq[key] * 0.1)
                elif abs(ph - pka[key]) < 0.85 and abs(ph - pka[key]) > 0.6:
                    charge += (1 * freq[key] * 0.125)
                elif abs(ph - pka[key]) < 0.6 and abs(ph - pka[key]) > 0.35:
                    charge += (1 * freq[key] * 0.25)
                elif abs(ph - pka[key]) < 0.35 and abs(ph - pka[key]) > 0.15:
                    charge += (1 * freq[key] * 0.33)
                elif abs(ph - pka[key]) < 0.15:
                    charge += (1 * freq[key] * 0.5)
            if ph < pka[key] and key in acidic: #partial
                if abs(ph - pka[key])< 1.05 and abs(ph - pka[key]) > 0.85:
                    charge -= (1 * freq[key] * 0.1)
                elif abs(ph - pka[key]) < 0.85 and abs(ph - pka[key]) > 0.6:
                    charge -= (1 * freq[key] * 0.125)
                elif abs(ph - pka[key]) < 0.6 and abs(ph - pka[key]) > 0.35:
                    charge -= (1 * freq[key] * 0.25)
                elif abs(ph - pka[key]) < 0.35 and abs(ph - pka[key]) > 0.15:
                    charge -= (1 * freq[key] * 0.33)
                elif abs(ph - pka[key]) < 0.15:
                    charge -= (1 * freq[key] * 0.5)
        except:
            pass
    if ph > 9.5:
        charge -= 1
    if ph < 2.2:
        charge += 1
    print('OVERALL CHARGE:',charge)

def mw():
    weight = 18.01528*2
    MW={'A': 71.04, 'C': 103.01, 'D': 115.03, 'E': 129.04, 'F': 147.07, 'G': 57.02, 'H': 137.06, 'I': 113.08, 'K': 128.09, 'L': 113.08,'M': 131.04, 'N': 114.04, 'P': 97.05, 'Q': 128.06, 'R': 156.10, 'S': 87.03, 'T': 101.05, 'V': 99.07, 'W': 186.08, 'Y': 163.06 }
    for key in freq:
        if key in MW:
            weight += MW[key]
    print('MOLECULAR WEIGHT:',weight, 'g/mol')

def disulfide():
    tracker1 = 0
    tracker2 = 0
    di = 0
    cnumb = 0
    print('POSSIBLE DISULFIDE LINKS:')
    for x in range(len(protein)):
        if protein[x] == 'C':
            tracker1 = x
            cnumb +=1
            print('Cysteine #',cnumb)
            for y in range(len(protein)):
                if protein[y] == 'C':
                    tracker2 = y
                    if tracker1 != tracker2:
                        di += 1
                        print(tracker1+1, '->', tracker2+1)
    print('Total:', int(di/2))
    if di == 0:
        print('No disulfide links')

aaseq = protein
def findmotif():
    motif=str.upper(input("Input a motif. (Variable positions may be represent by 'X'): "))
    motiflength=len(motif)-str.count(motif,"X")
    mismatch = -1
    while mismatch < 0 or mismatch > motiflength:
        mismatch=0
        try:
            mismatch=int(input("Enter mismatch allowance number: "))
        except ValueError:
            pass
        if mismatch < 0 or mismatch > motiflength:
            print("Must be less than motif length, try again...")
    filteredscorelist=[]
    for loopcount1 in range(0,len(aaseq)+1-len(motif)):
        matchscore=0
        mismatchscore=0
        for loopcount2 in range(0,len(motif)):
            if motif[loopcount2] == "X":                                    #ignore X's in motif
                pass
            elif mismatchscore > mismatch:                                  #stop checking if score will not pass filter
                break
            elif aaseq[loopcount1+loopcount2] == motif[loopcount2]:         #add to score if sequence matches motif
                matchscore+=1
            else:
                mismatchscore+=1
        if matchscore >= motiflength-mismatch:
            filteredscorelist+=[[loopcount1,matchscore]]
    for x in range(0,len(filteredscorelist)):
        print("from",filteredscorelist[x][0] + 1,"to",filteredscorelist[x][0]+len(motif) + 1,":",aaseq[filteredscorelist[x][0]:filteredscorelist[x][0]+len(motif)])

def get_polarity(str):
    polarity = {'R':0,'K':0,'D':0,'E':0,'Q':1,'N':1,'H':1,'S':1,'T':1,'Y':1,'C':1,'M':1,'W':1,
                'A':2,'I':2,'L':2,'F':2,'V':2,'P':2,'G':2}
    numPolar = 0
    numNonPolar = 0
    numCharged = 0
    for letter in str:
        if letter in polarity:
            if polarity[letter] == 1:
                numPolar = numPolar + 1
            elif polarity[letter] == 2:
                numNonPolar = numNonPolar + 1
            else:
                numCharged = numCharged + 1
    print ("Number of polar: ",  numPolar)
    print ("Number of non polar: ", numNonPolar)
    print ("Number of charged: ", numCharged)


pI = {'A':6.0, 'F':5.48, 'G':5.97, 'S':5.58, 'I':6.02, 'L':5.98, 'M':5.74, 'N':5.41, 'P':6.30, 'Q':5.65, 'T':5.60,'W':5.89, 'V':5.96,'H':7.59, 'D':2.77, 'E':3.22, 'Y':5.66, 'C':5.07, 'K':9.74, 'R':10.76}

def getPI(protein):
    pass

def ntSeq(protein):
    reversecodons = {'G': ['GGU', 'GGA', 'GGG', 'GGC'], 'P': ['CCU', 'CCA', 'CCC', 'CCG'], 'F': ['UUC', 'UUU'],
                     'D': ['GAC', 'GAU'], 'E': ['GAA', 'GAG'], 'W': ['UGG'], 'C': ['UGU', 'UGC'],
                     'V': ['GUA', 'GUU', 'GUG', 'GUC'], 'K': ['AAA', 'AAG'],
                     'L': ['CUU', 'CUC', 'CUA', 'CUG', 'UUA', 'UUG'], 'Stop': ['UAA', 'UGA', 'UAG'],
                     'N': ['AAU', 'AAC'], 'M': ['AUG'], 'Q': ['CAG', 'CAA'], 'H': ['CAC', 'CAU'],
                     'A': ['GCU', 'GCG', 'GCC', 'GCA'], 'I': ['AUC', 'AUA', 'AUU'],
                     'T': ['ACG', 'UAU', 'UAC', 'ACC', 'ACA', 'ACU'], 'S': ['UCA', 'UCG', 'AGC', 'UCU', 'AGU', 'UCC'],
                     'R': ['CGG', 'AGA', 'CGA', 'AGG', 'CGU', 'CGC']}

    homosapiens = {'': 0.0, 'UUU': 17.6, 'UCU': 15.2, 'UAU': 12.2, 'UGU': 10.6,
                   'UUC': 20.3, 'UCC': 17.7, 'UAC': 15.3, 'UGC': 12.6,
                   'UUA': 7.7, 'UCA': 12.2, 'UAA': 1.0, 'UGA': 1.6,
                   'UUG': 12.9, 'UCG': 4.4, 'UAG': 0.8, 'UGG': 13.2,
                   'CUU': 13.2, 'CCU': 17.5, 'CAU': 10.9, 'CGU': 4.5,
                   'CUC': 19.6, 'CCC': 19.8, 'CAC': 15.1, 'CGC': 10.4,
                   'CUA': 7.2, 'CCA': 16.9, 'CAA': 12.3, 'CGA': 6.2,
                   'CUG': 39.6, 'CCG': 6.9, 'CAG': 34.2, 'CGG': 11.4,
                   'AUU': 16.0, 'ACU': 13.1, 'AAU': 17.0, 'AGU': 12.1,
                   'AUC': 20.8, 'ACC': 18.9, 'AAC': 19.1, 'AGC': 19.5,
                   'AUA': 7.5, 'ACA': 15.1, 'AAA': 24.4, 'AGA': 12.2,
                   'AUG': 22.0, 'ACG': 6.1, 'AAG': 31.9, 'AGG': 12.0,
                   'GUU': 11.0, 'GCU': 18.4, 'GAU': 21.8, 'GGU': 10.8,
                   'GUC': 14.5, 'GCC': 27.7, 'GAC': 25.1, 'GGC': 22.2,
                   'GUA': 7.1, 'GCA': 15.8, 'GAA': 29.0, 'GGA': 16.5,
                   'GUG': 28.1, 'GCG': 7.4, 'GAG': 39.6, 'GGG': 16.5}


    translated = ''
    for x in range(len(protein)):
        add = ['']
        for y in range(len(reversecodons[protein[x]])):
            if homosapiens[reversecodons[protein[x]][y]] > homosapiens[add[0]]:
                add = [reversecodons[protein[x]][y]]
            else:
                pass
        translated += add[0]
    print('MOST LIKELY NUCLEOTIDE SEQUENCE:',translated)


def reverseAssoc(x): #reverse dictionary not used in code but useful for switching between codon to AA and AA to codon dictionaries
    dictionary = {}
    for key in x:
        if x[key] in dictionary:
            dictionary [x[key]] += [key]
        else:
            dictionary[x[key]] = [key]
    return dictionary

def codonlookup(sequence):
    codons = {'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L', 'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
              'UAU': 'T', 'UAC': 'T', 'UAA': 'Stop', 'UAG': 'Stop', 'UGU': 'C', 'UGC': 'C', 'UGA': 'Stop', 'UGG': 'W',
              'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L', 'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
              'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
              'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'Start', 'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
              'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
              'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V', 'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
              'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'}
    output = {'RF1START': [], 'RF1STOP': [], 'RF2START': [], 'RF2STOP': [], 'RF3START': [], 'RF3STOP': []}
    sequence = sequence.replace('T', 'U')
    count = 0
    while count < 3:
        sequence0 = sequence[count:]
        itnum = len(sequence0)
        seqnum = itnum % 3
        if seqnum != 0:
            sequence0 = sequence0[:-seqnum]
        else:
            sequence0 = sequence0
        start0 = 0
        while start0 != len(sequence0):
            codcheck = str(sequence0[start0] + sequence0[start0 + 1] + sequence0[start0 + 2])
            if codcheck == 'AUG':
                key = 'RF' + str(count + 1) + 'START'
                output[key] += [start0]
            if codcheck == 'UAA' or codcheck == 'UAG' or codcheck == 'UGA':
                key = 'RF' + str(count + 1) + 'STOP'
                output[key] += [start0]
            start0 += 3
        count += 1
    rfcount = 0
    while rfcount < 3:
        print('Open reading frames using reading frame ' + str(rfcount + 1) + ' are: ')
        rflist = []
        sequencerf = sequence[rfcount:]
        itnumrf = len(sequencerf)
        seqnumrf = itnumrf % 3
        if seqnumrf != 0:
            sequencerf = sequencerf[:-seqnumrf]
        else:
            sequencerf = sequencerf
        startvalues = output['RF' + str(rfcount + 1) + 'START']
        stopvalues = output['RF' + str(rfcount + 1) + 'STOP']
        rfstartcounter = 0
        while startvalues != [] and stopvalues != [] and rfstartcounter < len(startvalues):
            rfstopcounter = 0
            while rfstopcounter < len(stopvalues):
                if stopvalues[rfstopcounter] > startvalues[rfstartcounter]:
                    readingframe = [sequencerf[startvalues[rfstartcounter]:stopvalues[rfstopcounter]]]
                    rflist += readingframe
                    print(readingframe)
                rfstopcounter += 1
            rfstartcounter += 1
        if rflist != []:
            largest = max(rflist)
            print('The largest reading frame for reading frame ' + str(rfcount + 1) + ' is: ' + str(largest))
            translate = 0
            codonstring = ''
            while translate < len(sequencerf):
                codchecktr = str(sequencerf[translate] + sequencerf[translate + 1] + sequencerf[translate + 2])
                codonstring += str(codons[codchecktr])
                translate += 3
            print('The translated string is:' + '\n' + codonstring)
        rfcount += 1
# running in reverse


aaFreq()
print('AA FREQUENCY:',freq)
get_polarity(protein)
mw()
disulfide()
ntSeq(protein)
charge()
findmotif()
sequence = (input('Enter nucleotide sequence to be translated:')).upper()
codonlookup(sequence)

import time
import os.path


def importTextFile():
    check = True
    while check == True:
        try:
            check = False
            sfile = input("Enter the file name (must be '.fa', no quotations): ")
            sfile = open(sfile, "r")
        except FileNotFoundError:
            print("That's not on your computer, dumbass")
            check = True
    print(sfile)
    linelist = ""
    line = "firstline"
    while line != "":
        if line == "firstline":  # avoids adding header from .fa file to the sequence to be searched
            line = sfile.readline()
        else:
            line = sfile.readline()
            linelist = linelist + line
    for element in [" ", "\n"]:
        linelist = str.replace(linelist, element, "")
    sfile.close()
    return str(linelist)


def findMotif(seq, motif, mismatch, motiflength, strand, direction):
    filteredscorelist = []
    ##    print("motiflength",motiflength)
    ##    print("seqtruuu",len(seq))
    ##    print(seq)
    ##    print("seqlength",len(seq)+1-motiflength)
    for loopcount1 in range(len(seq) + 1 - len(motif)):
        matchscore = 0
        mismatchscore = 0
        for loopcount2 in range(len(motif)):
            ##            print(seq[loopcount1+loopcount2],type(seq[loopcount1+loopcount2]))
            ##            print(motif[loopcount2][0],type(seq[loopcount1+loopcount2]))
            if len(motif[loopcount2]) > 1:
                ##                print("variable position")
                for loopcount3 in range(len(motif[loopcount2])):
                    if seq[loopcount1 + loopcount2] == motif[loopcount2][loopcount3]:
                        matchscore += 1
                        break
            else:
                ##                print("nonvariable position")
                if motif[loopcount2][0] == "X":  # ignore X's in motif
                    ##                    print("pass")
                    pass
                elif mismatchscore > mismatch:  # stop checking if score will not pass filter
                    ##                    print(mismatchscore, ">", mismatch, "so break")
                    break
                elif seq[loopcount1 + loopcount2] == (motif[loopcount2][0]):  # add to score if sequence matches motif
                    ##                    print(matchscore)
                    matchscore += 1
                ##                    print("add to matchscore")
                else:
                    mismatchscore += 1
                    ##                    print("add to mismatchscore")
                    ##        print("matchscore",matchscore)
        if matchscore >= motiflength - mismatch:
            ##            print("add to list")
            filteredscorelist += [[loopcount1, loopcount1 + len(motif) - 1, matchscore, strand, direction]]
    return filteredscorelist
    ##print(loopcount1)


# opens query sequence which will be searched
sequencetype = ""
while sequencetype == '':
    sequencetype = str.upper(input("Select 'DNA' or 'AA' alphabet: "))
    if sequencetype != "AA" and sequencetype != "DNA":
        print("Please enter 'DNA' or 'AA'...")
        sequencetype = ''
userinput = str.upper(input("Import .txt file? Y/N: "))
seq = ""
dnaseq = ""
if userinput == "Y":
    seq = str.upper(importTextFile())
else:
    seq = str.upper(input("Input a sequence to searched: "))
print("sequence: ", seq)

# identifies subject sequence(s) which will be searched for in query sequence
searching = True
while searching == True:
    motifstring = str.upper(input(
        "Input a motif. Variable positions may be represent by 'X' and relaxed positions may be represented by '(_/_)': "))
    if motifstring == "":
        break

    # converts string entry into list
    motif = []
    loopcount = 0
    motifvariablesites = str.count(motifstring, "X")
    while loopcount < len(motifstring):
        if motifstring[loopcount] in ['"', "'"]:
            loopcount += 1
        elif motifstring[loopcount] == "(":  # for sites that may be more than one character
            loopcount += 1
            variableposition = []
            while motifstring[loopcount - 1] != ")":
                if motifstring[loopcount] in ["/", ")"]:
                    loopcount += 1
                else:
                    variableposition += list(motifstring[loopcount])
                    loopcount += 1
            motif += [variableposition]
        else:
            motif += [list(motifstring[loopcount])]
            loopcount += 1
    print("Motif: ", motif)
    print("Length: ", len(motif))
    motiflength = len(motif) - motifvariablesites
    # NOTE: motiflength is the threshold needed to pass the search parameters. In all other cases len(motif) should be used.

    # sets allowable mismatch number
    mismatch = -1
    while mismatch < 0 or mismatch > motiflength:
        mismatch = 0
        try:
            mismatch = int(input("Enter mismatch allowance number: "))
        except ValueError:
            pass
        if mismatch < 0 or mismatch > motiflength:
            print("Must be less than motif length, try again...")

            # generates list of positions that satisfy the search conditions
    start = time.time()
    if sequencetype == "DNA":
        print("Searching positive strand in the forward direction...")
    else:
        print("Searching sequence in forward direction...")
    filteredscorelist = findMotif(seq, motif, mismatch, motiflength, 1, 1)
    ##print(filteredscorelist)
    if sequencetype == "DNA":
        print("Searching positive strand in the reverse direction...")
    else:
        print("Searching sequence in reverse direction...")
    filteredscorelist += findMotif(seq, motif[::-1], mismatch, motiflength, 1, -1)
    ##print(filteredscorelist)
    if sequencetype == "DNA":
        if dnaseq == "":
            DNA = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
            for element in range(len(seq)):
                dnaseq += DNA[seq[element]]
        print("Searching negative strand in the forward direction...")
        filteredscorelist += findMotif(dnaseq, motif, mismatch, motiflength, -1, 1)
        ##print(filteredscorelist)
        print("Searching negative strand in the reverse direction...")
        filteredscorelist += findMotif(dnaseq, motif[::-1], mismatch, motiflength, -1, -1)
        ##print(filteredscorelist)
    end = time.time()
    print("Total # of results: ", len(filteredscorelist))
    print("Total time elapsed: ", end - start)
    ##    savesearchresults=str.upper(input("Save results? Y/N: ")



    # prints the sequences that satisfy the search conditions
    ##    for x in range(0,len(filteredscorelist)):
    ##        print("from",filteredscorelist[x][0],"to",filteredscorelist[x][0]+len(motif),":",seq[filteredscorelist[x][0]:filteredscorelist[x][0]+len(motif)])

    # asks user if another motif should be searched
    continuesearch = str.upper(input("Search for another motif? Y/N: "))
    if continuesearch == "Y":
        pass
    else:
        searching = False
