# * coding:utf-8 *
# Author:sisul
#创建时间：2020/11/12 13:00
import yaml


def test_yaml_load():
    with open('../page/main.yaml') as f:
        steps = yaml.safe_load(f)
        print(steps)
    for step in steps:
        if 'by' in step.keys():
            print('查找元素')
        if 'action' in step.keys():
            print('多个动作解析')
            action = step['action']
            if 'click' in action:
                print('click动作')
            if 'send' == action:
                value = step['value']
                print(f'send{value}')

