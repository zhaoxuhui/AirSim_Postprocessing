# coding=utf-8
import os
import sys

if __name__ == '__main__':
    file_path = sys.argv[1]
    cur_dir = file_path[:file_path.rfind(os.path.sep)] + os.path.sep
    print(cur_dir)

    fin = open(file_path, "r")
    line = fin.readline().strip()
    line = fin.readline().strip()
    while (line):
        parts = line.split("\t")
        timestamp = parts[1]
        names = parts[-1]
        name_list = names.split(";")
        for i in range(len(name_list)):
            name = name_list[i]
            old_name_path = cur_dir + os.path.sep + "images" + os.path.sep + name

            name_prefix = name[:name.rfind("_") + 1]
            new_name_path = cur_dir + os.path.sep + "images" + os.path.sep + name_prefix + timestamp + ".png"

            name_path = file_path.rfind(os.path.sep)
            print(timestamp)

            os.rename(old_name_path, new_name_path)

        line = fin.readline().strip()
