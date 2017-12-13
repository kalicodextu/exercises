import json
import os
import yaml
import settings

from pymongo import MongoClient

def remove_dollar_sign(dict_temp):
        dict_temp = dict_temp
        temp = dict_temp.get('$schema')
        del dict_temp['$schema']
        dict_temp['schema'] = temp
        return dict_temp

def connect_and_manage():
    Client = MongoClient('mongodb://%s:%s@%s' % (settings.config['client']['user'],
                                             settings.config['client']['password'],
                                             settings.config['client']['host']))
    db = Client[settings.config['client']['db']]
    data_in_file = list()
    data_to_insert = list()
    data_to_update = list()

    #解析json格式文件
    for filename in os.listdir('jsonfiles'):
        if filename.endswith(".json"):
            with open('jsonfiles/' + filename) as f_obj:
                data = json.load(f_obj)

            for schema_name, schema_data in data.iteritems():
                schema_data = remove_dollar_sign(schema_data)
                document_temp = dict()
                document_temp['schemaName'] = schema_name
                document_temp['detail'] = schema_data
                same_name_flag = False
                for item in data_in_file:
                    if schema_name == item['schemaName']:
                        same_name_flag = True
                if not same_name_flag:
                    data_in_file.append(document_temp)
    #解析raml格式文件
    #for filename in os.listdir('jsonfiles'):
    #    if filename.endswith(".raml"):
    #        with open('jsonfiles/' + filename) as f:
    #            coll = yaml.load(f)


    #解析Python文件

    data_from_db = db['schema'].find({})
    for item in data_in_file:
        schema_name_new = item['schemaName']
        same_name_flag = False
        for item_from_db in data_from_db:
            if item_from_db['schemaName'] == schema_name_new:
                same_name_flag = True
                break
        if same_name_flag:
            data_to_update.append(item)
        else:
            data_to_insert.append(item)

    if len(data_to_insert) != 0:
        insert_result = db['schema'].insert_many(data_to_insert)
    if len(data_to_update) != 0:
        for item in data_to_update:
            earlier_name = item['schemaName']
            update_result = db['schema'].update({'schemaName': earlier_name}, item)

