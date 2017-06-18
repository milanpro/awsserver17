from database_connector import database_connector
import pandas as pd

def LastDay(day):
    db = database_connector()
    df = pd.read_sql("SELECT avg_heart_rate, sleep_duration, sleep_interrupts, coffein, calories, steps FROM data WHERE day = "+str(69-int(day))+";", db.engine)
    avg_hr = str(df.ix[0, 'avg_heart_rate'])
    slp_du = str(df.ix[0, 'sleep_duration'])
    slp_int = str(df.ix[0, 'sleep_interrupts'])
    coff = str(df.ix[0, 'coffein'])
    cal = str(df.ix[0, 'calories'])
    steps = str(df.ix[0, 'steps'])
    output = "Your average heart rate was "+avg_hr+" bpm,"\
                "you walked "+steps+" steps, slept "+slp_du+" hours "\
                "and consumed "+cal+" calories."
    if(int(steps)<=2000):
        output = output + " You should work out more often."
    else:
        output = output + " You were really active today!"
    return output
