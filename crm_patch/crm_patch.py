# coding:utf-8
import os


home_path = '/home/zuilive/PycharmProjects/pythonday/crm_patch'
patch_dir = home_path+'/patch'


# print(home_path)
# print(patch_dir)
patch_dict = [
    {'source': 'config', 'target': 'config', 'type': 'dir'},
    {'source': 'crm', 'target': 'lib/crm.jar', 'type': 'jar'},
    {'source': 'crm_ejb', 'target': 'lib/crm_ejb.jar', 'type': 'jar'},
]

for i in patch_dict:
    if i['type'] == 'dir':
        cmd = 'cp -rf '+os.path.join(patch_dir, i['source'], '*')+' '+os.path.join(home_path, i['target'])
        os.popen(cmd)
        print(cmd)
    elif i['type'] == 'jar':
        tmp_dir = os.path.join(patch_dir, 'tmp', i['source'])

        # 清理老目录
        if os.path.exists(tmp_dir):
            cmd = 'rm -rf '+tmp_dir
            result = os.popen(cmd).read()
            print(result)
        os.makedirs(tmp_dir)

        # 解压
        cmd = 'cp '+os.path.join(home_path, i['target'])+' '+tmp_dir+';cd '+tmp_dir+';/usr/jdk1.8.0_65/bin/jar -xvf '+i['source']+'.'+i['type']
        os.popen(cmd)
        print(cmd)

        # 更新
        cmd = 'cp -rf '+os.path.join(patch_dir, i['source'], '*')+' '+tmp_dir
        os.popen(cmd)
        print(cmd)

        # 压缩
        cmd = 'cd '+tmp_dir+';/usr/jdk1.8.0_65/bin/jar -cvf '+i['source']+'.'+i['type']+' *'
        os.popen(cmd)
        print(cmd)

        # 覆盖
        cmd = 'cp '+tmp_dir+'/'+i['source']+'.'+i['type']+' '+os.path.join(home_path, i['target'])
        os.popen(cmd)
        print(cmd)
