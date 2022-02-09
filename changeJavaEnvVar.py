import sys, os, subprocess

versionPathMap = {'8':os.environ['JAVA8'],'11':os.environ['JAVA11'],'16':os.environ['JAVA16']}
validArguments = ['8','11','16']
firstArgument = sys.argv[1]
print("First argument passed to script is: " + firstArgument)

def changeJavaVersion(_firstArgument):
    if _firstArgument in validArguments: 
        argumentValueFromMap = versionPathMap[_firstArgument]
        #Run elevated powershell command
        subprocess.run(["powershell", "-command", "Start-Process changeJavaVersion.bat {} -Verb runas".format(argumentValueFromMap)])
    elif _firstArgument == 'x':
        exit()
    else:
        print("""
        This script changes the JAVA_HOME system environment variable.
        Available input options are 8, 11, 16 (or x to exit):
        """)
        userInput = input("Enter input:")
        changeJavaVersion(userInput)

changeJavaVersion(firstArgument)    


