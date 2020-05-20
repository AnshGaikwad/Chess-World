# Hi There!
# This python script is written to
# install some python modules using
# pip. You can go through the code.

import subprocess
import sys
import get_pip


# Installing Function
def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])


# Installing python-chess
try:
    print("[GAME] Trying to import python-chess")
    import chess
except:
    print("[EXCEPTION] python-chess not installed")

    try:
        print("[GAME] Trying to install python-chess via pip")
        import pip

        install("python-chess")
        print("[GAME] python-chess has been installed")
    except:
        print("[EXCEPTION] Pip not installed on system")
        print("[GAME] Trying to install pip")
        get_pip.main()
        print("[GAME] Pip has been installed")
        try:
            print("[GAME] Trying to install python-chess")
            import pip

            install("python-chess")
            print("[GAME] python-chess has been installed")
        except:
            print("[ERROR 1] python-chess could not be installed")

# Installing flask
try:
    print("[GAME] Trying to import flask")
    import flask
except:
    print("[EXCEPTION] flask not installed")

    try:
        print("[GAME] Trying to install flask via pip")
        import pip

        install("flask")
        print("[GAME] flask has been installed")
    except:
        print("[EXCEPTION] Pip not installed on system")
        print("[GAME] Trying to install pip")
        get_pip.main()
        print("[GAME] Pip has been installed")
        try:
            print("[GAME] Trying to install flask")
            import pip

            install("flask")
            print("[GAME] flask has been installed")
        except:
            print("[ERROR 1] flask could not be installed")

# Installing webbrowser
try:
    print("[GAME] Trying to import webbrowser")
    import webbrowser
except:
    print("[EXCEPTION] webbrowser not installed")

    try:
        print("[GAME] Trying to install webbrowser via pip")
        import pip

        install("webbrowser")
        print("[GAME] webbrowser has been installed")
    except:
        print("[EXCEPTION] Pip not installed on system")
        print("[GAME] Trying to install pip")
        get_pip.main()
        print("[GAME] Pip has been installed")
        try:
            print("[GAME] Trying to install webbrowser")
            import pip

            install("webbrowser")
            print("[GAME] webbrowser has been installed")
        except:
            print("[ERROR 1] webbrowser could not be installed")

# Installing pyttsx3
try:
    print("[GAME] Trying to import pyttsx3")
    import pyttsx3
except:
    print("[EXCEPTION] pyttsx3 not installed")

    try:
        print("[GAME] Trying to install pyttsx3 via pip")
        import pip

        install("pyttsx3")
        print("[GAME] pyttsx3 has been installed")
    except:
        print("[EXCEPTION] Pip not installed on system")
        print("[GAME] Trying to install pip")
        get_pip.main()
        print("[GAME] Pip has been installed")
        try:
            print("[GAME] Trying to install pyttsx3")
            import pip

            install("pyttsx3")
            print("[GAME] pyttsx3 has been installed")
        except:
            print("[ERROR 1] pyttsx3 could not be installed")
