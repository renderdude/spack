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
#     spack install ospray
#
# You can edit this file again by typing:
#
#     spack edit ospray
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Ospray(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "https://github.com/ospray/OSPRay/archive/v1.8.5.tar.gz"

    version('1.8.5', sha256='6d85e103280aa4c8d0032a2cc3082f08a6021a79d22cf4a8e38b09f152f35f53')

    variant('mpi', default=False, description="Build OSPRay with MPI module")
    variant('oiio', default=False, description="Build OSPRay with OpenImageIO")

    depends_on('embree')
    depends_on('ispc')
    depends_on('mpi', when='+mpi')
    depends_on('openimageio', when='+oiio')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        cmake_args = []

        if '+mpi' in self.spec:
            cmake_args.append('-DOSPRAY_MODULE_MPI=ON')

        if '+oiio' in self.spec:
            cmake_args.append('-DOSPRAY_SG_OPENIMAGEIO=ON')

        return cmake_args
