#!/usr/bin/env python
# coding:utf-8

import requests
import load
import subprocess

rules_list = []


def parameter(server_url):
    # type: (object) -> object
    """
    :param server_url:
    """
    response = requests.get(server_url)
    response.encoding = "utf-8"
    """
    实现response的解析
    操作num，iptables规则
    """
    return


def active_rule(iprules):
    subprocess.call(["chmod 777 /etc/sysconfig/iptables"], shell=True)
    try:
        for iprule in iprules:
            if iprule in rules_list:
                pass
            else:
                try:
                    # subprocess.call([iprule],shell=True)
                    with open("/etc/sysconfig/iptables","a+",encoding='utf-8') as fp:
                        fp.write(iprule)
                except:
                    print('%s规则出现错误' % iprule)
                    break
                rules_list.append(iprule)
        fp.close()
        subprocess.call(["service iptables restart"], shell=True)

    except Exception as e:
        print(e)


def iptable_set(iprules,num=0):
    """
    num默认为0pass，1关闭，2开启，3重置规则,4 查看规则,5删除规则，6改规则
    :param iprules:
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
            with open('rule.txt',"w",encoding='utf-8') as f:
                for rule in rules_list:
                    f.write("\n" + rule)
                f.close()
        elif num == 5:
            for iprule in iprules:
                subprocess.call([iprule], shell=True)
                rules_list.remove(iprule)
            save()
        else:
            print("输入参数不对")
    except Exception as e:
        print(e)


def save():
    subprocess.call(["service iptables save"], shell=True)



if __name__ == '__main__':
    server_url = ""
