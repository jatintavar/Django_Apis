from rest_framework import serializers
from .models import *

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, data):
        author = data['author']
        title = data['title']

        # Check if a similar book already exists for the author
        if Book.objects.filter(author=author, title__iexact=title).exists():
            raise serializers.ValidationError("A similar book already exists for this author.")
       
       # Validate that an author cannot have more than 5 books
        if author.books.count() >= 5:
            raise serializers.ValidationError("An author cannot have more than 5 books.")

        return data


