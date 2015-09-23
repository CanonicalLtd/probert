#!/usr/bin/env python3
# -*- mode: python; -*-
#
# Copyright 2015 Canonical, Ltd.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This package is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""
probert
=========
Hardware probing tool
"""

from setuptools import setup, find_packages

import os
import sys

import probert

if sys.argv[-1] == 'clean':
    print("Cleaning up ...")
    os.system('rm -rf probert.egg-info build dist')
    sys.exit()

setup(name='probert',
      version=probert.__version__,
      description="Hardware probin tool", 
      long_description=__doc__,
      author='Canonical Engineering',
      author_email='ubuntu-dev@lists.ubuntu.com',
      url='https://github.com/CanonicalLtd/probert',
      license="AGPLv3+",
      scripts=['bin/probert'],
      packages=find_packages(),
      include_package_data=True,
)
