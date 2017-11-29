# coding: utf-8
import simplejson


def add_items(data, growth_nodes, items):
    first_unnone_item_idx = -1
    for (i, item) in enumerate(items):
        # 检查前面的空数据
        if first_unnone_item_idx < 0:
            if item:
                first_unnone_item_idx = i
            else:
                continue
        else:
            if not item:
                break
        if first_unnone_item_idx != 0 or i != 0:
            l_ = []
            try:
                growth_nodes[i] = l_        # 提前设置下一层
            except IndexError:
                growth_nodes.append(l_)     # 还没有这一次层的数据就 append
            growth_nodes[i - 1].append({item: l_})
        else:
            # 处理第一组
            data[item] = []
            growth_nodes.append(data[item])


def csv2dict(file_path):
    data = {}
    growth_nodes = []
    with open(file_path) as f:
        for line in f.readlines():
            line = line.strip()         # 删掉末尾换行
            if not line:
                continue                # 跳过空行
            items = line.split(',')     # 按逗号切分
            add_items(data, growth_nodes, items)
    return data


def find_key(data, growth_nodes, key):
    growth_nodes.append(data.keys()[0])
    if data.keys()[0] == key:
        # 找到，结束
        return True
    else:
        # 当前层未找到，往下一层
        for _data in data.values()[0]:
            if find_key(_data, growth_nodes, key):
                return True
        # 往下一层未找到，退回去
        growth_nodes.pop()
    if not growth_nodes:
        return False


def find(data, key):
    growth_nodes = []
    if find_key(data, growth_nodes, key):
        return '->'.join(growth_nodes)
    else:
        return 'Not found：{}'.format(key)


def main():
    csv_file = 'test.csv'
    data = csv2dict(csv_file)
    print(simplejson.dumps(data, ensure_ascii=False, indent=4))
    print(find(data, '收获西瓜'))
    print(find(data, '收获大西瓜'))


if __name__ == '__main__':
    main()
