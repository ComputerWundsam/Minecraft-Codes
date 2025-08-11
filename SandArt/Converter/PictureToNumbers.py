import sys
import re
from PIL import Image
from numpy import asarray
import numpy
numpy.set_printoptions(threshold=sys.maxsize)

# Write here the address of the image. 
image = Image.open("C:\\Users\\Admin\\Pictures\\Minecraft\\ConvertingPictures\\Neymar.gif")
f = open('C:\\Users\\Admin\\Desktop\\numberdata.txt', 'w')
 
# summarize some details about the image
numpydata = asarray(image)


# data
dataset = numpy.array2string(numpydata, max_line_width=None, separator=',')
re.sub("\\s+", ",", dataset.strip())

f.write(dataset)
f.close()
print("Job finished!")
