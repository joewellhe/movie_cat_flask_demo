import random
import string
import hashlib
import base64


class PasswordUtil(object):

    @staticmethod
    def gen_salt(length=16):
        salt_list = [random.choice(string.ascii_letters + string.digits) for _ in range(length)]
        return ''.join(salt_list)

    @staticmethod
    def gen_password(password, salt):
        m = hashlib.md5()
        pwd_str = "{}-{}".format(base64.encodebytes(password.encode("utf-8")), salt)
        m.update(pwd_str.encode("utf-8"))
        return m.hexdigest()

    @staticmethod
    def gen_auth_code(user):
        m = hashlib.md5()
        auth_str = "{}-{}-{}-{}-{}".format(user.id, user.login_name, user.login_pwd,
                                           user.login_salt, user.status)
        m.update(auth_str.encode("utf-8"))
        return m.hexdigest()

