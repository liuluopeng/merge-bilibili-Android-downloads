# 哔哩哔哩安卓缓存音视频合并脚本
# 2023-04-16 可用此方法. 可合并up主上传到视频、电视剧


## 用法
1. 把B站缓存的视频拷贝到电脑里
2. 创建一个输出文件夹,  修改脚本中的输入文件夹和输出文件夹
3. 运行脚本 `python3 main.py`

## 总结的经验:
- 安卓缓存位置: `Android/data/tv.bangumi.com/download`  `Android/data/com.bilibili.app.in`
- 所有的路径都用绝对路径
- 先看看能不能输出文件名,   然后再用ffmpeg合并
- windows和linux路径的区别, 自己不处理了, 交给os.path处理
- windows用`ffmpeg.exe`  Linux用`ffmpeg`

