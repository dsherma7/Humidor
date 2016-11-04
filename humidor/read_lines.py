import sys
import subprocess

def readlines(ref):
    cmd = 'samtools view' 
    p = str(subprocess.check_output(cmd + " " + ref,shell=True))
    return [p, p.count('\\n')]

class cigarString:
    """ Class to parse and handle sam formatted cigar strings """
    pattern = re.compile('([MIDNSHPX=])')

    def __init__(self, cigar):
        values = self.pattern.split(cigar)[:-1]
        self.paired = (values[n:n+2] for n in xrange(0, len(values), 2))  # pair values by twos

    def getAlignmentLength(self):
        g = 0
        for pair in self.paired:
            l = int(pair[0])
            t = pair[1]
            if t == 'M':
                g += l
            elif t == 'I':
                pass
            elif t == 'D':
                g += l
            elif t == 'N':
                pass
            elif t == 'S':
                pass
            elif t == 'H':
                pass
            elif t == 'P':
                pass
            elif t == 'X':
                pass
            elif t == '=':
                pass
            else:
                sys.stderr.write("encountered unhandled CIGAR character %s\n" % t)
                pass
        return g



[file, num_lines] = readlines(sys.argv[1])
print(num_lines)
