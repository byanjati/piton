
def isSubstr(str_a, str_b):
    return str_b.find(str_a) != -1

def subset(str_a, str_b):
    """
    We have to create the set chars of str_a
    and then compare to set chars of b
    """
    charset_a = set(str_a)
    charset_b = set(str_b)

    is_charset_a_in_charset_b = charset_a.intersection(charset_b) == charset_a
    return is_charset_a_in_charset_b

def prefix(str_a, str_b):
    """
    When str_a found the position of subset and
    the position is less than the length of str_b
    """
    return str_b.startswith(str_a)

def find_smallest_lexicograph(str_a, length):
    def create_smallest_lexicograph(str_a, length):
        """
        Backwards process from last char of the string
        Get latest char, Find the higher alphabet from the set
        If found the higher, set the flag true, then create a char with the greater char founded
        else just create the smallest char from the set
        Then, move to the n-1 char, do the same things on above
        do until the pointer position is 0
        and return the created string from the process

        from the flag false->true, cut the string, and join the new string with cutted string
        and return the join
        """

        set_str = set(str_a)
        if len(str_a) < length:
            new_str="%s%s"%(str_a, min(set_str) * (length-len(str_a)))
            return new_str
        else:
            reverse_str_a = str_a[:length][::-1]
            lexicograph_str = []
            flag_lexi = False

            def create_max_char(char, reverse_str_a):
                sorted_list_str = sorted(set(reverse_str_a))
                char_pos=sorted_list_str.index(char)
                return sorted_list_str[char_pos+1]

            for char in reverse_str_a:
                "find the greater char on the set compared with char loop"
                if char >= max(set_str):
                    lexicograph_str.append(min(set_str))
                else:
                    if char <= max(set_str) and flag_lexi == False:
                        new_max = create_max_char(char, set_str)
                        lexicograph_str.append(new_max)
                        flag_lexi=True
                if flag_lexi:
                    char_pos=reverse_str_a.find(char)
                    pre_lexi=reverse_str_a[char_pos+1:][::-1]
                    make_lexi_str = "".join(sorted(lexicograph_str, reverse=True))
                    new_str = "%s%s" % (pre_lexi, make_lexi_str)
                    return new_str

            make_lexi_str = "".join(sorted(lexicograph_str, reverse=True))
            return make_lexi_str
    return create_smallest_lexicograph(str_a, length)

def test_find_the_smallest_lexicographical_string_length_is_2():
    str_a = "abc"
    actual = find_smallest_lexicograph(str_a, 2)
    expected = "ac"

    assert expected == actual

def test_find_the_smallest_lexicographical_string_length_is_3():
    str_a = "ayy"
    actual = find_smallest_lexicograph(str_a, 3)
    expected = "yaa"

    assert expected == actual

def test_find_the_smallest_lexicographical_string_another():
    str_a = "baac"
    actual = find_smallest_lexicograph(str_a, 4)
    expected = "baba"

    assert expected == actual

def test_find_the_smallest_lexicographical_when_string_length_is_unsufficient():
    str_a = "ab"
    actual = find_smallest_lexicograph(str_a, 5)
    expected = "abaaa"

    assert expected == actual

def test_first_str_is_substring_of_second_str():
    "Example, that abc is a substring of abcd"
    actual = isSubstr("abc", "abcd")
    assert actual is True

def test_if_the_first_str_chars_are_the_subset_chars_of_second_str():
    "Example, that aca is the subset of abc"
    actual = subset("aca", "abcd")
    assert actual is True

def test_first_str_is_prefix_of_second_str_when_false():
    """
    Example, that abc is a prefix of abcd
    But, the def is not the prefix of cdef
    """
    actual = prefix("def", "cdef")
    assert actual is False

def test_first_str_is_prefix_of_second_str_when_true():
    """
    Example, that abc is a prefix of abcd
    But, the def is not the prefix of cdef
    """
    actual = prefix("def", "defabc")
    assert actual is True

n,k = [int(x) for x in input().split()]
input_string = str(input())
lexi = find_smallest_lexicograph(input_string, k)

print(lexi)
