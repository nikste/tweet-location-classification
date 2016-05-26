import gensim, logging






def train_w2v(sentences = [['first', 'sentence'], ['second', 'sentence']]):
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


    # train word2vec on the two sentences
    model = gensim.models.Word2Vec(sentences, min_count=1, size=100,workers=7)
    return model
    '''
    class MySentences(object):
        def __init__(self, dirname):
            self.dirname = dirname

        def __iter__(self):
            for fname in os.listdir(self.dirname):
                for line in open(os.path.join(self.dirname, fname)):
                    yield line.split()


    sentences = MySentences('/some/directory')  # a memory-friendly iterator
    model = gensim.models.Word2Vec(sentences)
    '''