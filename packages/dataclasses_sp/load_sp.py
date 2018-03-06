from dataclasses import dataclass, fields


@dataclass
class XDataClass(object):
    """dataclass can load dict or obj"""

    @classmethod
    def load(cls, data):
        """load a dict/obj to dataclass

        auto load dataclass fields recursively
        auto grab needed obj attrs
        """
        if isinstance(data, dict):
            print('>>> dict')
        else:
            print('>>> obj')
        # cls_fields = fields(cls)
        init()


    # @classmethod
    # def _load_inner(cls, ):


def main():
    print(XDataClass.load({'foo': 'bar'}))
    print(XDataClass.load(Foo('bar')))


if __name__ == '__main__':
    main()
