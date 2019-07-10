import re


def eq(value, expected):
    """ value is equal to expected

    >>> eq(1, 1)
    True
    """
    assert value == expected


def ne(value, expected):
    """ value is equal to expected

    >>> eq(1, 1)
    False
    """
    assert value != expected


def gt(value, expected):
    """ value is greater than expected

    >>> gt(1, 1)
    False

    >>> gt(1, 0)
    True

    >>> gt(1, 2)
    False
    """
    assert value > expected


def ge(value, expected):
    """ value is greater than or equal to expected

    >>> ge(1, 1)
    True

    >>> ge(1, 0)
    True

    >>> ge(1, 2)
    False
    """
    assert value >= expected


def abs_eq(value, expected):
    """ value is approx equal to expected
    """
    assert round(float(value), 2) == round(float(expected), 2)


def lt(value, expected):
    """ value is less than excepted
    """
    assert value < expected


def le(value, expected):
    """ value is less than or equal to excepted
    """
    assert value <= expected


def str_eq(value, expected):
    """ value is equal to excepted as string
    """
    assert str(value) == str(expected)


def float_eq(value, expected):
    """ value is equal to excepted as float
    """
    assert round(float(value), 2) == round(float(expected), 2)


def len_eq(value, expected):
    """ length of value is equal to excepted
    """
    assert isinstance(expected, int)
    assert len(value) == expected


def len_gt(value, expected):
    """ length of value is greater than excepted
    """
    assert isinstance(expected, int)
    assert len(value) > expected


def len_ge(value, expected):
    """ length of value is greater than or equal to excepted
    """
    assert isinstance(expected, int)
    assert len(value) >= expected


def len_lt(value, expected):
    """ length of value is less than excepted
    """
    assert isinstance(expected, int)
    assert len(value) < expected


def len_le(value, expected):
    """ length of value is less than or equal to excepted
    """
    assert isinstance(expected, int)
    assert len(value) <= expected


def contains(value, expected):
    """ value is contains expected
    """
    assert isinstance(value, list)
    assert expected in value


def contained_by(value, expected):
    """ value is contained by expected
    """
    assert isinstance(expected, list)
    assert value in expected


def type_eq(value, expected):
    assert isinstance(value, expected)


def regex(value, expected):
    assert isinstance(expected, str)
    assert isinstance(value, str)
    assert re.match(expected, value)


def startswith(value, expected):
    assert str(value).startswith(expected)


def endswith(value, expected):
    assert str(value).endswith(expected)


def object_contains(value, expected):
    assert str(expected) in str(value)


def object_not_contains(value, expected):
    assert str(expected) not in str(value)


mapper = {
    "eq": eq,
    "equals": eq,
    "==": eq,
    "abs_eq": abs_eq,
    "abs_equals": abs_eq,
    "lt": lt,
    "less_than": lt,
    "le": le,
    "less_than_or_equals": le,
    "gt": gt,
    "greater_than": gt,
    "ge": ge,
    "greater_than_or_equals": ge,
    "ne": ne,
    "not_equals": ne,
    "str_eq": str_eq,
    "string_equals": str_eq,
    "float_eq": float_eq,
    "float_equals": float_eq,
    "len_eq": len_eq,
    "length_equals": len_eq,
    "count_eq": len_eq,
    "len_gt": len_gt,
    "count_gt": len_gt,
    "length_greater_than": len_gt,
    "count_greater_than": len_gt,
    "len_ge": len_ge,
    "count_ge": len_ge,
    "length_greater_than_or_equals": len_ge,
    "count_greater_than_or_equals": len_ge,
    "len_lt": len_lt,
    "count_lt": len_lt,
    "length_less_than": len_lt,
    "count_less_than": len_lt,
    "len_le": len_le,
    "count_le": len_le,
    "length_less_than_or_equals": len_le,
    "count_less_than_or_equals": len_le,
    "contains": contains,
    "contained_by": contained_by,
    "type": type_eq,
    "regex": regex,
    "startswith": startswith,
    "endswith": endswith,
    "object_contains": object_contains,
    "object_not_contains": object_not_contains,
}


class CompareError(Exception):
    pass


def check(name, value, expected):
    if name not in mapper:
        raise CompareError("comparator {} is not found".format(name))

    try:
        return mapper.get(name)(value, expected)
    except AssertionError as e:
        msg = "assert error, expect {} {} {}, got error {}".format(
            value, name, expected, e
        )
        raise CompareError(msg)
