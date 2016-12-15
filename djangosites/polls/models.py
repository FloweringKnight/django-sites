from django.db import models
import datetime
from django.utils import timezone


# Create your models here.
class Question(models.Model):
	question_text = models.CharField(verbose_name='text which question\'s', max_length=200)
	pub_date = models.DateTimeField(verbose_name='datetime when pub')
	def __str__(self):
		return self.question_text

	def was_published_rencently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	was_published_rencently.admin_order_field = 'pub_date'
	was_published_rencently.boolean = True
	was_published_rencently.short_description = 'Published rencently?'


class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(verbose_name='text which choice\'s', max_length=200)
	votes = models.IntegerField(verbose_name='votes', default=0)
	def __str__(self):
		return self.choice_text
