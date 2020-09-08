# vernacular-challenge

1. The following Dockerfile works to create container image as intended.

2. 

3. Script to manage sidk space
    - By default it searches for audio files in /home/ubuntu/audios, to use custom directory,
      run the script as :-  $ python3 ./clean-audio.py ./ubuntu/new/audios
    - Creates a deleted-file-dd-mm-yyyy.log format in the directory you run it.
    - I have assumed the user to be ubuntu, so that files in /home/ubuntu are accessible,
      if that's not the case, sudo can be used.
