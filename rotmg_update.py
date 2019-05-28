#!/usr/bin/python

import urllib
import requests
import os.path
import os
import time
import json
import sys

def getVersion():
    response = urllib.urlopen("http://www.realmofthemadgod.com/version.txt?time=%s" % int(round(time.time() * 1000)))
    data = response.read()
    return data

def getLanguage(lang_id, version):
    filename = "%s/%s.txt" % (version, lang_id)
    if os.path.exists(filename):
        return
    print "Downloading language %s" % lang_id
    r = requests.post("https://realmofthemadgodhrd.appspot.com/app/getLanguageStrings", data={"languageType": lang_id})
    with open(filename, "wb") as file:
        file.write(r.content)

def downloadClient(version):
    filename = "%s/client.swf" % version
    if os.path.exists(filename):
        return False
    print "Downloading client %s" % version    
    urllib.urlretrieve("https://realmofthemadgodhrd.appspot.com/AssembleeGameClient%s.swf" % version, filename)
    return True

def downloadLoader(version):
    filename = "%s/AGCLoader.swf" % version
    if os.path.exists(filename):
        return False
    print "Downloading loader %s" % version    
    urllib.urlretrieve("http://www.realmofthemadgod.com/AGCLoader%s.swf" % version, filename)
    return True

def pushbulletNotification(apikey, version):
    try:
        from pushbullet import Pushbullet
        pb = Pushbullet(apikey)
        push = pb.push_note("Realm of the Mad God Updated!", "Version: %s" % version)
        print "Pushbullet notification sent!"
    except:
        print "Pushbullet not working, try pip install pushbullet.py"
        pass

# Usage: rotmg_update.py [Pushbullet API key]

version = getVersion()
if not os.path.exists(version):
    os.makedirs(version)

notification = downloadClient(version)
downloadLoader(version)
getLanguage("de", version)
getLanguage("en", version)
getLanguage("es", version)
getLanguage("fr", version)
getLanguage("it", version)
getLanguage("ru", version)
getLanguage("tr", version)
if notification and len(sys.argv) >= 2:
    pushbulletNotification(sys.argv[1], version)
