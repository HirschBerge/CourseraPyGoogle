#!/usr/bin/env python3
import re


def readFile():
    errorTypes = {}
    userInfo = {}
    with open("syslog.log", 'r+') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            status, msg, uname = regexin(line)
            if uname not in userInfo.keys():
                userInfo[uname] = {}
                userInfo[uname]['INFO'] = 0
                userInfo[uname]['ERROR'] = 0
            if status == "ERROR":
                # print(f"Error! {status} User: {uname}")
                if uname in userInfo.keys():
                    userInfo[uname]["ERROR"] += 1
                if msg in errorTypes:
                    errorTypes[msg] += 1
                if msg not in errorTypes:
                    errorTypes[msg] = 1
            if status == "INFO":
                if uname in userInfo.keys():
                    # print(f"Info! {status} User: {uname}")
                    userInfo[uname]["INFO"] += 1

        errorTypes = dict(sorted(errorTypes.items(), key=lambda item: item[1], reverse=True))
        userInfo = dict(sorted(userInfo.items(), key=lambda x: x[0], reverse=False))
        return errorTypes, userInfo


def regexin(line):
    typ = re.search(r"ticky: ([\w+]*):? ([\w' ]*)[\[#\d]*]?]? ?\((.*)\)$", line)
    return typ.group(1), typ.group(2), typ.group(3)


if __name__ == '__main__':
    errorsCount, userInfo = readFile()
    errorsCount = dict(sorted(errorsCount.items(), key=lambda item: item[1], reverse=True))
    userInfo = dict(sorted(userInfo.items(), key=lambda x: x[0], reverse=False))
    with open('user_statistics.csv', 'w', newline='') as user_csv:
        for key, value in userInfo.items():
            print(key, value)
            user_csv.write(f"{str(key)},{str(value['INFO'])},{str(value['ERROR'])}\n")

    # * Create CSV error_message
    with open('error_message.csv', 'w', newline='') as error_csv:
        for key, value in errorsCount.items():
            error_csv.write(f"{str(key).rstrip()},{str(value)}\n")
