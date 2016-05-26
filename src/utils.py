# -*- coding: utf-8 -*-
import gzip
import json
import re

import datetime

import pickle

from dataio import load_stopwords, write_training


def extract_tweet_text(in_tweet_list):
    out_text = []
    for el in in_tweet_list:
        out_text.append(el)
    return out_text



def remove_stopwords(jsonfilename = "/home/nikste/datasets/tweets/German_preprocessed.json.gz"):
    # reading
    stopwordlist = load_stopwords()
    stopwordlist = [word.decode('utf-8') for word in stopwordlist]
    tweet_list = []
    print type(stopwordlist[0])
    print stopwordlist
    counter = 0
    with gzip.GzipFile(jsonfilename, 'r') as infile:
        for line in infile:
            obj = json.loads(line)
            text = obj['text']
            if 'place' in obj.keys():
                if obj['place'] is not None:
                    if 'name' in obj['place'].keys():
                        counter += 1

                        if counter%int(1122168/100)==0:
                            print "processed",counter," tweets",counter/1122168.0*100,"%",datetime.datetime.now()

                        place = obj['place']['name']

                        text = re.sub(r'https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)
                        txt_pre = [word.replace(u'ü', 'ue').replace(u'ö','oe').replace(u'ä','ae').replace(u'ß','ss')
                                        for word in text
                                       .replace('!',' ')
                                       .replace('.',' ')
                                       .replace(',',' ')
                                       .replace(';',' ')
                                       .replace(':',' ')
                                       .replace('-',' ')
                                       .replace('?',' ')
                                       .lower().split()]
                        txt_nosw = [word for word in txt_pre if word not in stopwordlist]
                        #print txt_nosw
                        #print [word for word in txt_nosw if word.contains('ö')]
                        #print place,txt_nosw
                        obj = (txt_nosw,place)
                        tweet_list.append(obj)
                        # process obj
    return tweet_list


def preprocess_data():
    tweets = remove_stopwords()

    write_training(tweets)
# def remove_stopwords():
#     stopwordlist = load_stopwords()
#     dataset = load_data()
#     return stopwordlist
def convert_text_to_vecs_stream(model,inputd,outputfn):
    with open(outputfn,'wb') as f:
        counter = 0
        for r in range(0,len(inputd)):
            counter += 1
            if counter% 1000 == 0:
                print counter/float(len(inputd)) , datetime.datetime.now()
            for i in range(0,len(inputd[r])):
                inputd[r][i] = model[inputd[r][i]]
            for l in range(0,len(inputd[r])):
                if l == len(inputd[r]) - 1:
                    f.write(str(inputd[r][l]) + "\n")
                else:
                    f.write(str(inputd[r][l]) + ",")

def convert_text_to_vecs(input,model):
    print "starting to convert input to vectors:",datetime.datetime.now()
    counter = 0
    for r in range(0,len(input)):
        counter += 1
        if counter%int(len(input)/100) == 0:
            print counter/float(len(input)) * 100,datetime.datetime.now()
        for i in range(0,len(input[r])):
            #print input[r][i]
            input[r][i] = model[input[r][i]]
            #print input[r][i]
    print "saving to file",datetime.datetime.now()



    from sklearn.externals import joblib
    pickle.dump(input,open("/home/nikste/datasets/W2v_location.csv",'wb'),protocol=pickle.HIGHEST_PROTOCOL)
    # with open("/home/nikste/datasets/tweets/W2v_location.csv",'wb') as f:
    #     pass