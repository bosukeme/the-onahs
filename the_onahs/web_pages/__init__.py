from the_onahs.web_pages.news import collate_news


def get_news(text_header: str):
    all_news = collate_news()
    news = all_news[text_header]

    data = {
        "news": news
        }

    return data
