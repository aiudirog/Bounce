from distutils.core import setup
import os
import py2exe

origIsSystemDLL = py2exe.build_exe.isSystemDLL
def isSystemDLL(pathname):
	if os.path.basename(pathname).lower() in ("sdl_ttf.dll", "libogg-0.dll"):
        	return 0
	return origIsSystemDLL(pathname)
py2exe.build_exe.isSystemDLL = isSystemDLL

setup(windows=['bounce.py'],
    data_files=[('Balls', ["1.png",
                 		"2.png",
                 		"3.png",
                 		"4.png",
                 		"5.png",
                 		"6.png",
                 		"7.png",
                 		"8.png",
                        "9.png",
                        "10.png",
                        "11.png",
                        "12.png",
                        "13.png",
                        "14.png",
                        "15.png",
                        "16.png",
                        "17.png",
                        "18.png",
                        "19.png",
                        "20.png",
                        "21.png",
                        "22.png",
                        "23.png",
                        "24.png",
                        "25.png",
                        "26.png",]
           		)]
  	)