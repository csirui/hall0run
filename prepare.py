#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os


def main():
    # sh ./source/tyframework/shell2/game.sh -m ./source/tygame-sdk/configure/server/test_127001.json -noback -a start
    if not os.path.islink('source'):
        if os.path.exists('source'):
            print("请先删除source目录")
            exit(1)
    else:
        if os.path.realpath('source') == os.path.realpath('../hall0/source'):
            pass
        else:
            os.remove('source')

    if not os.path.exists('source'):
        os.symlink('../hall0/source', 'source')
    import sys
    sys.path.append(os.path.abspath('source/tyframework/shell2'))
    try:
        exec "import _pygamecontrol_._main_"
        exec "_pygamecontrol_._main_.main()"
        os.symlink('../script/control.json', 'bin/control.json')
    finally:
        # os.remove('source')
        pass


if __name__ == "__main__":
    main()
