README:

topicgetter.py:
- this was using an SVD model to extract topics, put in a separate utility file so that hyperparameters like num_topics could be tried systematically
preprocessor.py: 
- came about with the idea of automating the preprocessing steps in creating the input text, but that was easily copy-pasted

just_get_topics.ipynb:
Just used the article titles with stopwords removed as some ground truth topics. I debated the idea of using the first couple of sentences, word tokenized, with stopwords and punctuation removed from the article text, because those articles are typically written in that type of inverted-pyramid format
