import sys
import csv

import dateutil.parser
import facebook


class FbApi:
    API_VERSION = '2.8'

    @classmethod
    def get_graph(cls, token):
        return facebook.GraphAPI(access_token=token,
                                 version=cls.API_VERSION)

    @classmethod
    def calc_fb_reg_date(cls, user_token):
        """
        Get approximate user registration date by finding the oldest post in
        his feed.

        Assumptions:
            - User token has user_posts permission

        Alternative ways:
            - Get the oldest photo. Downsides: 1) Will require user_photos
            permission which is more suspicious. 2) Users are more likely to
            delete their oldest photo than delete the oldest post.
            - Build more complex logic to analyze multiple resources: feed,
            photos, likes, events, connections etc. Downsides: 1) lots of time.
            2) Lots of permissions

        :return: datetime obj
        """
        feed = []
        try:
            graph = cls.get_graph(user_token)
            # TODO paginate to the very end
            feed = graph.get_object("me/feed?fields=created_time")['data']
        except facebook.GraphAPIError as ex:
            raise Exception("Cannot determine registration date due to error:"
                            "{}".format(repr(ex)))
        if not feed:
            raise Exception("User has no posts, cannot determine his "
                            "approximate registration date.")

        oldest_post_date = dateutil.parser.parse(feed[-1]['created_time'])
        return oldest_post_date


class User:
    def __init__(self, fbid, token, username, regdate=None):
        self.fbid = fbid
        self.token = token
        self.username = username
        self._regdate = regdate

    @property
    def regdate(self):
        if not self._regdate:
            self._regdate = FbApi.calc_fb_reg_date(self.token)
        return self._regdate


def user_from_tuple(t):
    fbid, token, username = t
    return User(fbid, token, username)


def user_to_tuple(u):
    return u.username, u.fbid, u.regdate.strftime("%Y-%m-%d")


def read_users(file_csv_in):
    user_reader = csv.reader(file_csv_in)
    for row in user_reader:
        user = user_from_tuple(row)
        yield user


def write_users(users, file_csv_out):
    user_writer = csv.writer(file_csv_out)
    for user in users:
        row = user_to_tuple(user)
        user_writer.writerow(row)


def cli():
    path_csv_in = sys.argv[1]
    with open(path_csv_in, newline='') as csvfile:
        users = read_users(csvfile)
        write_users(users, sys.stdout)


if __name__ == "__main__":
    cli()
