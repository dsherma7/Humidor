def splitCigar(self, cigar):
    self.cigar = parseCigar(cigar)

    def parseCigar(self,cigar):
    	return cigar

cig = cigarString('M4I10M22S15')
print(cig.cigar)

temp1