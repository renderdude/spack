# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install ispc
#
# You can edit this file again by typing:
#
#     spack edit ispc
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Ispc(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://ispc.github.io/"
    url      = "https://github.com/ispc/ispc/archive/v1.11.0.tar.gz"
    git      = "https://github.com/ispc/ispc.git"

    version('develop', branch='master')
    version('1.12.0', sha256='9ebc29adcdf477659b45155d0f91e61120a12084e42113d0e9f4ce5cfdfbdcab')
    version('1.11.0', sha256='f48ef6e8a1fe5ad4fca691583bf7419f4dce1596e7ed850ff99cc017f8711b2f')
    version('1.10.0', sha256='0aa30e989f8d446b2680c9078d5c5db70634f40b9aa07db387aa35aa08dd0b81')
    version('1.9.2',  sha256='76a14e22f05a52fb0b30142686a6cb144b0415b39be6c9fcd3f17ac23447f0b2')
    version('1.9.1',  sha256='c52910a007f1b0c732dd1cb981e7c22f3b9b575f0b097a49f4e43fc7a3e7e976')
    version('1.9.0',  sha256='b151e50f80754d81302f968c66cc7444c65010c20d1f83382b94c22491bb3971')
    version('1.8.2',  sha256='d17ea68b7192d261a2830d6e00df656a73fbccd08a249433fcaf24a886902a9d')

    depends_on('flex')
    depends_on('bison')
    depends_on('python@2.7:2.8', when='@:1.11.99')
    depends_on('python@3.0:', when='@1.12:')
    depends_on('llvm@8.0.0~lldb~all_targets+enable_dump', when='@:1.12.99')
    depends_on('llvm@develop~lldb~all_targets+enable_dump', when='@develop')

    def cmake_args(self):
        args = ['-DARM_ENABLED:BOOL=OFF']
        return args
