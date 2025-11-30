from django import template

register = template.Library()


@register.filter
def split_tags(value, sep=','):
    """Split a comma-separated tags string and strip whitespace from each tag.

    Usage in template:
        {% load idea_tags %}
        {% for tag in idea.tags|split_tags %}...
    """
    if not value:
        return []
    try:
        parts = [p.strip() for p in value.split(sep) if p.strip()]
        return parts
    except Exception:
        return []
