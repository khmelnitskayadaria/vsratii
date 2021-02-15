import telepot
token = '1655604294:AAFxRUT-pnpVi3Hji091JhbuG_H83ILoKFY'
global TelegramBot
TelegramBot = telepot.Bot(token)
print(TelegramBot.getMe())

TelegramBot.getUpdates()
[{u'message': {u'date': 1459927254, u'text': u'/start', u'from': {u'username': u'vsratorecommends_bot', u'first_name': u'vsratorecommends', u'id': 1655604294}, u'message_id': 1, u'chat': {u'username': u'vsratorecommends_bot', u'first_name': u'vsratorecommends', u'type': u'private', u'id': 7350}}, u'update_id': 649179764}]


# /Users/dkhmelnitskaya/PycharmProjects/telegram/venv/bin/python /Users/dkhmelnitskaya/PycharmProjects/telegram/bot.py
# {'id': 1655604294, 'is_bot': True, 'first_name': 'vsratorecommends', 'username': 'vsratorecommends_bot', 'can_join_groups': True, 'can_read_all_group_messages': False, 'supports_inline_queries': False}
#
# Process finished with exit code 0