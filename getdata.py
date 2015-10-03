#! /usr/bin/env python
'''Download all data files from Google Drive (https://drive.google.com/folderview?id=0B2xSDxvcBl6KLWVTd0lLZ2E5Rmc&usp=sharing)'''

import urllib
import os
import sys


folder_url = 'https://googledrive.com/host/0B2xSDxvcBl6KLWVTd0lLZ2E5Rmc/'

filenames = [
		'f-I-curve/decreasing.dat', 
		'f-I-curve/increasing.dat',
		'f-I-curve/separate runs/-12pA.dat',
		'f-I-curve/separate runs/-1pA.dat', 
		'f-I-curve/separate runs/-5pA.dat', 
		'f-I-curve/separate runs/0pA.dat', 
		'f-I-curve/separate runs/10pA.dat', 
		'f-I-curve/separate runs/15pA.dat', 
		'f-I-curve/separate runs/20pA.dat', 
		'f-I-curve/separate runs/25pA.dat', 
		'f-I-curve/separate runs/30pA.dat', 
		'f-I-curve/separate runs/35pA.dat', 
		'f-I-curve/separate runs/40pA.dat', 
		'f-I-curve/separate runs/45pA.dat', 
		'f-I-curve/separate runs/50pA.dat', 
		'f-I-curve/separate runs/5pA.dat', 
		# TODO: These do not work because they are >150 MB, thus Google Drive returns a html page where you have to accept the download.
		# Possible workaround: Fetching files directly via https://googledrive.com/host/file-id downloads the files directly without showing the html prompt
		#'rheobase/-1.90pA.dat',
		#'rheobase/-1.91pA.dat'
	]


overwrite = (len(sys.argv) > 1 and sys.argv[1] == '-overwrite')

for filename in filenames:
	if os.path.exists(filename) and not overwrite:
		print filename, 'exists (use -overwrite to download again)'
	else:
		print 'Downloading {0}...'.format(filename),
		urllib.urlretrieve(folder_url + filename, filename)
		print 'Done'
