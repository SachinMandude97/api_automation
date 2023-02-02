import random


class CreatePayload():

    def create_title(self):
        text = ""
        possible = "abcdefghijklmnopqrstuvwxyz0123456789"

        for i in range(5):
            text += text.join(random.choices(possible))

        return text
        # print(text)
    # def username(self):
    #     text = ''
    #     possible = "abcdefghijklmnopqrstuvwxyz0123456789"
    #
    #     for i in range(5):
    #         text += text.join(random.choices(possible))
    #
    #     return text

# load = CreatePayload()
# load.create_title()
