from sklearn.cluster import KMeans
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

# vectorize the input documents

def tfidf_vector(path):
    corpus_train = []
    target_train = []

    f = open(path,'r+',encoding='UTF-8')
    for line in f.readlines():
        line = line.strip().split('\t')
        target_train.append(line[0]+'\t'+line[1])
        corpus_train.append(line[-1])
    f.close()

    count = CountVectorizer(max_df=0.4,min_df=0.01)
    counts_train = count.fit_transform(corpus_train)

    word_dict = {}

    for index,word in enumerate(count.get_feature_names()):
        word_dict[index] = word

    tfidftransformer = TfidfTransformer()
    tfidf_train = tfidftransformer.fit(counts_train).transform(counts_train)

    return tfidf_train,target_train

# topic cluster

def cluster_kmeans(tfidf_train,target_train,cluster_docs,num_clusters):
    f = open(cluster_docs,'w+',encoding='UTF-8')
    km = KMeans(n_clusters=num_clusters)
    km.fit(tfidf_train)
    clusters = km.labels_.tolist()
    for index,cluster in enumerate(clusters):
        f.write(target_train[index] + '\t' + str(cluster) + '\n')
    f.close()


tfidf_train,target_train = tfidf_vector('abstracts.txt')
cluster_kmeans(tfidf_train,target_train,'cluster.txt',10)