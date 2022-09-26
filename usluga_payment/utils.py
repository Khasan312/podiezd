import random 
import string


def random_number_generator(size=20, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))



def unique_number_generator(instance):

    order_new_id = random_number_generator()
    obj = instance.__class__
    qs_exists = obj.objects.filter(random_number=order_new_id).exists()
    if qs_exists:
        return order_new_id
    return order_new_id
