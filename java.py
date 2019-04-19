# coding: utf-8
import subprocess
import os

class Java():
    def __init__(self, f):
        self.file = f

    def version(self):
	version = subprocess.check_output(['java', '-version'], stderr=subprocess.STDOUT)
	#process = subprocess.Popen(['java', '--version'], stdout=subprocess.PIPE)
	#out, err = process.communicate()
	#process = os.popen('java --version').read()
        return "JAVA\n"+version+"\n"

        
        


