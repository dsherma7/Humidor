class cigarString:
	def __init__(self, cigar, pos):
		self.pos = pos;
		self.match=self.insert=self.delete=self.soft = []
		self.cigar = self.parseCigar(cigar)

	def parseCigar(self,cigar):
		for x in cigar:
			if x == 'M':
				self.match = 1
				# Do Something
			if x == 'I':
				self.insert = 1
				# Do Something
			if x == 'D':
				self.delete = 1
				# Do Something
			if x == 'N':
				self.delete = 1
				# Do Something
			if x == 'S':
				self.soft = 1
				# Do Something
			if x == 'H':
				self.hard = 1
				# Do Something
			if x == 'P':
				self.pad = 1
				# Do Something
			if x == '=':
				self.seq_match = 1
				# Do Something
			if x == 'X':
				self.mismatch = 1
				# Do Something
		return cigar

	def printAll(self):
		print(self.match)
		print(self.insert)
		print(self.delete)
		print(self.soft)

cig = cigarString('M4I10M22S15',6500)
print(cig.cigar)
cig.printAll()

