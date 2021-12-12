# #折线图 line = Line()
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
# line.render("line.html")
import jieba

print(list(jieba.cut('我今天吃了大盘鸡')))