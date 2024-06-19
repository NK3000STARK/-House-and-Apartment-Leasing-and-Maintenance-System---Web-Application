#!C:/Users/nandh/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql
cgitb.enable()
con= pymysql.connect(host="localhost", user="root", password="", database="user_register")
cur = con.cursor()
form = cgi.FieldStorage()

print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: 'Arial', sans-serif;
            overflow: hidden;
            background-color: #f8f9fa;
            /* Fallback color in case the background image is not loaded */
        }

        .background {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: url('./media/fbg.jpg') center/cover no-repeat;
            filter: blur(5px);
        }

        .form-container {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            text-align: center;
            z-index: 1;
        }

        .form-inline {
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 20px;
            background-color: rgba(255, 255, 255, 0.9);
            /* Semi-transparent white background */
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            /* Subtle box shadow */
        }

        .form-control {
            margin-bottom: 15px;
            padding: 10px;
            width: 300px;
            box-sizing: border-box;
            border: 1px solid #ccc;
            border-radius: 5px;
            font-size: 16px;
        }

        .btn {
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
        }

        .btn-primary {
            background-color: #007bff;
            color: #fff;
            border: none;
            border-radius: 5px;
        }

        .message {
            color: #333;
            font-size: 24px;
            margin-bottom: 20px;
            font-weight: bold;
            animation: fadeIn 1s ease-in-out;
            /* Add animation to the message */
        }

        /* Add animation to the form */
        .form-container {
            animation: fadeIn 1s ease-in-out;
        }

        @keyframes fadeIn {
            0% {
                opacity: 0;
            }

            100% {
                opacity: 1;
            }
        }
    </style>
    <title>User Forgot password</title>
</head>

<body>

    <div class="background"></div>

    <div class="form-container">
        <div class="message">Forgot Password? Don't worry, we are here to help. Enter your email:</div>
        <form method="post" enctype="multipart/form-data" class="form-inline">
            <input type="email" name="forgot_email" placeholder="Enter Your Email...." class="form-control p-2">
            <input type="submit" class="btn btn-primary" name="forgot_submit" id="forgot_submit">
        </form>
    </div>

</body>

</html>""")


ForgotEmail = form.getvalue("forgot_email")
ForgotSubmit = form.getvalue("forgot_submit")
if ForgotSubmit != None:
    q = """select  * from userregform where Email = '%s'""" %(ForgotEmail)
    cur.execute(q)
    rec = cur.fetchall()
    for i in rec:
        fname = i[1]
        fpass = i[14]
        femail = i[4]
        q = """insert into forgot_pass (Name,password,Email,status) values ('%s','%s','%s','new')"""%(fname,fpass,femail)
        cur.execute(q)
        con.commit()
        print("""<script>alert("Inserted into table")</script>""")