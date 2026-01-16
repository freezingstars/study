from wordcloud import WordCloud
import jieba
txt = '''
    蒹葭苍苍，白露为霜。
    所谓伊人，在水一方。
    溯洄从之，道阻且长。
    溯游从之，宛在水中央。

    蒹葭萋萋，白露未晞。
    所谓伊人，在水之湄。
    溯洄从之，道阻且跻。
    溯游从之，宛在水中坻。

    蒹葭采采，白露未已。
    所谓伊人，在水之涘。
    溯洄从之，道阻且右。
    溯游从之，宛在水中沚。   
    '''
jieba.add_word("蒹葭")
words=jieba.lcut(txt)
new_txt=' '.join(words)
wordcloud=WordCloud(font_path="msyh.ttc",\
                    background_color="white").generate(new_txt)
wordcloud.to_file(".\\poemcloud2.png")
