#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/7 19:33
# @Author  : ch4r0n
# @Site    : 
# @File    : miaodump_client.py
# @Software: PyCharm

import argparse
from miaodump import miaodump_converter


def main():
    opts = argparse.ArgumentParser(description="miaodump client")
    opts.add_argument('-p', '--path', default=None,
                      help="Dir to using the miaodump")
    opts.add_argument('-e', '--exclude', help="Exclude the SDK from file")
    opts.add_argument('-ed', '--exclude-default', default=False, nargs="?", const=True, help="using default value to "
                                                                                             "filter the file")
    opts.add_argument('--arch', default=False, nargs="?", const=True, help="choose a specific architecture from a "
                                                                           "universal binary")
    opts.add_argument('-o', '--output', help="output the header files <dir>")

    args = opts.parse_args()
    print(args)

    try:
        mdconv = miaodump_converter.MiaodumpConverter(
            file_path=args.path,
            exclude=args.exclude,
            default_exclude=args.exclude_default,
            arch=args.arch,
            output=args.output
        )
    except Exception, e:
        print(e)
        pass


if __name__ == '__main__':
    main()
