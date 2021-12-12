#1、图表绘制流程
'''chart_name = '图表类型'()  #初始化具体类型图标
chart_name.add_xaxis()     #添加横坐标名称
chart_name.add_yaxis()     #添加纵坐标名称
chart_name.render()'''        #生成 .html文件

#一、 创建一个Bar(柱状图/条形图) bar = Bar()
from pyecharts.faker import Faker        #创造虚构的、随机的数据
from pyecharts import options as opts    #生成图表需要用到的配置
from pyecharts.globals import ThemeType  #主题颜色的设置
from pyecharts.charts import Bar         #导入Bar柱状图

#第一步 创建Bar图设置主题颜色 以及尺寸大小
bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION ,width = '1080px' , height = '719px'))
#第三步 添加标题 窗口滑块 及x y轴的旋转角度
bar.set_global_opts(title_opts = opts.TitleOpts(
    title = 'Bar-基本实例' , subtitle = '副标题'),  #添加标题
    datazoom_opts = [opts.DataZoomOpts()],         #添加窗口滑块
xaxis_opts = opts.AxisOpts(axislabel_opts = opts.LabelOpts(rotate = 30))) #x轴旋转30度
#第四步 添加x,y轴的用户输入数据  '''add_xaxis(x轴标签列表)   add_yaxis(名称 , y轴列表)'''
# bar.add_xaxis(['衬衫','毛衣','领带','裤子','秋衣','高跟鞋','黑丝'])
# bar.add_yaxis('商家A' , [79 , 49 , 59 , 68 , 97 , 105 , 520])
#添加虚构数据  add_xaxis(x轴标签)  add_yaxis(名称 , y轴数据)  通过相同的stack设置可以堆叠
bar.add_xaxis(Faker.choose())
bar.add_yaxis('商家A' , Faker.values(), stack = 'stack1')
bar.add_yaxis('商家D' , Faker.values(), stack = 'stack2')  #设置stack = 'stack2' 将C D两组数据堆叠
#第五步 生成 .html文件
bar.render('普通柱状图2.html')
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

# # 二、3D柱状图
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
# bar3d.render('3D.html')