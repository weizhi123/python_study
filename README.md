python 学习空间
1、按Alt+Shift+F即可自动格式化代码
2、运行python文件：
F5
Terminal中输入：python hello.py
程序页面右键选择在“终端中运行Python文件3
3、git版本管理：
提交代码到远程分支步骤：
（1：拉取服务器代码，避免覆盖他人代码 git pull 
（2：查看当前项目中有哪些文件被修改过 git status 
（3：将状态改变的代码提交至缓存 git add + 文件 
    git add .  将所有的修改的文件提交到缓存区
（4：将代码提交到本地仓库中 git commit -m “修改项目代码”
    git commit -m用于提交暂存区的文件，git commit -am用于提交跟踪过的文件
（5：将缓存区代码推送到Git服务器 git push