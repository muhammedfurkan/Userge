import asyncio
import os
import sys
import time
from random import choice, randint

from userge import Config, Filters, Message, get_collection, userge
from userge.utils import time_formatter

PM_LOGGR_BOT_API_ID = int(-385618434)
PM_LOGGER = True


@userge.on_filters(Filters.private & Filters.outgoing & ~allowAllFilter)
async def outgoing_auto_approve(message: Message):
    check_bot = message.from_user.is_bot
    chat_id = message.from_user.id
    my_id = await userge.get_me()
    my_id = my_id.id
    if not check_bot and PM_LOGGER:
        try:
            await userge.forward_messages(
                chat_id=chat_id,
                from_chat_id=PM_LOGGR_BOT_API_ID,
                message_ids=message.message_id
            )
        except Exception as err:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            print(err)
