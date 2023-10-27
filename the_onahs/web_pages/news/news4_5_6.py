class News456:
    @classmethod
    def news4(cls):

        header_text = "Pharm XYZ Child Dedication"
        sub_header_text = "Celebration of a baby"

        image_path = ["/static/images/5453.jpg"]

        text_list = ["Pharmacist XYZ wishes to invite everyone to the dedication of his beautiful daugther",
                     "This is the second paragrah"
                     ]

        data = {
            "header_text": header_text,
            "sub_header_text": sub_header_text,
            "images": image_path,
            "text_list": text_list,
        }

        return data

    @classmethod
    def news5(cls):

        header_text = "Pharm ABC Child Dedication"
        sub_header_text = "Celebration of a baby"

        image_path = ["/static/images/sss.jpg"]

        text_list = ["Pharmacist ABC wishes to invite everyone to the dedication of his beautiful daugther",
                     "This is the second paragrah"
                     ]

        data = {
            "header_text": header_text,
            "sub_header_text": sub_header_text,
            "images": image_path,
            "text_list": text_list,
        }

        return data

    @classmethod
    def news6(cls):

        header_text = "Pharm DEF Child Dedication"
        sub_header_text = "Celebration of a baby"

        image_path = ["/static/images/656.jpg"]

        text_list = ["Pharmacist DEF wishes to invite everyone to the dedication of his beautiful daugther",
                     "This is the second paragrah"
                     ]

        data = {
            "header_text": header_text,
            "sub_header_text": sub_header_text,
            "images": image_path,
            "text_list": text_list,
        }

        return data


def collate_news_456():

    news_section = News456()
    news4 = news_section.news4()
    news5 = news_section.news5()
    news6 = news_section.news6()

    news456 = {
            news4['header_text']: {
                    "header_text": news4['header_text'],
                    "sub_header_text": news4['sub_header_text'],
                    "images": news4['images'],
                    "text_list": news4['text_list']
                    },

            news5['header_text']: {
                    "header_text": news5['header_text'],
                    "sub_header_text": news5['sub_header_text'],
                    "images": news5['images'],
                    "text_list": news5['text_list']
                    },

            news6['header_text']: {
                    "header_text": news6['header_text'],
                    "sub_header_text": news6['sub_header_text'],
                    "images": news6['images'],
                    "text_list": news6['text_list']
                    },
            }
    return news456, news4, news5, news6
