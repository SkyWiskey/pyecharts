#1、图表绘制流程
'''chart_name = '图表类型'()  #初始化具体类型图标
chart_name.add_xaxis()     #添加横坐标名称
chart_name.add_yaxis()     #添加纵坐标名称
chart_name.render()'''        #生成 .html文件

# #一、 创建一个Bar(柱状图/条形图) bar = Bar()
# from pyecharts.faker import Faker        #创造虚构的、随机的数据
# from pyecharts import options as opts    #生成图表需要用到的配置
# from pyecharts.globals import ThemeType  #主题颜色的设置
# from pyecharts.charts import Bar         #导入Bar柱状图
#
# #简单流程
# #第一步 创建Bar图
# bar = Bar()
# #第二步 设置主题颜色 以及尺寸大小
# bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION ,width = '1080px' , height = '719px'))
# #第三步 添加标题 窗口滑块 及x y轴的旋转角度
# bar.set_global_opts(title_opts = opts.TitleOpts(
#     title = 'Bar-基本实例' , subtitle = '副标题'),  #添加标题
#     datazoom_opts = [opts.DataZoomOpts()],         #添加窗口滑块
# xaxis_opts = opts.AxisOpts(axislabel_opts = opts.LabelOpts(rotate = 30))) #x轴旋转30度
# #第四步 添加x,y轴的用户输入数据  '''add_xaxis(x轴标签列表)   add_yaxis(名称 , y轴列表)'''
# # bar.add_xaxis(['衬衫','毛衣','领带','裤子','秋衣','高跟鞋','黑丝'])
# # bar.add_yaxis('商家A' , [79 , 49 , 59 , 68 , 97 , 105 , 520])
# #添加虚构数据  add_xaxis(x轴标签)  add_yaxis(名称 , y轴数据)  通过相同的stack设置可以堆叠
# bar.add_xaxis(Faker.choose())
# bar.add_yaxis('商家A' , Faker.values(), stack = 'stack1')
# bar.add_yaxis('商家B' , Faker.values(), stack = 'stack1')  #设置stack = 'stack1' 将A B两组数据堆叠
# bar.add_yaxis('商家C' , Faker.values(), stack = 'stack2')
# bar.add_yaxis('商家D' , Faker.values(), stack = 'stack2')  #设置stack = 'stack2' 将C D两组数据堆叠
# #第五步 生成 .html文件
# bar.render()
#
# #附加 1、x轴和y轴交换
# bar.reversal_axis()
# #附加 2、标记点和标记线
# bar.set_series_opts(label_opts = opts.LabelOpts(is_show = False), #不显示数字
#                     markpoint_opts = opts.MarkPointOpts(
#                         data = [opts.MarkPointItem(type_ = 'max',name = '最大值'), #点最大值
#                                opts.MarkPointItem(type_ = 'min' , name = '最小值') #点最小值
#                         ]),
#                     markline_opts = opts.MarkLineOpts(
#                         data = [opts.MarkLineItem(type_ = 'average',name = '平均值')] #线平均值
# ))
# #附加2x轴和y轴交换
# bar.reversal_axis()

# 二、3D柱状图
# from pyecharts.faker import Faker        #创造虚构的、随机的数据
# from pyecharts import options as opts    #生成图表需要用到的配置
# from pyecharts.globals import ThemeType  #主题颜色的设置
# from pyecharts.charts import Bar3D       #导入Bar3D图
# import random
#
# data = [[i , j ,random.randint(0,12)]  for i in range(24) for j in range(6)]
# # 数据格式: 一个列表,每一项都是一个由三个元素组成的列表/元组[x,y,z]
# #添加图表并渲染
# bar3d = Bar3D()
# bar3d.add(
#     "",    #名称
#     data,  #添加数据
#     xaxis3d_opts = opts.Axis3DOpts(Faker.clock , type_ = 'category'),   #设置X轴参数
#     yaxis3d_opts = opts.Axis3DOpts(Faker.week_en , type_ = 'category'), #设置Y轴参数
#     zaxis3d_opts = opts.Axis3DOpts(type_ = 'value')                     #设置Z轴参数
# )
# bar3d.set_global_opts(
#     visualmap_opts = opts.VisualMapOpts(max_ = 20),
#     title_opts = opts.TitleOpts(title = '3D装B图'),
# )
# bar3d.render()

#三、折线图 line = Line()
# from pyecharts.faker import Faker
# from pyecharts import options as opts
# from pyecharts.charts import Line
# #1、创建Line图
# line = Line()
# #2、添加数据
# line.add_xaxis(Faker.choose())
# line.add_yaxis('商家A', Faker.values(),
#                is_smooth = True,  #是否选择平滑
#                areastyle_opts=opts.AreaStyleOpts(   #添加参数
#                    opacity = 0.2,         #不透明度等于多少
#                    color='#000',))
#                    # dict(type='linear', x=0, y=0, x2=0, y2=1, colorStops=[{
#                    #     'offset': 0, 'color': 'red'
#                    # }, {'offset': 1, 'color': 'blue'
#                    #     }])))             #填充颜色
# line.add_yaxis('商家B' , Faker.values(), is_smooth = True , is_selected= True)
# #3、设置标题
# line.set_global_opts(title_opts = opts.TitleOpts(title = 'Line图'))
# # 4、生成 .html文件
# line.render()

#四、饼图 pie = Pie()
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Pie

#1、创建饼图
pie = Pie()
#2、添加数据
#系列数据项[(key1 , value1),(key2 , value2)] 掏空内部： radius = ['40','75'] 玫瑰形状：rostype='area'
pie.add("", [list(z) for z in zip(Faker.choose(), Faker.values())],radius=['40%','75%'],rosetype = 'area')
#3、添加标题
pie.set_global_opts(title_opts=opts.TitleOpts(title="Pie-设置颜色"))
#4、设置数据显示格式 b:c
pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
# 5、生成 .html文件
pie.render("pie.html")

#五、散点图
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import EffectScatter
from pyecharts.globals import SymbolType

# 1、创建带有涟漪效果的散点图
effect_scatter = EffectScatter()
# 2、添加数据
effect_scatter.add_xaxis(Faker.choose())
effect_scatter.add_yaxis(
    '',
    Faker.values(),
    symbol = SymbolType.ARROW)
#3、设置标题
effect_scatter.set_global_opts(title_opts = opts.TitleOpts(title = '带有涟漪效果的散点图'))
# 4、生成 .html文件
effect_scatter.render('散点图.html')

#六、漏斗图
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Funnel

# 1、创建漏斗图
funnel = Funnel()
# 2、添加数据 [(key1 , value1),(key2 , value2)]
funnel.add('商品' , [list(z) for z in zip(Faker.choose() , Faker.values())],
           label_opts = opts.LabelOpts(position = 'inside'))
#3、设置标题
funnel.set_global_opts(title_opts = (opts.TitleOpts(title = '漏斗图')))
#4、生成 .html文件
funnel.render('漏斗图.html')

#七、地理坐标系
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

#八、水球图 --用于一两个数据
from pyecharts.charts import Liquid
from pyecharts import options as opts

# 1、创建水球图
liquid = Liquid()
#2、添加数据
liquid.add('liquid',[0.521])
liquid.set_global_opts(title_opts=(opts.TitleOpts(title = '水球图')))
liquid.render('水球图.html')

#九、雷达图
from pyecharts.charts import Radar
from pyecharts import options as opts

#1、创建雷达图
radar = Radar()
#2、创建数据
#创建雷达数据
v1 = [[4300,10000,28000,35000,50000,19000],
      [3300,13000,25000,30000,48000,24000]]  #v1里有两个数据
v2 = [[5000,14000,28000,31000,42000,21000]]  #v2里有一个数据
radar.add_schema(
    schema = [opts.RadarIndicatorItem(name = '销售',max_ = 6500),
                opts.RadarIndicatorItem(name = '管理',max_ = 16000),
                opts.RadarIndicatorItem(name = '客服',max_ = 38000),
                opts.RadarIndicatorItem(name = '市场',max_ = 52000),
                opts.RadarIndicatorItem(name = '研发',max_ = 25000),
                opts.RadarIndicatorItem(name = '技术',max_ = 30000),
              ]
)
radar.add('预算分配' ,v1)
radar.add('实际开销' ,v2)
#设置标签
radar.set_series_opts(label_opts = (opts.LabelOpts(is_show = True)))
#设置标题
radar.set_global_opts(title_opts = (opts.TitleOpts(title = '雷达图')))
#生成.html文件
radar.render('雷达图.html')

#十、词云图
from pyecharts.charts import WordCloud
from pyecharts import options as opts

# 1、创建词云图
wordcloud = WordCloud()
# 2、创建数据  words = [(key,value),(key,value),(key,value)]
words = [('ysz',1000),('sst',800),('mlb',700),('wsk',520),
('wan',521),('xyf' , 999)]
wordcloud.add('' , words , word_size_range = [20,100])
wordcloud.set_global_opts(title_opts = opts.TitleOpts(title = '词云图'))
wordcloud.render('词云图.html')