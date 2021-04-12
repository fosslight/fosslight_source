#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2020 LG Electronics Inc.
# SPDX-License-Identifier: Apache-2.0

import getopt
import os
import sys
import json
import platform
from datetime import datetime
import logging

from ._write_oss_report_src import write_result_to_csv, write_result_to_excel
from ._parsing_scancode_file_item import parsing_file_item
from ._settings import init_log

logger = logging.getLogger(__name__)


def convert_json_to_excel(scancode_json, excel_name, csv_name):
    file_list = []
    try:
        sheet_list = {}
        if os.path.isfile(scancode_json):
            file_list = get_detected_licenses_from_scancode(
                scancode_json)
            if len(file_list) > 0:
                sheet_list["SRC"] = file_list
        elif os.path.isdir(scancode_json):
            for root, dirs, files in os.walk(scancode_json):
                for file in files:
                    if file.endswith(".json"):
                        try:
                            result_file = os.path.join(root, file)
                            file_list = get_detected_licenses_from_scancode(
                                result_file)
                            if len(file_list) > 0:
                                file_name = os.path.basename(file)
                                sheet_list["SRC_" + file_name] = file_list
                        except Exception as ex:
                            pass

        if len(sheet_list) > 0:
            write_result_to_excel(excel_name, sheet_list)
            if platform.system() != "Windows":
                write_result_to_csv(csv_name, sheet_list)
        else:
            logger.warn("There is no item to print in OSS-Report.")

    except Exception as ex:
        logger.warn(str(ex))

    return file_list


def get_detected_licenses_from_scancode(scancode_json_file):
    file_list = []
    try:
        logger.warn("Start parsing " + scancode_json_file)
        with open(scancode_json_file, "r") as st_json:
            st_python = json.load(st_json)
            rc, file_list = parsing_file_item(st_python["files"])
    except Exception as error:
        logger.warn("Error Parsing - "+str(error))
    logger.warn("|---Number of files detected: " + str(len(file_list)))
    return file_list


def print_help_msg():
    print("* Required :\n -p path_of_scancode_json_result")
    sys.exit()


def main():
    argv = sys.argv[1:]
    path_to_find_bin = os.getcwd()
    start_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    output_file_name = ""

    try:
        opts, args = getopt.getopt(argv, 'hp:o:')
        for opt, arg in opts:
            if opt == "-h":
                print_help_msg()
            elif opt == "-p":
                path_to_find_bin = arg
            elif opt == "-o":
                output_file_name = arg
    except Exception as error:
        pass

    if output_file_name == "":
        output_dir = os.getcwd()
        oss_report_name = "OSS-Report_" + start_time
        csv_file_name = "result_" + start_time
    else:
        oss_report_name = output_file_name
        csv_file_name = output_file_name
        output_dir = os.path.dirname(os.path.abspath(output_file_name))

    init_log(start_time, output_dir)

    convert_json_to_excel(path_to_find_bin,
                          oss_report_name + ".xlsx", csv_file_name + ".csv")


if __name__ == '__main__':
    main()