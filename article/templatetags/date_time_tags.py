from django import template
import datetime
from polls.templatetags import date_convertor

register = template.Library()


@register.filter
def to_date_format(date: datetime):
    return date_convertor.DateConvertor.to_date_format(date) if date is not None else None


@register.filter
def to_date_string_format(date: datetime):
    return date_convertor.DateConvertor.to_date_string_format(date) if date is not None else None


@register.filter
def to_time_12_format(date: datetime):
    return date_convertor.DateConvertor.to_time_12_format(date) if date is not None else None


@register.filter
def to_time_24_format(date: datetime):
    return date_convertor.DateConvertor.to_time_24_format(date) if date is not None else None


@register.filter
def time_ago(date: datetime):
    return date_convertor.DateConvertor.time_ago(date)
