#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires
import os

base = python_requires("boost_base/2.0.0@bincrafters/testing")


class BoostCallable_TraitsConan(base.BoostBaseConan):
    name = "boost_callable_traits"
    version = "1.70.0"
