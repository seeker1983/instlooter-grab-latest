import subprocess
import os
import zipfile
from pprint import pprint
import shutil
import drive
import config

def process(is_handle):
	download(is_handle)
	zip(is_handle)
	upload(is_handle)

def download(is_handle):
	if not is_handle:
		raise Exception('No is_handle');
	cmd = ['/usr/local/bin/instalooter', 'user', is_handle, '-T', config.name_template, '-n', str(config.max_images), 'downloads/' + is_handle]
	result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	print('Executed \'%s\' with return code %s' % (' '.join(cmd), result.returncode))
	#print('Stdout: \'%s\'' % result.stdout)
	#print('Stderr: \'%s\'' % result.stderr)

	return result

def zip(is_handle):
	archive = 'archives/' + is_handle
	dir = 'downloads/' + is_handle
	print('Archiving %s into %s.zip' % (dir,dir))
	shutil.make_archive(archive, 'zip', dir)

def upload(is_handle):
	file = 'archives/%s.zip' % is_handle
	print('Uploading %s' % file)
	return drive.upload(file, title=is_handle + '.zip')

if __name__ == '__main__':
	zip('espn')    
	upload('espn')    
