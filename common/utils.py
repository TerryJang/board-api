from exception import InvalidParam


class Utils:
    @staticmethod
    def check_password(request_pass, stored_pass):
        if request_pass != stored_pass:
            raise InvalidParam('비밀번호가 일치하지 않습니다.')