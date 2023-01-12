from module.util.console import Console
from ivyorm import Datasource

Console.log('==================================================================================================')
Console.log('===                                       New run                                              ===')
Console.log('==================================================================================================')

db: dict = {
    "database":"test",
    "host":"localhost",
    "user":"root",
    "password":"root",
    "port":"5432"
}

test = Datasource('model/test.json', db)

#test.drop()
#test.create()

arr = {'addressID':100,'fdfd':1,'code':'something'}

result = test.insert(arr)
Console.log(test.id)
Console.log(result)
Console.log(test.error)
Console.log(test.data)
#test.insert()
#test.insert()
#test.insert()


#test.where([{'ID',2}])
#test.field(['ID','addressID','stuff']).select()
#print(test.data)
