from datetime import datetime
logs = []


def addLog(logentry):
    logs.append(f'{logentry} -  {datetime.now()}')


def viewLog():
    print(logs)
