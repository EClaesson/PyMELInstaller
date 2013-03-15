PyMELInstaller is a Python script that installs PyMEL (for use in Maya scripts).

Don't download the *\_\_init\_\_.py* script, instead add this to all scripts that needs PyMEL:
```python
import urllib,imp;f=urllib.urlretrieve('https://raw.github.com/EClaesson/PyMELInstaller/master/__init__.py')[0];m=imp.load_source('pmi',f);m.installPyMEL()
```