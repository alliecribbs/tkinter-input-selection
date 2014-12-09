for i in range(3,7):

	f1 = open('N:\Project LFS\12300 Jobs\12315 - Anadarko I-Hub Riser Umb Study\Working Folder\Allie\DAF\BaseCase.yml','r')	
	f2 = open('N:\Project LFS\12300 Jobs\12315 - Anadarko I-Hub Riser Umb Study\Working Folder\Allie\DAF\H{}m_T{}s.yml'.format(i,j),'w') # Brackets indicate wave period
	for line in f1:
		f2.write(line.replace("WavePeriod: 3","WavePeriod: {}".format(i))) # WavePeriod: 3 indicates the ex. Basecase period 
	f2.close()  

f1.close()
