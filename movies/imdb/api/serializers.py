
from rest_framework import serializers
from imdb.models import Movie

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    movie_name = serializers.CharField()
    movie_desc = serializers.CharField()
    movie_status = serializers.BooleanField()



    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    # [if data posted/created is valid then create a new object of data]



    def update(self, instance ,validated_data):
        instance.movie_name = validated_data.get('movie_name', instance.movie_name)
        instance.movie_desc = validated_data.get('movie_desc', instance.movie_desc)
        instance.movie_status = validated_data.get('movie_status', instance.movie_status)
        instance.save()
        return instance
    # [HERE THE instance IS OLD DATA AND THE validated_data IS NEW DATA]
    #  SO WE ARE ADDING NEW DATA INTO OLD DATA, EVEN IF IT IS UPDATED OR NOT
    
    
