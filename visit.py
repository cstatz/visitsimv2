# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import subprocess

__author__ = 'Christoph Statz'


def get_include():

    visit_home = None

    try:
        p = subprocess.Popen(['visit', '-env'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except OSError:
        raise OSError("Path to visit executable is not set!")

    out = p.communicate()[0].decode('ascii').split('\n')
    print(out)
    for line in out:
        tmp = line.strip().split('=')
        if tmp[0].startswith("VISITHOME"):
            visit_home = tmp[1].strip()

    visit_include = [ visit_home+"/include", visit_home+"/include/visit/include"]
    return visit_include 

def get_library_dirs():

    visit_home = None

    try:
        p = subprocess.Popen(['visit', '-env'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except OSError:
        raise OSError("Path to visit executable is not set!")

    out = p.communicate()[0].decode('ascii').split('\n')

    for line in out:
        tmp = line.strip().split('=')
        if tmp[0].startswith("VISITHOME"):
            visit_home = tmp[1].strip()

    visit_lib = [ visit_home+"/lib", visit_home+"/libsim/V2/lib"]
    return visit_lib 


if __name__ == '__main__':
    print(get_include())
    print(get_library_dirs())

