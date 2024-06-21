# Robbot

Robbot is a small search field that opens on the bottom right of your screen:

![img.png](docs/screenshot.png)

After entering something and hitting ENTER, it will generate a Python Jupyter notebook with the response.

![img.png](docs/screenshot2.png)

You can make use of it by installing [tkinter](https://docs.python.org/3/library/tkinter.html) and [bia-bob](https://github.com/haesleinhuepf/bia-bob?tab=readme-ov-file#installation). It is recommended to install them in a conda environment.

```
pip install tkinter bia-bob
```

You can then create a new shortcut in this folder (replace USERNAME with your username):

```
C:\Users\USERNAME\AppData\Roaming\Microsoft\Windows\Start Menu\Programs
```

The shortcut should point to the following command (replace ENVIRONMENT with the name of your conda environment)

```
C:\Users\haase\mambaforge\envs\ENVIRONMENT\python.exe robbot.py
```

And the working directory should be the folder where robbot.py is located.

