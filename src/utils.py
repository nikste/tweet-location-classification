# -*- coding: utf-8 -*-
import gzip
import json
import re

import datetime

import pickle

import gc

from dataio import load_stopwords, write_training
import numpy as np

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
    # with open(outputfn,'wb') as f:
    counter = 0
    parts = 1000
    print "before saving:", len(inputd)
    for it in range(1,len(inputd)/parts + 1 ):
        counter += 1
        full = []
        # print "computing:",(it - 1) * len(inputd)
        for i in range((it - 1) * len(inputd)/parts,it * len(inputd)/parts):
            intermediate = []
            for r in range(0,len(inputd[i])):
                intermediate.append(model[inputd[i][r]])

            full.append(intermediate)
        print "saving rows:",it," of ", len(inputd)/parts
        pickle.dump(intermediate,open(outputfn + "_" + str(it),'wb'),protocol=pickle.HIGHEST_PROTOCOL)

    if(int(len(inputd)/parts) < len(inputd)/float(parts)):
        full = []
        for i in range(int(len(inputd)/parts) * parts ,len(inputd)):
            intermediate = []
            for r in range(0, len(inputd[i])):
                intermediate.append(model[inputd[i][r]])
            full.append(intermediate)
        print "saving rows:", counter, " of ", len(inputd) / 1000
        pickle.dump(intermediate, open(outputfn + "_" + str(counter), 'wb'), protocol=pickle.HIGHEST_PROTOCOL)

            # if counter% 1000 == 0:
            #     print counter/float(len(inputd)) , datetime.datetime.now()
            # for i in range(0,len(inputd[r])):
            #     inputd[r][i] = model[inputd[r][i]]
            # for l in range(0,len(inputd[r])):
            #     if l == len(inputd[r]) - 1:
            #         f.write(str(inputd[r][l]) + "\n")
            #     else:
            #         f.write(str(inputd[r][l]) + ",")
def load_data_vecs(outputfn):
    pass

def convert_text_to_vecs(input,model):
    print "starting to convert input to vectors:",datetime.datetime.now()
    counter = 0
    maximum = -9999
    for i in range(0,len(input)):

        if len(input[i])> maximum:
            print len(input[i]),input[i]
            maximum = len(input[i])
    gc.collect()
    print "allocating for",len(input),maximum,100
    res = np.zeros((len(input),maximum,100))
    for r in range(0,len(input)):
        counter += 1
        if counter%int(len(input)/100) == 0:
            print counter/float(len(input)) * 100,datetime.datetime.now()
        for i in range(0,len(input[r])):
            #print input[r][i]
            # input[r][i] = model[input[r][i]]
            res[r][i] = model[input[r][i]]
            #print input[r][i]
    print "saving to file",datetime.datetime.now()



    from sklearn.externals import joblib
    joblib.dump(res,"/home/nikste/datasets/location_dataset/W2v_location.csv.pickle",compress=0,cache_size=3)
    # pickle.dump(input,open("/home/nikste/datasets/W2v_location.csv.pickle",'wb'),protocol=pickle.HIGHEST_PROTOCOL)
    # with open("/home/nikste/datasets/tweets/W2v_location.csv",'wb') as f:
    #     pass