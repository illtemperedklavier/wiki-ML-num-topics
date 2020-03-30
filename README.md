README:

The newest file in there is word_vector_clusters.ipynb. The theory there was that the word vectors would encode semantic relations that could be clustered. That seems to be a viable approach for yielding clusters of words that appear to be similar. Next would be to test for an optimal number of clusters, by seeing what number of clusters will result in the words within an article being broadly similar in location. 



topicgetter.py:
- this was using an SVD model to extract topics, put in a separate utility file so that hyperparameters like num_topics could be tried systematically
preprocessor.py: 
- came about with the idea of automating the preprocessing steps in creating the input text, but that was easily copy-pasted
for unsupervised topic modelling, try LDA
given more time, I'd do more research on things like this: "Unsupervised Topic Modeling for Short Texts Using Distributed
Representations of Words" https://www.aclweb.org/anthology/W15-1526.pdf , that claim to beat LDA

simple idea for a different dataset: how possible is it to identify topics by what students have questions about?

With this, there's a good idea about the topics in the title

how many topics? try using the number of titles

tasks:
    - change to remove punctuation before tokenization
    - bonus - sent_tokenize the Wiki articles for data augmentation
    - "ground truth" doesn't exist here, but the article titles and first couple of lines of the articles probably contain key terms
    

having tried finding agreement between models - seems to be a bad idea, because what's to say a topic is matched to another? obvious logic hole

new plan: make word2vec vectors from the corpus*
    - cluster said vectors into n categories - consider those "topics"
    - find cluster mean
    - find most similar vector
    
*considered doc2vec, but since word vectors supposedly take the context into account, I'll take the automatic data augmentation

