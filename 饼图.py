# #饼图 pie = Pie()
# from pyecharts.faker import Faker
# from pyecharts import options as opts
# from pyecharts.charts import Pie
#
# #1、创建饼图
# pie = Pie()
# #2、添加数据
# #系列数据项[(key1 , value1),(key2 , value2)] 掏空内部： radius = ['40','75'] 玫瑰形状：rostype='area'
list1 =['NBA','CBA','国际足球','中国足球','步行街','游戏电竞','自建板块','运动装备','综合体育','虎扑社团','站务管理']
list2 =[232345,16976,44381,124,512266,129065,3805,35124,4454,646,34467]
# pie.add("", [list(z) for z in zip(list1, list2)],radius=['40%','75%'],rosetype = 'area')
# #3、添加标题
# pie.set_global_opts(title_opts=opts.TitleOpts(title="果酱面包配料比例"))
# #4、设置数据显示格式 b:c
# pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
# # 5、生成 .html文件
# pie.render("pie.html")
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.globals import ThemeType

c = (Pie(init_opts=opts.InitOpts(theme=ThemeType.ROMANTIC)).add("",[list(z) for z in zip(list1, list2)],
        radius=["40%", "55%"],label_opts=opts.LabelOpts(
                    position="outside",
                    formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
                    background_color="#eee",
                    border_color="#aaa",
                    border_width=1,
                    border_radius=4,
                    rich={"a": {"color": "#999", "lineHeight": 22, "align": "center"},
                          "abg": {"backgroundColor": "#e3e3e3","width": "100%","align": "right",
                                  "height": 22,"borderRadius": [4, 4, 0, 0],},
                          "hr": { "borderColor": "#aaa","width": "100%","borderWidth": 0.5,"height": 0,},
                          "b": {"fontSize": 16, "lineHeight": 33},
                          "per": {"color": "#eee","backgroundColor": "#334455","padding": [2, 4],
                                "borderRadius": 2,},}
),).set_global_opts(title_opts=opts.TitleOpts(subtitle="虎扑各板块发帖数")).render("pie_rich_label.html"))
