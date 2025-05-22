import sys
from model import *

init(new=True)

h = open(sys.argv[1])
for l in h:
    l = l.strip('\t|\n')
    sl = l.split('\t|\t')
    taxid = int(sl[0])
    rank = sl[2]
    t = Taxonomy(taxid=taxid, rank=rank, scientific_name=None, parent=None)
h.close()
