from linebot.models import (
    TextSendMessage, ImageSendMessage,
)
import random

def create_message(input):

    janken = ['グー', 'チョキ', 'パー']

    if input not in janken:
        with open('memory.txt', 'w') as f:
            f.write(input)

        if input in memory:
            message = TextSendMessage(text = '同じこと言うの禁止')

            return message
        else:
            if
            message = TextSendMessage(text = 'こんにちは！\nじゃんけんしよー\n\nあ、グー・チョキ・パーのどれかで入力してな')

            return message
    else:
        reply = random.choice(janken)
        message = TextSendMessage(reply)

        return message

def save_file_at_new_dir(new_dir_path, new_filename, new_file_content, mode='w'):
    os.makedirs(new_dir_path, exist_ok=True)
    with open(os.path.join(new_dir_path, new_filename), mode) as f:
        f.write(new_file_content)


        """
        message = ImageSendMessage(
        preview_image_url = 'https://madao-line-bot-01.herokuapp.com/images/nagaku_naru.png',
        original_content_url = 'https://madao-line-bot-01.herokuapp.com/images/nagaku_naru.png'
        """





"""

    # じゃんけん
    if input not in janken:
        message = TextSendMessage('じゃんけんしようよ\nグー・チョキ・パーのどれかを入力してね')

        return message
    else:
        reply = random.choice(janken)
        message = TextSendMessage(reply)
        return message

"""
