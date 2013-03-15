# Copyright (C) 2013 Emanuel Claesson

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import urllib, os, sys, shutil
from zipfile import ZipFile

_lastShownPct = 0
_downloadedBytes = 0

def getPyMELDir(version):
	return os.path.join(os.path.expanduser('~'), 'PyMEL', 'pymel-' + version)

def getPyMELRootDir():
	return os.path.join(os.path.expanduser('~'), 'PyMEL')

def _addPyMELToPath(version):
	pymelDir = getPyMELDir(version)

	if(not (pymelDir in sys.path)):
		sys.path.append(pymelDir)
		print('PyMEL ' + version + ' added to path')

def _downloadCallback(blocks, blockSize, totalSize):
	global _lastShownPct, _downloadedBytes

	_downloadedBytes += blockSize
	pct = (float(_downloadedBytes) / totalSize) * 100.0
	pctTen = round(pct, -1)

	if pctTen > _lastShownPct:
		_lastShownPct = pctTen
		print str(int(pctTen)) + '%'

def installPyMEL(version = '1.0.5rc2'):
	"""If the specified version of PyMEL is not installed, it is installed in '<User Home>/PyMEL/<version>'.
	   version is a git tag name."""

	global _lastShownPct, _downloadedBytes

	if not os.path.exists(getPyMELDir(version)):
		_lastShownPct = 0
		_downloadedBytes = 0

		pymelDir = getPyMELRootDir()
		if not os.path.exists(pymelDir):
			os.makedirs(pymelDir)

		pymelZipPath = os.path.join(pymelDir, 'pymel.zip')

		print('Downloading PyMEL ' + version + '...')
		urllib.urlretrieve('https://github.com/LumaPictures/pymel/archive/' + version + '.zip', pymelZipPath, _downloadCallback)

		print('Extracting...')
		pymelZip = ZipFile(pymelZipPath)
		pymelZip.extractall(pymelDir)
		pymelZip.close()
		os.remove(pymelZipPath)

		print('Cleaning up...')
		for f in ['.gitignore', '.hgignore', 'CHANGELOG.rst', 'LICENSE', 'README', 'setup.py']:
			try:
				os.remove(os.path.join(getPyMELDir(version), f))
			except:
				pass

		for d in ['docs', 'examples', 'tests']:
			try:
				shutil.rmtree(os.path.join(getPyMELDir(version), d))
			except:
				pass

	_addPyMELToPath(version)