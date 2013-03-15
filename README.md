PyMELInstaller is a Python script that installs PyMEL (for use in Maya scripts).

Don't download the *\_\_init\_\_.py* script, instead add this to all scripts that needs PyMEL:
```python
import urllib,imp,os;f=os.path.join(os.path.expanduser('~'),'PMI.py')
if not os.path.exists(f): urllib.urlretrieve('http://goo.gl/M0zWp',f);imp.load_source('pmi',f).installPyMEL()
```

If you want a certain version of PyMEL to be installed, you can pass the git tag name as parameter to the last method call (installPyMEL()).
Default is '1.0.5rc2'.

If the requested version of PyMEL already is installed, nothing is done, except making sure it's in the path.