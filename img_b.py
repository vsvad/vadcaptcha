from PIL import Image,ImageDraw,ImageFont,ImageFilter
import os
from random import randint
def build(fout,code):
	fnt = ImageFont.truetype(os.path.join('resources','ttf','font.ttf'), 40)
	img=Image.new('RGB',(200,50),'#a0a0a0')
	d = ImageDraw.Draw(img)
	d.text((0,0),code,font=fnt,fill=(0,0,0))
	del d
	img=img.filter(ImageFilter.BLUR)
	img.save(fout)