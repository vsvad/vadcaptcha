import numpy as np
import os
from scipy.io.wavfile import read,write
from random import randint
def build(fout,code):
	files=[os.path.join('resources','audio',f'{i}.wav') for i in code]
	res=[]
	for file in files:
		rate,data=read(file)
		res+=list(data)
	write(fout,rate,np.array(res,'int16'))