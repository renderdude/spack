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
#     spack install ptex
#
# You can edit this file again by typing:
#
#     spack edit ptex
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Ptex(MakefilePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "http://ptex.us/com"
    url      = "https://github.com/wdas/ptex/archive/v2.3.2.tar.gz"
    git      = "https://github.com/wdas/ptex.git"

    # FIXME: Add proper versions and checksums here.
    version('develop', branch='main')
    version('2.3.2',   sha256='30aeb85b965ca542a8945b75285cd67d8e207d23dbb57fcfeaab587bb443402b')
    version('2.3.1',   sha256='126ab1f55f1e6a59e5b70860924ddda0254d3202b2fbddd4852c3f5c0da1cd56')
    version('2.3.0.1', sha256='baae4307983231fbe31c7de5c59e08e813de12924c0c89f41bea05d6000d4cf5')
    version('2.3.0',   sha256='285947961ac7da2a7a15955259e271a50e485793e1d596d9f254c847301eda92')
    version('2.2.1',   sha256='1a714bb4a972c16b1f16602d9ba7c57ee6f3819c64905979e4769c158b636318')

    depends_on('cmake', type='build')
    depends_on('pkg-config', type='build')
    depends_on('zlib')

    def edit(self, spec, prefix):
        env['NO_NINJA'] = "1"

    def build(self, spec, prefix):
        make('prefix="' + prefix + '"')

