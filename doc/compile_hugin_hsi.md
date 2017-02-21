# Compile Hugin and HSI with specific version of python

*This tutorial is made based on an installation for ubuntu 16.04.*

You will need to compile Hugin with some added cmake constants to have hsi compiled in the correct python version.

## Dependencies
First install 'some' dependencies :
```bash
apt-get install swig build-essential autoconf automake1.11 libtool flex bison gdb   libc6-dev libgcc1 cmake pkg-config help2man checkinstall libwxgtk3.0-dev libtiff5-dev libpng12-dev   libopenexr-dev libexiv2-dev freeglut3-dev libglew-dev libboost-dev   libboost-thread-dev libboost-regex-dev libboost-filesystem-dev   libboost-iostreams-dev libboost-system-dev libboost-signals-dev   gettext liblapack-dev libxi-dev libxmu-dev libtclap-dev liblensfun-dev libvigraimpex-dev libpano13-dev libimage-exiftool-perl enblend python-argparse libimage-exiftool-perl enblend liblcms2-dev libsqlite3-dev python3-dev
```

## Get hugin latest sources

Download the lastest source code archive [https://sourceforge.net/projects/hugin/files/hugin/](here).
Extract it :
```bash
mkdir hugin
cd hugin
tar jxvf hugin-2016.2.0.tar.bz2
mkdir hugin.build
cd hugin.build
```

## Compile the source

You will need to set the following options :

* PYTHON_INCLUDE_DIR
* PYTHON_LIBRARY
* PYTHON_EXECUTABLE

For instance :
```bash
cd hugin.build
cmake ../hugin-2016.2.0/ -DENABLE_LAPACK=YES -DCPACK_BINARY_DEB:BOOL=ON -DCPACK_BINARY_NSIS:BOOL=OFF  -DCPACK_BINARY_RPM:BOOL=OFF -DCPACK_BINARY_STGZ:BOOL=OFF -DCPACK_BINARY_TBZ2:BOOL=OFF  -DCPACK_BINARY_TGZ:BOOL=OFF -DCPACK_BINARY_TZ:BOOL=OFF -DCMAKE_BUILD_TYPE=RelWithDebInfo  -DBUILD_HSI:BOOL=ON -DSWIG_EXECUTABLE=/usr/bin/swig3.0 -DPYTHON_INCLUDE_DIR=/usr/include/python3.5/ -DPYTHON_LIBRARY=/usr/lib/python3.5/config-3.5m-x86_64-linux-gnu/libpython3.5.so -DPYTHON_EXECUTABLE=/usr/bin/python3.5
```

Then compile and install :
```bash
make
sudo make install
```

## Test it's good
Finally check HSI is install.

```bash
$ python3.5
Python 3.5.2 (default, Nov 17 2016, 17:05:23)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import hsi
```

Go back to the [../README.mdl](README.md) and add the symbolic link.
