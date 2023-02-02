from wordcloud import WordCloud
from pecab import PeCab
from collections import Counter

pecab = PeCab()

# open으로 txt파일을 열고 readlines()를 이용하여 한줄씩 읽는다.
noun = []
with open("result.csv", "r") as f:
    reader = f.readlines()
    for i, line in enumerate(reader):
        print(i, line)
        noun = noun + pecab.nouns(line)

# 가장 많이 나온 단어부터 40개를 저장한다.
counts = Counter(noun)
tags = counts.most_common(40)


# WordCloud를 생성한다.
# 한글을 분석하기위해 font를 한글로 지정해주어야 된다. macOS는 .otf , window는 .ttf 파일의 위치를
# 지정해준다. (ex. '/Font/GodoM.otf')
wc = WordCloud(font_path='../../../NanumSquareNeoOTF-aLt.otf',
               background_color="white", max_font_size=60)
cloud = wc.generate_from_frequencies(dict(tags))


# 생성된 WordCloud를 test.jpg로 보낸다.
cloud.to_file('test.jpg')
