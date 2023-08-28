import calendar
import datetime

mes_actual = datetime.datetime.now().month
print(mes_actual)
nombre_mes = calendar.month_name[mes_actual]
print(nombre_mes)
