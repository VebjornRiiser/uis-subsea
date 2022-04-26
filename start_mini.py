import os
os.system("ssh subsea@10.0.0.2 -i RovRsaKey killall python3.10")
os.system("ssh subsea@10.0.0.2 -i RovRsaKey python3.10 UiS-subsea-Bildebehandling/python/main.py")
