# encoding: utf-8
#!/usr/bin/python

import sys, os
import commands
from workflow import Workflow


reload(sys)
sys.setdefaultencoding('utf-8')


adb_path = str('/Users/egan/Library/Android/sdk/platform-tools/adb')

logo_list=['google','honor','huawei','meizu','oneplus','oppo','samsung','smartisan','vivo','xiaomi']


def get_factor_logo(logo):
    logo = logo.lower()
    for factory in logo_list:
        if logo.find(factory) > -1:
            return factory
    return "android"


def get_phone_factory(device):
    # adb -d shell getprop ro.product.brand
    command_get_phone_factory = adb_path + " -s " + device + " -d shell getprop ro.product.brand"
    _result = commands.getstatusoutput(command_get_phone_factory)
    if _result[0] == 0:
        return _result[1]
    return "Android"

def main(wf):
    
    devices = commands.getstatusoutput(adb_path + " devices")
    if devices[0] == 0:
        res = devices[1].split("\n")
        for i in res:
            if i.endswith("\tdevice"):
                # device_list.append(i.split("\t")[0])
                device = i.split("\t")[0]
                title= get_phone_factory(device)
                arg = subtitle=device
                wf.add_item(
                    title="手机：" + title,
                    subtitle=subtitle,
                    icon="logo/" + get_factor_logo(title) + ".png",
                    arg=arg,
                    valid=True
                )
    else:
        wf.add_item(title="请先连接手机或模拟器",subtitle="并确保adb已配置,开发者模式已开启")
    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
