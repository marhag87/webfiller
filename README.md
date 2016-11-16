Webfiller
=========

Interface between Google Chrome and pass

Requirements:
-------------
* pass
* Graphical passphrase tool, like pinentry-qt
* "Url in title" chrome plugin: https://chrome.google.com/webstore/detail/url-in-title/ignpacbgnbnkaiooknalneoeladjnfgb

Config:
-------
Set up config file like this:
```
<url from chrome title>:
    username: <optional username>
    password: <pass store>
```
Example:
```
www.reddit.com:
    username: trololololo
    password: internet/reddit
```
