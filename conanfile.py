#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class BoostCallable_TraitsConan(ConanFile):
    name = "Boost.Callable_Traits"
    version = "1.66.0"
    commit_id = "0ce9138ce86095eab9c09d171fecb5f72c4457f7"
    url = "https://github.com/bincrafters/conan-boost-poly_collection"
    description = "Please visit http://www.boost.org/doc/libs/1_66.0/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    short_paths = True
    lib_short_names = ["callable_traits"]
    
    def source(self):
        source_url = "https://github.com/boostorg"
        for lib_short_name in self.lib_short_names:
            self.run("git clone --branch=master {0}/{1}.git".format(source_url, lib_short_name))
            with tools.chdir(lib_short_name):
                self.run("git checkout {0}".format(self.commit_id))
    
    # TODO: Switch to this method after 1.66.0 release
    # def source(self):
        # boostorg_github = "https://github.com/boostorg"
        # archive_name = "boost-" + self.version  
        # for lib_short_name in self.lib_short_names:
            # tools.get("{0}/{1}/archive/{2}.tar.gz"
                # .format(boostorg_github, lib_short_name, archive_name))
            # os.rename(lib_short_name + "-" + archive_name, lib_short_name)

    def package(self):
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)		

    def package_id(self):
        self.info.header_only()