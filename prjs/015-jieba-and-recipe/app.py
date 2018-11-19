from collections import defaultdict

import jieba


recipe_title_data = defaultdict(dict)


def cut_txt(txt: str, mark: str):
    seg_list = jieba.cut(txt, cut_all=False)
    # print(f"{txt} -> " + " | ".join(seg_list))  # 精确模式
    recipe_title_data[txt][mark] = "_".join(seg_list)


def main():
    titles = []
    with open('recipe_titles.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            _line = line.strip()
            if not _line:
                continue
            titles.append(_line)

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

    for title in titles:
        cut_txt(title, 'c2')

    for txt, data in list(recipe_title_data.items())[1175:1200]:
        t1 = data["c1"]
        t2 = data["c2"]
        r = '==' if t1 == t2 else 'xx'
        print(f'{txt} -> {t1} ## {t2} {r}')
    print(len(recipe_title_data))


if __name__ == '__main__':
    main()
