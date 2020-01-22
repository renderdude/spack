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
    """OpenVDB is an Academy Award-winning open-source C++ library comprising 
       a novel hierarchical data structure and a suite of tools for the efficient 
       storage and manipulation of sparse volumetric data discretized on 
       three-dimensional grids."""

    homepage = "https://www.openvdb.org"
    url      = "https://github.com/AcademySoftwareFoundation/openvdb/archive/v6.0.0.tar.gz"

    version('7.0.0', sha256='97bc8ae35ef7ccbf49a4e25cb73e8c2eccae6b235bac86f2150707efcd1e910d')
    version('6.2.1', sha256='d4dd17ad571d4dd048f010e6f4b7657391960ed73523ed1716a17e7cf1806f71')
    version('6.2.0', sha256='a2069255b2408b56900d8d4552a9804df7974aecbdd16aad3223d22088c72a43')
    version('6.1.0', sha256='d8803214c245cf0ca14a2c30cd215b183147c03c888c59fc642f213f98b4d68f')
    version('6.0.0', sha256='dbdf3048336444c402e5d3727c9bfb2e84454b8d0fd468ba92a8c7225e24b7b4')
    version('5.2.0', sha256='86b3bc51002bc25ae8d69991228228c79b040cb1a5803d87543b407645f6ab20')
    version('5.1.0', sha256='eb5a8011732bcdeb115de9a38f640ee376bcb85b54e060d3b1ab08f9dc92f40b')
    version('5.0.0', sha256='1d39b711949360e0dba0895af9599d0606ca590f6de2d7c3a6251211fcc00348')
    version('4.0.2', sha256='7d995976cf124136b874d006496c37589f32de1b877ee7ccce626710823e8dbb')

    variant('python', default=False, description="Build python bindings")
    extends('python', when='+python')
    depends_on('py-numpy', when='+python', type=('build', 'run'))
    #patch('boost_numpy.patch', when='+python')

    depends_on('boost', when='~python')
    depends_on('boost+python+numpy', when='+python')
    depends_on('intel-tbb')
    depends_on('ilmbase')
    depends_on('openexr')
    depends_on('c-blosc')
    depends_on('cppunit')
    depends_on('glfw')
    depends_on('pkg-config', type='build')

    def cmake_args(self):
        args = ['-DBLOSC_LOCATION=%s' % self.spec['c-blosc'].prefix]
        args.extend(['-DTBB_ROOT=%s' % self.spec['intel-tbb'].prefix])
        args.extend(['-DILMBASE_LOCATION=%s' % self.spec['ilmbase'].prefix])
        args.extend(['-DOPENEXR_LOCATION=%s' % self.spec['openexr'].prefix])
        args.extend(['-DOpenexr_ILMIMF_LIBRARY=%s/lib/libIlmImf.dylib' % self.spec['openexr'].prefix])
        args.extend(['-DCPPUNIT_LOCATION=%s' % self.spec['cppunit'].prefix])
        args.extend(['-DUSE_GLFW3=ON'])
        args.extend(['-DGLFW3_USE_STATIC_LIBS=ON'])
        args.extend(['-DGLFW3_LOCATION=%s' % self.spec['glfw'].prefix])
        args.extend(['-DCMAKE_CXX_FLAGS=-fPIC -std=c++11'])
        args.extend(['-DOPENVDB_BUILD_UNITTESTS:BOOL=OFF'])
        args += ["-DOPENVDB_BUILD_PYTHON_MODULE:BOOL={0}".format(
            'ON' if '+python' in self.spec else 'OFF')]
        args += ["-DUSE_NUMPY={0}".format(
            'ON' if '+python' in self.spec else 'OFF')]
        return args
