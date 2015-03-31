from Bio import ExPASy
from Bio import SwissProt

id = "Q5SLP9" 
handle = ExPASy.get_sprot_raw(id)
record = SwissProt.read(handle)

for x in record.cross_references:
    if x[2][0:2] == 'P:':
        print x[2][2:]
