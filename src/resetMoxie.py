import os
import shutil

#Reset TorCHAT and Moxie

print 'Soft reset because we do not wanna have to come with a new tree structure again'
print 'Cleaning MOXIE'
if os.path.isfile("me.info"):
    os.remove("me.info")
if os.path.isfile("sendBuffer.txt"):
    os.remove("sendBuffer.txt")

if os.path.isfile("moxielogout.txt"):
    os.remove("moxielogout.txt")

print 'Cleaning BUMP'
if os.path.isfile("historyaddresses.txt"):
    os.remove("historyaddresses.txt")
    open("historyaddresses.txt", 'a').close()

print 'Cleaning TorChat'
if os.path.isfile("torchat/torchat.ini"):
    os.remove("torchat/torchat.ini")

if os.path.isfile("torchat/buddy-list.txt"):
    os.remove("torchat/buddy-list.txt")

if os.path.isfile("torchat/Tor/tor.pid"):
    os.remove("torchat/Tor/tor.pid")

if os.path.isfile("torchat/pid-torchat.txt"):
    os.remove("torchat/pid-torchat.txt")

if os.path.isfile("torchat/statusUpdates.txt"):
    os.remove("torchat/statusUpdates.txt")
    open("torchat/statusUpdates.txt", 'a').close()
