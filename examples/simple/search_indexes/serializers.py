import json

from rest_framework import serializers

__all__ = (
    'BookDocumentSerializer',
    'PublisherDocumentSerializer',
    'TagSerializer',
)


class TagSerializer(serializers.Serializer):
    """Helper serializer for the Tag field of the Book document."""

    title = serializers.CharField()

    class Meta(object):
        """Meta options."""

        fields = ('title',)
        read_only_fields = ('title',)


class BookDocumentSerializer(serializers.Serializer):
    """Serializer for the Book document."""

    id = serializers.IntegerField(read_only=True)

    title = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    summary = serializers.CharField(read_only=True)

    publisher = serializers.CharField(read_only=True)
    publication_date = serializers.DateField(read_only=True)
    state = serializers.CharField(read_only=True)
    isbn = serializers.CharField(read_only=True)
    price = serializers.FloatField(read_only=True)
    pages = serializers.IntegerField(read_only=True)
    stock_count = serializers.IntegerField(read_only=True)
    tags = serializers.SerializerMethodField()

    class Meta(object):
        """Meta options."""

        fields = (
            'id',
            'title',
            'description',
            'summary',
            'publisher',
            'publication_date',
            'state',
            'isbn',
            'price',
            'pages',
            'stock_count',
            'tags',
        )
        read_only_fields = (
            'id',
            'title',
            'description',
            'summary',
            'publisher',
            'publication_date',
            'state',
            'isbn',
            'price',
            'pages',
            'stock_count',
            'tags',
        )

    # def get_id(self, obj):
    #     """Get id."""
    #     return int(obj.meta.id)

    def get_tags(self, obj):
        """Get tags."""
        return json.loads(obj.tags)


class PublisherDocumentSerializer(serializers.Serializer):
    """Serializer for Publisher document."""

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    address = serializers.CharField(read_only=True)
    city = serializers.CharField(read_only=True)
    state_province = serializers.CharField(read_only=True)
    country = serializers.CharField(read_only=True)
    website = serializers.CharField(read_only=True)

    class Meta(object):
        """Meta options."""

        fields = read_only_fields = (
            'id',
            'name',
            'address',
            'city',
            'state_province',
            'country',
            'website',
        )
        read_only_fields = fields