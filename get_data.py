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
    output = "Deine Herzfrequenz betrug heute im Durchschnitt "+avg_hr+" bpm,"\
                "du bist "+steps+" Schritte gelaufen, hast "+slp_du+" Stunden geschlafen"\
                "und "+cal+" Kalorien konsumiert."
    """
    if(int(steps)<=2000):
        output = output + "Du solltest dich etwas mehr bewegen."
    else:
        output = output + "Du hast dich heute viel bewegt!"
    """
    return output
