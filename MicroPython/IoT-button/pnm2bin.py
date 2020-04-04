
import os
import sys


fn = sys.argv[1]

print("Opening %s" % fn)

with open(fn, 'rb') as f:
        f.readline() # Magic number
        f.readline() # Creator comment
#        f.readline() # Dimensions
        data = bytearray(f.read())



basename, _ = os.path.splitext(fn)
sn = '%s.bin' % basename
print("Saving %s" % sn)
filehandle = open(sn, 'wb')
filehandle.write(data)
filehandle.close()

