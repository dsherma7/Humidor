import sys
import subprocess

def readlines(ref):
    cmd = 'samtools view' 
    p = str(subprocess.check_output(cmd + " " + ref,shell=True))
    return [p, p.count('\\n')]

def 


[file, num_lines] = readlines(sys.argv[1])
print(num_lines)
