PyMELInstaller is a Python script that installs PyMEL (for use in Maya scripts).

Don't download the *\_\_init\_\_.py* script, instead add this to all scripts that needs PyMEL:
```python
import urllib,imp,os;u=os.path.expanduser('~');f=os.path.join(u, 'PMI_fetch.py');e=not os.path.exists(f);if e: urllib.urlretrieve('https://raw.github.com/EClaesson/PyMELInstaller/master/__init__.py', f);if e: m=imp.load_source('pmi',f);if e: m.installPyMEL();
```