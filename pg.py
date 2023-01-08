from module.util.console import Console



from module.datasource import Datasource

Console.log(' ==================================================================================================')
Console.log('===            New run                                                                         ===')
Console.log('==================================================================================================')
test = Datasource('test.json')

test.drop()
test.create()

arr = {'addressID':100}

test.insert(arr)
test.insert()
test.insert()
test.insert()


test.where([{'ID',2}])
test.field(['ID','addressID','stuff']).select()
print(test.data)
