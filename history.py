import datetime as dt
def result_logger(i,result,calc):
    time=dt.datetime.now()
    time =  time.strftime("Date: %d.%m.%Y  Time: %H:%M")
    with open('C:/Users/Владимир/Desktop/Python/HomeWorks/HomeWork7/Calc/log.txt', 'a') as file:
        file.write(f'{i}: {time} ,Calculator: {calc}, Operation: {result}')
def close_log():
    with open('log.txt', 'a') as file:
        file.close()
        
git remote add origin https://github.com/VladimirTialin/Room5Calc.git
git branch -M main
git push -u origin main