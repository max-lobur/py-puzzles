from datetime import datetime

import fb_calc


def test_user_from_tuple():
    user_t = ("100015396787297", "EAACEdEose", "Mary Seligsteinwitz")
    user = fb_calc.user_from_tuple(user_t)
    assert user.fbid == user_t[0]
    assert user.token == user_t[1]
    assert user.username == user_t[2]


def test_user_to_tuple():
    user = fb_calc.User("id", "test_token", "name last",
                        datetime(2015, 2, 3))
    user_t = fb_calc.user_to_tuple(user)
    assert user_t == (user.username, user.fbid,
                      user.regdate.strftime("%Y-%m-%d"))


def test_user_regdate(monkeypatch):
    fake_regdate = datetime(2016, 3, 4)

    def mock_calc(*args, **kwargs):
        return fake_regdate
    monkeypatch.setattr(fb_calc.FbApi, 'calc_fb_reg_date', mock_calc)

    user = fb_calc.User("id", "test_token", "name last")
    assert user.regdate == fake_regdate
