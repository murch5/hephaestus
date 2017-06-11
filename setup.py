from distutils.core import setup
from plotmanager.__init__ import __version__ as version

setup(
    name='plotmanager',
    version=version,
    packages=['plotmanager','plotmanager.plottype'],
    url='',
    license='None',
    author='Ryan',
    author_email='',
    description='Plot Manager Wrapper for Matplotlib/seaborn',
    include_package_data=True
)
