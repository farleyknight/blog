##
# Constants
##                      

BINARY_WORD2VEC_DATA = '<word2vec binary format taken from the original word2vec project on Google code>'

##                      
# Import libraries      
##

import simplejson
import decimal

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.http import HttpResponse

import gensim

##                      
# Utility
##

def as_json(variable):
    json = simplejson.dumps(variable)
    return HttpResponse(json, content_type="application/json")

def parse_array_string(get, name):
    param = get.get(name, None)
    if param == None:
        return []
    else:
        return param.split(",")

##                      
# HTTP Methods          
##                                                                                                                      


def word2vec(request):
    model         = gensim.models.word2vec.Word2Vec.load_word2vec_format(BINARY_WORD2VEC_DATA, binary=True)
    positive      = parse_array_string(request.GET, 'pos')
    negative      = parse_array_string(request.GET, 'neg')
    response_data = model.most_similar(positive=positive, negative=negative)
    hashes        = [{"word": d[0], "score": decimal.Decimal(str(d[1]))} for d in response_data]

    return as_json(hashes)

##
# URL Patterns
##                      

urlpatterns = patterns('', (r'', word2vec))
