from django.db import models

class Task(models.Model):
	task_text = models.TextField()
	main_task = models.ForeignKey('self', on_delete = models.CASCADE, null = True, blank = True)
	def getTask_text(self):
		return self.task_text
	def __str__(self):
		return self.task_text