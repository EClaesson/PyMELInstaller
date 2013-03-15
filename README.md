PyMELInstaller is a Python script that installs PyMEL (for use in Maya scripts).

Don't download the *\_\_init\_\_.py* script, instead add this to all scripts that needs PyMEL:
```python
import urllib,imp,os;f=os.path.join(os.path.expanduser('~'), 'PMI.py');e=not os.path.exists(f);if e: urllib.urlretrieve('http://goo.gl/M0zWp',f);if e: m=imp.load_source('pmi',f);if e: m.installPyMEL();
```