import os

class GenerateProcesses(object):
    processCard = None
    processDirectory = None
    
    def __parseCard(self, card):
        with open(card) as procCard:
            for line in procCard:
                if "output " in line:
                    self.processDirectory = os.path.join(os.path.dirname(os.path.abspath(card)), line.replace("output ",""))
    
    def importProcessCard(self, pathToProcessCard):
        if os.path.isfile(pathToProcessCard):
            print 'Importing process card: {}'.format(pathToProcessCard)
            self.processCard = pathToProcessCard
            self.__parseCard(self.processCard)
        else:
            raise TypeError('Process card is not valid!')

    def runMadGraph(self, pathToProcessCard):
        try:
            os.system('mg5_aMC ' + pathToProcessCard)
        except:
            print "An error occurred. Is MadGraph in your path variables??? O.o"
            return

    def invoke(self, pathToProcessCard):
        self.importProcessCard(pathToProcessCard)
        self.runMadGraph(pathToProcessCard)

    def main(self, argv):
        processCard =  None
        if argv is None:
            cardInput = raw_input("Type path to card: ")
            processCard = str(cardInput)
        else:
            processCard = argv
        invoke(self.processCard)

def main(argv=None):
    GenerateProcesses().main(argv)

if __name__ == '__main__':
    main()
