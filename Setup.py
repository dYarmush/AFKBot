from setuptools import setup

APP = ['AFKBot.py']
OPTIONS = {'iconfile': 'afk.ico', 'packages': ['puaoutgui', 'random', 'timesetup.y']}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)