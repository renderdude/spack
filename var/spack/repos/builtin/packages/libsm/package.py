# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import sys
from spack import *


class Libsm(AutotoolsPackage, XorgPackage):
    """libSM - X Session Management Library."""

    homepage = "http://cgit.freedesktop.org/xorg/lib/libSM"
    xorg_mirror_path = "lib/libSM-1.2.2.tar.gz"

    version('1.2.3', sha256='1e92408417cb6c6c477a8a6104291001a40b3bb56a4a60608fdd9cd2c5a0f320')
    version('1.2.2', sha256='14bb7c669ce2b8ff712fbdbf48120e3742a77edcd5e025d6b3325ed30cf120f4')

    depends_on('libice@1.0.5:')

    depends_on('xproto', type='build')
    depends_on('xtrans', type='build')
    depends_on('pkgconfig', type='build')
    depends_on('util-macros', type='build')
    if sys.platform != 'darwin':
        # On macOS systems, Spack's libuuid conflicts with the system-installed
        # version and breaks anything linked against Cocoa/Carbon. Since the
        # system-provided version is sufficient to build Python's UUID support,
        # the easy solution is to only depend on Spack's libuuid when *not* on
        # a Mac.
        depends_on('libuuid')
