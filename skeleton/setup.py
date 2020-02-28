try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config={
    'descriptionn':'My Project',
    'author':'My name:SJ',
    'url':'URL to get it at.',
    'download_url':'you can get in github,my username is 13827790799SJ.',
    'autor_email':'a164648474@gmail.com',
    'version':'0.1',
    'install_requires':['nose'],
    'packages':['NAME'],
    'scripts':[],
    'name':'projectname'
}

setup(**config)