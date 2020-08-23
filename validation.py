import re
class Validation:

    def valid_contact_no(self,no):
        if re.match(r'^[0-9]{10}$',no) is not None:
            return True
        else:
            print("Re-enter contact no")
            return False
    def valid_email_id(self,id):
        if re.match(r'[A-za-z0-9]+\@[a-z]+\.([a-z]+\.)?(com|net|in|edu)',id) is not None:
            return True
        else:
            print("Re-enter email id")
            return False

    #all1 = patten.findall(no)
    # all1 = re.match(patten,no)
    # for i in all1:
    #     print(i)
    #multiple string patten 
    # if re.search("\d{10}",no):
    #     print("true")
    # else:
    #     print("no")
    #only one string match patten
    # if re.match('\d{10}',no) is not None:
    #    print("true")
