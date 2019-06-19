# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import os


class PyPyside2(PythonPackage):
    """Python bindings for Qt."""
    homepage = "https://download.qt.io/official_releases/QtForPython/pyside2"
    url      = "https://download.qt.io/official_releases/QtForPython/pyside2/PySide2-5.12.3-src/pyside-setup-everywhere-src-5.12.3.tar.xz"
    list_url = 'http://download.qt.io/official_releases/QtForPython/pyside2/'
    list_depth = 3

    version('5.12.3', sha256='4f7aab7d4bbaf1b3573cc989d704e87b0de55cce656ae5e23418a88baa4c6842')
    version('5.12.2', sha256='ed974c0592019cbbcd4e4db3b18cf4f2af2c399cc1650e5c526be3efd7562bc1')
    version('5.11.2', sha256='18f572f1f832e476083d30fccabab167450f2a8cbe5cd9c6e6e4fa078ccb86c2')
    version('5.11.1', sha256='9cbc3cbb03c6c1ddba8de7a651c84b269f87ebd4a0991a1f9acc8b2d0ccdfb83')
    depends_on('cmake', type='build')

    depends_on('py-setuptools', type='build')
    depends_on('py-sphinx', type=('build', 'run'))
    depends_on('qt')
    depends_on('llvm')

    def install(self, spec, prefix):
        """Install everything from build directory."""
        install_args = self.install_args(spec, prefix)
        # Combine all phases into a single setup.py command,
        # otherwise extensions are rebuilt without rpath by install phase:
        self.setup_py('build', 'install', *install_args)