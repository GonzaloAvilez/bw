# -*- coding: utf-8 -*-
from django.db import models
from utils.models import TimeStamp, Status


class Slide(TimeStamp, Status):
	title = models.CharField(
		max_length=20
		)
	image = models.FileField('Imagen',upload_to='slides/') 

	class Meta:
		verbose_name='Slide'
		verbose_name_plural = 'Slides'


