# big_screen
数据大屏可视化

# 功能

便利性工具, 结构简单, 直接传数据就可以实现数据大屏

# 安装

```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple flask
```

# 运行

```
cd big_screen;
python app.py;
```

* 大数据可视化展板通用模板 http://127.0.0.1:5000/        

* 4600 万企业数据大屏可视化 http://127.0.0.1:5000/corp    

* (2020-09) 厦门 10 万招聘数据大屏可视化 http://127.0.0.1:5000/job    

# 示例

![image](https://github.com/TurboWay/imgstore/blob/master/bigscreen/corp.jpg)

# 使用

- 1、编辑 data.py 中的 SourceData 类（或者新增类，新增的话需要编辑 app.py 增加路由，请参考 CorpData/JobData）
- 2、从任何地方读取你的数据，按照 SourceDataDemo 的数据格式，填充到 SourceData 类
- 3、运行 python app.py 查看数据变更后的效果

# 参考

> https://gitee.com/lvyeyou/DaShuJuZhiDaPingZhanShi
