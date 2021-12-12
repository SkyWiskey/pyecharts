#词云图
from pyecharts.charts import WordCloud
from pyecharts import options as opts

# 1、创建词云图
wordcloud = WordCloud()
# 2、创建数据  words = [(key,value),(key,value),(key,value)]
words = [('ysz',1000),('sst',800),('mlb',700),('wsk',520),
('wan',521),('xyf' , 999)]
# 词云图轮廓，有 'circle', 'cardioid', 'diamond', 'triangle-forward', 'triangle', 'pentagon', 'star' 可选
wordcloud.add('' , words , word_size_range = [20,100],shape = 'diamond')
wordcloud.set_global_opts(title_opts = opts.TitleOpts(title = '词云图'))
wordcloud.render('词云图.html')