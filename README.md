# Google Drive for Linux Unnoficial version
### Useful links
  * Google Console: https://console.developers.google.com/start/api?id=drive
  * Quick start api: https://developers.google.com/drive/v3/web/quickstart/python
  * About filese and folders: https://developers.google.com/drive/v3/reference/files
  * About filese and folders: https://developers.google.com/drive/v3/web/manage-downloads
  * Query parameters: https://developers.google.com/drive/v3/web/search-parameters
  * Outh permissions: https://developers.google.com/drive/v3/web/about-auth

### Libs
you need to download these libs:
* [pip] - command: python get-pip
* [ftfy] - command: python -m pip install ftfy==4.4.3 (for python 2.x)
* [Google Client Library] - command: python -m pip install --upgrade google-api-python-client

### Running
Execute ```run.py```

```sh
$ python run.py
```

### Development
Want to contribute? Great! Send me a message.

### Todos
 - Write Tests
 - Download files
 - Check if file has changed (version file) on cloud
 - If file was changed in machine, send to cloud

### License
GLP 3.0

   [pip]: <https://pip.pypa.io/en/stable/installing/>
   [ftfy]: <https://github.com/LuminosoInsight/python-ftfy>
   [Google Client Library]: <https://developers.google.com/api-client-library/python/start/installation>