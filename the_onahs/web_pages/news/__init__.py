from the_onahs.web_pages.news.news1_2_3 import collate_news_123
from the_onahs.web_pages.news.news4_5_6 import collate_news_456


def collate_news():

    news123, _, _, _ = collate_news_123()
    news456, _, _, _ = collate_news_456()

    news_data_inner = {}

    for key, value in news123.items():
        _dict = {key: value}
        news_data_inner.update(_dict)

    for key, value in news456.items():
        _dict = {key: value}
        news_data_inner.update(_dict)

    return news_data_inner
