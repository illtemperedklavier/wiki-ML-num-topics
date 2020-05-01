README:

The newest file in there is word_vector_clusters.ipynb. The theory there was that the word vectors would encode semantic relations that could be clustered. That seems to be a viable approach for yielding clusters of words that appear to be similar. Next would be to test for an optimal number of clusters, by seeing what number of clusters will result in the words within an article being broadly similar in location. 



topicgetter.py:
- This was using an SVD model to extract topics, put in a separate utility file so that hyperparameters like num_topics could be tried systematically

preprocessor.py: 
- This came about with the idea of automating the preprocessing steps in creating the input text, but that was easily copy-pasted
for unsupervised topic modelling, try LDA

examine_term_agreement.ipynb:
- In this, I supposed that if different unsupervised algorithms came up with topics that had terms in common, those terms were likely indicators of topics. While I found it a compelling idea, it would be computationally intractible to scale, to compare every cluster to every other cluster. 



With more time, I'd do more research on newer unsupervised topic modelling approaches like this: "Unsupervised Topic Modeling for Short Texts Using Distributed Representations of Words" https://www.aclweb.org/anthology/W15-1526.pdf that claim to beat LDA

With this, there's a good idea about the topics in the title

    
the plan:
    - process all articles and titles
    - train word vectors on all articles
    - split to train/test (0.5)
    - train KNN (10) on train
    - predict labels for all in test
    - create new set, where all in original_article in test get sent_tokenized and split into new examples, then process as before
    - split into train/test (0.8/0.2 of the 0.5 test from earlier)
    - evaluate on test/test


