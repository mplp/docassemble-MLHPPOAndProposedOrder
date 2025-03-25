import os
import sys
from setuptools import setup, find_namespace_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')

def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.MLHPPOAndProposedOrder',
      version='0.0.16',
      description=('A Personal Protection Order for use in Michigan Courts'),
      long_description='# docassemble.MLHMotionRegardingChangeOfDomicile\r\n\r\nA motion regarding change of domicile in Michigan\r\n\r\n## Authors:\r\n\r\n* Rami Lorca',
      long_description_content_type='text/markdown',
      author='Rami Lorca',
      author_email='rami@lemmalegal.com',
      license='The MIT License (MIT)',
      url='https://michiganlegalhelp.org/resources/family/do-it-yourself-personal-protection-order',
      packages=find_namespace_packages(),
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/MLHPPOAndProposedOrder/', package='docassemble.MLHPPOAndProposedOrder'),
     )

