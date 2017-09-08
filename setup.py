from setuptools import setup

setup(name='object_explorer',
      version='0.1',
      description="Standalone version of Spyder's variable explorer",
      license='MIT',
      packages=['object_explorer', 'object_explorer.widgets', 'object_explorer.utilities'],
      zip_safe=False)
