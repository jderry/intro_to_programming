def unroll_loop(inputFile, outputFile, num):
   '''unroll_loop(inputFile of dataset, outputFile of script, number of records to compare to 1 record)
   '''
   with open(inputFile) as inFile:
      LoS = inFile.read().splitlines()
      LoL = []
      for record in LoS:
         LoL.append(record.split())
   LoL.pop(0) # pop off the label line
   
   with open(outputFile, 'a') as outFile:
      # outFile.write("#!/usr/bin/python\n")
      outFile.write("with open(" + "'" + inputFile + "'" + ") as inFile:\n")
      outFile.write("   LoS = inFile.read().splitlines()\n")
      outFile.write("   LoL = []\n")
      outFile.write("   for record in LoS:\n")
      outFile.write("      LoL.append(record.split())\n")
      outFile.write("   LoL.pop(0)\n")
      
      outFile.write("num = " + str(num) + "\n")
      outFile.write("r = float(0.000416667) # define r\n")
      outFile.write("candidate_pairs_lin = set()\n")
      
      outFile.write("for i in range(len(LoL) - num):\n")
      for j in range(1, num):
         outFile.write("   if ((float(LoL[i][1]) - float(LoL[i+" + str(int(j)) + "][1]))**2 + (float(LoL[i][2]) - float(LoL[i+" + str(int(j)) +  "][2]))**2)**(1/2) <= r: \n")
         outFile.write("      candidate_pairs_lin.add(frozenset([LoL[i][0], LoL[i+" + str(int(j)) + "][0]]))\n")
      outFile.write("for i in range(len(LoL) - num, len(LoL)-1):\n")
      outFile.write("   for j in range(i+1, len(LoL)):\n")
      outFile.write("      if ((float(LoL[i][1]) - float(LoL[j][1]))**2 + (float(LoL[i][2]) - float(LoL[j][2]))**2)**(1/2) <= r: \n")
      outFile.write("         candidate_pairs_lin.add(frozenset([LoL[i][0], LoL[j][0]]))\n")        

         
