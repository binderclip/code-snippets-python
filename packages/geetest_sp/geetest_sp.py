from geetest import GeetestLib


GEETEST_ID = 'e285deeeeeeeeeeeeeeeeeeeeeeeeeee'
GEETEST_KEY = '16f7317eeeeeeeeeeeeeeeeeeeeeeeee'


def get_status_and_response_str(gt, user_id):
    return gt.pre_process(user_id), gt.get_response_str()
    # {"success": 1, "gt": "e285deeeeeeeeeeeeeeeeeeeeeeeeeee", "challenge": "2cd858e8243972a277a715dd7a45e82a"}
    # {"success": 0, "gt": "e285deeeeeeeeeeeeeeeeeeeeeeeeeee", "challenge": "70efdf2ec9b086079795c442636b55fb1f"}


def main():
    gt = GeetestLib(GEETEST_ID, GEETEST_KEY)
    user_id = 1
    get_status_and_response_str(gt, user_id)


if __name__ == '__main__':
    main()
