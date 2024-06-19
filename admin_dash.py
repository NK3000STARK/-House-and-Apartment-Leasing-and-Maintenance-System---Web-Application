#!C:/Users/nandh/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql,os,smtplib
cgitb.enable()
con= pymysql.connect(host="localhost", user="root", password="", database="user_register")
cur = con.cursor()
form = cgi.FieldStorage()

q = """select * from forgot_pass where status = 'new' """
cur.execute(q)
rec = cur.fetchall()
print("""
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css">
      <script src="https://cdn.jsdelivr.net/npm/jquery@3.7.1/dist/jquery.slim.min.js"></script>
      <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js"></script>
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <table border="2px">
    <tr>
    <th>ID </th>
    <th>NAME </th>
    <th>EMAIL </th>
    <th>PASSWORD </th>
    </tr>
""")
for i in rec:

    print("""
      
    <tr>
    <form method = "post" enctype="multipart/form-data">
    <td><input type="text" name ="fid" value= "%s"></td>
    <td><input type="text" name ="fname" value= "%s"></td>
    <td><input type="text" name ="femail" value= "%s"></td>
    <td><input type="text" name ="fpass" value= "%s"></td>
    <td>
    <input type = "submit" name = "approve" class = "btn btn-success" value = "Approve">
    <input type = "submit" name = "reject" class = "btn btn-danger" value="Reject">
    </td>
    </form>
    </tr>
    </table>
    """%(i[0],i[1],i[2],i[3]))


Approve = form.getvalue("approve")
Reject = form.getvalue("reject")
fid = form.getvalue("fid")
fname = form.getvalue("fname")
femail = form.getvalue("femail")
fpass = form.getvalue("fpass")


if Approve != None:
    q = """update forgot_pass set status = '%s' where id = '%s' """%(Approve,fid)
    cur.execute(q)
    con.commit()
    fromadd = "snandhu712@gmail.com"
    password = "rpqdkhnufllixgtq"
    toadd = femail
    subject = "User Name and Password regarding"
    body = "Your User Name password and  ---> {}, {}".format(femail,fpass)
    msg = "Subject : {} \n\n {} ".format(subject, body)
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login(fromadd, password)
    server.sendmail(fromadd, toadd, msg)
    server.quit()
    print("""
                <script>
                alert("UserName and Password sended successfully")
                </script>
                """)