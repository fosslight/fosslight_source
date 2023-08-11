#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2023 LG Electronics Inc.
# SPDX-License-Identifier: Apache-2.0

import os
import logging
import re
import fosslight_util.constant as constant
import mmap

logger = logging.getLogger(constant.LOGGER_NAME)


def get_file_list(path_to_scan):
    file_list = []
    for root, dirs, files in os.walk(path_to_scan):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list


def get_spdx_downloads(path_to_scan):
    download_dict = {}
    find_word = re.compile(rb"SPDX-PackageDownloadLocation\s*:\s*(\S+)", re.IGNORECASE)

    file_list = get_file_list(path_to_scan)

    for file in file_list:
        rel_path_file = os.path.relpath(file, path_to_scan)
        # remove the path_to_scan from the file paths
        if os.path.getsize(file) > 0:
            with open(file, "r") as f:
                with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mmap_obj:
                    for word in find_word.findall(mmap_obj):
                        if rel_path_file in download_dict:
                            download_dict[rel_path_file].append(word.decode('utf-8'))
                        else:
                            download_dict[rel_path_file] = [word.decode('utf-8')]
    return download_dict
