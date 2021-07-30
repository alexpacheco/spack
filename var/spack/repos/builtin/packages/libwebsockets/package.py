# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Libwebsockets(CMakePackage):
    """C library for lightweight websocket clients and servers."""

    homepage = "https://github.com/warmcat/libwebsockets"
    url      = "https://github.com/warmcat/libwebsockets/archive/v2.1.0.tar.gz"
    maintainers = ['ax3l']

    version('4.1.6', sha256='402e9a8df553c9cd2aff5d7a9758e9e5285bf3070c82539082864633db3deb83')
    version('4.1.5', sha256='682bbc60528a63b462a245c3b0497eb9892e49ad144639d31b1f594ca43cb1d6')
    version('4.1.4', sha256='00da77b4b89db3e0b1a2778f756f08d55d7f6b1632e18d981fc399c412866147')
    version('4.1.3', sha256='228a0fce3a382b98f3ae140620711c1d855f4dd80ec06f4d08a3c4e093ac3fa8')
    version('4.1.2', sha256='f15a7189c5fe6109d260615dec8a0c6dfc962ed5931fb6f0fddd72fbe49f02b0')
    version('4.1.1', sha256='35bda295e031284fa7a5e0bd3eef23ee1477846759492aec62cc1102754b3515')
    version('2.2.1', sha256='e7f9eaef258e003c9ada0803a9a5636757a5bc0a58927858834fb38a87d18ad2')
    version('2.1.1', sha256='96183cbdfcd6e6a3d9465e854a924b7bfde6c8c6d3384d6159ad797c2e823b4d')
    version('2.1.0', sha256='bcc96aaa609daae4d3f7ab1ee480126709ef4f6a8bf9c85de40aae48e38cce66')
    version('2.0.3', sha256='cf0e91b564c879ab98844385c98e7c9e298cbb969dbc251a3f18a47feb94342c')
    version('1.7.9', sha256='86a5105881ea2cb206f8795483d294e9509055decf60436bcc1e746262416438')

    depends_on('cmake', type='build')
    depends_on('gmake', type='build')
    depends_on('zlib', type=('build', 'link'))
    depends_on('openssl', type=('build', 'link'))

    depends_on('mbedtls', type=('build', 'link'))
    depends_on('libuv', type=('build', 'link'))

    def cmake_args(self):
        args = ['-DLWS_WITH_LIBUV=ON']
        return args


