#!C:/Users/nandh/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql


cgitb.enable()
con= pymysql.connect(host="localhost", user="root", password="", database="user_register")
cur = con.cursor()
form = cgi.FieldStorage()
userid = form.getvalue("id")

import datetime
import calendar
from  datetime import datetime
from datetime import date,timedelta

date1 = datetime.now().day
c= datetime.now().month
month = calendar.month_name[c]



q = """select * from userregform  where id = '%s'""" % userid
cur.execute(q)
rec = cur.fetchall()
uemail = rec[0][4]
uname = rec[0][1]


print("""
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>User Dashboard</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha2/dist/css/bootstrap.min.css">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha2/dist/js/bootstrap.bundle.min.js"></script>

  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" />

  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css">
  <script src="https://cdn.jsdelivr.net/npm/jquery@3.7.1/dist/jquery.slim.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

  <style>
    /*@import url("https://fonts.googleapis.com/css2?family=Poppins&display=swap");*/

    *,
    ::after,
    ::before {
      box-sizing: border-box;
    }

    body {
      font-family: "Poppins", sans-serif;
      font-size: 0.875rem;
      opacity: 1;
      overflow-y: scroll;
      margin: 0;
    }

    a {
      cursor: pointer;
      text-decoration: none;
      font-family: "Poppins", sans-serif;
    }

    li {
      list-style: none;
    }



    /* Layout for admin dashboard skeleton */

    .wrapper {
      align-items: stretch;
      display: flex;
      width: 100%;
    }

    #sidebar {
      max-width: 264px;
      min-width: 264px;
      background-color: #deeaf5;

      transition: all 0.35s ease-in-out;
    }

    .main {
      display: flex;
      flex-direction: column;
      min-height: 100vh;
      min-width: 0;
      overflow: hidden;
      transition: all 0.35s ease-in-out;
      width: 100%;
      background-color: #ecf5fb;
    }

    /* Sidebar Elements Style */

    .sidebar-logo {
      padding: 1.15rem;
    }

    .sidebar-logo a {
      color: #17cef8;
      font-size: 1.15rem;
      font-weight: 600;
    }

    .sidebar-nav {
      flex-grow: 1;
      list-style: none;
      margin-bottom: 0;
      padding-left: 0;
      margin-left: 0;
    }

    .sidebar-header {
      color: black;
      font-size: 0.75rem;
      padding: 1.5rem 1.5rem 0.375rem;
    }

    .sidebar-dropdown .sidebar-item {
      background-color: rgb(92, 101, 109);
      transition: all 0.1s ease-out;
    }

    a.sidebar-link {
      padding: 0.625rem 1.625rem;

      color: rgb(255, 255, 255);
      position: relative;
      display: block;
      font-size: 0.875rem;
    }

    a.sidebar-link:hover {
      background-color: rgba(255, 255, 255, 0.447);
      transition: all 0.2s ease-out;
      color: rgb(0, 0, 0);
      text-decoration: none;
    }

    .sidebar-link[data-bs-toggle="collapse"]::after {
      border: solid;
      border-width: 0 0.075rem 0.075rem 0;
      content: "";
      display: inline-block;
      padding: 2px;
      position: absolute;
      right: 1.5rem;
      top: 1.4rem;
      transform: rotate(-135deg);
      transition: all 0.2s ease-out;
    }

    .sidebar-link[data-bs-toggle="collapse"].collapsed::after {
      transform: rotate(45deg);
      transition: all 0.2s ease-out;
    }



    .navbar-expand .navbar-nav {
      margin-left: auto;
    }

    .content {
      flex: 1;
      max-width: 100vw;
      width: 100vw;
    }


    .content {
      max-width: auto;
      width: auto;
    }


    /* Sidebar Toggle */

    #sidebar.collapsed {
      margin-left: -264px;
    }

    @media (max-width:767.98px) {
      .js-sidebar {
        margin-left: -264px;
      }

      #sidebar.collapsed {
        margin-left: 0;
      }
    }
  </style>
</head>
""")
print("""
<body>
  <div class="wrapper">
    <div id="sidebar" class="js-sidebar" style="background-color: #343a40;">
      <!-- Content For Sidebar -->
      <div class="h-100">
        <div class="sidebar-logo">
          <a href="#"><img src="./media/logo_dash dark.png" alt="" height="64px" style="border-radius: 10px;" /></a>
        </div>
        <ul class="sidebar-nav">
          <li>
            <div class="sidebar-header border-bottom bg-info text-light p-1 my-1"
              style="border-radius: 30px;margin-left: 6px;margin-right:10px ;">
              <p style="font-size: 15px; text-align: center" class="mt-3 ml-2">
                <i class="fa fa-tachometer" aria-hidden="true" style="justify-content: center"></i> Welcome ( User )
              </p>
            </div>
          </li>
          <li class="sidebar-item">
            <div class="text-info small fw-bold text-uppercase px-3 pt-4">
              PROFILE
            </div>
            <a href="user_profile.py?id=%s" class="sidebar-link ">
              <span class="me-2"><i class="fa fa-user" aria-hidden="true"></i></span>
              <span>PROFILE</span>
            </a>
          </li>
          <li class="my-4">
            <hr class="bg-light">
          </li>

          <li class="sidebar-item">
            <div class="text-info small fw-bold text-uppercase px-3 mb-3">
              PROPERTY DETAILS
            </div>

          <li class="sidebar-item">
            <a href="#" class="sidebar-link collapsed" data-bs-target="#property" data-bs-toggle="collapse"
              aria-expanded="false">
              <span class="me-2"><i class="fa fa-building" aria-hidden="true"></i></span>
              <span>PROPERTY</span>
            </a>
            <ul id="property" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#sidebar">
              <li class="sidebar-item">
                <a href="user_requested_property.py?id=%s" class="sidebar-link ">
                  <span class="me-2"><i class="fa fa-clock-o" aria-hidden="true"></i></span>
                  <span>Requested property</span>
                </a>
              </li>
              <li class="sidebar-item">
                <a href="user_accepted_property.py?id=%s" class="sidebar-link">
                  <span class="me-2"><i class="fa fa-check-circle" aria-hidden="true"></i></span>
                  <span>Accepted Property</span>
                </a>
              </li>
              <li class="sidebar-item">
                <a href="user_rent_more.py?id=%s" class="sidebar-link ">
                  <span class="me-2"><i class="fa fa-plus" aria-hidden="true"></i></span>
                  <span>Rent More</span>
                </a>
              </li>
            </ul>
          </li>


          </li>
          <li class="sidebar-item">
            <a href="user_payment.py?id=%s" class="sidebar-link">
              <span class="me-2"><i class="fa fa-money" aria-hidden="true"></i></span>
              <span>RENT PAYMENT</span>
            </a>
          </li>

          <li class="sidebar-item">
            <a href="user_PREVIOUS_complaints.py?id=%s" class="sidebar-link">
              <span class="me-2"><i class="fa fa-comments" aria-hidden="true"></i></span>
              <span>PREVIOUS COMPLAINTS</span>
            </a>
          </li>


        </ul>
      </div>
    </div>
    <div class="main">
      <nav class="navbar navbar-expand px-4 border-bottom bg-dark navbar-dark"
        style="overflow: hidden;text-wrap: nowrap;">
        <button class="btn btn-primary" id="sidebar-toggle" type="button">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="navbar-collapse navbar">

        </div>
        <a href="Home_page.py" class="btn btn-danger "><i class="fa fa-sign-out" aria-hidden="true"></i>
          Logout</a>
      </nav>

      <main class="content px-3 py-2">
        <div class="container-fluid">
            <div class="row justify-content-center">
                            <div class="col-lg-12">

                                <div id="acceptdiv" >
                                    <div class="card card-body mt-5" style="overflow:auto;text-wrap: nowrap;">
                                       <table class="table table-bordered table-responsive">
                                         <tr class="bg-dark text-light">
                                           <th>ID</th>
                                           <th>Property Name</th>
                                           <th>Property Type</th>
                                           <th>Owner Name</th>
                                           <th>Monthly Rent </th>
                                           <th>Payment </th>
                                           <th>Month</th>
                                           <th></th>
                                           
                                           
                                         </tr>

"""%(userid,userid,userid,userid,userid,userid))

q1 = "select * from payment where uemail = '%s' and status = 'unpaid' and payed = 0 and property_status = 'Approve' and vacate_status = 'occupied'"% uemail
cur.execute(q1)
precord = cur.fetchall()



for i in precord:
        payed = i[8]
        print("""

                                        <tr>
                                                <form method="post" enctype="multipart/form-data">
                                                  <td><input type = "number" value="%s" name = "pid" style = "border:none;width:50px"></td>
                                                  <td><input type = "text" value = "%s" name = "pname" style = "border:none;"></td>
                                                  <td><input type = "text" value = "%s" name = "ptype" style = "border:none;width:70px"></td>
                                                  <td><input type = "text" value = "%s" name = "owname" style = "border:none;width:70px"></td>
                                                  <td><input type = "number" value="%s" name = "rent" style = "border:none;width:120px"></td>

                                                  <td><input type = "number" name = "payed" value="%s" class ="form-control"style = "border:none;width:120px" readonly></td>
                                                  <td>%s, %s</td>
                                                  <td><input type = "button" data-toggle="modal" data-target="#rentpay%s" name= "pay" class = "btn btn-success" value = "Pay Rent"></td>
                                                
                                        </tr>

                                     </div>
                                </div>
                            </div>  


                        </div>
                </div>
                
                <div class="modal fade text-left" id="rentpay%s" role="dialog">
                    <div class="modal-dialog">
                        <!-- Modal content-->
                        <div class="modal-content" style="background-image: linear-gradient(to bottom right, #365486, #7FC7D9); color: white;">
                            <div class="modal-header">
                                <h5 class="modal-title" id="exampleModalLabel">Payment Form</h5>
                                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                    <span aria-hidden="true">&times;</span>
                                </button>
                            </div>
                            <div class="modal-body">
                                <div class="row">
                                    <!-- Card Payment -->
                                    <div class="col-md-12">
                                        <h5>Payment Details</h5>
                                        <div class="form-group">
                                            <label for="paymentMethod">Select Payment Method:</label>
                                            <select class="form-control" id="paymentMethod" name="paymentMethod" onchange="showPaymentFields()">
                                                <option value="card">Card</option>
                                                <option value="netbanking">Netbanking</option>
                                                <option value="gpay">GPay</option>
                                                <!-- Add other payment options as needed -->
                                            </select>
                                        </div>
                
                                        <!-- Card Details -->
                                        <div id="cardDetails" style="display:none;">
                                            <!-- Card Payment Fields -->
                                            <div class="input-group mb-3">
                                                <div class="input-group-prepend">
                                                    <span class="input-group-text" id="basic-addon1"><i class="fa fa-credit-card" aria-hidden="true"></i></span>
                                                </div>
                                                <input type="text" name="cardNumber" pattern="\d{16}" class="form-control" placeholder="Card Number">
                                            </div>
                                            <div class="input-group mb-3">
                                                <div class="input-group-prepend">
                                                    <span class="input-group-text" id="basic-addon1"><i class="fa fa-calendar" aria-hidden="true"></i></span>
                                                </div>
                                                <input type="text" name="expiryDate" pattern="(0[1-9]|1[0-2])\/[0-9]{2}" class="form-control" placeholder="Expiry Date (MM/YY)">
                                            </div>
                                            <div class="input-group mb-3">
                                                <div class="input-group-prepend">
                                                    <span class="input-group-text" id="basic-addon1"><i class="fa fa-lock" aria-hidden="true"></i></span>
                                                </div>
                                                <input type="text" name="cvv" pattern="\d{3}" class="form-control" placeholder="CVV">
                                            </div>
                                            <div class="input-group mb-3">
                                                <div class="input-group-prepend">
                                                    <span class="input-group-text" id="basic-addon1"><i class="fa fa-money" aria-hidden="true"></i></span>
                                                </div>
                                                <input type="number" readonly name="cardAmount" class="form-control" placeholder="Enter Payment amount" value="%s">
                                            </div>
                                        </div>
                
                                        <!-- Netbanking Details -->
                                        <div id="netbankingDetails" style="display:none;">
                                            <!-- Netbanking Payment Fields -->
                                            <div class="input-group mb-3">
                                                <div class="input-group-prepend">
                                                    <span class="input-group-text" id="basic-addon1">Account Number</span>
                                                </div>
                                                <input type="text" name="accountNumber" pattern="\d{10}" class="form-control" placeholder="Enter Account Number">
                                            </div>
                                            <div class="input-group mb-3">
                                                <div class="input-group-prepend">
                                                    <span class="input-group-text" id="basic-addon1">IFSC Code</span>
                                                </div>
                                                <input type="text" name="ifscCode" class="form-control" placeholder="Enter IFSC Code">
                                            </div>
                                            <div class="input-group mb-3">
                                                <div class="input-group-prepend">
                                                    <span class="input-group-text" id="basic-addon1"><i class="fa fa-money" aria-hidden="true"></i></span>
                                                </div>
                                                <input type="number" readonly name="netbamount" class="form-control" value= "%s">
                                            </div>
                                            <!-- Add more fields as needed for Netbanking -->
                                        </div>
                
                                        <!-- GPay Details -->
                                        <div id="gpayDetails" style="display:none;">
                                            <!-- GPay Payment Fields -->
                                            <div class="input-group mb-3">
                                                <div class="input-group-prepend">
                                                    <span class="input-group-text" id="basic-addon1"><i class="fa fa-mobile" aria-hidden="true"></i></span>
                                                </div>
                                                <input type="text" name="upi" class="form-control" placeholder="Enter UPI ID">
                                            </div>
                                            <div class="input-group mb-3">
                                                <div class="input-group-prepend">
                                                    <span class="input-group-text" id="basic-addon1"><i class="fa fa-money" aria-hidden="true"></i></span>
                                                </div>
                                                <input type="number" readonly name="gpayamount" class="form-control" value= "%s">
                                            </div>
                                            <!-- Add more fields as needed for GPay -->
                                        </div>
                                    </div>
                                </div>
                
                                <input type="submit" name="submitPayment" class="btn btn-primary my-3" value="PAY">
                                <button type="button" class="btn btn-outline-dark float-right" data-dismiss="modal">CANCEL</button>
                                </form>
                            </div>
                        </div>
                    </div>


<script>
    function showPaymentFields() {
        var paymentMethod = document.getElementById("paymentMethod").value;
        document.getElementById("cardDetails").style.display = (paymentMethod === "card") ? "block" : "none";
        document.getElementById("netbankingDetails").style.display = (paymentMethod === "netbanking") ? "block" : "none";
        document.getElementById("gpayDetails").style.display = (paymentMethod === "gpay") ? "block" : "none";
    }
</script>

            </main>

        </div>
    </div>

    <script >
        const sidebarToggle = document.querySelector("#sidebar-toggle");
        sidebarToggle.addEventListener("click",function(){
        document.querySelector("#sidebar").classList.toggle("collapsed");});
    </script>
</body>

</html>""" %(i[0],i[3],i[2],i[6],i[8],payed,i[10],i[11],i[0],i[0],payed,payed,payed))


from datetime import date

today = date.today()
pid = form.getvalue("pid")
ptype = form.getvalue("ptype")
pname = form.getvalue("pname")
owname = form.getvalue("owname")
rent = form.getvalue("rent")
payed = form.getvalue("payed")
cashAmount = form.getvalue("cashAmount")
cardNumber = form.getvalue("cardNumber")
expiryDate = form.getvalue("expiryDate")
cvv = form.getvalue("cvv")
cardAmount = form.getvalue("cardAmount")
payoption = form.getvalue("paymentMethod")
paybtn = form.getvalue("submitPayment")
gpayupi = form.getvalue("upi")
netAcc = form.getvalue("accountNumber")
netifsc = form.getvalue("ifscCode")
if paybtn != None:

        if payoption == "gpay":
                print(payed,payoption,pid)
                q6 = """update payment set upid = '%s', payed = '%s', status = 'paid', paymentMethod= '%s', payment_date = '%s', payment_status = 'request' where id = '%s' """%(gpayupi,payed,payoption,today,pid)
                cur.execute(q6)
                con.commit()
                print("""
                <script>
                alert("payment successful through Gpay ")
                location.href="user_payment.py?id=%s"
                </script>"""%(userid))


        if payoption == "card":
                q5 = """update payment set payed = '%s', status = 'paid', paymentMethod= '%s', cardno = '%s', expiryDate= '%s', cvv ='%s', cardAmount = '%s',payment_date = '%s',payment_status = 'request'  where id = '%s' """%(payed,payoption,cardNumber,expiryDate,cvv,cardAmount,today,pid)
                cur.execute(q5)
                con.commit()
                print("""
                <script>
                alert("payment successful from Your card")
                location.href="user_payment.py?id=%s"
                </script>"""%(userid))

        if payoption == "netbanking":
                q7 = """update payment set payed = '%s', status = 'paid', paymentMethod= '%s', net_accno = '%s' , net_ifsc = '%s',payment_date = '%s', payment_status = 'request' where id = '%s' """%(payed,payoption,netAcc,netifsc,today,pid)
                cur.execute(q7)
                con.commit()
                print("""
                <script>
                alert("payment successful through netbanking")
                location.href="user_payment.py?id=%s"
                </script>"""%(userid))

q1 = """select * from payment where uid = '%s'"""%(userid)
cur.execute(q1)
daterec = cur.fetchall()
now = datetime.now()
current_date = now.strftime("%d")
#nextdate = current_date + timedelta(days=1)
pdate = daterec[0][10]



if 26 == current_date   :

        q = """update payment set status = 'unpaid' , payed= 0 , paymentMethod= ' ',cardno = ' ',cvv = ' ',expiryDate = ' ',cardAmount =  ' ', upid = ' ', net_accno = ' ',net_ifsc = ' ',payment_status = ' ' where uid = '%s'"""% userid
        cur.execute(q)
        con.commit()

if paybtn != None:

        pid = form.getvalue("pid")
        ptype = form.getvalue("ptype")
        pname = form.getvalue("pname")
        owname = form.getvalue("owname")
        rent = form.getvalue("rent")
        payed = form.getvalue("payed")
        dateis = date.today()
        q = """ insert into payment_history (uid,uname,propertyName,propertyType,owname,payed,date,payment_method) values ('%s','%s','%s','%s','%s','%s','%s','%s')"""%(userid,uname,ptype,pname,owname,payed,dateis,payoption)
        cur.execute(q)
        con.commit()
        print("""
                    <script>
                    location.href="user_payment.py?id=%s"
                    </script>
                    """ % userid)


