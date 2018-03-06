import json
import datetime
from typing import NamedTuple


class AutoReplyType(object):
    KEYWORD = 1
    EVENT = 2


class KeywordReplyMatchType(object):
    ALL_MATCH = 1
    PART_MATCH = 2


def to_reply_dto(data, reply_type):
    reply_type_to_dto = {
        AutoReplyType.KEYWORD: KeywordReplyDTO,
        AutoReplyType.EVENT: EventReplyDTO,
    }
    try:
        return reply_type_to_dto[reply_type](**data)
    except KeyError:
        raise TypeError("Could not detect type. ")


class KeywordReplyDTO(NamedTuple):
    keyword: str
    match_type: int
    msg_text: str


class EventReplyDTO(NamedTuple):
    event_key: str
    msg_text: str


class AutoReplyDTO(NamedTuple):
    mp_id: int
    reply_type: int
    reply: NamedTuple
    create_time: datetime.datetime
    update_time: datetime.datetime

    @classmethod
    def from_model(cls, dao):
        return cls(
            mp_id=dao.mp_id,
            reply_type=dao.reply_type,
            reply=to_reply_dto(json.loads(dao.data), dao.reply_type),
            create_time=dao.create_time,
            update_time=dao.update_time,
        )


class AutoReplyDAO(object):
    def __init__(self, mp_id, reply_type, data):
        self.mp_id = mp_id
        self.reply_type = reply_type
        self.data = json.dumps(data)
        self.create_time = datetime.datetime.now()
        self.update_time = datetime.datetime.now()


def main():
    dao = AutoReplyDAO(**{
        'mp_id': 100,
        'reply_type': AutoReplyType.EVENT,
        'data': {
            'event_key': 'big_watermelon',
            'msg_text': '大西瓜',
        }
    })
    dto = AutoReplyDTO.from_model(dao)
    print(dto)
    print(dict(dto._asdict()))


if __name__ == '__main__':
    main()
