#漏斗图
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