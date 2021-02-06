import sys
import audio_b
import os
import img_b
from colorama import *
if sys.platform.startswith('nt'):
	init(convert=True)
else:
	init()
sys.argv[0]=os.path.basename(sys.argv[0])
if len(sys.argv)==1 or sys.argv[1] not in 'help new_code build_image build_audio'.split():
	sys.stderr.write(f'''Error! Usage:
{sys.argv[0]} help
''')
	sys.exit(1)
def new_code():
	c=''
	for i in range(8):
		c+=str(randint(0,9))
	print(c)
def help():
	print(f'''Type:
{sys.argv[0]} help
{sys.argv[0]} new_code
{sys.argv[0]} build_image {Fore.GREEN}your_code path_to_save_image{Style.RESET_ALL}
{sys.argv[0]} build_audio {Fore.GREEN}your_code path_to_save_audio{Style.RESET_ALL}
''')
def build_audio(code,fout):
	if not code.isdigit():
		sys.stderr.write(f'{Fore.RED}ERROR: invalid code!{Style.RESET_ALL}\n')
		sys.exit(1)
	if not fout.endswith('.wav'):
		sys.stderr.write(f'{Fore.YELLOW}WARNING: output format is wav only!{Style.RESET_ALL}\n')
	audio_b.build(fout,code)
def build_image(code,fout):
	if not code.isdigit():
		sys.stderr.write(f'{Fore.RED}ERROR: invalid code!{Style.RESET_ALL}\n')
		sys.exit(1)
	img_b.build(fout,code)
def run(c,args):
	eval(c)(*args)
if sys.argv[1] in 'help new_code'.split():
	if sys.argv[2:]!=[]:
		sys.stderr.write('Expected 1 argument({sys.argv[1]}), found {len(sys.argv[1:])}!\n')
		sys.exit(1)
else:
	if len(sys.argv[2:])!=2:
		sys.stderr.write('Expected 3 arguments, found {len(sys.argv[1:])}!\n')
		sys.exit(1)
run(sys.argv[1],sys.argv[2:])