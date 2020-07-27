"""
In Windows Active Directory,
a group can consist of user(s) and group(s) themselves.
We can construct this hierarchy as such.
Where User is represented by str representing their ids.
"""
class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

"""
Write a function that provides an efficient
look up of whether the user is in a group.
"""
def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.users:
        return True

    for sub_group in group.groups:
        if is_user_in_group(user, sub_group):
            return True

    return False

parent = Group("parent")
child = Group("child")
sub_child = Group("sub_child")

non_parent = Group("non_parent")
child_sibling = Group("child_sibling")
sub_child_sibling = Group("sub_child_sibling")
sub_sub_child = Group("sub_sub_child")

parent.add_group(child)
parent.add_group(child_sibling)
child.add_group(sub_child)
child.add_group(sub_child_sibling)
sub_child.add_group(sub_sub_child)

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

# when user in group, true
assert( is_user_in_group(sub_child_user, sub_child) is True )

# when user group in group, true
assert( is_user_in_group(sub_child_user, child) is True )

# when user group in group in group, true
assert( is_user_in_group(sub_child_user, parent) is True )

# when user not in group
assert( is_user_in_group(sub_child_user, non_parent ) is False )
assert( is_user_in_group(sub_child_user, child_sibling ) is False )
assert( is_user_in_group(sub_child_user, sub_child_sibling ) is False )
assert( is_user_in_group(sub_child_user, sub_sub_child ) is False )
