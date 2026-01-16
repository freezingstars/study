from wordcloud import WordCloud
import jieba

with open("./movie_titles.txt", "r", encoding="utf-8") as f:
    text = f.read()
text = text.replace("·", "")
jieba.add_word("哈利波特", freq=200)
words = jieba.lcut(text)
stopwords = {'的', '之', '吧'}
words = [w for w in words if w not in stopwords and len(w) > 1]
text = ' '.join(words)

wc = WordCloud(
    width=800,
    height=400,
    background_color="white",
    font_path="msyh.ttc"
).generate(text)

wc.to_file("movie_wordcloud.png")
