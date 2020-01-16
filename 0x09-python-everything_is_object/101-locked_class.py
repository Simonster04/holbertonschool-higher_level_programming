#!/usr/bin/python3
class LockedClass:
    """ only avoids the user to create a new instance attribute
     called firts_name """
    __slots__ = ['first_name']
