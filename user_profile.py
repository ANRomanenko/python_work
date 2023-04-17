# Использование произвольного набора именованных аргументов

def build_profile(first, last, **user_info):
    """Строит словарь с информацией для пользователя"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')

print(user_profile)
print()


def make_sendvich(*args):
    print("\nMake sendvich please:")
    for sendv in args:
        print(f"- {sendv}")


make_sendvich('burger')
make_sendvich('sosiska', 'testo v sosiske')
make_sendvich('kartoha', 'pizza', 'kapusta')