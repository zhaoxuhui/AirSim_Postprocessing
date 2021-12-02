# coding=utf-8
import os
import sys
from HaveFun import common
import shutil

if __name__ == '__main__':
    file_path = sys.argv[1]
    cur_dir = file_path[:file_path.rfind(os.path.sep)] + os.path.sep
    print(cur_dir)

    left_target_dir = cur_dir + "images_left" + os.path.sep
    right_target_dir = cur_dir + "images_right" + os.path.sep
    common.isDirExist(left_target_dir)
    common.isDirExist(right_target_dir)

    fout = open(cur_dir + "/timestamps.txt", "w")

    fin = open(file_path, "r")
    line = fin.readline().strip()
    line = fin.readline().strip()
    while (line):
        parts = line.split("\t")
        timestamp = parts[1]
        names = parts[-1]
        name_list = names.split(";")

        print(timestamp)
        fout.write(timestamp + "\n")
        for i in range(len(name_list)):
            name = name_list[i]
            old_name_path = cur_dir + os.path.sep + "images" + os.path.sep + name

            if name.__contains__("left"):
                new_name_path = left_target_dir + os.path.sep + timestamp + ".png"
            elif name.__contains__("right"):
                new_name_path = right_target_dir + os.path.sep + timestamp + ".png"

            shutil.copy2(old_name_path, new_name_path)

        line = fin.readline().strip()
    fin.close()
    fout.close()
