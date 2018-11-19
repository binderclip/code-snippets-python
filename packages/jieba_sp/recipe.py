import jieba


def cut_txt(txt: str):
    seg_list = jieba.cut(txt, cut_all=False)
    print(f"{txt} -> " + " | ".join(seg_list))  # 精确模式



def main():
    jieba.load_userdict('recipe.txt')

    titles = [
        '冻干水果牛轧糖',
        '老北京烫饭',
        '芋头蛋卷',
        '葱油芋头',
    ]
    for title in titles:
        cut_txt(title)


if __name__ == '__main__':
    main()
