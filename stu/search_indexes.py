#coding=UTF-8
from haystack import indexes
from stu.models import *

#注意格式
class InformationIndex(indexes.SearchIndex,indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    #给title,content设置索引
    iname = indexes.NgramField(model_attr='iname')
    iauthor = indexes.NgramField(model_attr='iauthor')

    def get_model(self):
        return Information

    def index_queryset(self, using=None):
        return self.get_model().objects.order_by('inum')
