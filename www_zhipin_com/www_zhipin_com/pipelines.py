# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class WwwZhipinComPipeline(object):
#    def __init__(self):
#        self.file = codecs.open('../../data/ftchinese/ftchinese.json', 'w', encoding='utf-8')
#        self.file.write('[')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.file.write(line)
        return item
#    def close_spider(self, spider):
#        position = self.file.tell()
#        print('position = %s' % position)
#        self.file.write(']')
#        self.file.close()

