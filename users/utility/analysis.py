import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
def Forecast_analysis():
    from django.conf import settings
    import os
    path = os.path.join(settings.MEDIA_ROOT, 'stockForecast.csv')
    df = pd.read_csv(path, encoding="ISO-8859-1")
    x_label = df['Date'] = pd.to_datetime(df['Date'])
    y_label = df['Close'].tolist()
    y1_label = df['Open'].tolist()
    x = np.array(x_label[::5])
    y = np.array(y_label[::5])
    y1 = np.array(y1_label[::5])
    plt.plot(x,y,'g',linewidth=1,label="Close")
    plt.plot(x,y1,'r',linewidth=1,label="Open")
    plt.legend()
    plt.show()
