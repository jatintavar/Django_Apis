from django.db import models

# Create your models here.
class Author(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	email = models.EmailField()
	bio = models.TextField()

	def __str__(self):
		return self.name


class Book(models.Model):
    id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    publication_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
    	return self.title