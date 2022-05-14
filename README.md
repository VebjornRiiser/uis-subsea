# UiS Subsea - ROV Topside System
#### DATBAC-1 21H - Bacheloroppgave i datateknologi

This project consist of:
* The GUI
* Network handler
* Handler for controller input


### How to install
Installing is done by (assumes that you have Python 3.10 and pip installed and added to path):

* Download the project.
* Make sure VLC is installed on your computer. https://www.videolan.org/
* To install all the required Python libraries run:
```
pip install -r requirements.txt
```
* Open port 6900 for TCP communication for receiving and sending.
* Start the program by running:
```
python main.py
```


### Start Mini PC

```
import os
os.system("ssh subsea@10.0.0.2 -i RovRsaKey killall python3.10")
os.system("ssh subsea@10.0.0.2 -i RovRsaKey python3.10 UiS-subsea-Bildebehandling/python/main.py")
```

