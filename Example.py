import os
from InvokeMadGraph import GenerateProcesses
from MultiRunScan import RunScan

# here's how to generate the diagrams
# we simply instantiate the class and call the invoke method with the path to the process card
generateDiagrams = GenerateProcesses()
generateDiagrams.invoke("SampleProcessesCard.dat")

# now let's do a scan across some energies
# first we instantiate the class
run = RunScan()

# here we are auto-generating a card to set beam energies between e_min and e_max with n equispaced bins for the process we generated diagrams for above
run.generateBeamEnergyScanCard(350, 400, 49, generateDiagrams.processDirectory)

# now let's run it!
run.runScan()
