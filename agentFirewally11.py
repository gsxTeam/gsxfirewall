# coding=utf-8
import requests
import load
import telnetlib
import mylogger
import time


logger = mylogger.Logger(logname='myiptc.log', logger='myiptc').getlog()
rules_list = []


def parameter(url):
    """
    :type url: object
    """
    response = requests.get(url)
    response.encoding = "utf-8"
    """实现response的解析"""

    """返回ip,端口，用户名，密码，操作num，iptables规则"""
    return


def connect_host(ip,port,username,password):
    try:
        tn = telnetlib.Telnet(ip,port=port,timeout=10)
        tn.read_until("login: ")
        tn.write(username + "\n")
        if password:
            tn.read_until("Password: ")
            tn.write(password + "\n")
    except:
        return False
    return True


def active_rule(iprules,tn):
    logger.debug('rolling task')
    try:
        for iprule in iprules:
            if iprule in rules_list:
                pass
            else:
                try:
                    tn.write("echo " + iprule + "\n")
                except:
                    print('%s规则出现错误' % iprule)
                    break
                rules_list.append(iprule)
                tn.write("echo " + "service iptables save\n")
                tn.write("echo " + "service iptables restart\n")

    except Exception as e:
        logger.error(e)
    tn.close()


def iptable_set(tn,num=0):
    """
    num默认为0pass，为1关闭，为2开启，为3重置规则,4 所有规则
    :param tn:
    :param num:
    :return:
    """
    try:
        if num == 1:
            tn.write("echo " + "service iptables stop")
        elif num == 2:
            tn.write("echo " + "service iptables start")
        elif num == 3:
            tn.write("echo " + "iptables -P INPUT ACCEPT")
            tn.write("echo " + "iptables -F")
        elif num == 4:
            tn.write("echo " + "iptables -L")
            # 返回所有规则
        else:
            pass

    except Exception as e:
        logger.error(e)


if __name__ == '__main__':
    url = ""
    while True:
        time.sleep(3600)


