import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#pd.set_option("display.max_colwidth", 200)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

def make_topics(articles, num_topics): 
    """
    articles: a series of lists of tokenized words with stopwords removed
    num_topics: trying different numbers of topics
    
    """
    articles = articles.apply(lambda x: ' '.join(x))

    vectorizer = TfidfVectorizer(stop_words='english', 
                                 max_features= 1000,
                                max_df=0.5,
                                smooth_idf=True)

    X = vectorizer.fit_transform(articles)

    print("shape: ", X.shape)

    # SVD represent documents and terms in vectors 
    svd_model = TruncatedSVD(n_components=num_topics, algorithm='randomized', n_iter=100, random_state=122)

    svd_model.fit(X)

    len(svd_model.components_)

    terms = vectorizer.get_feature_names()

    """
    for i, comp in enumerate(svd_model.components_):
        terms_comp = zip(terms, comp)
        sorted_terms = sorted(terms_comp, key= lambda x:x[1], reverse=True)[:7]
        print("Topic "+str(i)+": ")
        for t in sorted_terms:
            print(t[0])
            print(" ")
        """
    topic_dict = {}
    
    for i, comp in enumerate(svd_model.components_):
            terms_comp = zip(terms, comp)
            sorted_terms = sorted(terms_comp, key= lambda x:x[1], reverse=True)[:7]
           	#print("Topic "+str(i)+": ")
            specific_terms = []
            for t in sorted_terms:
                specific_terms.append(t[0])
            
            topic_dict["Topic"+str(i)] = specific_terms


    return svd_model, terms, topic_dict

