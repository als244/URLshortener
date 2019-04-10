from django.db import models


class Link(models.Model):
    url = models.CharField(max_length=255, default = '')
    shortened = models.CharField(max_length=8, unique=True, default='abcd1234')
    timeCreated = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default = 0)

    def __str__(self):
    	return '%s' % (self.url)

class Clicked(models.Model):
	link = models.ForeignKey(Link, models.DO_NOTHING)
	clickAt = models.DateField(auto_now=True)

	def __str__(self):
		return '%s' % (self.link.url)
