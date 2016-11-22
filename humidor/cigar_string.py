class cigarString:
	def __init__(self, cigar, pos):
		self.pos = pos;
		#self.match=self.insert=self.delete=self.soft = []
		self.vals = self.parseCigar(cigar)

	def parseCigar(self,cigar):
		vals = dict()
		for x in cigar:
			if x == 'M':
				self.match = 1
				vals.update({'match':1})
				# Do Something
			if x == 'I':
				self.insert = 1
				vals.update({'insert':1})
				# Do Something
			if x == 'D':
				self.delete = 1
				vals.update({'delete':1})
				# Do Something
			if x == 'N':
				self.skip = 1
				vals.update({'skip':1})
				# Do Something
			if x == 'S':
				self.soft = 1
				vals.update({'soft':1})
				# Do Something
			if x == 'H':
				self.hard = 1
				vals.update({'hard':1})
				# Do Something
			if x == 'P':
				self.pad = 1
				vals.update({'pad':1})
				# Do Something
			if x == '=':
				self.seq_match = 1
				vals.update({'seq_match':1})
				# Do Something
			if x == 'X':
				self.mismatch = 1
				vals.update({'mismatch':1})
				# Do Something
		return vals
	def __iter__(self):
		return cigarIter(1,len(self.vals),self.vals.copy());

	def printAll(self):
		print(self.match)
		print(self.insert)
		print(self.delete)
		print(self.soft)

class cigarIter:
    def __init__(self, low, high, vals):
        self.current = low
        self.high = high
        self.keys = list(vals)
        self.vals = vals

    def __iter__(self):
        return self

    def __next__(self): # Python 2: def next(self)
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.vals[self.keys[self.current-1]]


cig = cigarString('M4I10M22S15',6500)
for items in cig:
	print(items)

#cig = cigarString('M4I10M22S15',6500)
#print(cig.cigar)
#cig.printAll()

