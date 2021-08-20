import matplotlib.pyplot as plt
import numpy as np
from io import StringIO
#from app.models import FunctionModel
  
def return_graph(x, y):
    #compositemodel = FunctionModel.objects.get(pk=id)
    #x = np.arange(0, int(compositemodel.interval))
    #y = eval(compositemodel.function)
    x = np.arange(0, int(x))
    y = eval(y)
    fig = plt.figure()
    plt.plot(x, y)
    return fig
    

'''def return_graph(x, y):

    try:
        x = np.arange(0, int(x))
        y = eval(y)
    
        fig = plt.figure()
        plt.plot(x, y)
    
        imgdata = StringIO()
        fig.savefig(imgdata, format='svg')
        imgdata.seek(0)

        data = imgdata.getvalue()
        return data
    except:
        return 'Проверьте правильность ввода.'''
    

'''def return_graph():

    x = np.arange(0,np.pi*3,.1)
    y = np.sin(x)

    fig = plt.figure()
    plt.plot(x,y)

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data'''