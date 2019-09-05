# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 13:19:34 2019

@author: user
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import nltk 
#nltk.download('stopwords')

from nltk.corpus import stopwords 
from nltk.stem.porter import PorterStemmer
df=pd.read_csv('C:\\Users\\user\\Desktop\\Python_Setup\\Machine Learning Sections\\9. Natural Language Processing\\Restaurant_Reviews.tsv', delimiter= '\t',quoting=3)
import re
corpus=[]
for i in range(0,1000):
    review= re.sub('[^a-zA-Z]',' ',df['Review'][i]).lower()
    review=review.split()
    ps  = PorterStemmer()
    review=[ ps.stem(word) for word in review if not word in stopwords.words('english') ]


