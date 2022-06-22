#! python3
# mapit opens a browser window with a map using an address
#from the command line or clipboard

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste() 

webbrowser.open('https://www.google.com/maps/place/' + address)