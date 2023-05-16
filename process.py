# from databaselink import append_to_excel
def sno():
    with open('lastcode', 'r') as lt:
        no = int(lt.readline())
        no += 1
        with open('lastcode', 'w') as ltw:
            ltw.write(str(no))
        with open('firstcode', 'r') as ft:
            code = str(ft.readline())
            sno = str(code) + str(no)
    return sno


def save_file(name, email, phoneno, dob, message, ID,file_url):
#     append_to_excel(id=ID, name=name, email=email, phno=phoneno, dob=dob, message=message, file_url=file_url)
      pass
