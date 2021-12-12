#雷达图
from pyecharts.charts import Radar
from pyecharts import options as opts

#1、创建雷达图
radar = Radar()
#2、创建数据
#创建雷达数据
v1 = [[6,7,5,7,8,7]]  #我的数据
radar.add_schema(
    schema = [  opts.RadarIndicatorItem(name = '常规型',max_ = 10),
                opts.RadarIndicatorItem(name = '现实型',max_ = 10),
                opts.RadarIndicatorItem(name = '研究型',max_ = 10),
                opts.RadarIndicatorItem(name = '管理型',max_ = 10),
                opts.RadarIndicatorItem(name = '社会型',max_ = 10),
                opts.RadarIndicatorItem(name = '艺术型',max_ = 10),
              ]
)
radar.add('我的人格' ,v1)
#设置标签
radar.set_series_opts(label_opts = (opts.LabelOpts(is_show = True)))
#设置标题
radar.set_global_opts(title_opts = (opts.TitleOpts(title = '人格分析')))
#生成.html文件
radar.render('雷达图.html')