from .models import *
from rest_framework import serializers
#validator not success

class TrackSerializer(serializers.Serializer):
    def Title_start_y(value):
        if value[0].lower() !='y':
            raise serializers.ValidationError("jdkjhskd")

    order = models.CharField(max_length=200,null=True)
    title = models.CharField(max_length=200, null=True, validators=[Title_start_y])
    duration = models.IntegerField(default=0)
    album = models.ForeignKey(Album, related_name='tracks',on_delete=models.CASCADE,null= True)

#     def create(self, validated_data):
#         return self

class TrackSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['order', 'title', 'duration']
#validation field and object level
    # def validate_duration(self, attrs):
    #     if attrs <=3:
    #         return attrs
    #     raise serializers.ValidationError("field level validation not success duration greater than 3") 
    def validate(self, attrs):
        duration = attrs.get('duration')
        title = attrs.get('title')
        if duration == 2 and title != 'nothing':
            return attrs
        raise serializers.ValidationError("object level validation not successcondition not setisfied")               

class AlbumSerializer(serializers.ModelSerializer):
    # tracks = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='title'
    # )
    tracks = TrackSerializer1(many=True)
    class Meta:
        model = Album
        fields = ['album_name', 'artist','tracks']
    '''
    if we want to change of output of serializer then use to_representation method 
    '''
    # def to_representation(self, instance):
    #     # import pdb;pdb.set_trace()
    #     representation = super().to_representation(instance)
    #     track={}
    #     track['title'] = Track.objects.get(id=1).title
    #     return track
    '''
    when we add an extra field in our output then use methodserializerfield 
    '''    
    # track = serializers.SerializerMethodField()
    # def get_tracks(self):
    #     return Track.objects.all()


    def create(self, validated_data):
        return Album.objects.create(**validated_data)
        # import pdb;pdb.set_trace()
        # tracks_data = validated_data.pop('tracks')
        # album = Album.objects.create(**validated_data)
        # for track_data in tracks_data:
        #     Track.objects.create(album=album, **track_data)
        # return album
