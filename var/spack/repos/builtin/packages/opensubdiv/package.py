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
#     spack install opensubdiv
#
# You can edit this file again by typing:
#
#     spack edit opensubdiv
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Opensubdiv(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "https://github.com/PixarAnimationStudios/OpenSubdiv/archive/v3_3_3.tar.gz"
    git      = "https://github.com/PixarAnimationStudios/OpenSubdiv.git"

    version('develop',   branch='dev')
    version('3_3_3',     sha256='2dc81b3a085e692cca3166ac88751e4674a9ddf5b5d7935adf677bb2bd3f2d2f')
    version('3_3_2',     sha256='d11a0f21bcf21156f9071ea49050ec6675b77776b9dba33b8e30b072d82a8b05')
    version('3_3_1',     sha256='a7a518e63c0526772b24b4598bfc879cb5ed84557e69512b27141aa54a13e51b')
    version('3_3_0',     sha256='93d364340518515129fe199c80c4030f666ff71414d9c543e1526f14b5ffc8d0')

    depends_on('intel-tbb')
    depends_on('ptex@develop')
    depends_on('glew')
    depends_on('glfw')

    def cmake_args(self):
        args = ['-DNO_CUDA=1']
        args.extend(['-DTBB_LOCATION=%s' % self.spec['intel-tbb'].prefix])
        args.extend(['-DPTEX_LOCATION=%s' % self.spec['ptex'].prefix])
        args.extend(['-DGLFW_LOCATION=%s' % self.spec['glfw'].prefix])
        if 'darwin' in self.spec.architecture:
            args.extend(['-DNO_METAL=0'])
        else:
            args.extend(['-DGLEW_LOCATION=%s' % self.spec['glew'].prefix])

        return args
