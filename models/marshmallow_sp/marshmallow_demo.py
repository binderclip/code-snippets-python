import datetime
from marshmallow import Schema, fields


class ArtistSchema(Schema):
    name = fields.Str()


class AlbumSchema(Schema):
    title = fields.Str()
    release_date = fields.Date()
    artist = fields.Nested(ArtistSchema())


def main():
    bowie = dict(name='David Bowie')
    album = dict(artist=bowie, title='Hunky Dory', release_date=datetime.date(1971, 12, 17))

    schema = AlbumSchema()
    result = schema.dump(album)
    print(result)
    # pprint(result.data, indent=2)


if __name__ == '__main__':
    main()
