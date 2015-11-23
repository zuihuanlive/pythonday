# coding:utf-8
import os
package_dir = '/apps/aicrm/update/package'
home_dir = '/apps/aicrm'


# 解压更新函数
def update(package_dir, package_name, tmp_dir, app_path):

	package = os.path.join(package_dir, package_name)
	# print(package)
	tmp_dir = os.path.join(package_dir, tmp_dir)
	# print(tmp_dir)

	if not os.path.isfile(package):
		print('文件:' + package + '不存在')
	if os.path.isdir(tmp_dir):
		cmd_line = 'rm -rf ' + tmp_dir
		os.popen(cmd_line)
		print(cmd_line)
	else:
		os.mkdir(tmp_dir)

	cmd_line = 'unzip ' + package + ' -d ' + tmp_dir
	os.popen(cmd_line)
	# update
	cmd_line = 'cp -rf ' + tmp_dir + '/* ' + app_path
	print(cmd_line)
	os.popen(cmd_line)

app_path = os.path.join(home_dir, 'config')
# print(app_path)
update(package_dir, 'process_config.jar', 'process_config', app_path)

app_path = os.path.join(home_dir, 'lib')
update(package_dir, 'process_lib.jar', 'process_lib', app_path)
