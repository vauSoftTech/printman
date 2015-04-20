#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""

    Copyright    : 2015 April. A. R. Bhatt.
    Organization : VAU SoftTech
    Project      : PrintMan - Columnar ASCII Printing Helper Class
    Script Name  : header-template.py
    License      : GNU General Public License v3.0


    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""

import sys
import getopt


class PrintMan:
    def __init__(self, title, subtitle):
        super().__init__()
        self.title = title
        self.subtitle = subtitle
        self.total_lines = 72
        self.total_columns = 80
        self.header_sep = "="
        self.row_sep = "-"
        self.col_sep = "|"
        self.columns = []
        self.current_line_no = 0
        return

    def clear_columns(self):
        self.columns = []
        return

    def add_column_specs(self, column_name, data_type="s", width=10, align="<"):
        self.columns.append([column_name, data_type, width, align])
        return

    def print_titles(self):
        x = self.title.strip().upper().center(self.total_columns-4)
        x = self.col_sep + " {} ".format(x) + self.col_sep
        print(x)
        x = self.subtitle.strip().lower().center(self.total_columns-4)
        x = self.col_sep + " {} ".format(x) + self.col_sep
        print(x)
        self.current_line_no = 2
        return

    def print_headers(self):
        x = "|" + (self.header_sep * (self.total_columns-2)) + "|"
        print(x)

        this_row = []
        for column in self.columns:
            col_nm = column[0]
            col_type = column[1]
            col_w = column[2]
            col_a = column[3]
            y = "{!s:{}{}s}".format(col_nm, col_a, col_w)
            this_row.append(y)

        x = "| " + " | ".join(this_row).ljust(self.total_columns-4) + " |"
        print(x)

        x = "|" + (self.header_sep * (self.total_columns-2)) + "|"
        print(x)

        self.current_line_no += 3
        return

    def print_footers(self):
        x = "|" + (self.header_sep * (self.total_columns-2)) + "|"
        print(x)
        x = "Printed using PrintMan by VAU SoftTech.\f"
        print(x)
        self.current_line_no += 2
        return

    def print_data(self, data, print_row_sep=False):
        lines_required = 2 if print_row_sep else 1
        lines_available = self.total_lines - self.current_line_no

        if lines_available < lines_required:
            self.print_footers()
            self.current_line_no = 0
            self.print_headers()

        row_to_print = []
        for i, column in enumerate(data):
            align_specs = self.columns[i][3]
            width_specs = self.columns[i][2]
            a = "{!s:{}{}s}".format(column, align_specs, width_specs)
            row_to_print.append(a)

        x = "| " + " | ".join(row_to_print).ljust(self.total_columns-4) + " |"
        print(x)
        self.current_line_no += 1

        if print_row_sep:
            row_to_print = []
            for i, column in enumerate(data):
                align_specs = self.columns[i][3]
                width_specs = self.columns[i][2]
                a = "{!s:{}{}s}".format("".ljust(int(float(width_specs)), "-"), align_specs, width_specs)
                row_to_print.append(a)
            x = "| " + " + ".join(row_to_print).ljust(self.total_columns-4, "-") + " |"
            print(x)
            self.current_line_no += 1

        return


def test():
    p = PrintMan("Title", "Sub Title")
    p.add_column_specs( "Col 1", "d", "5", ">")
    p.add_column_specs("Col 2", "s", "10", "<")
    p.add_column_specs("Col 3", "s", "19", "^")
    p.add_column_specs("col 4", "s", "11", ">")
    p.add_column_specs("col 5", "s", "11", ">")

    p.print_titles()
    p.print_headers()

    data = ("1", "abcd", "lmnop", "xyz", 12345)
    p.print_data(data, True)
    data = ("2", "abcd", "lmnop", "xyz", 12345.55)
    p.print_data(data, True)
    data = ("3", "abcd", "", "", 5)
    p.print_data(data, False)

    p.print_footers()
    return


def main():
    if (len(sys.argv) >= 2) and (sys.argv[1] == "--test"):
        test()
    else:
        print("Nothing to see by running this script like this!")
    return


if __name__ == '__main__':
    main()
