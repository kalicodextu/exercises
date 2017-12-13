from pymongo import MongoClient
from bson.son import SON
import pprint
from bson.code import Code

db = MongoClient().aggregation_example
result = db.things.insert_many(
        [
            {"x":1,"tags":["dog","cat"]},
            {"x":2,"tags":["cat"]},
            {"x":2,"tags":["mouse","cat","dog"]},
            {"x":3,"tags":[]}
            ]
        )

print(result.inserted_ids)

pipeline = [
        {"$unwind":"$tags"},
        {"$group":{"_id":"$tags","count":{"$sum":1}}},
        {"$sort":SON([("count",-1),("_id",-1)])}
        ]

pprint.pprint(list(db.things.aggregate(pipeline)))

print(db.command('aggregate','things',pipeline = pipeline,explain=True))

mapper = Code("""
        function(){
            this.tags.forEach(function(z){
                emit(z,1);
            });
        }
        """
        )

reducer = Code("""
        function(key,values){
            var total =0;
            for (var i = 0;i < values.length;i++){
                total +=values[i];
            }
            return total;
        }
        """)
#map reduce
result =db.things.map_reduce(mapper,reducer,"myresults")

for doc in result.find():
    pprint.pprint(doc)
#Advanced map/reduce
pprint.pprint(db.things.map_reduce(mapper,reducer,"myresults",full_response=True))


#clear all messages
clear_state=db.things.delete_many({})
print(clear_state.deleted_count)

