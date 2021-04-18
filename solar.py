import matplotlib.pyplot as plt
import datetime
import solarsystem

def create_positions():
    now    = datetime.datetime.utcnow()
    now    = datetime.datetime.now(datetime.timezone.utc)
    year   = now.year
    month  = now.month
    day    = now.day
    hour   = now.hour
    minute = now.minute
    UT     = 0
    dst    = 0

    Hr = solarsystem.Heliocentric(year=year, month=month, day=day, hour=hour, minute=minute,
                             UT=UT, dst=dst, view='rectangular' )
    planetspositionsHrect=Hr.planets()

    return planetspositionsHrect

def create_plot(planetspositionsHrect):
    forplot=[]
    planetname=[]
    for key in planetspositionsHrect:
        planetname.append(key)
        forplot.append(   planetspositionsHrect[key] )

    plt.figure(figsize=(15,15))
    ax = plt.gca()
    ax.cla()
    ax.set_xlim((-33, 33))
    ax.set_ylim((-33, 33))
    a=0.5
    ax.plot(0,0,'.', label='Sun')

    for i in range(8):
        ax.plot(forplot[i][0] , forplot[i][1] ,'.', markersize=10, label=planetname[i])
        if (i >1) & (i < 10):
            ax.add_artist(plt.Circle((0, 0), ((abs(forplot[i][0])**2+abs(forplot[i][1])**2)**0.5), color='r', fill=False))
    ax.annotate('Mars', (forplot[3][0] , forplot[3][1]))
    ax.legend()
    return plt

def image_out(file_name):
    pos = create_positions()
    plt = create_plot(pos)
    plt.savefig(file_name)
