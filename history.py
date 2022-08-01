import datetime as dt
def result_logger(i,result,calc):
    time=dt.datetime.now()
    time =  time.strftime("Date: %d.%m.%Y  Time: %H:%M")
    with open('log.txt', 'a') as file:
        file.write(f'{i}: {time} ,Calculator: {calc}, Operation: {result}')
def counter():
    try:
        with open('log.txt', 'r') as file:
            return int(file.readlines()[-1][0])+1
    except: return 1

