Welcome to PyDa: Python Digital Assistant
This is a GUI Based Python Digital Assistant made using several APIs.

APIs used are:
1) wikipedia
2) wolframalpha
3) wxPython - for GUI(Graphical User Interface)

Other Libraries and requirements:
1) pyttsx3 - Python text to speech - so that PyDa can read out the answer for you
2) SpeechRecognition - so that PyDa can recognize the audio input
3) PyAudio - so that PyDa can play audio 

Before running this on your PC
Install the following requirements:

1) pip install wolframalpha
2) pip install wikipedia
3) pip install -U wxPython
4) pip install pyttsx3
5) pip install SpeechRecognition==3.4.3
6) Install PyAudio according to your python-type version (32 or 64) 
    You can check your python version by typing python in cmd and you'll see something like
    "
    Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    "
    "[MSC v.1916 32 bit (Intel)]" - this tells that my PC has 32 bit python
    So, I'll download 32 bit PyAudio from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
    After downloading the PyAudio.whl file, save the file in your current directory and then in your text editor's terminal:
    enter "pip install PyAudio-0.2.11-cp38-cp38-win32.whl" - as of mine.


Run the application:
python PyDa.py


There are 2 ways to use this application:
1) by TEXT
2) by SPEECH

1) by TEXT
    After entering python PyDa.py in terminal, a GUI will Pop-up, greeting and asking you for the question.
    Enter your question, for example:
     Who is Amitabh Bachchan?
     What is 2+2?
     17*9
     George Bush
     etc.
    
    PyDa will then find an answer for you and will show you it as a text.

2) by SPEECH
    After entering python PyDa.py in terminal, a GUI will Pop-up, greeting and asking you for the question.
    DO NOT TYPE ANYTHING NOW. PRESS ENTER.
    Then, use your Microphone to ask the question, like:
    say on your microphone, "Who is Amitabh Bachchan"
    PyDa will then recognize your question and then put is as text on question label.
    Press ENTER.
    PyDa will then show you the output.

I hope you like my PyDa Project.
Many more coming for J.A.R.V.I.S.

Thankyou!!



Thank You!! 