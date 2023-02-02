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


class TrackSerializer1(serializers.ModelSerializer):
    def create(self, validated_data):
        return Track.objects.create(**validated_data)
    class Meta:
        model = Track
        fields = ['order', 'title', 'duration','album']
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
"""
backword relation
"""
class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    # tracks = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='track-detail',
    #     lookup_field='titles'
    # )
    # tracks = serializers.StringRelatedField(many=True)
    # tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # tracks = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='title'
    # )
    tracks = TrackSerializer1(many=True)
    class Meta:
        model = Album
        fields = ['id','album_name', 'artist','tracks']
        # fields = ['album_name', 'artist']

class AlbumSerializernew(serializers.ModelSerializer):
    # data = serializers.SerializerMethodField()
    class Meta:
        model = Album
        fields = '__all__'  

    # def get_data(self, obj):
    #     import pdb;pdb.set_trace()
    #     if self.context['request'].user.has_perm('something.add_something'):
    #        return 'hello'

class SearchSerializer(serializers.ModelSerializer):
    search = serializers.SerializerMethodField()
    class Meta:
        model = Search
        fields =['address','date','search'] 

    # def get_search(self, obj):
    #     context={}
    #     context['data'] = Album.objects.filter(id=1)
    #     return AlbumSerializernew(context,{"context":context})


"""
Farword relation 
"""
class Trackserializer(serializers.ModelSerializer):
    # album = serializers.SlugRelatedField(read_only=True, slug_field='album_name')
    
    class Meta:
        model = Track
        fields =  ['id','album','duration','title','order']   


    '''
    if we want to change of output of serializer then use to_representation method 
    '''
    def to_representation(self, instance):
        # import pdb;pdb.set_trace()
        representation = super().to_representation(instance)
        track={}
        album={}
        # track['track_data']=representation
        obj=Track.objects.get(id=22)
        track['id']=obj.album.id
        track['album_name'] = obj.album.album_name
        track['artist']= obj.album.artist
        album['album_data']=track
        return album
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
