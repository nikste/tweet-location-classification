import datetime
from gensim.models import Word2Vec

from dataio import load_raw_tweets_linewise, write_training, load_dataset
from compute_word2vec import train_w2v
from utils import remove_stopwords, convert_text_to_vecs, convert_text_to_vecs_stream

# load_raw_tweets_linewise()

data = load_dataset()

# extract data:

print data[0][0].split()
print data[1]
print data[0]
w2v_data = []
for el in data:
    w2v_data.append(el[0].split())

# model = train_w2v(w2v_data)
# model.save('mymodel')
# print model
# # print model.most_similar(positive=['feierabend', 'king'], negative=['man'], topn=1)
# print model.most_similar(positive=['feierabend'], topn=1)
#
print "loadeing model:",datetime.datetime.now()
model = Word2Vec.load('mymodel5it')
print "loaded model:",datetime.datetime.now()


outputfn = "/home/nikste/datasets/W2v_location_.csv"

# convert_text_to_vecs_stream(model,w2v_data,outputfn)
convert_text_to_vecs(w2v_data,model)
# convert_text_to_vecs(w2v_data,model)
#
# model.train(w2v_data)
#
# model.save('mymodel5it')
# print model.most_similar(positive=['feierabend'],topn=20)

# d_old = [('mittag', 0.8585379123687744), ('#kaffee', 0.8245978355407715), ('urlaub', 0.8152041435241699), ('fruehstuecken', 0.8093037605285645), ('\xf0\x9f\x99\x8c', 0.8070610165596008), ('fruehstueck', 0.8070576786994934), ('\xf0\x9f\x98\x80', 0.7989702224731445), ('\xe2\x98\xba', 0.7947691082954407), ('gemuetlich', 0.7898156642913818), ('\xf0\x9f\x98\x83', 0.7889785170555115)]
# d = [('mittag', 0.7557923197746277), ('#kaffee', 0.7455747723579407), ('fruehstuecken', 0.7212720513343811), ('#feierabend', 0.7098262310028076), ('urlaub', 0.707230269908905), ('arbeitstag', 0.7020295858383179), ('\xf0\x9f\x99\x8c', 0.700904905796051), ('kaffee', 0.6971965432167053), ('fruehstueck', 0.6904301047325134), ('mittagessen', 0.6867313981056213)]
# d_4 = [('#kaffee', 0.6694605350494385), ('mittag', 0.649980902671814), ('#feierabend', 0.6476913094520569), ('gemuetlich', 0.641122043132782), ('freutag', 0.6278537511825562), ('fruehstuecken', 0.6240630745887756), ('urlaub', 0.6205250024795532), ('mittagsschlaf', 0.6203385591506958), ('kaffee', 0.6181964874267578), ('arbeitstag', 0.6172178983688354)]
# d_5 =[('#kaffee', 0.6453618407249451), ('#feierabend', 0.6299434900283813), ('gemuetlich', 0.6272793412208557), ('freutag', 0.6125092506408691), ('mittag', 0.6112803816795349), ('mittagsschlaf', 0.6035125255584717), ('arbeitstag', 0.5914018750190735), ('urlaub', 0.5898501873016357), ('kaffee', 0.5871087908744812), ('fruehstuecken', 0.5820245146751404), ('mittagessen', 0.5677179098129272), ('ausgeschlafen', 0.5579003691673279), ('#montag', 0.5491889119148254), ('mahlzeit', 0.5485547184944153), ('n8', 0.5340226888656616), ('entspannen', 0.5336139798164368), ('tee', 0.532920241355896), ('kaeffchen', 0.5313902497291565), ('abend', 0.5275278687477112), ('montag', 0.5254732966423035)]

# for i in range(0,len(d)):
#     print i,d[i][0]
#     print i,d_old[i][0]