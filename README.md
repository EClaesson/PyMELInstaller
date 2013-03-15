PyMELInstaller is a Python script that installs PyMEL (for use in Maya scripts).

Don't download the *\_\_init\_\_.py* script, instead add this to all scripts that needs PyMEL:
```python
eval("import urllib,imp,os;f=os.path.join(os.path.expanduser('~'),'PMI.py');if not os.path.exists(f):\n  urllib.urlretrieve('http://goo.gl/M0zWp',f);imp.load_source('pmi',f).installPyMEL()")
```