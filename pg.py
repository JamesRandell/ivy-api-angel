from quart import Quart
from quart_cors import cors



from module.datasource import Datasource


test = Datasource('test.json')

test.where([{'ID',2}])
test.field(['ID','addressID','stuff']).select()

