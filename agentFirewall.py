#!/usr/bin/env python
# coding:utf-8
import os
import requests
import load
import time
import subprocess

rules_list = []


def parameter(url):
    """
    :type url: object
    """
    response = requests.get(url)
    response.encoding = "utf-8"
    """
    实现response的解析
    操作num，iptables规则
    """
    return


def active_rule(iprules):
    try:
        for iprule in iprules:
            if iprule in rules_list:
                pass
            else:
                try:
                    subprocess.call([iprule],shell=True)
                except:
                    print('%s规则出现错误' % iprule)
                    break
                rules_list.append(iprule)
                save()

    except Exception as e:
        print(e)


def iptable_set( num=0):
    """
    num默认为0pass，1关闭，2开启，3重置规则,4 所有规则
    :param num:
    :return:
    """
    try:
        if num == 1:
            subprocess.call(["service iptables stop"], shell=True)
        elif num == 2:
            subprocess.call(["service iptables start"], shell=True)
        elif num == 3:
            subprocess.call(["iptables -P INPUT ACCEPT"], shell=True)
            subprocess.call(["iptables -F"], shell=True)
			save()
        elif num == 4:
            subprocess.call(["iptables -L"], shell=True)
            # 返回所有规则
        else:
            pass
    except Exception as e:
        print(e)


def save():
    subprocess.call(["service iptables save"], shell=True)
    subprocess.call(["service iptables restart"],shell=True)


if __name__ == '__main__':
    url = ""
