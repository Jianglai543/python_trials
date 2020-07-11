import operator


class userId:
    def __init__(self, name):
        self.user_id = name

    def __repr__(self):
        return 'userId({})'.format(self.user_id)

user = [userId(2), userId(33), userId(77)]
user_sort = sorted(user, key = lambda x: x.user_id)
print(user_sort)

user_sort2 = sorted(user, key=operator.attrgetter('user_id'))
print(user_sort2)
