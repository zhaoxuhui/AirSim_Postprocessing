# coding=utf-8
import os
import sys

if __name__ == '__main__':
    file_path = sys.argv[1]
    cur_dir = file_path[:file_path.rfind(os.path.sep)] + os.path.sep

    fout = open(cur_dir + "/groundtruth_TUM.txt", "w")

    fin = open(file_path, "r")
    line = fin.readline().strip()
    line = fin.readline().strip()
    while (line):
        parts = line.split("\t")
        timestamp = float(parts[1]) / 1000.0
        pos_x = parts[2]
        pos_y = parts[3]
        pos_z = parts[4]

        quat_w = parts[5]
        quat_x = parts[6]
        quat_y = parts[7]
        quat_z = parts[8]

        fout.write(str(timestamp) + " " +
                   pos_x + " " +
                   pos_y + " " +
                   pos_z + " " +
                   quat_x + " " +
                   quat_y + " " +
                   quat_z + " " +
                   quat_w + "\n")

        line = fin.readline().strip()

    fin.close()
    fout.close()
