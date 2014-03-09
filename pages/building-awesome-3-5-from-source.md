title: Building Awesome 3.5 from Source in Debian Sid
date: 2014-03-07 17:25 +0200
edited: 2014-03-09 21:03 +0200
tags: debian, awesome, stupid wiki

So here's a small how to based on previous <small>rage</small> post with Awesome 3.5

First, install dependencies: (stupid debian wiki not listing every one of them)

    sudo apt-get install cmake liblua5.1-dev imagemagick libxcb-randr0-dev libxcb-xtest0-dev libxcb-xinerama0-dev libxcb-shape0-dev libxcb-keysyms1-dev libxcb-icccm4-dev libx11-xcb-dev lua-lgi-dev libstartup-notification0-dev libxdg-basedir-dev libxcb-image0-dev libxcb-util0-dev libgdk-pixbuf2.0-dev lua5.1 libxcb-cursor-dev libcairo2-dev

Fetch the source from git with:

    git clone git://git.naquadah.org/awesome.git

    cd awesome

    git remote add origin-debian git://git.debian.org/git/users/acid/awesome.git

    git fetch origin-debian

Let's build it!

    cmake -DCMAKE_PREFIX_PATH=/usr -DSYSCONFDIR=/etc && make

Then install it with:

    sudo make install

    sudo ldconfig -v

Ta-da! You are done.
