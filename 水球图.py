#水球图 --用于一两个数据
from pyecharts.charts import Liquid
from pyecharts import options as opts

# 1、创建水球图
liquid = Liquid()
#2、添加数据   可以添加shape (SVG)  shape = 'path://SVG路径'
liquid.add('liquid',[0.521],)
liquid.set_global_opts(title_opts=(opts.TitleOpts(title = '水球图')))
liquid.render('水球图.html')