#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires
import os

base = python_requires("boost_base/1.68.0@bincrafters/stable")

class BoostCallable_TraitsConan(base.BoostBaseConan):
    name = "boost_callable_traits"
    version = "1.68.0"
    url = "https://github.com/bincrafters/conan-boost_callable_traits"
    lib_short_names = ["callable_traits"]
    header_only_libs = ["callable_traits"]
