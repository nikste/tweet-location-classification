# -*- coding: utf-8 -*-
import gzip
import json

import datetime

data_dir = "/home/nikste/datasets/tweets/"

stopword_file = "/home/nikste/datasets/german_stopwords/stopwords.txt"


def load_raw_tweets(fname = "Germany.json.gz"):#fname = "Germany.json.gz"):
    print "loading dataset:",datetime.datetime.now()
    fullfilename = data_dir + fname
    with gzip.open(fullfilename, 'rb') as f:
        for l in f:
            print l


        # file_contents = f.read()
    print "loaded:", datetime.datetime.now()
    # correct json string
    # file_contents.replace("\n",",")
    # file_contents = "[" + file_contents + "]"
    file_contents_list = file_contents.split("\n")
    json_list = []
    print "loaded ", len(file_contents_list)
    print "converting to json:", datetime.datetime.now()
    c = 0
    for j in file_contents_list:
        #print "item:",j,"isempty:",j == ''
        if c%1000 == 0:
            print c
        if not j == '':
            tw = json.loads(j,encoding='utf-8')
            if 'lang' in tw.keys:
                if tw['lang'] == 'de':
                    json_list.append(tw)
        c += 1
    print "done",datetime.datetime.now()
    # print file_content

    #checkout first
    # el = json_list[1]
    # for k in el.keys():
    #     print k,":",el[k]
    #     if k == 'place':
    #         for k2 in el[k].keys():
    #             print "    ",k2,":",el[k][k2]
    # locationset = set()
    # for el in json_list:
    #     locationset.add( el['place']['name'])
    # for el in locationset:
    #     print el
    # print "number of cities:", len(locationset)
    """
    "countries":
    Frankreich
    Deutschland
    Holland
    Niederlande

    Česká republika
    Poland
    Czech Republic
    Holanda
    The Netherlands
    Francia
    Nederland
    """
    # with open(data_dir + 'German_preprocessed.json', 'w') as outfile:
    #     json.dump(json_list, outfile)

    with gzip.GzipFile(data_dir + 'German_preprocessed.json.gz', 'w') as outfile:
        for obj in json_list:
            outfile.write(json.dumps(obj) + '\n')

def load_raw_tweets_linewise(fname = "Germany.json.gz"):
    print "loading dataset:", datetime.datetime.now()
    fullfilename = data_dir + fname
    linecounter = 0
    outcounter = 0
    with gzip.open(fullfilename, 'rb') as infile:
        with gzip.GzipFile(data_dir + 'German_preprocessed.json.gz', 'w') as outfile:
            for l in infile:
                linecounter += 1
                if linecounter% int(4768027/100.0) == 0:
                    print datetime.datetime.now()
                    print "datapoints input:", linecounter
                    print "datapoints output:", outcounter
                    ratio = outcounter/float(linecounter)
                    print "ratio:", ratio , "projected filesize:", ratio*1300,"mb"
                    print "done:", linecounter/4768027.0*100.0,"%"
                # process one line
                tw = json.loads(l, encoding='utf-8')
                if 'lang' in tw.keys():
                    if tw['lang'] == 'de':
                        outcounter += 1
                        # ok continue plz
                        outfile.write(json.dumps(tw) + '\n')
            outfile.close()
        infile.close()
    """
    "countries":
    Frankreich
    Deutschland
    Holland
    Niederlande

    Česká republika
    Poland
    Czech Republic
    Holanda
    The Netherlands
    Francia
    Nederland
    """

def load_stopwords():
    with open(stopword_file) as f:
        stopwords = f.readlines()
    stopwords_clean = []
    for el in stopwords:
        stopwords_clean.append(el[:-2].decode(errors='ignore'))
    return stopwords_clean


def write_training(data,fname = "/home/nikste/datasets/tweets/trainingdata.csv"):
    with open(fname,'w') as f:
        for l in data:
            for w in l[0]:
                f.write(w.encode('utf-8') + " ")
            print l[1]
            f.write("," + l[1].encode('utf-8') + "\n")

def load_dataset(fname = "/home/nikste/datasets/tweets/trainingdata.csv"):
    import csv
    with open(fname, 'rb') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data

