import re
import sys
import subprocess
import cigar_string

def readlines(ref):
	cmd = 'samtools view' 
	p = str(subprocess.check_output(cmd + " " + ref,shell=True))
	return [p, p.count('\\n')]

def parseLines(ref):
	[file, num_lines] = readlines(ref)
	lines = file.split("t")
	ctr = 0;
	for ln in lines:
		ctr+=1
		if ctr == 5:
			print(ln)
		if ctr == 15:
			ctr = 0


		
	

		

parseLines(sys.argv[1])
#cig = cigarString('M4I10M22S15',6500)
#for items in cig:
#	print(items)
 


#cig.printAll()

