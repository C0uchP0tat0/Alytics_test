from django.db import models
from django_matplotlib import MatplotlibFigureField
from datetime import datetime

class FunctionModel(models.Model):
    function = models.CharField(max_length=50,
                                verbose_name='Функция')
    interval = models.IntegerField(verbose_name='Интервал t,дней')
    processing_date = models.DateTimeField(auto_now=True, blank=True, 
                                    verbose_name='Дата обработки')
    function_plot = MatplotlibFigureField(figure='return_graph',
                                    verbose_name="График", silent=True)

    def __str__(self):
        return self.function
    
    