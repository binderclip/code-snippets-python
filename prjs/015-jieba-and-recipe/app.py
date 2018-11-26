from collections import defaultdict

import jieba


recipe_title_data = defaultdict(dict)


def cut_txt(txt: str, mark: str):
    seg_list = jieba.cut_for_search(txt)
    # print(f"{txt} -> " + " | ".join(seg_list))  # 精确模式
    recipe_title_data[txt][mark] = "_".join(seg_list)


def get_titles_from_file():
    with open('recipe_tstring_typesitles.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            _line = line.strip()
            if not _line:
                continue
            yield _line


def get_titles():
    return [
        '鱼豆腐',
        '方便面',
        '意面',
        '意大利面',
    ]


def main():
    titles = []
    # titles.extend(get_titles_from_file())
    titles.extend(get_titles())

    for title in titles:
        cut_txt(title, 'c1')

    jieba.load_userdict('recipe.txt')
    jieba.del_word('红海')
    jieba.del_word('超快')
    jieba.del_word('炒鱿鱼')
    jieba.del_word('手上')
    jieba.del_word('手版')
    jieba.del_word('烤鸡')
    jieba.del_word('烧鸡')
    jieba.del_word('炖鸡')
    jieba.del_word('咖喱鸡')
    jieba.del_word('大利')

    for title in titles:
        cut_txt(title, 'c2')

    for txt, data in list(recipe_title_data.items()):
        t1 = data["c1"]
        t2 = data["c2"]
        r = '==' if t1 == t2 else 'xx'
        print(f'{txt} -> {t1} ## {t2} {r}')
    print(len(recipe_title_data))


if __name__ == '__main__':
    main()
