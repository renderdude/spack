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
#     spack install usd
#
# You can edit this file again by typing:
#
#     spack edit usd
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

import os
from spack import *


class Usd(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "https://github.com/PixarAnimationStudios/USD/archive/v19.05.tar.gz"
    git      = "https://github.com/PixarAnimationStudios/USD.git"

    version('develop',   branch='dev')
    version('20.05', sha256='622403872f530fe7d9d291dc8a98132c5bc979f64b82b834718d4e26aacfb9fd')
    version('20.02', sha256='b70e2d4e21be24246215d2d2c0c90c66a2627b54e3d450fbbd6193d1284c6734')
    version('19.11', sha256='84f3bb123f7950b277aace096d678c8876737add0ed0b6ccb77cabb4f32dbcb0')
    version('19.07', sha256='e3fdfccdaa18f72563a31bb5c397048910edbddbf62b451fcea8c104fe76a0fd')
    version('19.05', sha256='4ffc67435fc4d6dad4a337a7ec8da5715f225c37ee30354434453072e95dfbac')
    version('19.03', sha256='86a3bd3875e7b0b27de2e120fa8149e398d9adb081771db8d28a3799fff35bbe')
    version('19.01', sha256='27b0263570bbf35f34ed2f09c89c7b8d5996a25fd2694d5aca0664df1ba78839')
    version('18.11', sha256='e94a99cacfa2b67a87ea7b6386cecfdd2ce2d8ec8261b73407744b47a4fa1463')
    version('18.09', sha256='7f5b7905c976cc7a1983ef9dfd8f298366872e1b4d6dcd2f05a2e55f4057da75')

    variant('python', default=True, description='Enable Python binding')
    variant('renderman', default=False, description='Enable Hydra backend for RenderMan')

#    patch('boost_168.patch', when='@:19.11^boost@1.68:')
#    patch('v20.02_boost_168.patch', when='@20.02:^boost@1.68:')

    depends_on('python', when='+python')
    depends_on('intel-tbb')
    depends_on('boost@1.70:')
    depends_on('opensubdiv')
    depends_on('openexr')
    depends_on('openimageio@1.8.15')
    depends_on('ptex@develop')
    depends_on('glew')
    depends_on('py-pyside2')

    def cmake_args(self):
        args = ['-DPXR_BUILD_OPENIMAGEIO_PLUGIN=TRUE']
        args.extend(['-DTBB_ROOT_DIR=%s' % self.spec['intel-tbb'].prefix])
        args.extend(['-DPTEX_LOCATION=%s' % self.spec['ptex'].prefix])
        args.extend(['-DGLEW_LOCATION=%s' % self.spec['glew'].prefix])
        args.extend(['-DOPENEXR_LOCATION=%s' % self.spec['openexr'].prefix])
        args.extend(['-DOPENSUBDIV_LOCATION=%s' % self.spec['opensubdiv'].prefix])
        args.extend(['-DOIIO_LOCATION=%s' % self.spec['openimageio'].prefix])
        args.extend(['-DBOOST_ROOT=%s' % self.spec['boost'].prefix])
        if '+python' in self.spec:
            python_exe = self.spec['python'].command.path
            python_lib = self.spec['python'].libs[0]
            python_include_dir = self.spec['python'].headers.directories[0]
            args.extend([
                '-DPXR_USE_PYTHON_3=ON',
                '-DPYTHON_EXECUTABLE={0}'.format(python_exe),
                '-DPYTHON_LIBRARY={0}'.format(python_lib),
                '-DPYTHON_INCLUDE_DIR={0}'.format(python_include_dir),
            ])
        if '+renderman' in self.spec:
            if 'RMANTREE' in os.environ:
                args.extend(['-DPXR_BUILD_PRMAN_PLUGIN=TRUE'])
                args.extend(['-DRENDERMAN_LOCATION=%s' % os.environ['RMANTREE']])
            else:
                raise InstallError('Must have HOUDINI_ROOT set with +houdini')

        return args
