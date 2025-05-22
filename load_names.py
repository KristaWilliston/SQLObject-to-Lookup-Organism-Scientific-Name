import sys
from model import *

init(new=True)

h = open(sys.argv[1])
for l in h:
    l = l.strip('\t|\n')
    sl = l.split('\t|\t')
    taxid = int(sl[0])
    rank = sl[3]
    t = Taxonomy.byTaxid(taxid)
    n=Name(name=name, name_class=name_class, taxonomy=t)
h.close()
