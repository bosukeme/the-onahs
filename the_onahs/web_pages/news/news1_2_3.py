class SliderSection:

    @classmethod
    def slider1(cls):

        header_text = "Pharmacy Emblem"
        short_description = f"Pharmacy Emblem is cool to have in your premises.\
                            Instead of spending much money to do a signage, \
                                acquiring this can save the purpose. <br> <u> <a href='http://127.0.0.1:5000/news/{header_text}'> Read more ...</a></u> "

        slider_images = [
            "/static/images/WhatsAppImage2023-10-19at12.35.20PM.jpeg",
            "/static/images/WhatsAppImage2023-10-17at3.17.31PM.jpeg"
        ]

        text_list = [
            "Pharmacy Emblem is cool to have in your premises. Instead of spending much money to do a signage, acquiring this can save the purpose",
            "This is the second paragrah"
            ]
        sub_header_text = "hey"

        data = {
            "header_text": header_text,
            "short_description": short_description,
            "images": slider_images,
            "text_list": text_list,
            "sub_header_text": sub_header_text
        }

        return data

    @classmethod
    def slider2(cls):

        header_text = "Jewel City 2023"
        short_description = f"Jewel City 2023 Nestled in the northeastern region of Nigeria, \
                            Gombe State is a hidden gem waiting to be discovered by \
                                adventurous travelers. <br> <u> <a href='http://127.0.0.1:5000/news/{header_text}'> Read more ...</a></u>"
        slider_images = [
            "/static/images/jewel.jpeg",
            "/static/images/jewel1.jpeg"
        ]

        text_list = [
            "Jewel City 2023 Nestled in the northeastern region of Nigeria, Gombe State is a hidden gem waiting to be discovered by adventurous travelers.",
            "Another paragrash should be here",
            ]

        sub_header_text = "hey"

        data = {
            "header_text": header_text,
            "short_description": short_description,
            "images": slider_images,
            "text_list": text_list,
            "sub_header_text": sub_header_text
        }

        return data

    @classmethod
    def slider3(cls):

        header_text = "Ibom Day 2023"
        short_description = f"Ibom Day 2023 is a day set aside for community pharmacist practicing in AKWA IBOM to ..... \
                            <br> <u> <a href='http://127.0.0.1:5000/news/{header_text}'> Read more ...</a></u>"

        slider_images = [
            "/static/images/ibomday.enc",
            "/static/images/ibomday.enc"
        ]
        text_list = [
            "Ibom Day 2023 is a day set aside for community pharmacist practicing in AKWA IBOM to ..... ",
            "Another paragraph should be here",
            ]

        sub_header_text = "hey"

        data = {
            "header_text": header_text,
            "short_description": short_description,
            "images": slider_images,
            "text_list": text_list,
            "sub_header_text": sub_header_text
        }

        return data


def collate_news_123():

    slider_section = SliderSection()

    slider1 = slider_section.slider1()
    slider2 = slider_section.slider2()
    slider3 = slider_section.slider3()

    news123 = {
        slider1['header_text']: {
            "header_text": slider1['header_text'],
            "sub_header_text": slider1['sub_header_text'],
            "short_description": slider1['short_description'],
            "images": slider1['images'],
            "text_list": slider1['text_list']
            },

        slider2['header_text']: {
            "header_text": slider2['header_text'],
            "sub_header_text": slider2['sub_header_text'],
            "short_description": slider2['short_description'],
            "images": slider2['images'],
            "text_list": slider2['text_list']
            },

        slider3['header_text']: {
            "header_text": slider3['header_text'],
            "sub_header_text": slider3['sub_header_text'],
            "short_description": slider3['short_description'],
            "images": slider3['images'],
            "text_list": slider3['text_list']
            }
    }

    return news123, slider1, slider2, slider3
