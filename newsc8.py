# -*- coding: utf-8 -*-

from LineAPI.linepy import *
from LineAPI.akad.ttypes import Message
from LineAPI.akad.ttypes import ContentType as Type
from gtts import gTTS
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from googletrans import Translator
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, six, ast, pytz, urllib, urllib3, urllib.parse, traceback, atexit, subprocess

ririn = LINE("Eve16JwCcBsrTYfusNi5.fj0S/qYKVWGRwpehA8QPbq./EpXPM8XdmUTi+mYh6VKpqyctFD+PnBlxQZbJo1uwxQ=")
#ririn = LINE("")
ririnMid = ririn.profile.mid
ririnProfile = ririn.getProfile()
ririnSettings = ririn.getSettings()
ririnPoll = OEPoll(ririn)
botStart = time.time()

print ("╔═════════════════════════\n║╔════════════════════════\n║╠❂➣ DNA BERHASIL LOGIN\n║╚════════════════════════\n╚═════════════════════════")

msg_dict = {}

wait = {
    "autoAdd": True,
    "autoJoin": True,
    "autoLeave": False,
    "autoRead": False,
    "autoRespon": True,
    "autoResponPc": True,
    "autoJoinTicket": True,
    "checkContact": False,
    "checkPost": False,
    "checkSticker": False,
    "changePictureProfile": False,
    "changeGroupPicture": [],
    "keyCommand": "",
    "myProfile": {
        "displayName": "",
        "coverId": "",
        "pictureStatus": "",
        "statusMessage": ""
    },
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    },
    "Protectcancel": True,
    "Protectgr": True,
    "Protectinvite": True,
    "Protectjoin": False,
    "setKey": False,
    "sider": False,
    "unsendMessage": True
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

read = {
    "ROM": {},
    "readPoint": {},
    "readMember": {},
    "readTime": {}
}

list_language = {
    "list_textToSpeech": {
        "id": "Indonesia",
        "af" : "Afrikaans",
        "sq" : "Albanian",
        "ar" : "Arabic",
        "hy" : "Armenian",
        "bn" : "Bengali",
        "ca" : "Catalan",
        "zh" : "Chinese",
        "zh-cn" : "Chinese (Mandarin/China)",
        "zh-tw" : "Chinese (Mandarin/Taiwan)",
        "zh-yue" : "Chinese (Cantonese)",
        "hr" : "Croatian",
        "cs" : "Czech",
        "da" : "Danish",
        "nl" : "Dutch",
        "en" : "English",
        "en-au" : "English (Australia)",
        "en-uk" : "English (United Kingdom)",
        "en-us" : "English (United States)",
        "eo" : "Esperanto",
        "fi" : "Finnish",
        "fr" : "French",
        "de" : "German",
        "el" : "Greek",
        "hi" : "Hindi",
        "hu" : "Hungarian",
        "is" : "Icelandic",
        "id" : "Indonesian",
        "it" : "Italian",
        "ja" : "Japanese",
        "km" : "Khmer (Cambodian)",
        "ko" : "Korean",
        "la" : "Latin",
        "lv" : "Latvian",
        "mk" : "Macedonian",
        "no" : "Norwegian",
        "pl" : "Polish",
        "pt" : "Portuguese",
        "ro" : "Romanian",
        "ru" : "Russian",
        "sr" : "Serbian",
        "si" : "Sinhala",
        "sk" : "Slovak",
        "es" : "Spanish",
        "es-es" : "Spanish (Spain)",
        "es-us" : "Spanish (United States)",
        "sw" : "Swahili",
        "sv" : "Swedish",
        "ta" : "Tamil",
        "th" : "Thai",
        "tr" : "Turkish",
        "uk" : "Ukrainian",
        "vi" : "Vietnamese",
        "cy" : "Welsh"
    },
    "list_translate": {    
        "af": "afrikaans",
        "sq": "albanian",
        "am": "amharic",
        "ar": "arabic",
        "hy": "armenian",
        "az": "azerbaijani",
        "eu": "basque",
        "be": "belarusian",
        "bn": "bengali",
        "bs": "bosnian",
        "bg": "bulgarian",
        "ca": "catalan",
        "ceb": "cebuano",
        "ny": "chichewa",
        "zh-cn": "chinese (simplified)",
        "zh-tw": "chinese (traditional)",
        "co": "corsican",
        "hr": "croatian",
        "cs": "czech",
        "da": "danish",
        "nl": "dutch",
        "en": "english",
        "eo": "esperanto",
        "et": "estonian",
        "tl": "filipino",
        "fi": "finnish",
        "fr": "french",
        "fy": "frisian",
        "gl": "galician",
        "ka": "georgian",
        "de": "german",
        "el": "greek",
        "gu": "gujarati",
        "ht": "haitian creole",
        "ha": "hausa",
        "haw": "hawaiian",
        "iw": "hebrew",
        "hi": "hindi",
        "hmn": "hmong",
        "hu": "hungarian",
        "is": "icelandic",
        "ig": "igbo",
        "id": "indonesian",
        "ga": "irish",
        "it": "italian",
        "ja": "japanese",
        "jw": "javanese",
        "kn": "kannada",
        "kk": "kazakh",
        "km": "khmer",
        "ko": "korean",
        "ku": "kurdish (kurmanji)",
        "ky": "kyrgyz",
        "lo": "lao",
        "la": "latin",
        "lv": "latvian",
        "lt": "lithuanian",
        "lb": "luxembourgish",
        "mk": "macedonian",
        "mg": "malagasy",
        "ms": "malay",
        "ml": "malayalam",
        "mt": "maltese",
        "mi": "maori",
        "mr": "marathi",
        "mn": "mongolian",
        "my": "myanmar (burmese)",
        "ne": "nepali",
        "no": "norwegian",
        "ps": "pashto",
        "fa": "persian",
        "pl": "polish",
        "pt": "portuguese",
        "pa": "punjabi",
        "ro": "romanian",
        "ru": "russian",
        "sm": "samoan",
        "gd": "scots gaelic",
        "sr": "serbian",
        "st": "sesotho",
        "sn": "shona",
        "sd": "sindhi",
        "si": "sinhala",
        "sk": "slovak",
        "sl": "slovenian",
        "so": "somali",
        "es": "spanish",
        "su": "sundanese",
        "sw": "swahili",
        "sv": "swedish",
        "tg": "tajik",
        "ta": "tamil",
        "te": "telugu",
        "th": "thai",
        "tr": "turkish",
        "uk": "ukrainian",
        "ur": "urdu",
        "uz": "uzbek",
        "vi": "vietnamese",
        "cy": "welsh",
        "xh": "xhosa",
        "yi": "yiddish",
        "yo": "yoruba",
        "zu": "zulu",
        "fil": "Filipino",
        "he": "Hebrew"
    }
}

try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")
    
wait["myProfile"]["displayName"] = ririnProfile.displayName
wait["myProfile"]["statusMessage"] = ririnProfile.statusMessage
wait["myProfile"]["pictureStatus"] = ririnProfile.pictureStatus
coverId = ririn.getProfileDetail()["result"]["objectId"]
wait["myProfile"]["coverId"] = coverId

def restartBot():
    print ("[ INFO ] BOT RESTART")
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    ririn.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))

def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                ririn.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]
            
def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        ririn.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        ririn.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMessage(to, Message, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes._from = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        line.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)

        
def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "╔══[Mention {} User]\n╠ ".format(str(len(mid)))
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "╠ "
            else:
                try:
                    textx += "╚══[ {} ]".format(str(ririn.getGroup(to).name))
                except:
                    pass
        ririn.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        ririn.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def command(text):
    pesan = text.lower()
    if wait["setKey"] == True:
        if pesan.startswith(wait["keyCommand"]):
            cmd = pesan.replace(wait["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
    
def helpmessage():
    if wait['setKey'] == True:
        key = wait['keyCommand']
    else:
        key = ''
    helpMessage =   "╔════════════════════╗" + "\n" + \
                    "                    ✰ ᴅɴᴀ ʙᴏᴛ ✰" + "\n" + \
                    "╚════════════════════╝" + "\n" + \
                    "╔════════════════════╗" + "\n" + \
                    "                ◄]·✪·Public·✪·[►" + "\n" + \
                    "╠════════════════════╝" + "\n" + \
                    "╠❂➣ " + key + "ᴛʀᴀɴsʟᴀᴛᴇ " + "\n" + \
                    "╠❂➣ " + key + "ᴛᴛs " + "\n" + \
                    "╠❂➣ " + key + "ᴍᴇ" + "\n" + \
                    "╠❂➣ " + key + "ᴍʏᴍɪᴅ" + "\n" + \
                    "╠❂➣ " + key + "ᴍʏɴᴀᴍᴇ" + "\n" + \
                    "╠❂➣ " + key + "ᴍʏʙɪᴏ" + "\n" + \
                    "╠❂➣ " + key + "ᴍʏᴘɪᴄᴛᴜʀᴇ" + "\n" + \
                    "╠❂➣ " + key + "ᴍʏᴠɪᴅᴇᴏᴘʀᴏғɪʟᴇ" + "\n" + \
                    "╠❂➣ " + key + "ᴍʏᴄᴏᴠᴇʀ" + "\n" + \
                    "╠❂➣ " + key + "ɢʀᴏᴜᴘᴄʀᴇᴀᴛᴏʀ" + "\n" + \
                    "╠❂➣ " + key + "ɢʀᴏᴜᴘɪᴅ" + "\n" + \
                    "╠❂➣ " + key + "ɢʀᴏᴜᴘɴᴀᴍᴇ" + "\n" + \
                    "╠❂➣ " + key + "ɢʀᴏᴜᴘᴘɪᴄᴛᴜʀᴇ" + "\n" + \
                    "╠❂➣ " + key + "ᴍᴇɴᴛɪᴏɴ" + "\n" + \
                    "╠❂➣ " + key + "ʟᴜʀᴋɪɴɢ「ᴏɴ/ᴏғғ/ʀᴇsᴇᴛ」" + "\n" + \
                    "╠❂➣ " + key + "ʟᴜʀᴋɪɴɢ" + "\n" + \
                    "╠════════════════════╗" + "\n" + \
                    "                ◄]·✪·Admin·✪·[►" + "\n" + \
                    "╠════════════════════╝" + "\n" + \
                    "╠❂➣ " + key + "sᴘ" + "\n" + \
                    "╠❂➣ " + key + "sᴘᴇᴇᴅ" + "\n" + \
                    "╠❂➣ " + key + "sᴛᴀᴛᴜs" + "\n" + \
                    "╠❂➣ " + key + "sᴇᴛ" + "\n" + \
                    "╠❂➣ ᴍʏᴋᴇʏ" + "\n" + \
                    "╠❂➣ sᴇᴛᴋᴇʏ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╠❂➣ " + key + "ᴄʜᴇᴄᴋᴄᴏɴᴛᴀᴄᴛ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╠❂➣ " + key + "ᴄʜᴇᴄᴋᴘᴏsᴛ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╠❂➣ " + key + "ᴄʜᴇᴄᴋsᴛɪᴄᴋᴇʀ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╠❂➣ " + key + "sᴛᴇᴀʟᴄᴏɴᴛᴀᴄᴛ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
                    "╠❂➣ " + key + "sᴛᴇᴀʟᴍɪᴅ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
                    "╠❂➣ " + key + "sᴛᴇᴀʟɴᴀᴍᴇ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
                    "╠❂➣ " + key + "sᴛᴇᴀʟʙɪᴏ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
                    "╠❂➣ " + key + "sᴛᴇᴀʟᴘɪᴄᴛᴜʀᴇ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
                    "╠❂➣ " + key + "sᴛᴇᴀʟᴠɪᴅᴇᴏᴘʀᴏғɪʟᴇ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
                    "╠❂➣ " + key + "sᴛᴇᴀʟᴄᴏᴠᴇʀ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
                    "╠❂➣ " + key + "ɢʀᴏᴜᴘᴛɪᴄᴋᴇᴛ" + "\n" + \
                    "╠❂➣ " + key + "ɢʀᴏᴜᴘᴛɪᴄᴋᴇᴛ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╠❂➣ " + key + "ɢʀᴏᴜᴘᴍᴇᴍʙᴇʀʟɪsᴛ" + "\n" + \
                    "╠❂➣ " + key + "ɢʀᴏᴜᴘɪɴғᴏ" + "\n" + \
                    "╠❂➣ " + key + "ᴄʜᴀɴɢᴇɢʀᴏᴜᴘᴘɪᴄᴛᴜʀᴇ" + "\n" + \
                    "╠❂➣ " + key + "ᴍɪᴍɪᴄ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╠❂➣ " + key + "ᴍɪᴍɪᴄʟɪsᴛ" + "\n" + \
                    "╠❂➣ " + key + "ᴍɪᴍɪᴄᴀᴅᴅ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
                    "╠❂➣ " + key + "ᴍɪᴍɪᴄᴅᴇʟ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
                    "╠❂➣ " + key + "ᴄʜᴇᴄᴋᴅᴀᴛᴇ「ᴅᴀᴛᴇ」" + "\n" + \
                    "╠❂➣ " + key + "ᴄʜᴇᴄᴋᴡᴇʙsɪᴛᴇ「ᴜʀʟ」" + "\n" + \
                    "╠❂➣ " + key + "ᴄʜᴇᴄᴋᴘʀᴀʏᴛɪᴍᴇ「ʟᴏᴄᴀᴛɪᴏɴ」" + "\n" + \
                    "╠❂➣ " + key + "ᴄʜᴇᴄᴋᴡᴇᴀᴛʜᴇʀ「ʟᴏᴄᴀᴛɪᴏɴ」" + "\n" + \
                    "╠❂➣ " + key + "ᴄʜᴇᴄᴋʟᴏᴄᴀᴛɪᴏɴ「ʟᴏᴄᴀᴛɪᴏɴ」" + "\n" + \
                    "╠❂➣ " + key + "ɪɴsᴛᴀɪɴғᴏ 「ᴜsᴇʀɴᴀᴍᴇ」" + "\n" + \
                    "╠❂➣ " + key + "sᴇᴀʀᴄʜʏᴏᴜᴛᴜʙᴇ「sᴇᴀʀᴄʜ」" + "\n" + \
                    "╠❂➣ " + key + "sᴇᴀʀᴄʜᴍᴜsɪᴄ 「sᴇᴀʀᴄʜ」" + "\n" + \
                    "╠❂➣ " + key + "sᴇᴀʀᴄʜʟʏʀɪᴄ 「sᴇᴀʀᴄʜ」" + "\n" + \
                    "╠❂➣ " + key + "sᴇᴀʀᴄʜɪᴍᴀɢᴇ 「sᴇᴀʀᴄʜ」" + "\n" + \
                    "╠❂➣ " + key + "sɪᴅᴇʀ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╠════════════════════╗" + "\n" + \
                    "                 ◄]·✪·Owner·✪·[►" + "\n" + \
                    "╠════════════════════╝" + "\n" + \
                    "╠❂➣ " + key + "ʀᴇsᴛᴀʀᴛ" + "\n" + \
                    "╠❂➣ " + key + "ʀᴜɴᴛɪᴍᴇ" + "\n" + \
                    "╠❂➣ " + key + "ᴀᴜᴛᴏᴀᴅᴅ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╠❂➣ " + key + "ᴀᴜᴛᴏᴊᴏɪɴ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╠❂➣ " + key + "ᴀᴜᴛᴏᴊᴏɪɴᴛɪᴄᴋᴇᴛ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╠❂➣ " + key + "ᴀᴜᴛᴏʟᴇᴀᴠᴇ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╠❂➣ " + key + "ᴀᴜᴛᴏʀᴇᴀᴅ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╠❂➣ " + key + "ᴀᴜᴛᴏʀᴇsᴘᴏɴ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╠❂➣ " + key + "ᴀᴜᴛᴏʀᴇsᴘᴏɴᴘᴄ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╠❂➣ " + key + "ᴜɴsᴇɴᴅᴄʜᴀᴛ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╠❂➣ " + key + "ᴄʜᴀɴɢᴇɴᴀᴍᴇ:「ǫᴜᴇʀʏ」" + "\n" + \
                    "╠❂➣ " + key + "ᴄʜᴀɴɢᴇʙɪᴏ:「ǫᴜᴇʀʏ」" + "\n" + \
                    "╠❂➣ " + key + "ᴄʟᴏɴᴇᴘʀᴏғɪʟᴇ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
                    "╠❂➣ " + key + "ʀᴇsᴛᴏʀᴇᴘʀᴏғɪʟᴇ" + "\n" + \
                    "╠❂➣ " + key + "ʙᴀᴄᴋᴜᴘᴘʀᴏғɪʟᴇ" + "\n" + \
                    "╠❂➣ " + key + "ᴄʜᴀɴɢᴇᴘɪᴄᴛᴜʀᴇᴘʀᴏғɪʟᴇ" + "\n" + \
                    "╠❂➣ " + key + "ɢʀᴏᴜᴘʟɪsᴛ" + "\n" + \
                    "╠════════════════════╗" + "\n" + \
                    "               ᴄʀᴇᴅɪᴛs ʙʏ : ©ᴅ̶ᴇ̶ᴇ̶ ✯" + "\n" + \
                    "╚════════════════════╝" + "\n" + \
                    "╔════════════════════╗" + "\n" + \
                    "                   ✰ ᴅɴᴀ ʙᴏᴛ  ✰" + "\n" + \
                    "╚════════════════════╝"
    return helpMessage

def helptexttospeech():
    if wait['setKey'] == True:
        key = wait['keyCommand']
    else:
        key = ''
    helpTextToSpeech =  "╔════════════════════╗" + "\n" + \
                        "                    ✰ ᴅɴᴀ ʙᴏᴛ ✰" + "\n" + \
                        "╚════════════════════╝" + "\n" + \
                        "╔════════════════════╗" + "\n" + \
                        "          ◄]·✪·ᴛᴇxᴛᴛᴏsᴘᴇᴇᴄʜ·✪·[►" + "\n" + \
                        "╠════════════════════╝ " + "\n" + \
                        "╠❂➣ " + key + "ᴀғ : ᴀғʀɪᴋᴀᴀɴs" + "\n" + \
                        "╠❂➣ " + key + "sǫ : ᴀʟʙᴀɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴀʀ : ᴀʀᴀʙɪᴄ" + "\n" + \
                        "╠❂➣ " + key + "ʜʏ : ᴀʀᴍᴇɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʙɴ : ʙᴇɴɢᴀʟɪ" + "\n" + \
                        "╠❂➣ " + key + "ᴄᴀ : ᴄᴀᴛᴀʟᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴢʜ : ᴄʜɪɴᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ᴢʜʏᴜᴇ : ᴄʜɪɴᴇsᴇ (ᴄᴀɴᴛᴏɴᴇsᴇ)" + "\n" + \
                        "╠❂➣ " + key + "ʜʀ : ᴄʀᴏᴀᴛɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴄs : ᴄᴢᴇᴄʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴅᴀ : ᴅᴀɴɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ɴʟ : ᴅᴜᴛᴄʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴇɴ : ᴇɴɢʟɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴇɴᴀᴜ : ᴇɴɢʟɪsʜ (ᴀᴜsᴛʀᴀʟɪᴀ)" + "\n" + \
                        "╠❂➣ " + key + "ᴇɴᴜᴋ : ᴇɴɢʟɪsʜ (ᴜᴋ)" + "\n" + \
                        "╠❂➣ " + key + "ᴇɴᴜs : ᴇɴɢʟɪsʜ (ᴜs)" + "\n" + \
                        "╠❂➣ " + key + "ᴇᴏ : ᴇsᴘᴇʀᴀɴᴛᴏ" + "\n" + \
                        "╠❂➣ " + key + "ғɪ : ғɪɴɴɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ғʀ : ғʀᴇɴᴄʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴅᴇ : ɢᴇʀᴍᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴇʟ : ɢʀᴇᴇᴋ" + "\n" + \
                        "╠❂➣ " + key + "ʜɪ : ʜɪɴᴅɪ" + "\n" + \
                        "╠❂➣ " + key + "ʜᴜ : ʜᴜɴɢᴀʀɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ɪs : ɪᴄᴇʟᴀɴᴅɪᴄ" + "\n" + \
                        "╠❂➣ " + key + "ɪᴅ : ɪɴᴅᴏɴᴇsɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ɪᴛ : ɪᴛᴀʟɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴊᴀ : ᴊᴀᴘᴀɴᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ᴋᴍ : ᴋʜᴍᴇʀ (ᴄᴀᴍʙᴏᴅɪᴀɴ)" + "\n" + \
                        "╠❂➣ " + key + "ᴋᴏ : ᴋᴏʀᴇᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʟᴀ : ʟᴀᴛɪɴ" + "\n" + \
                        "╠❂➣ " + key + "ʟᴠ : ʟᴀᴛᴠɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴍᴋ : ᴍᴀᴄᴇᴅᴏɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ɴᴏ : ɴᴏʀᴡᴇɢɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴘʟ : ᴘᴏʟɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴘᴛ : ᴘᴏʀᴛᴜɢᴜᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ʀᴏ : ʀᴏᴍᴀɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʀᴜ : ʀᴜssɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "sʀ : sᴇʀʙɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "sɪ : sɪɴʜᴀʟᴀ" + "\n" + \
                        "╠❂➣ " + key + "sᴋ : sʟᴏᴠᴀᴋ" + "\n" + \
                        "╠❂➣ " + key + "ᴇs : sᴘᴀɴɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴇsᴇs : sᴘᴀɴɪsʜ (sᴘᴀɪɴ)" + "\n" + \
                        "╠❂➣ " + key + "ᴇsᴜs : sᴘᴀɴɪsʜ (ᴜs)" + "\n" + \
                        "╠❂➣ " + key + "sᴡ : sᴡᴀʜɪʟɪ" + "\n" + \
                        "╠❂➣ " + key + "sᴠ : sᴡᴇᴅɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴛᴀ : ᴛᴀᴍɪʟ" + "\n" + \
                        "╠❂➣ " + key + "ᴛʜ : ᴛʜᴀɪ" + "\n" + \
                        "╠❂➣ " + key + "ᴛʀ : ᴛᴜʀᴋɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴜᴋ : ᴜᴋʀᴀɪɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴠɪ : ᴠɪᴇᴛɴᴀᴍᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ᴄʏ : ᴡᴇʟsʜ" + "\n" + \
                        "╠════════════════════╗" + "\n" + \
                        "               ᴄʀᴇᴅɪᴛs ʙʏ : ©ᴅ̶ᴇ̶ᴇ̶ ✯" + "\n" + \
                        "╚════════════════════╝" + "\n" + \
                        "╔════════════════════╗" + "\n" + \
                        "                    ✰ ᴅɴᴀ ʙᴏᴛ ✰" + "\n" + \
                        "╚════════════════════╝" + "\n" + \
                        "ᴄᴏɴᴛᴏʜ : " + key + "sᴀʏ-ɪᴅ ʀɪʀɪɴ"
    return helpTextToSpeech

def helptranslate():
    if wait['setKey'] == True:
        key = wait['keyCommand']
    else:
        key = ''
    helpTranslate = "╔════════════════════╗" + "\n" + \
                        "                     ✰ ᴅɴᴀ ʙᴏᴛ ✰" + "\n" + \
                        "╚════════════════════╝" + "\n" + \
                        "╔════════════════════╗" + "\n" + \
                        "             ◄]·✪·ᴛʀᴀɴsʟᴀᴛᴇ·✪·[►" + "\n" + \
                        "╠════════════════════╝" + "\n" + \
                        "╠❂➣ " + key + "ᴀғ : ᴀғʀɪᴋᴀᴀɴs" + "\n" + \
                        "╠❂➣ " + key + "sǫ : ᴀʟʙᴀɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴀᴍ : ᴀᴍʜᴀʀɪᴄ" + "\n" + \
                        "╠❂➣ " + key + "ᴀʀ : ᴀʀᴀʙɪᴄ" + "\n" + \
                        "╠❂➣ " + key + "ʜʏ : ᴀʀᴍᴇɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴀᴢ : ᴀᴢᴇʀʙᴀɪᴊᴀɴɪ" + "\n" + \
                        "╠❂➣ " + key + "ᴇᴜ : ʙᴀsǫᴜᴇ" + "\n" + \
                        "╠❂➣ " + key + "ʙᴇ : ʙᴇʟᴀʀᴜsɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʙɴ : ʙᴇɴɢᴀʟɪ" + "\n" + \
                        "╠❂➣ " + key + "ʙs : ʙᴏsɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʙɢ : ʙᴜʟɢᴀʀɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴄᴀ : ᴄᴀᴛᴀʟᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴄᴇʙ : ᴄᴇʙᴜᴀɴᴏ" + "\n" + \
                        "╠❂➣ " + key + "ɴʏ : ᴄʜɪᴄʜᴇᴡᴀ" + "\n" + \
                        "╠❂➣ " + key + "ᴢʜᴄɴ : ᴄʜɪɴᴇsᴇ (sɪᴍᴘʟɪғɪᴇᴅ)" + "\n" + \
                        "╠❂➣ " + key + "ᴢʜᴛᴡ : ᴄʜɪɴᴇsᴇ (ᴛʀᴀᴅɪᴛɪᴏɴᴀʟ)" + "\n" + \
                        "╠❂➣ " + key + "ᴄᴏ : ᴄᴏʀsɪᴄᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʜʀ : ᴄʀᴏᴀᴛɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴄs : ᴄᴢᴇᴄʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴅᴀ : ᴅᴀɴɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ɴʟ : ᴅᴜᴛᴄʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴇɴ : ᴇɴɢʟɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴇᴏ : ᴇsᴘᴇʀᴀɴᴛᴏ" + "\n" + \
                        "╠❂➣ " + key + "ᴇᴛ : ᴇsᴛᴏɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴛʟ : ғɪʟɪᴘɪɴᴏ" + "\n" + \
                        "╠❂➣ " + key + "ғɪ : ғɪɴɴɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ғʀ : ғʀᴇɴᴄʜ" + "\n" + \
                        "╠❂➣ " + key + "ғʏ : ғʀɪsɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ɢʟ : ɢᴀʟɪᴄɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴋᴀ : ɢᴇᴏʀɢɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴅᴇ : ɢᴇʀᴍᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴇʟ : ɢʀᴇᴇᴋ" + "\n" + \
                        "╠❂➣ " + key + "ɢᴜ : ɢᴜᴊᴀʀᴀᴛɪ" + "\n" + \
                        "╠❂➣ " + key + "ʜᴛ : ʜᴀɪᴛɪᴀɴ ᴄʀᴇᴏʟᴇ" + "\n" + \
                        "╠❂➣ " + key + "ʜᴀ : ʜᴀᴜsᴀ" + "\n" + \
                        "╠❂➣ " + key + "ʜᴀᴡ : ʜᴀᴡᴀɪɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ɪᴡ : ʜᴇʙʀᴇᴡ" + "\n" + \
                        "╠❂➣ " + key + "ʜɪ : ʜɪɴᴅɪ" + "\n" + \
                        "╠❂➣ " + key + "ʜᴍɴ : ʜᴍᴏɴɢ" + "\n" + \
                        "╠❂➣ " + key + "ʜᴜ : ʜᴜɴɢᴀʀɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ɪs : ɪᴄᴇʟᴀɴᴅɪᴄ" + "\n" + \
                        "╠❂➣ " + key + "ɪɢ : ɪɢʙᴏ" + "\n" + \
                        "╠❂➣ " + key + "ɪᴅ : ɪɴᴅᴏɴᴇsɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ɢᴀ : ɪʀɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ɪᴛ : ɪᴛᴀʟɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴊᴀ : ᴊᴀᴘᴀɴᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ᴊᴡ : ᴊᴀᴠᴀɴᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ᴋɴ : ᴋᴀɴɴᴀᴅᴀ" + "\n" + \
                        "╠❂➣ " + key + "ᴋᴋ : ᴋᴀᴢᴀᴋʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴋᴍ : ᴋʜᴍᴇʀ" + "\n" + \
                        "╠❂➣ " + key + "ᴋᴏ : ᴋᴏʀᴇᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴋᴜ : ᴋᴜʀᴅɪsʜ (ᴋᴜʀᴍᴀɴᴊɪ)" + "\n" + \
                        "╠❂➣ " + key + "ᴋʏ : ᴋʏʀɢʏᴢ" + "\n" + \
                        "╠❂➣ " + key + "ʟᴏ : ʟᴀᴏ" + "\n" + \
                        "╠❂➣ " + key + "ʟᴀ : ʟᴀᴛɪɴ" + "\n" + \
                        "╠❂➣ " + key + "ʟᴠ : ʟᴀᴛᴠɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʟᴛ : ʟɪᴛʜᴜᴀɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʟʙ : ʟᴜxᴇᴍʙᴏᴜʀɢɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴍᴋ : ᴍᴀᴄᴇᴅᴏɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴍɢ : ᴍᴀʟᴀɢᴀsʏ" + "\n" + \
                        "╠❂➣ " + key + "ᴍs : ᴍᴀʟᴀʏ" + "\n" + \
                        "╠❂➣ " + key + "ᴍʟ : ᴍᴀʟᴀʏᴀʟᴀᴍ" + "\n" + \
                        "╠❂➣ " + key + "ᴍᴛ : ᴍᴀʟᴛᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ᴍɪ : ᴍᴀᴏʀɪ" + "\n" + \
                        "╠❂➣ " + key + "ᴍʀ : ᴍᴀʀᴀᴛʜɪ" + "\n" + \
                        "╠❂➣ " + key + "ᴍɴ : ᴍᴏɴɢᴏʟɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴍʏ : ᴍʏᴀɴᴍᴀʀ (ʙᴜʀᴍᴇsᴇ)" + "\n" + \
                        "╠❂➣ " + key + "ɴᴇ : ɴᴇᴘᴀʟɪ" + "\n" + \
                        "╠❂➣ " + key + "ɴᴏ : ɴᴏʀᴡᴇɢɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴘs : ᴘᴀsʜᴛᴏ" + "\n" + \
                        "╠❂➣ " + key + "ғᴀ : ᴘᴇʀsɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴘʟ : ᴘᴏʟɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴘᴛ : ᴘᴏʀᴛᴜɢᴜᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ᴘᴀ : ᴘᴜɴᴊᴀʙɪ" + "\n" + \
                        "╠❂➣ " + key + "ʀᴏ : ʀᴏᴍᴀɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʀᴜ : ʀᴜssɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "sᴍ : sᴀᴍᴏᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ɢᴅ : sᴄᴏᴛs ɢᴀᴇʟɪᴄ" + "\n" + \
                        "╠❂➣ " + key + "sʀ : sᴇʀʙɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "sᴛ : sᴇsᴏᴛʜᴏ" + "\n" + \
                        "╠❂➣ " + key + "sɴ : sʜᴏɴᴀ" + "\n" + \
                        "╠❂➣ " + key + "sᴅ : sɪɴᴅʜɪ" + "\n" + \
                        "╠❂➣ " + key + "sɪ : sɪɴʜᴀʟᴀ" + "\n" + \
                        "╠❂➣ " + key + "sᴋ : sʟᴏᴠᴀᴋ" + "\n" + \
                        "╠❂➣ " + key + "sʟ : sʟᴏᴠᴇɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "sᴏ : sᴏᴍᴀʟɪ" + "\n" + \
                        "╠❂➣ " + key + "ᴇs : sᴘᴀɴɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "sᴜ : sᴜɴᴅᴀɴᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "sᴡ : sᴡᴀʜɪʟɪ" + "\n" + \
                        "╠❂➣ " + key + "sᴠ : sᴡᴇᴅɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴛɢ : ᴛᴀᴊɪᴋ" + "\n" + \
                        "╠❂➣ " + key + "ᴛᴀ : ᴛᴀᴍɪʟ" + "\n" + \
                        "╠❂➣ " + key + "ᴛᴇ : ᴛᴇʟᴜɢᴜ" + "\n" + \
                        "╠❂➣ " + key + "ᴛʜ : ᴛʜᴀɪ" + "\n" + \
                        "╠❂➣ " + key + "ᴛʀ : ᴛᴜʀᴋɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴜᴋ : ᴜᴋʀᴀɪɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴜʀ : ᴜʀᴅᴜ" + "\n" + \
                        "╠❂➣ " + key + "ᴜᴢ : ᴜᴢʙᴇᴋ" + "\n" + \
                        "╠❂➣ " + key + "ᴠɪ : ᴠɪᴇᴛɴᴀᴍᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ᴄʏ : ᴡᴇʟsʜ" + "\n" + \
                        "╠❂➣ " + key + "xʜ : xʜᴏsᴀ" + "\n" + \
                        "╠❂➣ " + key + "ʏɪ : ʏɪᴅᴅɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ʏᴏ : ʏᴏʀᴜʙᴀ" + "\n" + \
                        "╠❂➣ " + key + "ᴢᴜ : ᴢᴜʟᴜ" + "\n" + \
                        "╠❂➣ " + key + "ғɪʟ : ғɪʟɪᴘɪɴᴏ" + "\n" + \
                        "╠❂➣ " + key + "ʜᴇ : ʜᴇʙʀᴇᴡ" + "\n" + \
                        "╠════════════════════╗" + "\n" + \
                        "              ᴄʀᴇᴅɪᴛs ʙʏ : ©ᴅ̶ᴇ̶ᴇ̶ ✯" + "\n" + \
                        "╚════════════════════╝" + "\n" + \
                        "╔════════════════════╗" + "\n" + \
                        "                    ✰ ᴅɴᴀ ʙᴏᴛ ✰" + "\n" + \
                        "╚════════════════════╝" + "\n" + \
                        "ᴄᴏɴᴛᴏʜ : " + key + "ᴛʀ-ɪᴅ ʀɪʀɪɴ"
    return helpTranslate

def ririnBot(op):
    try:
        if op.type == 0:
            print ("[ 0 ] Succes")
            return

        if op.type == 5:
            print ("[ 5 ] Add Contact")
            if wait["autoAdd"] == True:
                ririn.findAndAddContactsByMid(op.param1)
            ririn.sendMessage(to, "Halo, ᴛʜᴀɴᴋs ғᴏʀ ᴀᴅᴅ ᴍᴇ \nᴅɴᴀ ʙᴏᴛ \nᴏᴘᴇɴ ᴏʀᴅᴇʀ sᴇʟғʙᴏᴛ ᴏɴʟʏ\nsᴇʟғʙᴏᴛ + ᴀssɪsᴛ\nʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ\nᴀʟʟ ʙᴏᴛ ᴘʏᴛʜᴏɴ з \nᴍɪɴᴀᴛ ᴘᴄ ᴀᴋᴜɴ ᴅɪ ʙᴀᴡᴀʜ \nᴄʀᴇᴀᴛᴏʀ line.me/ti/p/ppgIZ0JLDW")

        if op.type == 13:
            print ("[ 13 ] Invite Into Group")
            if ririnMid in op.param3:
                if wait["autoJoin"] == True:
                    ririn.acceptGroupInvitation(op.param1)
                dan = ririn.getContact(op.param2)
                tgb = ririn.getGroup(op.param1)
                ririn.sendMessage(op.param1, "ʜᴀʟᴏ, ᴛʜx ғᴏʀ ɪɴᴠɪᴛᴇ ᴍᴇ")
                ririn.sendContact(op.param1, op.param2)
                ririn.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
                
        if op.type == 15:
        	dan = ririn.getContact(op.param2)
        	tgb = ririn.getGroup(op.param1)
        	ririn.sendMessage(op.param1, "ɴᴀʜ ᴋᴀɴ ʙᴀᴘᴇʀ 「{}」, ɢᴀᴋ ᴜsᴀʜ ʙᴀʟɪᴋ ᴅɪ {} ʟᴀɢɪ ʏᴀ\nsᴇʟᴀᴍᴀᴛ ᴊᴀʟᴀɴ ᴅᴀɴ sᴇᴍᴏɢᴀʜ ᴛᴇɴᴀɴɢ ᴅɪʟᴜᴀʀ sᴀɴᴀ 😘😘😘".format(str(dan.displayName),str(tgb.name)))
        	ririn.sendContact(op.param1, op.param2)
        	ririn.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
        	
        if op.type == 17:
        	dan = ririn.getContact(op.param2)
        	tgb = ririn.getGroup(op.param1)
        	sendMention(op.param1, "ʜᴏʟᴀ @!         ,\nᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ɢʀᴏᴜᴘ {} \nᴊᴀɴɢᴀɴ ʟᴜᴘᴀ ᴄʜᴇᴄᴋ ɴᴏᴛᴇ ʏᴀ \nᴀᴡᴀs ᴋᴀʟᴀᴜ ʙᴀᴘᴇʀᴀɴ 😘😘😘".format(str(tgb.name)),[op.param2])
        	ririn.sendContact(op.param1, op.param2)
        	ririn.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))

        if op.type in [22, 24]:
            print ("[ 22 And 24 ] NOTIFIED INVITE INTO ROOM & NOTIFIED LEAVE ROOM")
            if wait["autoLeave"] == True:
                sendMention(op.param1, "ᴡᴏʏ ᴋɴᴛʟᴏ @!         ,\nɴɢᴀᴘᴀɪɴ ɪɴᴠɪᴛᴇ ɢᴡ")
                ririn.leaveRoom(op.param1)

        if op.type == 25:
            try:
                print ("[ 25 ] SEND MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                setKey = wait["keyCommand"].title()
                if wait["setKey"] == False:
                    setKey = ''
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != ririn.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if msg.contentType == 0:
                        if text is None:
                            return
                        else:
                            cmd = command(text)
                            if cmd == "help":
                                helpMessage = helpmessage()
                                ririn.sendMessage(to, str(helpMessage))
                            elif cmd == "tts":
                                helpTextToSpeech = helptexttospeech()
                                ririn.sendMessage(to, str(helpTextToSpeech))
                            elif cmd == "translate":
                                helpTranslate = helptranslate()
                                ririn.sendMessage(to, str(helpTranslate))
                            elif cmd.startswith("changekey:"):
                                sep = text.split(" ")
                                key = text.replace(sep[0] + " ","")
                                if " " in key:
                                    ririn.sendMessage(to, "ᴅᴏɴ'ᴛ ᴛʏᴘᴏ ʙʀᴏ")
                                else:
                                    wait["keyCommand"] = str(key).lower()
                                    ririn.sendMessage(to, "sᴜᴄᴄᴇs ᴄʜᴀɴɢᴇ ᴋᴇʏ [ {} ]".format(str(key).lower()))
                            elif cmd == "sp":
                            	ririn.sendMessage(to, "❂➣ ʟᴏᴀᴅɪɴɢ...")
                            	sp = int(round(time.time() *1000))
                            	ririn.sendMessage(to,"ᴍʏ sᴘᴇᴇᴅ : %sms" % (sp - op.createdTime))
                            elif cmd == "speed":
                            	start = time.time()
                            	ririn.sendMessage(to, "❂➣ ʟᴏᴀᴅɪɴɢ...")
                            	elapsed_time = time.time() - start
                            	ririn.sendMessage(to, "ᴍʏ sᴘᴇᴇᴅ : %sms" % (elapsed_time))
                            elif cmd == "runtime":
                                timeNow = time.time()
                                runtime = timeNow - botStart
                                runtime = format_timespan(runtime)
                                ririn.sendMessage(to, "ʀᴜɴɴɪɴɢ ɪɴ.. {}".format(str(runtime)))
                            elif cmd == "restart":
                                ririn.sendMessage(to, "ʙᴏᴛ ʜᴀᴠᴇ ʙᴇᴇɴ ʀᴇsᴛᴀʀᴛ")
                                restartBot()
# Pembatas Script #
                            elif cmd == "autoadd on":
                                wait["autoAdd"] = True
                                ririn.sendMessage(to, "ᴀᴜᴛᴏ ᴀᴅᴅ ᴏɴ")
                            elif cmd == "autoadd off":
                                wait["autoAdd"] = False
                                ririn.sendMessage(to, "ᴀᴜᴛᴏ ᴀᴅᴅ ᴏғғ")
                            elif cmd == "autojoin on":
                                wait["autoJoin"] = True
                                ririn.sendMessage(to, "ᴀᴜᴛᴏ ᴊᴏɪɴ ᴏɴ")
                            elif cmd == "autojoin off":
                                wait["autoJoin"] = False
                                ririn.sendMessage(to, "ᴀᴜᴛᴏ ᴊᴏɪɴ ᴏɴ ᴏғғ")
                            elif cmd == "autoleave on":
                                wait["autoLeave"] = True
                                ririn.sendMessage(to, "ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ ᴏɴ")
                            elif cmd == "autoleave off":
                                wait["autoLeave"] = False
                                ririn.sendMessage(to, "ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ ᴏғғ")
                            elif cmd == "autoresponpc on":
                                wait["autoResponPc"] = True
                                ririn.sendMessage(to, "ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ғᴏʀ ᴘᴇʀsᴏɴᴀʟ ᴄʜᴀᴛ ᴏɴ")
                            elif cmd == "autoresponpc off":
                                wait["autoResponPc"] = False
                                ririn.sendMessage(to, "ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ғᴏʀ ᴘᴇʀsᴏɴᴀʟ ᴄʜᴀᴛ ᴏғғ")
                            elif cmd == "autorespon on":
                                wait["autoRespon"] = True
                                ririn.sendMessage(to, "ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴏɴ")
                            elif cmd == "autorespon off":
                                wait["autoRespon"] = False
                                ririn.sendMessage(to, "ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴏғғ")
                            elif cmd == "autoread on":
                                wait["autoRead"] = True
                                ririn.sendMessage(to, "ᴀᴜᴛᴏ ʀᴇᴀᴅ ᴏɴ")
                            elif cmd == "autoread off":
                                wait["autoRead"] = False
                                ririn.sendMessage(to, "ᴀᴜᴛᴏ ʀᴇᴀᴅ ᴏғғ")
                            elif cmd == "autojointicket on":
                                wait["autoJoinTicket"] = True
                                ririn.sendMessage(to, "ᴊᴏɪɴ ʙʏ ᴛɪᴄᴋᴇᴛ ᴏɴ")
                            elif cmd == "autoJoinTicket off":
                                wait["autoJoin"] = False
                                ririn.sendMessage(to, "ᴊᴏɪɴ ʙʏ ᴛɪᴄᴋᴇᴛ ᴏғғ")
                            elif cmd == "checkcontact on":
                                wait["checkContact"] = True
                                ririn.sendMessage(to, "ᴄʜᴇᴄᴋ ᴄᴏɴᴛᴀᴄᴛ ᴏɴ")
                            elif cmd == "checkcontact off":
                                wait["checkContact"] = False
                                ririn.sendMessage(to, "ᴄʜᴇᴄᴋ ᴄᴏɴᴛᴀᴄᴛ ᴏғғ")
                            elif cmd == "checkpost on":
                                wait["checkPost"] = True
                                ririn.sendMessage(to, "ᴄʜᴇᴄᴋ ᴘᴏsᴛ ᴏɴ")
                            elif cmd == "checkpost off":
                                wait["checkPost"] = False
                                ririn.sendMessage(to, "ᴄʜᴇᴄᴋ ᴘᴏsᴛ ᴏғғ")
                            elif cmd == "checksticker on":
                                wait["checkSticker"] = True
                                ririn.sendMessage(to, "ᴄʜᴇᴄᴋ sᴛɪᴄᴋᴇʀ ᴏɴ")
                            elif cmd == "checksticker off":
                                wait["checkSticker"] = False
                                ririn.sendMessage(to, "ᴄʜᴇᴄᴋ sᴛɪᴄᴋᴇʀ ᴏғғ")
                            elif cmd == "unsendchat on":
                                wait["unsendMessage"] = True
                                ririn.sendMessage(to, "ᴜɴsᴇɴᴅ ᴍᴇssᴀɢᴇ ᴏɴ")
                            elif cmd == "unsendchat off":
                                wait["unsendMessage"] = False
                                ririn.sendMessage(to, "ᴜɴsᴇɴᴅ ᴍᴇssᴀɢᴇ ᴏғғ")
                            elif cmd == "status":
                                try:
                                    ret_ = "╔═════[ ·✪·sᴛᴀᴛᴜs·✪· ]═════╗"
                                    if wait["autoAdd"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴀᴜᴛᴏ ᴀᴅᴅ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴀᴜᴛᴏ ᴀᴅᴅ 「⚫」"
                                    if wait["autoJoin"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴀᴜᴛᴏ ᴊᴏɪɴ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴀᴜᴛᴏ ᴊᴏɪɴ 「⚫」"
                                    if wait["autoLeave"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ 「⚫」"
                                    if wait["autoJoinTicket"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴊᴏɪɴ ᴛɪᴄᴋᴇᴛ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴊᴏɪɴ ᴛɪᴄᴋᴇᴛ 「⚫」"
                                    if wait["autoRead"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴀᴜᴛᴏ ʀᴇᴀᴅ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴀᴜᴛᴏ ʀᴇᴀᴅ 「⚫」"
                                    if wait["autoRespon"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ 「⚫」"
                                    if wait["autoResponPc"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴘᴄ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴘᴄ 「⚫」"
                                    if wait["checkContact"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴄʜᴇᴄᴋ ᴄᴏɴᴛᴀᴄᴛ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴄʜᴇᴄᴋ ᴄᴏɴᴛᴀᴄᴛ 「⚫」"
                                    if wait["checkPost"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴄʜᴇᴄᴋ ᴘᴏsᴛ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴄʜᴇᴄᴋ ᴘᴏsᴛ 「⚫」"
                                    if wait["checkSticker"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴄʜᴇᴄᴋ sᴛɪᴄᴋᴇʀ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴄʜᴇᴄᴋ sᴛɪᴄᴋᴇʀ 「⚫」"
                                    if wait["setKey"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] sᴇᴛ ᴋᴇʏ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] sᴇᴛ ᴋᴇʏ 「⚫」"
                                    if wait["unsendMessage"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴜɴsᴇɴᴅ ᴍsɢ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴜɴsᴇɴᴅ ᴍsɢ 「⚫」"
                                    ret_ += "\n╚═════[ ✯ ᴅɴᴀ ʙᴏᴛ ✯ ]═════╝"
                                    ririn.sendMessage(to, str(ret_))
                                except Exception as e:
                                    ririn.sendMessage(msg.to, str(e))
                            elif cmd == "set":
                                try:
                                    ret_ = "╔═════[ ·✪·  s ᴇ ᴛ  ·✪· ]═════╗"
                                    if wait["Protectcancel"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴘʀᴏᴛᴇᴄᴛ ᴄᴀɴᴄᴇʟ 「🔒」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴘʀᴏᴛᴇᴄᴛ ᴄᴀɴᴄᴇʟ 「🔓」"
                                    if wait["Protectgr"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴘʀᴏᴛᴇᴄᴛ ɢʀ 「🔒」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴘʀᴏᴛᴇᴄᴛ ɢʀ 「🔓」"
                                    if wait["Protectinvite"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴘʀᴏᴛᴇᴄᴛ ɪɴᴠɪᴛᴇ 「🔒」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴘʀᴏᴛᴇᴄᴛ ɪɴᴠɪᴛᴇ 「🔓」"
                                    if wait["Protectjoin"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴘʀᴏᴛᴇᴄᴛ ᴊᴏɪɴ 「🔒」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴘʀᴏᴛᴇᴄᴛ ᴊᴏɪɴ 「🔓」"
                                    ret_ += "\n╚═════[ ✯ ᴅɴᴀ ʙᴏᴛ ✯ ]═════╝"
                                    ririn.sendMessage(to, str(ret_))
                                except Exception as e:
                                    ririn.sendMessage(msg.to, str(e))
# Pembatas Script #
                            elif cmd == "crash":
                                ririn.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                            elif cmd.startswith("changename:"):
                                sep = text.split(" ")
                                string = text.replace(sep[0] + " ","")
                                if len(string) <= 20:
                                    profile = ririn.getProfile()
                                    profile.displayName = string
                                    ririn.updateProfile(profile)
                                    ririn.sendMessage(to,"ᴄʜᴀɴɢᴇ ɴᴀᴍᴇ sᴜᴄᴄᴇs :{}".format(str(string)))
                            elif cmd.startswith("changebio:"):
                                sep = text.split(" ")
                                string = text.replace(sep[0] + " ","")
                                if len(string) <= 500:
                                    profile = ririn.getProfile()
                                    profile.statusMessage = string
                                    ririn.updateProfile(profile)
                                    ririn.sendMessage(to,"ᴄʜᴀɴɢᴇ ᴘʀᴏғɪʟᴇ sᴜᴄᴄᴇs :{}".format(str(string)))
                            elif cmd == "me":
                                sendMention(to, "@!", [sender])
                                ririn.sendContact(to, sender)
                            elif cmd == "mymid":
                                ririn.sendMessage(to, "[ ᴍɪᴅ ]\n{}".format(sender))
                            elif cmd == "myname":
                                contact = ririn.getContact(sender)
                                ririn.sendMessage(to, "[ ᴅɪsᴘʟᴀʏ ɴᴀᴍᴇ ]\n{}".format(contact.displayName))
                            elif cmd == "mybio":
                                contact = ririn.getContact(sender)
                                ririn.sendMessage(to, "[ sᴛᴀᴛᴜs ᴍᴇssᴀɢᴇ ]\n{}".format(contact.statusMessage))
                            elif cmd == "mypicture":
                                contact = ririn.getContact(sender)
                                ririn.sendImageWithURL(to,"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                            elif cmd == "myvideoprofile":
                                contact = ririn.getContact(sender)
                                ririn.sendVideoWithURL(to,"http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))
                            elif cmd == "mycover":
                                channel = ririn.getProfileCoverURL(sender)          
                                path = str(channel)
                                ririn.sendImageWithURL(to, path)
                            elif cmd.startswith("cloneprofile "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = ririn.getContact(ls)
                                        ririn.cloneContactProfile(ls)
                                        ririn.sendMessage(to, "ᴄʟᴏɴᴇ ᴘʀᴏғɪʟᴇ sᴜᴄᴄᴇs : {}".format(contact.displayName))
                            elif cmd == "restoreprofile":
                                try:
                                    ririnProfile = ririn.getProfile()
                                    ririnProfile.displayName = str(wait["myProfile"]["displayName"])
                                    ririnProfile.statusMessage = str(wait["myProfile"]["statusMessage"])
                                    ririnProfile.pictureStatus = str(wait["myProfile"]["pictureStatus"])
                                    ririn.updateProfileAttribute(8, ririnProfile.pictureStatus)
                                    ririn.updateProfile(ririnProfile)
                                    coverId = str(wait["myProfile"]["coverId"])
                                    ririn.updateProfileCoverById(coverId)
                                    ririn.sendMessage(to, "ʀᴇsᴛᴏʀᴇ ᴘʀᴏғɪʟᴇ sᴜᴄᴄᴇs, ᴡᴀɪᴛ ᴀ ғᴇᴡ ᴍɪɴᴜᴛᴇs")
                                except Exception as e:
                                    ririn.sendMessage(to, "ʀᴇsᴛᴏʀᴇ ᴘʀᴏғɪʟᴇ ғᴀɪʟᴇᴅ")
                                    logError(error)
                            elif cmd == "backupprofile":
                                try:
                                    profile = ririn.getProfile()
                                    wait["myProfile"]["displayName"] = str(profile.displayName)
                                    wait["myProfile"]["statusMessage"] = str(profile.statusMessage)
                                    wait["myProfile"]["pictureStatus"] = str(profile.pictureStatus)
                                    coverId = ririn.getProfileDetail()["result"]["objectId"]
                                    wait["myProfile"]["coverId"] = str(coverId)
                                    ririn.sendMessage(to, "ʙᴀᴄᴋᴜᴘ ᴘʀᴏғɪʟᴇ sᴜᴄᴄᴇs")
                                except Exception as e:
                                    ririn.sendMessage(to, "ʙᴀᴄᴋᴜᴘ ᴘʀᴏғɪʟᴇ ғᴀɪʟᴇᴅ")
                                    logError(error)
                            elif cmd.startswith("stealmid "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    ret_ = "[ Mid User ]"
                                    for ls in lists:
                                        ret_ += "\n{}".format(str(ls))
                                    ririn.sendMessage(to, str(ret_))
                            elif cmd.startswith("stealname "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = ririn.getContact(ls)
                                        ririn.sendMessage(to, "[ Display Name ]\n{}".format(str(contact.displayName)))
                            elif cmd.startswith("stealbio "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = ririn.getContact(ls)
                                        ririn.sendMessage(to, "[ sᴛᴀᴛᴜs ᴍᴇssᴀɢᴇ ]\n{}".format(str(contact.statusMessage)))
                            elif cmd.startswith("stealpicture"):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = ririn.getContact(ls)
                                        path = "http://dl.profile.line.naver.jp/{}".format(contact.pictureStatus)
                                        ririn.sendImageWithURL(to, str(path))
                            elif cmd.startswith("stealvideoprofile "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = ririn.getContact(ls)
                                        path = "http://dl.profile.line.naver.jp/{}/vp".format(contact.pictureStatus)
                                        ririn.sendVideoWithURL(to, str(path))
                            elif cmd.startswith("stealcover "):
                                if ririn != None:
                                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for ls in lists:
                                            channel = ririn.getProfileCoverURL(ls)
                                            path = str(channel)
                                            ririn.sendImageWithURL(to, str(path))
# Pembatas Script #
                            elif cmd == 'groupcreator':
                                group = ririn.getGroup(to)
                                GS = group.creator.mid
                                ririn.sendContact(to, GS)
                            elif cmd == 'groupid':
                                gid = ririn.getGroup(to)
                                ririn.sendMessage(to, "[ɢʀᴏᴜᴘ ɪᴅ : : ]\n" + gid.id)
                            elif cmd == 'grouppicture':
                                group = ririn.getGroup(to)
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                ririn.sendImageWithURL(to, path)
                            elif cmd == 'groupname':
                                gid = ririn.getGroup(to)
                                ririn.sendMessage(to, "[ɢʀᴏᴜᴘ ɴᴀᴍᴇ : ]\n" + gid.name)
                            elif cmd == 'groupticket':
                                if msg.toType == 2:
                                    group = ririn.getGroup(to)
                                    if group.preventedJoinByTicket == False:
                                        ticket = ririn.reissueGroupTicket(to)
                                        ririn.sendMessage(to, "[ ɢʀᴏᴜᴘ ᴛɪᴄᴋᴇᴛ ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                                    else:
                                        ririn.sendMessage(to, "ᴛʜᴇ ǫʀ ɢʀᴏᴜᴘ ɪs ɴᴏᴛ ᴏᴘᴇɴ ᴘʟᴇᴀsᴇ ᴏᴘᴇɴ ɪᴛ ғɪʀsᴛ ᴡɪᴛʜ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ {}openqr".format(str(wait["keyCommand"])))
                            elif cmd == 'groupticket on':
                                if msg.toType == 2:
                                    group = ririn.getGroup(to)
                                    if group.preventedJoinByTicket == False:
                                        ririn.sendMessage(to, "ᴀʟʀᴇᴀᴅʏ ᴏᴘᴇɴ")
                                    else:
                                        group.preventedJoinByTicket = False
                                        ririn.updateGroup(group)
                                        ririn.sendMessage(to, "sᴜᴄᴄᴇs ᴏᴘᴇɴ ǫʀ ɢʀᴏᴜᴘ")
                            elif cmd == 'groupticket off':
                                if msg.toType == 2:
                                    group = ririn.getGroup(to)
                                    if group.preventedJoinByTicket == True:
                                        ririn.sendMessage(to, "ᴀʟʀᴇᴀᴅʏ ᴄʟᴏsᴇᴅ")
                                    else:
                                        group.preventedJoinByTicket = True
                                        ririn.updateGroup(group)
                                        ririn.sendMessage(to, "sᴜᴄᴄᴇs ᴄʟᴏsᴇ ǫʀ ɢʀᴏᴜᴘ")
                            elif cmd == 'groupinfo':
                                group = ririn.getGroup(to)
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "ɴᴏᴛ ғᴏᴜɴᴅ"
                                if group.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    gQr = "ᴄʟᴏsᴇᴅ"
                                    gTicket = "ɴᴏʟ'"
                                else:
                                    gQr = "ᴏᴘᴇɴ"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(ririn.reissueGroupTicket(group.id)))
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                ret_ = "╔════[ ·✪ɢʀᴏᴜᴘ ɪɴғᴏ✪· ]════╗"
                                ret_ += "\n╠❂➣ ɢʀᴏᴜᴘ ɴᴀᴍᴇ : {}".format(str(group.name))
                                ret_ += "\n╠❂➣ ɢʀᴏᴜᴘ ɪᴅ : {}".format(group.id)
                                ret_ += "\n╠❂➣ ᴄʀᴇᴀᴛᴏʀ :  {}".format(str(gCreator))
                                ret_ += "\n╠❂➣ ᴍᴇᴍʙᴇʀ : {}".format(str(len(group.members)))
                                ret_ += "\n╠❂➣ ᴘᴇɴᴅɪɴɢ : {}".format(gPending)
                                ret_ += "\n╠❂➣ ǫʀ ɢʀᴏᴜᴘ : {}".format(gQr)
                                ret_ += "\n╠❂➣ ᴛɪᴄᴋᴇᴛ ɢʀᴏᴜᴘ : {}".format(gTicket)
                                ret_ += "\n╚═════[ ✯ ᴅɴᴀ ʙᴏᴛ ✯ ]═════╝"
                                ririn.sendMessage(to, str(ret_))
                                ririn.sendImageWithURL(to, path)
                            elif cmd == 'memberlist':
                                if msg.toType == 2:
                                    group = ririn.getGroup(to)
                                    ret_ = "╔══[ ᴍᴇᴍʙᴇʀ  ʟɪsᴛ ]══✪"
                                    no = 0 + 1
                                    for mem in group.members:
                                        ret_ += "\n╠❂➣ {}. {}".format(str(no), str(mem.displayName))
                                        no += 1
                                    ret_ += "\n╚═══[ ᴛᴏᴛᴀʟ : {} ]═══✪".format(str(len(group.members)))
                                    ririn.sendMessage(to, str(ret_))
                            elif cmd == 'grouplist':
                                    groups = ririn.groups
                                    ret_ = "╔═[ ✯ ɢʀᴏᴜᴘ  ʟɪsᴛ ✯ ]═✪"
                                    no = 0 + 1
                                    for gid in groups:
                                        group = ririn.getGroup(gid)
                                        ret_ += "\n╠❂➣ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                                        no += 1
                                    ret_ += "\n╚═══[ ᴛᴏᴛᴀʟ : {} ]═══✪".format(str(len(groups)))
                                    ririn.sendMessage(to, str(ret_))
# Pembatas Script #
                            elif cmd == "changepictureprofile":
                                wait["changePictureProfile"] = True
                                ririn.sendMessage(to, "sᴇɴᴅ ᴘɪᴄᴛᴜʀᴇ")
                            elif cmd == "changegrouppicture":
                                if msg.toType == 2:
                                    if to not in wait["changeGroupPicture"]:
                                        wait["changeGroupPicture"].append(to)
                                    ririn.sendMessage(to, "sᴇɴᴅ ᴘɪᴄᴛᴜʀᴇ")
                            elif cmd == 'mention':
                                group = ririn.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                k = len(nama)//100
                                for a in range(k+1):
                                    txt = u''
                                    s=0
                                    b=[]
                                    for i in group.members[a*100 : (a+1)*100]:
                                        b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                        s += 7
                                        txt += u'@Zero \n'
                                    ririn.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                                    ririn.sendMessage(to, "Total {} Mention".format(str(len(nama))))
                                    
                            elif cmd == "sider on":
                            	try:
                            		del cctv['point'][msg.to]
                            		del cctv['sidermem'][msg.to]
                            		del cctv['cyduk'][msg.to]
                            	except:
                            		pass
                            	cctv['point'][msg.to] = msg.id
                            	cctv['sidermem'][msg.to] = ""
                            	cctv['cyduk'][msg.to]=True
                            	wait["Sider"] = True
                            	ririn.sendMessage(msg.to,"sɪᴅᴇʀ sᴇᴛ ᴛᴏ ᴏɴ")
                            elif cmd == "sider off":
                            	if msg.to in cctv['point']:
                            		cctv['cyduk'][msg.to]=False
                            		wait["Sider"] = False
                            		ririn.sendMessage(msg.to,"sɪᴅᴇʀ sᴇᴛ ᴛᴏ ᴏғғ")
                            	else:
                            		ririn.sendMessage(msg.to,"sɪᴅᴇʀ ɴᴏᴛ sᴇᴛ")           
                            elif cmd == "lurking on":
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if receiver in read['readPoint']:
                                    try:
                                        del read['readPoint'][receiver]
                                        del read['readMember'][receiver]
                                        del read['readTime'][receiver]
                                    except:
                                        pass
                                    read['readPoint'][receiver] = msg_id
                                    read['readMember'][receiver] = ""
                                    read['readTime'][receiver] = readTime
                                    read['ROM'][receiver] = {}
                                    ririn.sendMessage(receiver,"ʟᴜʀᴋɪɴɢ sᴇᴛ ᴏɴ")
                                else:
                                    try:
                                        del read['readPoint'][receiver]
                                        del read['readMember'][receiver]
                                        del read['readTime'][receiver]
                                    except:
                                        pass
                                    read['readPoint'][receiver] = msg_id
                                    read['readMember'][receiver] = ""
                                    read['readTime'][receiver] = readTime
                                    read['ROM'][receiver] = {}
                                    ririn.sendMessage(receiver,"sᴇᴛ ʀᴇᴀᴅɪɴɢ ᴘᴏɪɴᴛ : \n" + readTime)
                            elif cmd == "lurking off":
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if receiver not in read['readPoint']:
                                    ririn.sendMessage(receiver,"ʟᴜʀᴋɪɴɢ sᴇᴛ ᴏғғ")
                                else:
                                    try:
                                        del read['readPoint'][receiver]
                                        del read['readMember'][receiver]
                                        del read['readTime'][receiver]
                                    except:
                                        pass
                                    ririn.sendMessage(receiver,"ᴅᴇʟᴇᴛᴇ ʀᴇᴀᴅɪɴɢ ᴘᴏɪɴᴛ : \n" + readTime)
        
                            elif cmd == "lurking reset":
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if msg.to in read["readPoint"]:
                                    try:
                                        del read["readPoint"][msg.to]
                                        del read["readMember"][msg.to]
                                        del read["readTime"][msg.to]
                                        del read["ROM"][msg.to]
                                    except:
                                        pass
                                    read['readPoint'][receiver] = msg_id
                                    read['readMember'][receiver] = ""
                                    read['readTime'][receiver] = readTime
                                    read['ROM'][receiver] = {}
                                    ririn.sendMessage(msg.to, "ʀᴇsᴇᴛ ʀᴇᴀᴅɪɴɢ ᴘᴏɪɴᴛ : \n" + readTime)
                                else:
                                    ririn.sendMessage(msg.to, "ʟᴜʀᴋɪɴɢ ɴᴏᴛ ᴀᴋᴛɪᴠᴇ, ᴄᴏᴜʟᴅ ɴᴏᴛ ʙᴇ ʀᴇsᴇᴛ")
                                    
                            elif cmd == "lurking":
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if receiver in read['readPoint']:
                                    if read["ROM"][receiver].items() == []:
                                        ririn.sendMessage(receiver,"ɴᴏ sɪᴅᴇʀ")
                                    else:
                                        chiya = []
                                        for rom in read["ROM"][receiver].items():
                                            chiya.append(rom[1])
                                        cmem = ririn.getContacts(chiya) 
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = '[ ʀ ᴇ ᴀ ᴅ ᴇ ʀ ]\n'
                                    for x in range(len(cmem)):
                                        xname = str(cmem[x].displayName)
                                        pesan = ''
                                        pesan2 = pesan+"@c\n"
                                        xlen = str(len(zxc)+len(xpesan))
                                        xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                        zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                    text = xpesan+ zxc + "\n" + readTime
                                    try:
                                        ririn.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    except Exception as error:
                                        print (error)
                                    pass
                                else:
                                    ririn.sendMessage(receiver,"ʟᴜʀᴋɪɴɢ ɴᴏᴛ ᴀᴄᴛɪᴠᴇ")
                            elif cmd.startswith("mimicadd"):
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:
                                        wait["mimic"]["target"][target] = True
                                        ririn.sendMessage(msg.to,"ᴛᴀʀɢᴇᴛ ᴀᴅᴅᴇᴅ")
                                        break
                                    except:
                                        ririn.sendMessage(msg.to,"ғᴀɪʟᴇᴅ ᴀᴅᴅᴇᴅ ᴛᴀʀɢᴇᴛ")
                                        break
                            elif cmd.startswith("mimicdel"):
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:
                                        del wait["mimic"]["target"][target]
                                        ririn.sendMessage(msg.to,"ᴛᴀɢᴇᴛ ᴅᴇʟᴇᴛᴇᴅ")
                                        break
                                    except:
                                        ririn.sendMessage(msg.to,"ғᴀɪʟ ᴅᴇʟᴇᴛᴇᴅ ᴛᴀʀɢᴇᴛ")
                                        break
                                    
                            elif cmd == "mimiclist":
                                if wait["mimic"]["target"] == {}:
                                    ririn.sendMessage(msg.to,"ɴᴏ ᴛᴀʀɢᴇᴛ")
                                else:
                                    mc = "╔════[ ·✪·ᴍɪᴍɪᴄ ʟɪsᴛ·✪· ]════╗"
                                    for mi_d in wait["mimic"]["target"]:
                                        mc += "\n╠❂➣ "+ririn.getContact(mi_d).displayName
                                    mc += "\n╚═════[  ✯ ᴅɴᴀ ʙᴏᴛ ✯ ]═════╝"
                                    ririn.sendMessage(msg.to,mc)
                                
                            elif cmd.startswith("mimic"):
                                sep = text.split(" ")
                                mic = text.replace(sep[0] + " ","")
                                if mic == "on":
                                    if wait["mimic"]["status"] == False:
                                        wait["mimic"]["status"] = True
                                        ririn.sendMessage(msg.to,"ᴍɪᴍɪᴄ ᴏɴ")
                                elif mic == "off":
                                    if wait["mimic"]["status"] == True:
                                        wait["mimic"]["status"] = False
                                        ririn.sendMessage(msg.to,"ᴍɪᴍɪᴄ ᴏғғ")
# Pembatas Script #   
                            elif cmd.startswith("checkwebsite"):
                                try:
                                    sep = text.split(" ")
                                    query = text.replace(sep[0] + " ","")
                                    r = requests.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link={}".format(urllib.parse.quote(query)))
                                    data = r.text
                                    data = json.loads(data)
                                    ririn.sendImageWithURL(to, data["result"])
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("checkdate"):
                                try:
                                    sep = msg.text.split(" ")
                                    tanggal = msg.text.replace(sep[0] + " ","")
                                    r = requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                                    data=r.text
                                    data=json.loads(data)
                                    ret_ = "[ D A T E ]"
                                    ret_ += "\nDate Of Birth : {}".format(str(data["data"]["lahir"]))
                                    ret_ += "\nAge : {}".format(str(data["data"]["usia"]))
                                    ret_ += "\nBirthday : {}".format(str(data["data"]["ultah"]))
                                    ret_ += "\nZodiak : {}".format(str(data["data"]["zodiak"]))
                                    ririn.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("checkpraytime "):
                                separate = msg.text.split(" ")
                                location = msg.text.replace(separate[0] + " ","")
                                r = requests.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(location))
                                data = r.text
                                data = json.loads(data)
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                if data[1] != "sᴜʙᴜʜ : " and data[2] != "ᴅᴢᴜʜᴜʀ : " and data[3] != "ᴀsʜᴀʀ : " and data[4] != "ᴍᴀɢʜʀɪʙ : " and data[5] != "ɪsʜᴀ : ":
                                    ret_ = "╔═══[ ᴊᴀᴅᴡᴀʟ sʜᴏʟᴀᴛ ]"
                                    ret_ += "\n╠══[ sᴇᴋɪᴛᴀʀ " + data[0] + " ]"
                                    ret_ += "\n╠❂➣ ᴛᴀɴɢɢᴀʟ : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                    ret_ += "\n╠❂➣ ᴊᴀᴍ : " + datetime.strftime(timeNow,'%H:%M:%S')
                                    ret_ += "\n╠❂➣ " + data[1]
                                    ret_ += "\n╠❂➣ " + data[2]
                                    ret_ += "\n╠❂➣ " + data[3]
                                    ret_ += "\n╠❂➣ " + data[4]
                                    ret_ += "\n╠❂➣ " + data[5]
                                    ret_ += "\n╚════[ ✯ ᴅɴᴀ ʙᴏᴛ ✯ ]"
                                    ririn.sendMessage(msg.to, str(ret_))
                            elif cmd.startswith("checkweather "):
                                try:
                                    sep = text.split(" ")
                                    location = text.replace(sep[0] + " ","")
                                    r = requests.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(location))
                                    data = r.text
                                    data = json.loads(data)
                                    tz = pytz.timezone("Asia/Makassar")
                                    timeNow = datetime.now(tz=tz)
                                    if "result" not in data:
                                        ret_ = "╔═══[ ᴡᴇᴀᴛʜᴇʀ sᴛᴀᴛᴜs ]"
                                        ret_ += "\n╠❂➣ ʟᴏᴄᴀᴛɪᴏɴ : " + data[0].replace("Temperatur di kota ","")
                                        ret_ += "\n╠❂➣ sᴜʜᴜ : " + data[1].replace("Suhu : ","") + "°ᴄ"
                                        ret_ += "\n╠❂➣ ᴋᴇʟᴇᴍʙᴀʙᴀɴ : " + data[2].replace("Kelembaban : ","") + "%"
                                        ret_ += "\n╠❂➣ ᴛᴇᴋᴀɴᴀɴ ᴜᴅᴀʀᴀ : " + data[3].replace("Tekanan udara : ","") + "ʜᴘᴀ "
                                        ret_ += "\n╠❂➣ ᴋᴇᴄᴇᴘᴀᴛᴀɴ ᴀɴɢɪɴ : " + data[4].replace("Kecepatan angin : ","") + "ᴍ/s"
                                        ret_ += "\n╠════[ ᴛɪᴍᴇ sᴛᴀᴛᴜs ]"
                                        ret_ += "\n╠❂➣ ᴛᴀɴɢɢᴀʟ : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                        ret_ += "\n╠❂➣ ᴊᴀᴍ : " + datetime.strftime(timeNow,'%H:%M:%S') + " ᴡɪʙ"
                                        ret_ += "\n╚════[ ✯ ᴅɴᴀ ʙᴏᴛ ✯ ]"
                                        ririn.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("checklocation "):
                                try:
                                    sep = text.split(" ")
                                    location = text.replace(sep[0] + " ","")
                                    r = requests.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(location))
                                    data = r.text
                                    data = json.loads(data)
                                    if data[0] != "" and data[1] != "" and data[2] != "":
                                        link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                        ret_ = "╔═══[ ʟᴏᴄᴀᴛɪᴏɴ sᴛᴀᴛᴜs ]"
                                        ret_ += "\n╠❂➣ ʟᴏᴄᴀᴛɪᴏɴ : " + data[0]
                                        ret_ += "\n╠❂➣  ɢᴏᴏɢʟᴇ ᴍᴀᴘs : " + link
                                        ret_ += "\n╚════[ ✯ ᴅɴᴀ ʙᴏᴛ ✯ ]"
                                        ririn.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("instainfo"):
                                try:
                                    sep = text.split(" ")
                                    search = text.replace(sep[0] + " ","")
                                    r = requests.get("https://www.instagram.com/{}/?__a=1".format(search))
                                    data = r.text
                                    data = json.loads(data)
                                    if data != []:
                                        ret_ = "╔══[ Profile Instagram ]"
                                        ret_ += "\n╠ Nama : {}".format(str(data["graphql"]["user"]["full_name"]))
                                        ret_ += "\n╠ Username : {}".format(str(data["graphql"]["user"]["username"]))
                                        ret_ += "\n╠ Bio : {}".format(str(data["graphql"]["user"]["biography"]))
                                        ret_ += "\n╠ Pengikut : {}".format(str(data["graphql"]["user"]["edge_followed_by"]["count"]))
                                        ret_ += "\n╠ Diikuti : {}".format(str(data["graphql"]["user"]["edge_follow"]["count"]))
                                        if data["graphql"]["user"]["is_verified"] == True:
                                            ret_ += "\n╠ Verifikasi : Sudah"
                                        else:
                                            ret_ += "\n╠ Verifikasi : Belum"
                                        if data["graphql"]["user"]["is_private"] == True:
                                            ret_ += "\n╠ Akun Pribadi : Iya"
                                        else:
                                            ret_ += "\n╠ Akun Pribadi : Tidak"
                                        ret_ += "\n╠ Total Post : {}".format(str(data["graphql"]["user"]["edge_owner_to_timeline_media"]["count"]))
                                        ret_ += "\n╚══[ https://www.instagram.com/{} ]".format(search)
                                        path = data["graphql"]["user"]["profile_pic_url_hd"]
                                        ririn.sendImageWithURL(to, str(path))
                                        ririn.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("instapost"):
                                try:
                                    sep = text.split(" ")
                                    text = text.replace(sep[0] + " ","")   
                                    cond = text.split("|")
                                    username = cond[0]
                                    no = cond[1] 
                                    r = requests.get("http://rahandiapi.herokuapp.com/instapost/{}/{}?key=betakey".format(str(username), str(no)))
                                    data = r.text
                                    data = json.loads(data)
                                    if data["find"] == True:
                                        if data["media"]["mediatype"] == 1:
                                            ririn.sendImageWithURL(msg.to, str(data["media"]["url"]))
                                        if data["media"]["mediatype"] == 2:
                                            ririn.sendVideoWithURL(msg.to, str(data["media"]["url"]))
                                        ret_ = "╔══[ Info Post ]"
                                        ret_ += "\n╠ Jumlah Like : {}".format(str(data["media"]["like_count"]))
                                        ret_ += "\n╠ Jumlah Comment : {}".format(str(data["media"]["comment_count"]))
                                        ret_ += "\n╚══[ Caption ]\n{}".format(str(data["media"]["caption"]))
                                        ririn.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("instastory"):
                                try:
                                    sep = text.split(" ")
                                    text = text.replace(sep[0] + " ","")
                                    cond = text.split("|")
                                    search = str(cond[0])
                                    if len(cond) == 2:
                                        r = requests.get("http://rahandiapi.herokuapp.com/instastory/{}?key=betakey".format(search))
                                        data = r.text
                                        data = json.loads(data)
                                        if data["url"] != []:
                                            num = int(cond[1])
                                            if num <= len(data["url"]):
                                                search = data["url"][num - 1]
                                                if search["tipe"] == 1:
                                                    ririn.sendImageWithURL(to, str(search["link"]))
                                                if search["tipe"] == 2:
                                                    ririn.sendVideoWithURL(to, str(search["link"]))
                                except Exception as error:
                                    logError(error)
                                    
                            elif cmd.startswith("say-"):
                                sep = text.split("-")
                                sep = sep[1].split(" ")
                                lang = sep[0]
                                say = text.replace("say-" + lang + " ","")
                                if lang not in list_language["list_textToSpeech"]:
                                    return ririn.sendMessage(to, "ʟᴀɴɢᴜᴀɢᴇ ɴᴏᴛ ғᴏᴜɴᴅ")
                                tts = gTTS(text=say, lang=lang)
                                tts.save("hasil.mp3")
                                ririn.sendAudio(to,"hasil.mp3")
                                
                            elif cmd.startswith("searchimage"):
                                try:
                                    separate = msg.text.split(" ")
                                    search = msg.text.replace(separate[0] + " ","")
                                    r = requests.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(search))
                                    data = r.text
                                    data = json.loads(data)
                                    if data["result"] != []:
                                        items = data["result"]
                                        path = random.choice(items)
                                        a = items.index(path)
                                        b = len(items)
                                        ririn.sendImageWithURL(to, str(path))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("searchmusic "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                search = str(cond[0])
                                result = requests.get("http://api.ntcorp.us/joox/search?q={}".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "╔══[ ʀᴇsᴜʟᴛ ᴍᴜsɪᴄ ]"
                                    for music in data["result"]:
                                        num += 1
                                        ret_ += "\n╠ {}. {}".format(str(num), str(music["single"]))
                                    ret_ += "\n╚══[ ᴛᴏᴛᴀʟ {} ᴍᴜsɪᴄ ] ".format(str(len(data["result"])))
                                    ret_ += "\n\nᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴅᴇᴛᴀɪʟs ᴍᴜsɪᴄ, sɪʟᴀʜᴋᴀɴ ɢᴜɴᴀᴋᴀɴ ᴄᴏᴍᴍᴀɴᴅ {}sᴇᴀʀᴄʜᴍᴜsɪᴄ {}|「ɴᴜᴍʙᴇʀ」".format(str(setKey), str(search))
                                    ririn.sendMessage(to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["result"]):
                                        music = data["result"][num - 1]
                                        result = requests.get("http://api.ntcorp.us/joox/song_info?sid={}".format(str(music["sid"])))
                                        data = result.text
                                        data = json.loads(data)
                                        if data["result"] != []:
                                            ret_ = "╔══════[ ᴍᴜsɪᴄ ]"
                                            ret_ += "\n╠❂➣ ᴛɪᴛʟᴇ : {}".format(str(data["result"]["song"]))
                                            ret_ += "\n╠❂➣ ᴀʟʙᴜᴍ : {}".format(str(data["result"]["album"]))
                                            ret_ += "\n╠❂➣ sɪᴢᴇ : {}".format(str(data["result"]["size"]))
                                            ret_ += "\n╠❂➣ ʟɪɴᴋ :  {}".format(str(data["result"]["mp3"][0]))
                                            ret_ += "\n╚════[ ✯ ᴅɴᴀ ʙᴏᴛ ✯ ]"
                                            ririn.sendImageWithURL(to, str(data["result"]["img"]))
                                            ririn.sendMessage(to, str(ret_))
                                            ririn.sendAudioWithURL(to, str(data["result"]["mp3"][0]))
                            elif cmd.startswith("searchlyric"):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                search = cond[0]
                                api = requests.get("http://api.secold.com/joox/cari/{}".format(str(search)))
                                data = api.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "╔══[ ʀᴇsᴜʟᴛ ʟʏʀɪᴄ ]"
                                    for lyric in data["results"]:
                                        num += 1
                                        ret_ += "\n╠❂➣ {}. {}".format(str(num), str(lyric["single"]))
                                    ret_ += "\n╚══[ ᴛᴏᴛᴀʟ {} ᴍᴜsɪᴄ ]".format(str(len(data["results"])))
                                    ret_ += "\n\nᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴅᴇᴛᴀɪʟs ʟʏʀɪᴄ, sɪʟᴀʜᴋᴀɴ ɢᴜɴᴀᴋᴀɴ ᴄᴏᴍᴍᴀɴᴅ {}sᴇᴀʀᴄʜʟʏʀɪᴄ {}|「ɴᴜᴍʙᴇʀ」".format(str(setKey), str(search))
                                    ririn.sendMessage(to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["results"]):
                                        lyric = data["results"][num - 1]
                                        api = requests.get("http://api.secold.com/joox/sid/{}".format(str(lyric["songid"])))
                                        data = api.text
                                        data = json.loads(data)
                                        lyrics = data["results"]["lyric"]
                                        lyric = lyrics.replace('ti:','Title - ')
                                        lyric = lyric.replace('ar:','Artist - ')
                                        lyric = lyric.replace('al:','Album - ')
                                        removeString = "[1234567890.:]"
                                        for char in removeString:
                                            lyric = lyric.replace(char,'')
                                        ririn.sendMessage(msg.to, str(lyric))
                            elif cmd.startswith("searchyoutube"):
                                sep = text.split(" ")
                                search = text.replace(sep[0] + " ","")
                                params = {"search_query": search}
                                r = requests.get("https://www.youtube.com/results", params = params)
                                soup = BeautifulSoup(r.content, "html5lib")
                                ret_ = "╔══[ ʀᴇsᴜʟᴛ ʏᴏᴜᴛᴜʙᴇ ]"
                                datas = []
                                for data in soup.select(".yt-lockup-title > a[title]"):
                                    if "&lists" not in data["href"]:
                                        datas.append(data)
                                for data in datas:
                                    ret_ += "\n╠❂➣{} ]".format(str(data["title"]))
                                    ret_ += "\n╠❂ https://www.youtube.com{}".format(str(data["href"]))
                                ret_ += "\n╚══[ ᴛᴏᴛᴀʟ {} ᴠɪᴅᴇᴏ ]".format(len(datas))
                                ririn.sendMessage(to, str(ret_))
                            elif cmd.startswith("tr-"):
                                sep = text.split("-")
                                sep = sep[1].split(" ")
                                lang = sep[0]
                                say = text.replace("tr-" + lang + " ","")
                                if lang not in list_language["list_translate"]:
                                    return ririn.sendMessage(to, "Language not found")
                                translator = Translator()
                                hasil = translator.translate(say, dest=lang)
                                A = hasil.text
                                ririn.sendMessage(to, str(A))
# Pembatas Script #
# Pembatas Script #
                        if text.lower() == "mykey":
                            ririn.sendMessage(to, "ᴋᴇʏᴄᴏᴍᴍᴀɴᴅ sᴀᴀᴛ ɪɴɪ [ {} ]".format(str(wait["keyCommand"])))
                        elif text.lower() == "setkey on":
                            wait["setKey"] = True
                            ririn.sendMessage(to, "ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢᴀᴋᴛɪғᴋᴀɴ sᴇᴛᴋᴇʏ")
                        elif text.lower() == "setkey off":
                            wait["setKey"] = False
                            ririn.sendMessage(to, "ʙᴇʀʜᴀsɪʟ ᴍᴇɴᴏɴᴀᴋᴛɪғᴋᴀɴ sᴇᴛᴋᴇʏ")
# Pembatas Script #
                    elif msg.contentType == 1:
                        if wait["changePictureProfile"] == True:
                            path = ririn.downloadObjectMsg(msg_id)
                            wait["changePictureProfile"] = False
                            ririn.updateProfilePicture(path)
                            ririn.sendMessage(to, "sᴜᴄᴄᴇs ᴄʜᴀɴɢᴇ ᴘʜᴏᴛᴏ ᴘʀᴏғɪʟᴇ")
                        if msg.toType == 2:
                            if to in wait["changeGroupPicture"]:
                                path = ririn.downloadObjectMsg(msg_id)
                                wait["changeGroupPicture"].remove(to)
                                ririn.updateGroupPicture(to, path)
                                ririn.sendMessage(to, "sᴜᴄᴄᴇs ᴄʜᴀɴɢᴇ ᴘʜᴏᴛᴏ ɢʀᴏᴜᴘ")
                    elif msg.contentType == 7:
                        if wait["checkSticker"] == True:
                            stk_id = msg.contentMetadata['STKID']
                            stk_ver = msg.contentMetadata['STKVER']
                            pkg_id = msg.contentMetadata['STKPKGID']
                            ret_ = "╔════[ sᴛɪᴄᴋᴇʀ ɪɴғᴏ ] "
                            ret_ += "\n╠❂➣ sᴛɪᴄᴋᴇʀ ɪᴅ : {}".format(stk_id)
                            ret_ += "\n╠❂➣ sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋᴀɢᴇs ɪᴅ : {}".format(pkg_id)
                            ret_ += "\n╠❂➣ sᴛɪᴄᴋᴇʀ ᴠᴇʀsɪᴏɴ : {}".format(stk_ver)
                            ret_ += "\n╠❂➣ sᴛɪᴄᴋᴇʀ ᴜʀʟ : line://shop/detail/{}".format(pkg_id)
                            ret_ += "\n╚════[ ✯ ᴅɴᴀ ʙᴏᴛ ✯ ]"
                            ririn.sendMessage(to, str(ret_))
                    elif msg.contentType == 13:
                        if wait["checkContact"] == True:
                            try:
                                contact = ririn.getContact(msg.contentMetadata["mid"])
                                if ririn != None:
                                    cover = ririn.getProfileCoverURL(msg.contentMetadata["mid"])
                                else:
                                    cover = "Tidak dapat masuk di line channel"
                                path = "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                                try:
                                    ririn.sendImageWithURL(to, str(path))
                                except:
                                    pass
                                ret_ = "╔═══[ ᴅᴇᴛᴀɪʟs ᴄᴏɴᴛᴀᴄᴛ ]"
                                ret_ += "\n╠❂➣ ɴᴀᴍᴀ : {}".format(str(contact.displayName))
                                ret_ += "\n╠❂➣ ᴍɪᴅ : {}".format(str(msg.contentMetadata["mid"]))
                                ret_ += "\n╠❂➣ ʙɪᴏ : {}".format(str(contact.statusMessage))
                                ret_ += "\n╠❂➣ ɢᴀᴍʙᴀʀ ᴘʀᴏғɪʟᴇ : http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                                ret_ += "\n╠❂➣ ɢᴀᴍʙᴀʀ ᴄᴏᴠᴇʀ : {}".format(str(cover))
                                ret_ += "\n╚════[ ✯ ᴅɴᴀ ʙᴏᴛ ✯ ]"
                                ririn.sendMessage(to, str(ret_))
                            except:
                                ririn.sendMessage(to, "ᴋᴏɴᴛᴀᴋ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ")
                    elif msg.contentType == 16:
                        if wait["checkPost"] == True:
                            try:
                                ret_ = "╔════[ ᴅᴇᴛᴀɪʟs ᴘᴏsᴛ ]"
                                if msg.contentMetadata["serviceType"] == "GB":
                                    contact = ririn.getContact(sender)
                                    auth = "\n╠❂➣ ᴀᴜᴛʜᴏʀ : {}".format(str(contact.displayName))
                                else:
                                    auth = "\n╠❂➣ ᴀᴜᴛʜᴏʀ : {}".format(str(msg.contentMetadata["serviceName"]))
                                purl = "\n╠❂➣ ᴜʀʟ : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                ret_ += auth
                                ret_ += purl
                                if "mediaOid" in msg.contentMetadata:
                                    object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                    if msg.contentMetadata["mediaType"] == "V":
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n╠❂➣ ᴏʙᴊᴇᴄᴛ ᴜʀʟ : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                            murl = "\n╠❂➣ ᴍᴇᴅɪᴀ ᴜʀʟ : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n╠❂➣ ᴏʙᴊᴇᴄᴛ ᴜʀʟ : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                            murl = "\n╠❂➣ ᴍᴇᴅɪᴀ ᴜʀʟ : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                        ret_ += murl
                                    else:
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n╠❂➣ ᴏʙᴊᴇᴄᴛ ᴜʀʟ : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n╠❂➣ ᴏʙᴊᴇᴄᴛ ᴜʀʟ : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                    ret_ += ourl
                                if "stickerId" in msg.contentMetadata:
                                    stck = "\n╠❂➣ sᴛɪᴄᴋᴇʀ : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                    ret_ += stck
                                if "text" in msg.contentMetadata:
                                    text = "\n╠❂➣ ɴᴏᴛᴇ : {}".format(str(msg.contentMetadata["text"]))
                                    ret_ += text
                                ret_ += "\n╚════[ ✯ ᴅɴᴀ ʙᴏᴛ ✯ ]"
                                ririn.sendMessage(to, str(ret_))
                            except:
                                ririn.sendMessage(to, "ɪɴᴠᴀʟɪᴅ ᴘᴏsᴛ")
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
                
        if op.type == 26:
            msg = op.message
            if wait["autoResponPc"] == True:
                if msg.toType == 0:
                    ririn.sendChatChecked(msg._from,msg.id)
                    contact = ririn.getContact(msg._from)
                    cName = contact.displayName
                    balas = ["╔════════════════════╗\n                   「ᴀᴜᴛᴏ ʀᴇᴘʟʏ」\n                             ʙʏ:\n                    ✰ ᴅɴᴀ ʙᴏᴛ ✰\n╚════════════════════╝\n\nʜᴀʟʟᴏ 「" + cName + "」\nᴍᴏʜᴏɴ ᴍᴀᴀғ sᴀʏᴀ sᴇᴅᴀɴɢ sɪʙᴜᴋ, ɪɴɪ ᴀᴅᴀʟᴀʜ ᴘᴇsᴀɴ ᴏᴛᴏᴍᴀᴛɪs, ᴊɪᴋᴀ ᴀᴅᴀ ʏᴀɴɢ ᴘᴇɴᴛɪɴɢ ᴍᴏʜᴏɴ ʜᴜʙᴜɴɢɪ sᴀʏᴀ ɴᴀɴᴛɪ, ᴛᴇʀɪᴍᴀᴋᴀsɪʜ...","╔════════════════════╗\n                   「ᴀᴜᴛᴏ ʀᴇᴘʟʏ」\n                             ʙʏ:\n                    ✰ ᴅɴᴀ ʙᴏᴛ ✰\n╚════════════════════╝\n\nʜᴀʟʟᴏ 「" + cName + "」\nsᴀʏᴀ ʟᴀɢɪ sɪʙᴜᴋ ʏᴀ ᴋᴀᴋ ᴊᴀɴɢᴀɴ ᴅɪɢᴀɴɢɢᴜ","╔════════════════════╗\n                   「ᴀᴜᴛᴏ ʀᴇᴘʟʏ」\n                             ʙʏ:\n                    ✰ ᴅɴᴀ ʙᴏᴛ ✰\n╚════════════════════╝\n\nʜᴀʟʟᴏ 「" + cName + "」\nsᴀʏᴀ sᴇᴅᴀɴɢ ᴛɪᴅᴜʀ ᴋᴀᴋ"]
                    dee = "" + random.choice(balas)
                    ririn.sendImageWithURL(msg._from, "http://dl.profile.line-cdn.net{}".format(contact.picturePath))
                    ririn.sendMessage(msg._from,dee)
                
        if op.type == 26:
            try:
                print ("[ 26 ] RECIEVE MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != ririn.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if wait["autoRead"] == True:
                        ririn.sendChatChecked(to, msg_id)
                    if to in read["readPoint"]:
                        if sender not in read["ROM"][to]:
                            read["ROM"][to][sender] = True
                    if sender in wait["mimic"]["target"] and wait["mimic"]["status"] == True and wait["mimic"]["target"][sender] == True:
                        text = msg.text
                        if text is not None:
                            ririn.sendMessage(msg.to,text)
                    if wait["unsendMessage"] == True:
                        try:
                            msg = op.message
                            if msg.toType == 0:
                                ririn.log("[{} : {}]".format(str(msg._from), str(msg.text)))
                            else:
                                ririn.log("[{} : {}]".format(str(msg.to), str(msg.text)))
                                msg_dict[msg.id] = {"text": msg.text, "from": msg._from, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                        except Exception as error:
                            logError(error)
                    if msg.contentType == 0:
                        if text is None:
                            return
                        if "/ti/g/" in msg.text.lower():
                            if wait["autoJoinTicket"] == True:
                                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                links = link_re.findall(text)
                                n_links = []
                                for l in links:
                                    if l not in n_links:
                                        n_links.append(l)
                                for ticket_id in n_links:
                                    group = ririn.findGroupByTicket(ticket_id)
                                    ririn.acceptGroupInvitationByTicket(group.id,ticket_id)
                                    ririn.sendMessage(to, "sᴜᴄᴄᴇssғᴜʟʟʏ ᴇɴᴛᴇʀᴇᴅ ᴛʜᴇ ɢʀᴏᴜᴘ %s" % str(group.name))
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if ririnMid in mention["M"]:
                                    if wait["autoRespon"] == True:
                                    	ririn.sendChatChecked(msg._from,msg.id)
                                    	contact = ririn.getContact(msg._from)
                                    	ririn.sendImageWithURL(msg._from, "http://dl.profile.line-cdn.net{}".format(contact.picturePath))
                                    	sendMention(sender, "ᴏɪ ᴍʙʟᴏ @!      ,\nɴɢᴀᴘᴀɪɴ ᴛᴀɢ ᴛᴀɢ ɢᴡ", [sender])
                                    	dee = "" + random.choice(balas)
                                    break
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
        if op.type == 65:
            print ("[ 65 ] NOTIFIED DESTROY MESSAGE")
            if wait["unsendMessage"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                            contact = ririn.getContact(msg_dict[msg_id]["from"])
                            if contact.displayNameOverridden != None:
                                name_ = contact.displayNameOverridden
                            else:
                                name_ = contact.displayName
                                ret_ = "sᴇɴᴅ ᴍᴇssᴀɢᴇ ᴄᴀɴᴄᴇʟʟᴇᴅ."
                                ret_ += "\nsᴇɴᴅᴇʀ : @!"       
                                ret_ += "\nsᴇɴᴅ ᴀᴛ : {}".format(str(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"]))))
                                ret_ += "\nᴛʏᴘᴇ : {}".format(str(Type._VALUES_TO_NAMES[msg_dict[msg_id]["contentType"]]))
                                ret_ += "\nᴛᴇxᴛ : {}".format(str(msg_dict[msg_id]["text"]))
                                sendMention(at, str(ret_), [contact.mid])
                            del msg_dict[msg_id]
                        else:
                            ririn.sendMessage(at,"sᴇɴᴛᴍᴇssᴀɢᴇ ᴄᴀɴᴄᴇʟʟᴇᴅ,ʙᴜᴛ ɪ ᴅɪᴅɴ'ᴛ ʜᴀᴠᴇ ʟᴏɢ ᴅᴀᴛᴀ.\nsᴏʀʀʏ > <")
                except Exception as error:
                    logError(error)
                    traceback.print_tb(error.__traceback__)
                    
        if op.type == 55:
        	try:
        		group_id = op.param1
        		user_id=op.param2
        		subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
        	except Exception as e:
        		print(e)
	      
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                    	ririn.sendMention(op.param1, "ᴡᴏʏ ☞ @! ☜ \nᴅɪᴇᴍ ᴅɪᴇᴍ ʙᴀᴇ...\nsɪɴɪ ɪᴋᴜᴛ ɴɢᴏᴘɪ", [op.param2])
                                    else:
                                    	ririn.sendMessage(op.param1, "ᴍʙʟᴏ ☞ @! ☜ \nɴɢɪɴᴛɪᴘ ᴅᴏᴀɴɢ ʟᴜ\nsɪɴɪ ɢᴀʙᴜɴɢ", [op.param2])
                                else:
                                	ririn.sendMessage(op.param1, "ᴛᴏɴɢ ☞ @! ☜ \nɴɢᴀᴘᴀɪɴ ʟᴜ...\nɢᴀʙᴜɴɢ ᴄʜᴀᴛ sɪɴɪ", [op.param2])
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass
                
        if op.type == 55:
            print ("[ 55 ] NOTIFIED READ MESSAGE")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                else:
                   pass
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
    except Exception as error:
        logError(error)
        traceback.print_tb(error.__traceback__)

while True:
    try:
        delete_log()
        ops = ririnPoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                ririnBot(op)
                ririnPoll.setRevision(op.revision)
    except Exception as error:
        logError(error)
        
def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
atexit.register(atend)
