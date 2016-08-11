date: 2016-08-31 22:05
slug: a-python-exploration-1-version-2-or-3-google-course
title: A Python exploration: Version 2 or 3? With Google's course
tags: Python, Programming, Linux, Reference
status: draft

<!-- PELICAN_BEGIN_SUMMARY -->
It had been a longtime wish of mine to *properly* learn Python, more than occasional dilettante tinkering. 
At the time of registering this domain name, most prominent advice offered upon a Google search was for beginners to learn python 2.x instead of 3.x.. 
Now (in mid-2006) however the opinions are more balanced, with more recommending to learn 3.x first if not to take a balanced approach with both v2 and v3.

<!-- PELICAN_END_SUMMARY -->

### Installed versions
----------------

This is being ran on an [Ubuntu 16.04 Linux](https://wiki.ubuntu.com/XenialXerus/ReleaseNotes) environment.
Default version of python running may be found out by:

    :::console
    $ python -V
    Python 2.7.12

To unpack what goes on here, the file executed by default upon simply calling `python` from command line is:

    :::console
    $ which python
    /usr/bin/python

This is a symbolic link that points to a Python 2.7 executable:

    :::console
    $ readlink -f $(which python)
    /usr/bin/python2.7

This is also accessible by simply calling `python2`. Use of Python 2 may be forced thus if necessary.
Python 3 is also simultaneously installed as `python3` and is more or less the latest stable Python 3 release at the time of Ubuntu release:

    :::console
    $ python3 -V
    Python 3.5.2

All installed versions in `/usr/bin` are (some extras redacted):

    :::console
    $ ls -l /usr/bin/python*
    /usr/bin/python -> python2.7
    /usr/bin/python2 -> python2.7
    /usr/bin/python2.7
    /usr/bin/python3 -> python3.5
    /usr/bin/python3.3
    /usr/bin/python3.5

More versions such as 2.6, 3.4 etc. may be installed using the `apt-get install` command.

### Virtual environments
-------------


