from jsonschema import Draft4Validator

schema ={
        "properties":{
            "name":{"type":"string"},
            "phones":{
                "properties":{
                    "home":{"type":"string"}
                    },
                },
            },
	"maxProperties":2,
	"minProperties":2,
        }

instance = {"name":"a123","phones":{"home":"0731"},"hello":"world"}

errors=Draft4Validator(schema).iter_errors(instance)

print(errors is None)

sentinel=object()
if next(errors,sentinel) is sentinel:
    print('iterator was empty')

print(errors)
for i in errors:
    print(i)
