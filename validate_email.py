"""  Python challenge 2
Given an integer N followed by N email addresses.
Valid email addresses must follow these rules:
        • It must have the username@domainname.extension format type.
        • The username can only contain letter s, digits, dashes and underscores.
        • The website name can only have letters and digits.
        • The maximum length of the extension is 3
Program prints a list containing only valid email addresses in lexicographical order.
"""
import re


def check(email_id):
    """
    This function validates if given email id is valid or not.
    :param email_id: email address
    :return: boolean value
    """
    regex = '^\w+([\.-]?\w+)*@([a-zA-Z0-9])+(\.\w{1,3})$'
    if re.fullmatch(regex, email_id):
        return True
    return False


# Driver Code
if __name__ == '__main__':
    lex_lst = []
    N = int(input("Number of email addresses : "))
    for i in range(N):
        email = input("Enter email {} : ".format(i + 1))
        if check(email):
            lex_lst.append(email)

    print("Outut: {}".format(sorted(lex_lst)))
