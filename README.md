# About Enumcrt
Enumcrt is a python tool designed to enumerate subdomains of websites using CRTSH.The traffic sent to enumcrt.py gets reflected in the website crtsh.CRTSH is a  Certificate Transparency (CT) website which is used to perform a Certificate Search. This simple python tool scrapes the website and loads all subdomain obtain as result.

# Enumcrt overload

While enumeration subdomain of certain sites like (Google,Yahoo...) the tool may not respond.This is due the slow response form the CRTSH site and hence enumeration of huge list of domain is not possible.Even though the tool can easily crawl up to 2000+ URLs if available.


# Installation and Requirements

This requires Python 2.7 and We will soon release an update which supports Python 3.x

`git clone https://github.com/Tibinsunny/enumcrt.git`

Enumcrt depends on the json, urllib, and argparse python modules.

For installation on windows:

`c:\python27\python.exe -m pip install -r requirements.txt`


# Usage and Options

Option | Use
------------ | -------------
-u | This is the paramater which collects the url to be scanned
-o | This is the output file.Obtained results can be stored in a file using this option


# ScreenShot

If you want to embed images, this is how you do it:

![Image of Yaktocat](https://github.com/Tibinsunny/enumcrt/blob/master/screenshot/enum-crt.PNG)


# Examples

`enumcrt.py -u example.com` This lists out subdomain

`enumcrt.py -u example.com -o test.txt` This stores entire result to test.txt

# Version

This is a beta version.I hope you guys can help me in triggering bugs in the tool.Please do report bugs to tibinsunny95@gmail.com.

Happy Hacking !!!




