# -*- coding: utf-8 -*-
import gzip
import json

data_dir = "/home/nikste/datasets/tweets/"

def load_raw_tweets(fname = "Germany.json.gz"):#fname = "Germany.json.gz"):
    fullfilename = data_dir + fname
    with gzip.open(fullfilename, 'rb') as f:
        file_contents = f.read()

    # correct json string
    # file_contents.replace("\n",",")
    # file_contents = "[" + file_contents + "]"
    file_contents_list = file_contents.split("\n")
    json_list = []
    for j in file_contents_list:
        #print "item:",j,"isempty:",j == ''
        if not j == '':
            tw = json.loads(j,encoding='utf-8')
            if tw['lang'] == 'de':
                json_list.append(tw)
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
