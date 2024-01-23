from django.utils.translation import get_language
from django.conf import settings
import jdatetime
import datetime
import timeago
import pytz
import re

# Writing a tag template to date convertor
PERSIAN_MONTH_NAMES = [
    "",
    "فروردین",
    "اردیبهشت",
    "خرداد",
    "تیر",
    "مرداد",
    "شهریور",
    "مهر",
    "آبان",
    "آذر",
    "دی",
    "بهمن",
    "اسفند"
]

PERSIAN_WEEKDAY_NAMES = [
    "شنبه",
    "یکشنبه",
    "دوشنبه",
    "سه‌شنبه",
    "چهارشنبه",
    "پنجشنبه",
    "جمعه"
]


class DateConvertor:
    @staticmethod
    def is_valid(date: str):
        if get_language() == "fa":
            return re.match(
                "^[1-4]\d{3}\/((0[1-6]\/((3[0-1])|([1-2][0-9])|(0[1-9])))|((1[0-2]|(0[7-9]))\/(30|([1-2][0-9])|(0[1-9]))))$",
                date)
        return re.match(
            "^\d{4}[\-\/\s]?((((0[13578])|(1[02]))[\-\/\s]?(([0-2][0-9])|(3[01])))|(((0[469])|(11))[\-\/\s]?(([0-2][0-9])|(30)))|(02[\-\/\s]?[0-2][0-9]))$",
            date)

    @staticmethod
    def to_current_time_zone_datetime(date: str):
        try:
            year, month, day = date.replace("-", "/").split("/")

            if get_language() == "fa":
                return jdatetime.datetime(year=int(year), month=int(month), day=int(day)).togregorian().replace(hour=12,
                                                                                                                minute=0,
                                                                                                                second=0)

            return datetime.datetime(year=int(year), month=int(month), day=int(day)).replace(hour=12, minute=0,
                                                                                             second=0)
        except Exception as e:
            print(e)

    @staticmethod
    def to_date_format(date: datetime):
        if get_language() == "fa":
            jalali_date = jdatetime.datetime.fromgregorian(datetime=date)
            return jalali_date.strftime("%Y/%m/%d")

        return date.strftime("%Y-%m-%d")

    @staticmethod
    def to_date_string_format(date: datetime):
        if get_language() == "fa":
            date = date.astimezone(pytz.timezone(settings.TIME_ZONE))
            jalali_date = jdatetime.datetime.fromgregorian(datetime=date)
            month_name = PERSIAN_MONTH_NAMES[int(jalali_date.strftime("%-m"))]
            day_name = PERSIAN_WEEKDAY_NAMES[int(jalali_date.strftime("%w"))]
            return jalali_date.strftime(f"{day_name} , %d {month_name} %Y")

        return date.strftime("%A, %d %B %Y")

    @staticmethod
    def to_time_24_format(date: datetime):
        return date.astimezone(pytz.timezone(settings.TIME_ZONE)).strftime("%H:%M")

    @staticmethod
    def to_time_12_format(date: datetime):
        return date.astimezone(pytz.timezone(settings.TIME_ZONE)).strftime("%I:%M %p")

    @staticmethod
    def time_ago(date: datetime):
        if get_language() == "fa":
            return timeago.format(date, datetime.datetime.now(), 'fa_IR')

        return timeago.format(date, datetime.datetime.now(), 'en')
