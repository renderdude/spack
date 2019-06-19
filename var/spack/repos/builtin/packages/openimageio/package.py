# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import platform

class Openimageio(CMakePackage):
    """OpenImageIO is a library for reading and writing images, and a bunch of
       related classes, utilities, and applications."""

    homepage = "http://www.openimageio.org"
    url      = "https://github.com/OpenImageIO/oiio/archive/Release-1.8.15.tar.gz"

    version('2.1.1-dev', sha256='339fb61e4a2b20f9e3d1facfb6a66e74163a718f9c1684ee33cb7c3b0cb0b55a')
    version('2.1.0-dev', sha256='4062181be521faca57bf95915ca4c6829773a1128cb341ac95d9db1d47018343')
    version('2.0.8',     sha256='3c4794b0e8674728389363de291bada25ff86b4a6f5582380ed2def1ca2e07ae')
    version('2.0.7',     sha256='3abe7e09c9d4e17e357c31c3cb856aea1fa7f79ab24f1fbe0bd46fd8fbd8c769')
    version('1.8.15', sha256='4d5b4ed3f2daaed69989f53c0f9364dd87c82dc0a09807b5b6e9008e2426e86f')

    # Core dependencies
    depends_on('cmake@3.2.2:', type='build')
    depends_on('boost@1.53:1.68', when='@:1.9', type=('build', 'link'))
    depends_on('boost@1.53:1.70', when='@2:', type=('build', 'link'))
    depends_on('libtiff@4.0:', type=('build', 'link'))
    depends_on('openexr@2.3:', type=('build', 'link'))
    depends_on('libpng@1.6:', type=('build', 'link'))

    # Optional dependencies
    variant('ffmpeg', default=False, description="Support video frames")
    depends_on('ffmpeg', when='+ffmpeg')

    variant('jpeg2k', default=False, description="Support for JPEG2000 format")
    depends_on('openjpeg', when='+jpeg2k')

    variant('python', default=False, description="Build python bindings")
    extends('python', when='+python')
    depends_on('py-numpy', when='+python', type=('build', 'run'))
    depends_on('py-pybind11', when='+python', type=('build', 'run'))

    variant('qt', default=False, description="Build qt viewer")
    depends_on('qt@5.6.0:+opengl', when='+qt')

    def cmake_args(self):
        args = ["-DUSE_FFMPEG={0}".format(
            'ON' if '+ffmpeg' in self.spec else 'OFF')]
        args += ["-DUSE_OPENJPEG={0}".format(
            'ON' if '+jpeg2k' in self.spec else 'OFF')]
        args += ["-DUSE_PYTHON={0}".format(
            'ON' if '+python' in self.spec else 'OFF')]
        args += ["-DUSE_QT={0}".format('ON' if '+qt' in self.spec else 'OFF')]

        mac_ver = tuple(platform.mac_ver()[0].split('.')[:2])
        if tuple(map(int, mac_ver)) >= (10, 13):
            args.extend(['-DCMAKE_CXX_FLAGS=-DGL_SILENCE_DEPRECATION'])
            
        return args
