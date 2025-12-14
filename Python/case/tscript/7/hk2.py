from wordcloud import WordCloud
import jieba
txt = ("假如生活欺骗了你，不要悲伤，不要心急！忧郁的日子里须要镇静：相信吧，"
       "快乐的日子将会来临！心儿永远向往着未来；现在却常是忧郁。"
       "一切都是瞬息，一切都将会过去；而那过去了的，就会成为亲切的怀恋。")
words = jieba.lcut(txt)
new_txt = ' '.join(words)
wordcloud = WordCloud(
    font_path="msyh.ttc",  # 指定中文字体路径（解决中文乱码问题）
                           # msyh.ttc 是Windows系统的“微软雅黑”字体，Mac可替换为"PingFang SC"
    background_color="white"  # 设置词云图片的背景色（默认黑色，此处改为白色更清晰）
).generate(new_txt)  # 基于分词后的文本生成词云
wordcloud.to_file(".\\poemcloud1.png")
