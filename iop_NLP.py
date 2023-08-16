# -*- encoding: utf-8 -*-
'''
@File         :   iop_NLP.py
@Introduction :   NLP by The Institute of Physics of the Chinese Academy of Sciences
@Version      :   1.0
@Contact      :   sywu@iphy.ac.cn
'''

import tensorflow as tf
import pandas as pd
import json,os
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split

class iopNLP():
    def __init__(self):
        self.__version__ = 1.0
        self.__author__ = 'iop'
        self.num_epochs = 5
        self.path = os.getcwd()
        self.name = 'iop_NLP_model'
        self.max_length = 512
    
    def getData(self):
        with open ('%s/data/data.json' % self.path,'r') as f:
            self.data = pd.DataFrame(json.load(f))

    def initial_tokenizer(self):
        self.getData()
        all_input = self.data.abstract.values
        self.tokenizer = Tokenizer(oov_token='<OOV>')
        self.tokenizer.fit_on_texts(all_input)
        self.vocab_size = len(self.tokenizer.word_index)
        if not os.path.exists('%s/model' % self.path):
            os.mkdir('%s/model' % self.path)
        elif os.path.exists('%s/model/text.json' % self.path):
            os.remove('%s/model/text.json' % self.path)
        with open('%s/model/text.json' % self.path,'a') as f:
            json.dump(self.tokenizer.to_json(),f)
    
    def word2vec(self,tokenizer,sentences):
        sequences = tokenizer.texts_to_sequences(sentences)
        return pad_sequences(sequences,maxlen = self.max_length,\
                            padding='post',truncating='post')
        
    def initial_model(self):
        self.initial_tokenizer()
        training_sentences,\
        testing_sentences,\
        self.training_label,\
        self.testing_label = train_test_split(
                                         self.data.abstract.values,
                                         self.data.label.values,\
                                         test_size=0.3
                                         )
        self.training_padded = self.word2vec(self.tokenizer,training_sentences)
        self.testing_padded = self.word2vec(self.tokenizer,testing_sentences)

    def create_model(self):
        self.model = tf.keras.Sequential([
                     tf.keras.layers.Embedding(self.vocab_size+1,
                                               128,
                                               input_length = self.max_length),
                     tf.keras.layers.GlobalAveragePooling1D(),
                     tf.keras.layers.Dense(64,activation='relu'),
                     tf.keras.layers.Dense(1,activation='sigmoid')
                     ])

    def fit_model(self):
        self.model.compile(
                           loss='binary_crossentropy', 
                           optimizer='adam', 
                           metrics=['accuracy']
                           )
        self.model.fit(
                       self.training_padded,
                       self.training_label,
                       epochs = self.num_epochs, 
                       validation_data=(
                                        self.testing_padded,
                                        self.testing_label
                                        ), 
                       verbose=2
                       )
        
    def save_model(self):
        if not os.path.exists('%s/model' % self.path):
            os.mkdir('%s/model' % self.path)
        tf.keras.models.save_model(self.model,'%s/model/%s.h5' % (self.path,self.name))
    
    def predict_sentences(self,sentences):
        model = tf.keras.models.load_model('%s/model/%s.h5' % (self.path,self.name))
        with open('%s/model/text.json' % self.path,'r') as f1:
            string = json.load(f1)
        tokenizer = tf.keras.preprocessing.text.tokenizer_from_json(string)
        padding = self.word2vec(tokenizer,sentences)
        return model.predict(padding)
    
    def main(self):
        self.initial_model()
        self.create_model()
        self.fit_model()
        self.save_model()

if __name__ == '__main__':
    model_new = iopNLP()
    model_new.main()
    print(model_new.predict_sentences(["""The exponential growth of literature is constraining researchers' access to comprehensive information in related fields. While natural language processing may offer an effective solution, it remains hindered by the lack of datasets. In this article, we introduce a novel method for generating literature classification models through semi-supervised learning. We apply this method to battery, superconducting, topological, and AI in material science, and we achieve promising results. Importantly, our approach demonstrates that even with insufficient data, the initial model can facilitate understanding the relationships between different research fields."""]))