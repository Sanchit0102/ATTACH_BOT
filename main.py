import os
import config
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


Bot = Client(
    "Attach Bot",
    bot_token=config.BOT_TOKEN,
    api_id=config.API_ID,
    api_hash=config.API_HASH
)


START_TEXT = """Hello {},
I am a media or file in a message attach bot. \n
I can attach photo, video, audio etc. using their public links in a message.
"""
HELP_TEXT = """**More Help**

**Steps :-**
- Just send a html or markdown message
- Reply a link for attaching

**Tips :-**
• Use Telegram public channel or group message links
• You can send any type of links for attaching"""

ABOUT_TEXT = """**About Me**

- **Bot :** `Attach Bot`
- **Developer :** [🥱](https://telegram.me/THE_DS_OFFICIAL)
- **Language :** [Python3](https://python.org)
- **Library :** [Pyrogram](https://pyrogram.org)"""

START_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('Updates', url='https://telegram.me/The_SILENT_TEAMS')
        ],
        [
            InlineKeyboardButton('Help', callback_data='help'),
            InlineKeyboardButton('About', callback_data='about'),
            InlineKeyboardButton('Close', callback_data='close')
        ]
    ]
)

HELP_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('Home', callback_data='home'),
            InlineKeyboardButton('About', callback_data='about'),
            InlineKeyboardButton('Close', callback_data='close')
        ]
    ]
)

ABOUT_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('Home', callback_data='home'),
            InlineKeyboardButton('Help', callback_data='help'),
            InlineKeyboardButton('Close', callback_data='close')
        ]
    ]
)


@Bot.on_callback_query()
async def cb_handler(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            reply_markup=START_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            reply_markup=HELP_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            reply_markup=ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await update.message.delete()


@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=START_BUTTONS
    )


@Bot.on_message(filters.private & filters.command(["help"]))
async def help(bot, update):
    await update.reply_text(
        text=HELP_TEXT,
        disable_web_page_preview=True,
        reply_markup=HELP_BUTTONS
    )


@Bot.on_message(filters.private & filters.command(["about"]))
async def about(bot, update):
    await update.reply_text(
        text=ABOUT_TEXT,
        disable_web_page_preview=True,
        reply_markup=ABOUT_BUTTONS
    )


@Bot.on_message(filters.text & filters.private & filters.reply & filters.regex(r'https?://[^\s]+'))
async def attach(bot, update):
    await update.reply_text(
        text=f"[\u2063]({update.text}){update.reply_to_message.text}",
        reply_markup=update.reply_to_message.reply_markup
    )


Bot.run()
