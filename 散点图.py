#散点图 effect_scatter = EffectScatter()
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import EffectScatter
from pyecharts.globals import SymbolType

# 1、创建带有涟漪效果的散点图
effect_scatter = EffectScatter()
# 2、添加数据
effect_scatter.add_xaxis(Faker.choose())
effect_scatter.add_yaxis('',Faker.values(),symbol = SymbolType.ARROW)  #设置散点图标样式
#3、设置标题
effect_scatter.set_global_opts(title_opts = opts.TitleOpts(title = '带有涟漪效果的散点图'))
# 4、生成 .html文件
effect_scatter.render('散点图.html')