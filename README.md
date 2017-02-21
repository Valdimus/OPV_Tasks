# Open Path View Tasks

## Todo

Write this software

## Requirements

You will need to install :
```bash
apt-get install imagemagick hugin
```
You also need to have a [https://github.com/OpenPathView/DirectoryManager](DirectoryManager server) and an [https://github.com/OpenPathView/OPV_DBRest](OPV_DBRest server) running.
These server handle campaings, lot ... data storing.

### Hugin Script Interface (HSI) module
You also need to have the Hugin Script Interface python module. It should be install by default with hugin but migth by install for the wrong version of python.
To check it (outside your venv) :
```bash
$ python3.5
Python 3.5.2 (default, Nov 17 2016, 17:05:23)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import hsi
```

If you don't have it ... dam you are about to recompile hugin ! To wrap your HSI in the good python version, follow the instructions [TODO](here).

If you have it installed on your system, you need to add it to your python virtual env, the easiest way to do so his to make a symbolic link from your system dist-packages/hsi.py module to venv dist-packages.
Follow this :
```bash
(global) $ python3.5 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))"  # get you global dist-package path
/usr/lib/python3/dist-packages
(venv) $ python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))"  # get you venv dist-package path
/home/benjamin/Documents/OpenPathView/code/OPV_Tasks/.venv/OPV_Tasks/lib/python3.5/site-packages
(vent) $ ln -s /usr/lib/python3/dist-packages/hsi.py /home/benjamin/Documents/OpenPathView/code/OPV_Tasks/.venv/OPV_Tasks/lib/python3.5/site-packages/ # make symbolic link
(vent) $ ln -s /usr/lib/python3/dist-packages/_hsi.so /home/benjamin/Documents/OpenPathView/code/OPV_Tasks/.venv/OPV_Tasks/lib/python3.5/site-packages/ # make symbolic link
```

## Install
```bash
pip install -r requirements.txt
python setup.py install
```

## Rotate Task
Will rotate a lot (it's 6 pictures) in portrait mode.
```bash
bin/opv-task-rotate 53 --debug
```

## License

Copyright (C) 2017 Open Path View, Maison Du Libre <br />
This program is free software; you can redistribute it and/or modify  <br />
it under the terms of the GNU General Public License as published by  <br />
the Free Software Foundation; either version 3 of the License, or  <br />
(at your option) any later version.  <br />
This program is distributed in the hope that it will be useful,  <br />
but WITHOUT ANY WARRANTY; without even the implied warranty of  <br />
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  <br />
GNU General Public License for more details.  <br />
You should have received a copy of the GNU General Public License along  <br />
with this program. If not, see <http://www.gnu.org/licenses/>.  <br />
