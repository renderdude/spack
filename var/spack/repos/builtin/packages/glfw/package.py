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
#     spack install glfw
#
# You can edit this file again by typing:
#
#     spack edit glfw
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Glfw(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "https://github.com/glfw/glfw/releases/download/3.2.1/glfw-3.2.1.zip"

    version('3.2.1',           sha256='b7d55e13e07095119e7d5f6792586dd0849c9fcdd867d49a4a5ac31f982f7326')
    version('3.2',             sha256='d9983a129732bd400869dd26c9ef2ed253b1da0cfb79585ab7af63a175d0f652')

    variant('shared', default=True, description="Build as shared library")

    # FIXME: Add dependencies if required.
    depends_on('opengl')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        cmake_args = []
        if '+shared' in self.spec:
            cmake_args.append('-DBUILD_SHARED_LIBS=ON')
        return cmake_args
