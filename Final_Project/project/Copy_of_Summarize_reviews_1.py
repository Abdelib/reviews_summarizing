def  run_all():

    return_list = []
    import json
    f = open("/Users/abdelrahmanibrahim/Documents/Data science Bootcamp/Final Project/data/nike_all_mens.json")
    data = json.load(f)

    reviews = []
    shows =[]
    body = ""

    for key in data:
      try:
        #pass
        body = key['title']

        for keys in key['reviews']['reviews']:
          shows.append(body)
          reviews.append(keys['body'])

        #
      except:
        pass


    # In[2]:


    import pandas as pd
    df = pd.DataFrame({'review':reviews,
            'Name':shows})

    df


    # In[3]:


    print(df.nunique())
    print(df.shape)


    # In[4]:


    def GetSummary(df):
      article_text = ""
      import re
      import nltk
      nltk.download('punkt')
      nltk.download('stopwords')
      for p in df ['review']:

        article_text += p
      # Removing Square Brackets and Extra Spaces
      article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
      article_text = re.sub(r'\s+', ' ', article_text)
      # Removing special characters and digits
      formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )
      formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)
      sentence_list = nltk.sent_tokenize(article_text)

      ##

      stopwords = nltk.corpus.stopwords.words('english')
      word_frequencies = {}
      for word in nltk.word_tokenize(formatted_article_text):
          if word not in stopwords:
              if word not in word_frequencies.keys():
                  word_frequencies[word] = 1
              else:
                  word_frequencies[word] += 1

      ##
      maximum_frequncy = max(word_frequencies.values())

      for word in word_frequencies.keys():
          word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
      ##
      sentence_scores = {}
      for sent in sentence_list:
          for word in nltk.word_tokenize(sent.lower()):
              if word in word_frequencies.keys():
                  if len(sent.split(' ')) < 30:
                      if sent not in sentence_scores.keys():
                          sentence_scores[sent] = word_frequencies[word]
                      else:
                          sentence_scores[sent] += word_frequencies[word]
      import heapq
      summary_sentences = heapq.nlargest(3, sentence_scores, key=sentence_scores.get)

      summary = ' '.join(summary_sentences)
      return summary


    # In[5]:



    title = []
    summary = []
    countReviewas = []
    for shoes in df['Name'].unique():
      title.append(shoes)
      value_list =[]
      value_list.append(shoes)
      boolean_series = df.Name.isin( value_list)
      filtered_df = df[boolean_series]


      countReviewas.append( filtered_df.shape[0])
      summary.append(GetSummary(filtered_df))
      filtered_df =filtered_df.drop_duplicates(subset=['review'], keep='first')

    dff = pd.DataFrame({'Name':title,'Summary':summary,'CountReviews':countReviewas})
    dff
    #for sho in df['Name'].unique():
      #print(sho)


    # In[6]:
    shoeName = "Nike SB Chron 2 Canvas"
    value_list =[]
    value_list.append(shoeName)
    boolean_series = df.Name.isin( value_list)
    boolean_series1 = dff.Name.isin( value_list)

    all_reviews = df[boolean_series]

    summary = dff[boolean_series1]

    pd.set_option('display.max_colwidth', None)
    #print(all_reviews.review.trim())
    print("\t\t\t\t\t\t\t\t----------------------------------All Reviews--------------------------------------------")
    pd.set_option('display.max_colwidth', None)
    print(all_reviews['review'])

    print("\t\t\t\t\t\t\t\t----------------------------------Summary Review--------------------------------------------")
    summary['Summary']



    # In[7]:


    dff ['Name'][8]


    # In[8]:


    dff ['Summary'][8]


    # In[9]:


    #visualisation
    Sorted = dff.sort_values('CountReviews',ascending=False)
    Sorted.head(10)
    return_list.append(Sorted)


    # In[10]:


    import matplotlib.pyplot as plt

    Shoes = Sorted['Name'].head(10)
    CountReviews = Sorted['CountReviews'].head(10)

    plt.bar(Shoes,CountReviews)
    plt.title('Top 10 most reviewed Shoes')
    plt.xlabel('Shoes')
    plt.ylabel('No of reviews')

    plt.xticks(rotation=90)
    for index, value in enumerate(CountReviews):
     plt.text(index,value,str(value))

    return_list.append(plt)

    return return_list




