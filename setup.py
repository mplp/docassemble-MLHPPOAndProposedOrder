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
      version='1.0.17',
      description=('A Personal Protection Order for use in Michigan Courts'),
      long_description='# docassemble.MLHMotionRegardingChangeOfDomicile\r\n\r\nA motion regarding change of domicile in Michigan\r\n\r\n## Authors:\r\n\r\n* Rami Lorca\r\n\r\n## Changelog:\r\n* 8/11/25  1.0.17 add logs to show when document assembly starts\r\n* 7/23/25  1.0.16 add upload size limit, remove additional pages upload function, fix display of upload table\r\n* 7/8/25   1.0.15 make legally incapacitated adult question more user-friendly and clarify how to edit; require a date on SA path events description; add obscene material language to SA screening question for minors; other minor improvements;\r\n* 6/26/25  1.0.14 allow excluding respondent from multiple other properties; update display title for download bundle; add snapshot of failed email-to-court attempts\r\n* 5/28/25  1.0.13 fix minor instructions language mistake\r\n* 5/27/25  1.0.12 remove option for user not to enter phone number\r\n* 5/6/25   1.0.11 various instruction edits/fixes\r\n* 5/5/25   1.0.10 add ability to edit ages; improve language for emancipation questions; improve domestic petition screening question; improve P-R relationship editing\r\n* 4/23/25  1.0.9 remove references to notarizing proof of service in instructions; other instructions updates\r\n* 4/21/25  1.0.8 exhibit upload improvements: fix deletion bug; for ETC counties, improve exhibit review and reset TOC\r\n* 4/21/25  1.0.7 add missing address unit to contact info sheet; update language on domestic SOF\r\n* 4/18/25  1.0.6 minor formatting and language/instruction updates\r\n* 4/17/25  1.0.5 fix review screen error; enhance email submission process\r\n* 4/14/25  1.0.4 update instructions\r\n* 4/9/25   1.0.3 fix confidential address field issues\r\n* 4/8/25   1.0.2 fix other protected property editing\r\n* 4/8/25   1.0.1 fix respondent DOB on special Wayne form\r\n* 4/7/25   1.0.0 launch',
      long_description_content_type='text/markdown',
      author='Rami Lorca',
      author_email='rami@lemmalegal.com',
      license='MIT',
      url='https://michiganlegalhelp.org/resources/family/do-it-yourself-personal-protection-order',
      packages=find_namespace_packages(),
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/MLHPPOAndProposedOrder/', package='docassemble.MLHPPOAndProposedOrder'),
     )

