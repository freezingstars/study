from wordcloud import WordCloud
import jieba

with open('.\\国歌.txt', 'r', encoding='utf-8') as f:
    txt_str = f.read()
words = jieba.lcut(txt_str)
new_txt = ' '.join(words)
wordcloud = WordCloud(font_path="msyh.ttc", \
                      background_color="white").generate(new_txt)
wordcloud.to_file(".\\song.png")
