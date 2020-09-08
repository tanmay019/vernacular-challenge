# vernacular-challenge

1. The following Dockerfile works to create container image as intended.
    - Build Instructions
      - $ cd path/to/repo
      - $ docker build -t my-custom-ubuntu:vernacular .
    - Run instructions
      - $ docker run -it my-custom-ubuntu:vernacular

2. following files contain necessary data on hardware spec.
    - $ cat /proc/cpuinfo
    - $ cat /proc/meminfo

3. Script to manage disk space
    - By default it searches for audio files in /home/ubuntu/audios, to use custom directory, run the script as :-  $ python3 ./clean-audio.py ./ubuntu/new/audios
    - Creates a deleted-file-dd-mm-yyyy.log format in the directory you run it.
    - I have assumed the user to be ubuntu, so that files in /home/ubuntu are accessible, if that's not the case, sudo can be used.
