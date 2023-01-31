from django import template
import random
import string

register = template.Library()


def my_random_filter(value):  # Only one argument.
    letters = string.ascii_letters
    rand_article_slag = ''.join(random.choice(letters) for i in range(5)) + '-' \
                        + ''.join(random.choice(letters) for i in range(5))
    return rand_article_slag


register.filter('my_random_filter', my_random_filter)
