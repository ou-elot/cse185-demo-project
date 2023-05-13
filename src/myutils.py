"""
Utilities for mypileup
"""

# Need "." "," based on match to refbase
# ^, $
def GetReadBase(pileupread, refbase):
	"""
	Extract the mpileup sequence of bases
	from a single read at a particular position

	Mimics the format of "read bases" specified here:
	http://www.htslib.org/doc/samtools-mpileup.html

	Parameters
	----------
	pileupread : pysam.PileupRead
	   The pileupread object from which 
	   to extract info
	refbase : str
	   Reference base for the position

	Returns
	-------
	nucstring : str
	   Representation of this read in
	   mpileup format
	"""
	# Extract read base
	read_base = pileupread.alignment.query_sequence[pileupread.query_position]

	# Set the base
	nucstring = ""
	if read_base == refbase:
		if pileupread.alignment.is_reverse():
			nucstring = ","
		else: nucstring = "."
	else:
		if pileupread.alignment.is_reverse():
			nucstring = read_base.lower()
		else: nucstring = read_base

	# Check if it is the first or last base of the read
	# TODO

	return pileupread.alignment.query_sequence[pileupread.query_position]

# TODO docs
# TODO convert to ascii
def GetQual(pileupread):
	return str(pileupread.alignment.query_qualities[pileupread.query_position])

