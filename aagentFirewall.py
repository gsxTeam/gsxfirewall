#!/usr/bin/python
# coding:utf-8

import time
import requests
import subprocess

rules_list = []


class TimeoutError(Exception):
    """自定义抛出异常"""
    pass


def command(iprule, timeout=60):
    p = subprocess.Popen(iprule, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True)
    t_start = time.time()
    excete_time = 0
    while True:
        if p.poll() is not None:  # 执行完毕返回0，未执行完返回None
            break
        excete_time = time.time() - t_start
        if timeout and excete_time > timeout:
            p.terminate()  # 超时即关闭进程发送信号
            raise TimeoutError(iprule, timeout)
        time.sleep(0.1)
    return p.stdout.read()  # 返回报错结果


def parameter(server_url):
    response = requests.get(server_url)
    res = response.text.encode("utf-8")
    res_dict = eval(res)
    code = res_dict["code"]  # 开启或者停止
    iprules_list = res_dict["rules"]  # 规则列表
    return code, iprules_list


def iptable_set(code,iprules_list):
    """
    code open 开启 ，close 关闭
    :return:
    """
    try:
        if code == "close":
            cmd_stop = "systemctl stop iptables "
            command(cmd_stop)
        elif code == "open":
            for iprule in iprules_list:
                if iprule in rules_list:
                    pass
                else:
                    try:
                        with open("/etc/sysconfig/iptables", "a+", encoding='utf-8') as fp:
                            fp.write(iprule)
                    except:
                        print('%s规则出现错误' % iprule)
                        break
                    rules_list.append(iprule)
            fp.close()
            cmd_save = "service iptables save"
            command(cmd_save)
            cmd_start = "systemctl start iptables"
            cmd_reset = "systemctl restart iptables.service"
            command(cmd_start)
        else:
            print("输入参数不对")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    server_url = "http://127.0.0.1:8082/ip_rules.md"
    code, iprules_list = parameter(server_url)
    iptable_set(code,iprules_list)