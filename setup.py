#!/usr/bin/env python3
import os
from pathlib import Path
from setuptools import setup, find_packages
from dac_picker.version import VERSION

PACKAGE_DIR = Path(os.path.join(os.path.dirname(__file__), 'dac_picker'))

if __name__ == '__main__':
    setup(
        name='dac_picker',
        version=VERSION,
        packages=find_packages(),
        include_package_data=True,
        install_requires=['setuptools', 'setuptools-git', 'Pillow'],
        license='gpl-3.0',
        url='https://github.com/ellysh/dota-auto-chess-picker',
        author='Ilya Shpigor',
        author_email='petrsum@gmail.com',
        description='Set of utilities for planning your strategy in Dota Auto Chess.',
        long_description=open("README.md").read(),
        long_description_content_type='text/markdown',
        download_url = 'https://github.com/ellysh/dota-auto-chess-picker/archive/master.zip',
        keywords=['dota2', 'counter-pick'],
        entry_points={
            'console_scripts': [
                'dac-combo-picker=dac_picker.combo_picker:main',
                'dac-items-picker=dac_picker.items_picker:main',
                'dac-pieces-picker=dac_picker.pieces_picker:main',
            ],
        },
        classifiers=[
            'Development Status :: 4 - Beta',

            'Intended Audience :: End Users/Desktop',
            'Topic :: Games/Entertainment :: Real Time Strategy',

            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
          ],

    )
