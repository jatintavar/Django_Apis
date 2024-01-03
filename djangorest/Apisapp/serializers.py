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
        # Validate that an author cannot have more than 5 books
        author = data['author']
        if author.books.count() >= 5:
            raise serializers.ValidationError("An author cannot have more than 5 books.")

        return data


