# -*- coding:utf-8 -*-

import sys,os
import commands
from workflow import Workflow

reload(sys)
sys.setdefaultencoding('utf-8')


def main(wf):
    selectDevice = os.getenv("device")
    adb_path = str('/Users/egan/Library/Android/sdk/platform-tools/adb')

    result = commands.getstatusoutput(adb_path + " -s " + selectDevice + " shell dumpsys activity | grep 'mFocusedActivity'")
    if result[0] != 0:
        result = commands.getstatusoutput(adb_path + " -s " + selectDevice + " shell dumpsys activity | grep 'mResumedActivity'")
    if result[0] == 0:
        # print("egan >>> " + str(len(result[1].split("\n")[0].split("/"))))
        try:
            # 对命令执行结果进行解析
            split_result = result[1].split("\n")[0].split("/")
            packages = split_result[0].split(" ")

            # # 获取包名以及当前页面的名字
            current_activity_path = packages[len(packages) - 1] + split_result[1].split(" ")[0]
            current_package = packages[len(packages) -1]
            # # print current_activity_path
            current_activity_path_list = current_activity_path.split('.')

            activity = current_activity_path_list[len(current_activity_path_list) - 1]
            # # print activity
            # # 对数据进行处理
            activity = activity.strip().replace('\r\n', ' ').replace('\n', ' ')
            # activity = "111"
            wf.add_item(
                        title="当前可见页面：" + activity,
                        subtitle="包名：" + current_package,
                        arg=activity,
                        valid=True
                    )
        except Exception:
            wf.add_item(
                    title="请先连接手机或模拟器",
                    subtitle="并确保adb已配置,开发者模式已开启",
                )
    else:
        wf.add_item(
                    title="请先连接手机或模拟器",
                    subtitle="并确保adb已配置,开发者模式已开启",
                )
    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))