# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import os.path


class Snpeff(Package):
#class Snpeff(Package, SourceforgePackage):
    """SnpEff is a variant annotation and effect prediction tool. It
    annotates and predicts the effects of genetic variants (such as
    amino acid changes)."""

    homepage = "https://snpeff.blob.core.windows.net"
    url = 'https://snpeff.blob.core.windows.net/versions/snpEff_latest_core.zip'
#    homepage = "http://snpeff.sourceforge.net/"
    sourceforge_mirror_path = "snpeff/snpEff_latest_core.zip"

    version('5.0', sha256='85d907b5dd9e9008a0cf245956e3c9077a31e45f21a1b580d9b98a53fd8dcb9d')
#    version('5.0', sha256='e28f1e6db30808e29cb835958d3971959655d77f543ade094fca9cac5a024cbc')
    version('2017-11-24', sha256='d55a7389a78312947c1e7dadf5e6897b42d3c6e942e7c1b8ec68bb35d2ae2244')

    depends_on('openjdk', type=('build', 'run'))

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install_tree('.', prefix.bin)
#        install_tree('snpEff', prefix.bin)

        # Set up a helper script to call java on the jar files,
        # explicitly codes the path for java and the jar files.
        scripts = ['snpEff', 'SnpSift']

        for script in scripts:
            script_sh = join_path(os.path.dirname(__file__), script + ".sh")
            script_path = join_path(prefix.bin, script)
            install(script_sh, script_path)
            set_executable(script_path)

            # Munge the helper script to explicitly point to java and the
            # jar file.
            java = self.spec['java'].prefix.bin.java
            kwargs = {'backup': False}
            filter_file('^java', java, script_path, **kwargs)
            filter_file(script + '.jar',
                        join_path(prefix.bin, script + '.jar'),
                        script_path, **kwargs)
