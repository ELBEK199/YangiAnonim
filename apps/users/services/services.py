from apps.users.models import User
from django.core.exceptions import ObjectDoesNotExist


def create_user_service(username, password, first_name='', last_name='', is_admin=False, is_active=True):
    user = User(
        username=username,
        first_name=first_name,
        last_name=last_name,
        is_admin=is_admin,
        is_active=is_active
    )
    user.set_password(password)
    user.save()
    return user


def update_user_service(user, data):
    # Faqat allowed fieldlarni update qilamiz
    for attr in ['username', 'first_name', 'last_name', 'is_admin', 'is_active']:
        if attr in data:
            setattr(user, attr, data[attr])
    # Password update bo‘lsa
    if 'password' in data and data['password']:
        user.set_password(data['password'])
    user.save()
    return user


def delete_user_service(user_id):
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        return True
    except ObjectDoesNotExist:
        return False


def get_user_by_id_service(user_id):
    try:
        return User.objects.get(id=user_id)
    except ObjectDoesNotExist:
        return None


def get_user_list_service():
    return User.objects.all().order_by('-date_joined')
