# elevatedEnvVarUtil
Utility script for changing environment variables on Windows 10 Enterprise from non-admin account.
The changeJavaVersion.bat-script needs to run from an elevated shell, this is done in the python-script by using subprocess to run the script in an elevated powershell instance (promts user to ender admin credentials). The solution is crude, but it gets the job done

## Usecase
When working on different projects you may need to change your environmental variables according to the project you are working on (in my case the Java-version). Instead of doing multiple klicks before getting to part where you can run environmental variables settings as admin, you can now do the following:
1. Hit windows-key, type 'cmd' and hit enter
2. Run command 'j [the java version you want, e.g 8]
3. This promts user to ender admin credentials
4. Profit

## Prerequisites
This script assumes that all the different java-versions are located under the same folder. This folder is stored as an environmental variable (JAVADIR). Moreover, the folders of the different Java-versions is then assumed to have their own environmental variable. Lastly, the environmental variable for the Java-version in use is expected to be JAVA_HOME
