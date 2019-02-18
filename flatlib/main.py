from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib.chart import Chart
from flatlib import const

date = Datetime('2018/11/30', '09:30', '+05:30')
pos = GeoPos('19n07','72e87')
chart = Chart(date,pos)

sun = chart.get(const.SUN)
print(sun)
