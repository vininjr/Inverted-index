import sys
from ind_inveted import Index_inverted

args = sys.argv[2:]
result = sys.argv[1]

for arg in args:
    result += " " + arg

index = Index_inverted()

h = index.sref(result)

index.write_file()

print('\n\n\t>>>>>>>>>>>>>>>>>>>> COMPLETE BUILDING <<<<<<<<<<<<<<<<<<<<\n\n')
