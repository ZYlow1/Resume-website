from django import template

register = template.Library()


@register.filter
def star_range(level):
    """返回星级评分的 HTML，level 为 1-5"""
    filled = "★" * level
    empty = "★" * (5 - level)
    return f'{filled}<span class="empty">{empty}</span>'
