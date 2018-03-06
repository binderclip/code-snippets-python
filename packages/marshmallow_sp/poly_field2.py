import json
from marshmallow import Schema, fields, post_load, pre_dump
from marshmallow_polyfield import PolyField


class AutoReplyType(object):
    KEYWORD = 1
    EVENT = 2


class AutoReply(object):
    def __init__(self, mp_id, reply_type, data):
        self.mp_id = mp_id
        self.reply_type = reply_type
        self.data = json.dumps(data)

    def __repr__(self):
        return f'AutoReply(mp_id={self.mp_id}, reply_type={self.reply_type}, data={repr(self.data)})'

    def __str__(self):
        return self.__repr__()


class KeywordReplyMatchType(object):
    ALL_MATCH = 1
    PART_MATCH = 2


class KeywordReplySchema(Schema):
    keyword = fields.Str()
    match_type = fields.Int()
    msg_text = fields.Str()


class EventReplySchema(Schema):
    event_key = fields.Str()
    msg_text = fields.Str()


def reply_serialization_schema_selector(_, obj):
    type_to_schema = {
        AutoReplyType.KEYWORD: KeywordReplySchema,
        AutoReplyType.EVENT: EventReplySchema,
    }
    try:
        return type_to_schema[obj.reply_type]()
    except KeyError:
        raise TypeError("Could not detect type.")


def reply_deserialization_schema_selector(_, data):
    type_to_schema = {
        AutoReplyType.KEYWORD: KeywordReplySchema,
        AutoReplyType.EVENT: EventReplySchema,
    }
    try:
        return type_to_schema[data['reply_type']]()
    except KeyError:
        raise TypeError("Could not detect type. ")


class AutoReplySchema(Schema):
    mp_id = fields.Int()
    reply_type = fields.Int()
    reply = PolyField(
        serialization_schema_selector=reply_serialization_schema_selector,
        deserialization_schema_selector=reply_deserialization_schema_selector,
        attribute="data",
    )

    @pre_dump
    def pre_dump(self, item):
        item.data = json.loads(item.data)
        return item

    @post_load
    def post_load(self, item):
        return AutoReply(**item)


def main():
    print('=== load ===')
    result = AutoReplySchema().load({
        'mp_id': 100,
        'reply_type': AutoReplyType.KEYWORD,
        'reply': {
            'keyword': '大西瓜',
            'match_type': KeywordReplyMatchType.ALL_MATCH,
            'msg_text': 'big watermelon',
        }
    })
    print(result)
    result = AutoReplySchema().load({
        'mp_id': 100,
        'reply_type': AutoReplyType.EVENT,
        'reply': {
            'event_key': 'big_watermelon',
            'msg_text': '大西瓜',
        }
    })
    print(result)
    print('=== dump ===')
    auto_reply = AutoReply(
        mp_id=100,
        reply_type=AutoReplyType.KEYWORD,
        data={"match_type": 1, "keyword": "大西瓜", "msg_text": "big watermelon"},
    )
    result = AutoReplySchema().dump(auto_reply)
    print(result)
    auto_reply = AutoReply(
        mp_id=100,
        reply_type=AutoReplyType.EVENT,
        data={"event_key": "big_watermelon", "msg_text": "大西瓜"},
    )
    result = AutoReplySchema().dump(auto_reply)
    print(result)


if __name__ == '__main__':
    main()
