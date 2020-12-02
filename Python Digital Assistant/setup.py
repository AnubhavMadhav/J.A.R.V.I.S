from cx_Freeze import setup, Executable

base = None    

executables = [Executable("PyDa.py", base=base)]

packages = ["idna","wikipedia","wolframalpha","wx","pyttsx3","speech_recognition"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "<any name>",
    options = options,
    version = "<any number>",
    description = '<any description>',
    executables = executables
)