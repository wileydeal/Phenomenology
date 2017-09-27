import os
from InvokeMadGraph import GenerateProcesses

class RunScan(object):
    scanProcessCard = False

    def runScan(self):
        """This invokes MadGraph with current instance of scanProcessCard"""
        if os.path.isfile(self.scanProcessCard) == False:
            raise TypeError('Import valid scan process card!')
        runMG = GenerateProcesses()
        runMG.runMadGraph(self.scanProcessCard)

    def importScanCard(self, scanCard):
        """Imports a user specified card for use in scanning"""
        # throw if file doesn't exist - to be caught when invoked
        if os.path.isfile(scanCard)==False:
            raise TypeError('Scan Card does not exist!\nHave you double checked the path?')

        # now set the scanProcessCard instance for use in any relevant methods in this class
        self.scanProcessCard = cardName

    def generateBeamEnergyScanCard(self, lowerLimit, upperLimit, nBins, processName):
        """Generates a card with nBins equispaced energy bins between lowerLimit (GeV) and upperLimit (GeV)"""
        # generate process card name, throw if already exists - to be caught when invoked
        cardName = str(processName) + '_EnergyScan.dat'
        cardName = cardName.replace('\n','').replace('\t','').replace('\r','')
        if os.path.isfile(cardName):
            raise TypeError('Energy Scan Card already exists!')
        
        # now set the scanProcessCard instance for use in any relevant methods in this class
        self.scanProcessCard = cardName
        
        # calculate the "step size" between energy scans
        stepSize = (upperLimit - lowerLimit)/float(nBins+1)
        
        # now let's write the actual card
        with open(self.scanProcessCard, 'a') as tempCard:
            tempCard.write('launch ' + processName + '\n')
            for i in range(0, nBins):
                # calculate the beam energy for i-th bin
                beamEnergy = lowerLimit + stepSize*i
                tempCard.write('set ebeam ' + str(beamEnergy) + '\n')
                tempCard.write('launch\n')
            tempCard.write('print_results --path=./' + processName + '.txt --format=short')