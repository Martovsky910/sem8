import html_creater as hc
import logger as l


n = int(input('Что вы хотите сделать? 1-Добавить новый адрес. 2-Вывести все адреса в адреской книге.'))
if n == 1:
    hc.create()

if n == 2:
    l.show()