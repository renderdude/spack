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
#     spack install openvdb
#
# You can edit this file again by typing:
#
#     spack edit openvdb
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Openvdb(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.openvdb.org"
    url      = "https://github.com/AcademySoftwareFoundation/openvdb/archive/v6.0.0.tar.gz"

    version('6.0.0', sha256='dbdf3048336444c402e5d3727c9bfb2e84454b8d0fd468ba92a8c7225e24b7b4')
    version('5.2.0', sha256='86b3bc51002bc25ae8d69991228228c79b040cb1a5803d87543b407645f6ab20')
    version('5.1.0', sha256='eb5a8011732bcdeb115de9a38f640ee376bcb85b54e060d3b1ab08f9dc92f40b')
    version('5.0.0', sha256='1d39b711949360e0dba0895af9599d0606ca590f6de2d7c3a6251211fcc00348')
    version('4.0.2', sha256='7d995976cf124136b874d006496c37589f32de1b877ee7ccce626710823e8dbb')

    # FIXME: Add dependencies if required.
    depends_on('boost+python')
    depends_on('intel-tbb')
    depends_on('ilmbase')
    depends_on('openexr')
    depends_on('c-blosc')
    depends_on('cppunit')
    depends_on('glfw')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = ['-DBLOSC_LOCATION=%s' % self.spec['c-blosc'].prefix]
        args.extend(['-DTBB_LOCATION=%s' % self.spec['intel-tbb'].prefix])
        args.extend(['-DILMBASE_LOCATION=%s' % self.spec['ilmbase'].prefix])
        args.extend(['-DOPENEXR_LOCATION=%s' % self.spec['openexr'].prefix])
        args.extend(['-DOpenexr_ILMIMF_LIBRARY=%s/lib/libIlmImf.dylib' % self.spec['openexr'].prefix])
        args.extend(['-DCPPUNIT_LOCATION=%s' % self.spec['cppunit'].prefix])
        args.extend(['-DUSE_GLFW3=ON'])
        args.extend(['-DGLFW3_USE_STATIC_LIBS=ON'])
        args.extend(['-DGLFW3_LOCATION=%s' % self.spec['glfw'].prefix])
        args.extend(['-DCMAKE_CXX_FLAGS=-fPIC -std=c++11'])
        args.extend(['-DOPENVDB_BUILD_UNITTESTS:BOOL=OFF'])
        args.extend(['-DOPENVDB_BUILD_PYTHON_MODULE:BOOL=OFF'])
        return args
