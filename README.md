# pyav-ffmpeg (fork)

This project is a fork of [pyav-ffmpeg](https://github.com/PyAV-Org/pyav-ffmpeg).
It provides binary builds of FFmpeg and its dependencies for `PyAV`_.

Build for the following platforms:
- Debian 12 (x86_64)
- Windows 11 (AMD64)

What differs from the original branch
- removed some video decoders/encoders
- removed some audio codecs

## Build:
- Linux, python 3.11.8
    ```sh
    conda create -n pyav python==3.11.8
    conda activate pyav
    sudo apt-get install gcc curl nasm
    python scripts/build-ffmpeg.py /tmp/vendor
    ```

.. _PyAV: https://github.com/PyAV-Org/PyAV
