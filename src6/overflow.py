from PIL import Image
from sys import argv

if len(argv)!=4:
    exit("error")

n = int(argv[1])
inm = argv[2]
out = argv[3]

inimage = Image.open(inm)
wid, hei = inimage.size
outimage = inimage.resize((wid*n,hei*n))

outimage.save(out)