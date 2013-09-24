import os
print "Preparing Install...."
os.system("python setup.py install")
print "Packaging..."
os.system("python setup.py py2exe")
print "Done!"