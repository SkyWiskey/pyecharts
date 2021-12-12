#地理坐标系
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.faker import Faker

#1、创建Geo
geo = Geo()
#2、添加地理坐标 可以是国家 省份
geo.add_schema(maptype="china")
#3、添加数据 [(key1 , value1),(key2, value2)]
geo.add("geo", [list(z) for z in zip(Faker.provinces, Faker.values())])
geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False))  #是否展示数据
#设置标题
geo.set_global_opts(visualmap_opts=opts.VisualMapOpts(), title_opts=opts.TitleOpts(title="Geo-基本示例"))
#生成 .html文件
geo.render("geo.html")
