from django import template
import random
import string

register = template.Library()


def my_random_filter_id_slag(value):  # Only one argument.
    if value == 'id':
        letters = string.digits
        return ''.join(random.choice(letters) for i in range(2))
    else:
        # slag
        letters = string.ascii_letters
        rand_article_slag = ''.join(random.choice(letters) for i in range(5)) + '-' \
                            + ''.join(random.choice(letters) for i in range(5))
        return rand_article_slag




register.filter('my_random_filter_id_slag', my_random_filter_id_slag)
