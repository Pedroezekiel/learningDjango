from rest_framework import serializers
from my_app.models import Book


class BookSerializer(serializers.ModelSerializer):  # noqap
    publisher = serializers.CharField(

    )
    class Meta:
        model = Book
        # fields = "__all__"
        exclude = ['date_publisher', 'genre', ]

    # title = serializers.CharField(max_length=255, verbose_name="Book title", )
    # description = serializers.CharField()
    # date_published = serializers.DateField(auto_now=True)
    # isbn = serializers.CharField(max_length=20)
    # price = serializers.DecimalField(max_digits=8, decimal_places=2),
    # genre = serializers.CharField(max_length=20, choices=GENRE_CHOICES)
    # published = serializers.ForeignKey('Publisher', on_delete=serializers.CASCADE, related_name="books")

    pass
