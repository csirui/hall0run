#!/usr/bin/env python
# -*- coding:utf-8 -*-


import os
import sys


def main():
    sys.path.append(os.path.abspath('bin'))
    os.environ['PATH_LOG'] = os.path.abspath('../logs')
    os.environ['PATH_WEBROOT'] = os.path.abspath('../webroot')
    try:
        exec 'import tyframework.server'
        exec 'tyframework.server.main()'
    finally:
        pass


if __name__ == "__main__":
    main()
