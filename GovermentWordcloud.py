import wordcloud,os
from scipy.misc import imread
import jieba
mask=imread("china.jpg")
excludes={}
f=open("新时代中国特色社会主义.txt","r")
t=f.read()
f.close()
ls=jieba.lcut(t)
txt=" ".join(ls)
w=wordcloud.WordCloud(width=1000,height=700,background_color="white",font_path="msyh.ttc",mask=mask)
w.generate(txt)
w.to_file("growwordcloud.png")
os.system("pause")