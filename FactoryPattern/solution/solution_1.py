import abc
import json
import xml.etree.ElementTree as et

class Song:
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist

# Product
class Serializer(abc.ABC):
    @abc.abstractmethod
    def serialize(self,song):
        pass

# Concrete Product
class JsonSerializer(Serializer):
    def serialize(self,song):
        song_info = {
            'id': song.song_id,
            'title': song.title,
            'artist': song.artist
        }
        return json.dumps(song_info)

# Concrete Product
class XmlSerializer(Serializer):
    def serialize(self,song):
        song_info = et.Element('song', attrib={'id': song.song_id})
        title = et.SubElement(song_info, 'title')
        title.text = song.title
        artist = et.SubElement(song_info, 'artist')
        artist.text = song.artist
        return et.tostring(song_info, encoding='unicode')



# Concrete Creator
class SerializeFactory:
    def _get_serializer(self, format):
        if format == 'json':
            return JsonSerializer()
        elif format == 'xml':
            return XmlSerializer()
        else:
            raise ValueError(format)


song = Song('1', 'Song name', 'Song Artist')

factory = SerializeFactory()
json_serializer = factory._get_serializer('json')
xml_serializer = factory._get_serializer('xml')

print(json_serializer.serialize(song))
print(xml_serializer.serialize(song))