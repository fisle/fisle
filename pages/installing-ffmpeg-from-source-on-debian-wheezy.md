title: Installing FFmpeg from source on Debian Wheezy
date: 2013-12-04 12:04 +0200
tags: ffmpeg, debian, wheezy

I needed to encode videos with FFmpeg for [my project](https://github.com/fisle/netflask) recently, but found it is not compiled with codecs I needed by default. Here's a guide how to do that by hand.

### Step 1 - Install dependecies ###
Install debian-multimedia repo by opening `/etc/apt/sources.list`:

    deb http://deb-multimedia.org wheezy main non-free
    deb-src http://deb-multimedia.org wheezy non-free

Next run the following to install the repository:

 `apt-get -y --force-yes install deb-multimedia-keyring; apt-get update`

Then install required packages:

    apt-get install subversion unzip frei0r-plugins-dev libdc1394-22-dev libfaac-dev \
    libmp3lame-dev libx264-dev libdirac-dev libxvidcore-dev libfreetype6-dev \
    libvorbis-dev libgsm1-dev libopencore-amrnb-dev libopencore-amrwb-dev \
    libopenjpeg-dev librtmp-dev libschroedinger-dev libspeex-dev libtheora-dev \
    libva-dev libvpx-dev libvo-amrwbenc-dev libvo-aacenc-dev libaacplus-dev libbz2-dev \
    libgnutls-dev libssl-dev libopenal-dev libv4l-dev libpulse-dev libmodplug-dev \
    libass-dev libcdio-dev libcdio-cdda-dev libcdio-paranoia-dev libvdpau-dev \
    libxfixes-dev libxext-dev libbluray-dev

Next download and compile libxavs with the following:

`svn co https://svn.code.sf.net/p/xavs/code/trunk xavs`

`cd xavs`

`./configure --enable-shared --disable-asm`

`make && make install`

### Step 2 - Install FFmpeg ###

Download source by issuing:

`wget http://www.ffmpeg.org/releases/ffmpeg-2.1.1.tar.gz`

Unzip it: `tar zxf ffmpeg-2.1.1.tar.gz && cd ffmpeg-2.1.1`

Next we configure it:

    ./configure --enable-gpl --enable-nonfree --enable-postproc --enable-pthreads \
    --enable-x11grab --enable-swscale --enable-version3 --enable-shared --disable-yasm \
    --enable-filter=movie --enable-frei0r --enable-libdc1394 --enable-libfaac \
    --enable-libmp3lame --enable-libx264 --enable-libxvid \
    --enable-libfreetype --enable-libvorbis --enable-libgsm --enable-libopencore-amrnb \
    --enable-libopencore-amrwb --enable-libopenjpeg --enable-librtmp \
    --enable-libschroedinger --enable-libspeex --enable-libtheora --enable-libvpx \
    --enable-libvo-amrwbenc --enable-libvo-aacenc --enable-libaacplus --enable-libxavs \
    --enable-bzlib --enable-openssl --enable-gnutls --enable-openal --enable-libv4l2 \
    --enable-libpulse --enable-libmodplug --enable-libass --enable-libcdio --enable-vdpau --enable-libbluray

After it's done configuring, let's start compiling:

`make && make install && ldconfig`

After the commands are finished, you are done!

FFmpeg is now installed!
