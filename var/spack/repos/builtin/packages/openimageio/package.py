# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
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

    version('2.3.1.1-dev', sha256='5cd2ef13ac7af65fd0e6a855da9153ca1e32ed44f9ba093ace1ccc2006772378')
    version('2.1.3-dev',   sha256='3d497c4d4eec901115d9d8dc308f91bbd8e63ffe6746a8960b06376afa96d126')
    version('2.1.2-dev',   sha256='f3dc1e1092b5ade130448a5064c3851ecbb6f36100254a2bd4a1eb06b34d2f04')
    version('2.0.10',      sha256='b9c4cb3754cfcf2b03707331c23d5b799a185deccbbc7b8768e0d4e10a535375')
    version('2.0.9',       sha256='0cc7f8db831482ada4f7c7f97859eb4db6b0fc3626100f94a89053da1e1a8615')
    version('1.8.15',      sha256='4d5b4ed3f2daaed69989f53c0f9364dd87c82dc0a09807b5b6e9008e2426e86f')

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
