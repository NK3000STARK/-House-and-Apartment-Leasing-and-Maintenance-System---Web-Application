#!C:/Users/nandh/AppData/Local/Programs/Python/Python311/python.exe
import smtplib
from datetime import date
print("content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql
cgitb.enable()
con= pymysql.connect(host="localhost", user="root", password="", database="user_register")
cur = con.cursor()
form = cgi.FieldStorage()
userid = form.getvalue("id")

q = """select * from userregform  where id = '%s'""" % userid
cur.execute(q)
rec = cur.fetchall()

uemail = rec[0][4]
uname = rec[0][1]

q1 = """select * from purchased_property where user_email = '%s' and status = 'Approve' and vacate_date = 0 and vacate_status = ''""" % uemail
cur.execute(q1)
rec1 = cur.fetchall()


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
        
                <main class="content px-3 py-2" >
                    <div class="container-fluid" >
                        <div class="row justify-content-center">
                            <div class="col-sm-12 col-lg-12 col-md-10 " >

                                    
                                    <div class="card card-body mt-5" style="overflow:auto;text-wrap: nowrap;">
                                    <p> Current Properties </p>
                                       <table class="table table-bordered table-responsive">
                                         <tr class="bg-dark text-light">
                                            <th>ID</th>
                                           <th>Property Name</th>
                                           <th>Owner Name</th>
                                           <th>Mobile</th>
                                           <th style = "width:50px;text-wrap:wrap">Property Type</th>
                                           <th>Owner Email</th>
                                           <th style = "width:30px;text-wrap:wrap">Plot/Home Number</th>

                                          
                                           <th>Rent</th>
                                           <th>Deposit</th>
                                           <th>Acknowledgement</th>


                                         </tr>
"""%(userid,userid,userid,userid,userid,userid))

for i in rec1:
    fn1 = "dbdoc/" + i[19]

    print("""

                                        <tr>
                                         <form method="post" enctype="multipart/form-data">
                                          <td><input name ="fid" value= "%s" style = "border:none;background:transparent;width:12px"></td>
                                          <td><input name ="pname" value= "%s" style = "border:none;background:transparent;width:80px;text-wrap:wrap"></td>
                                          <td><input name ="owname" value= "%s" style = "border:none;background:transparent;width:80px;text-wrap:wrap"></td>
                                          <td>%s</td>
                                          <td>%s</td>
                                          <td><input name ="pemail" value= "%s" style = "border:none;background:transparent;width:80px;text-wrap:wrap" readonly></td>
                                          <td>%s</td>
                                          <td>%s</td>
                                          <td>%s</td>
                                          
                                          <td><input type = "submit" name = "leave" class = "btn btn-danger" value = "vacate"><input type = "button" name = "complaint" class = "btn btn-warning ml-1" data-toggle="modal" data-target="#Complaintmod%s" value = "Complaint"></td>
                                          <td><a data-toggle="modal" data-target="#readmore%s" href = "">Read More.. </a></td>
                                         </form>
                                        </tr>

                                     </div>
                                </div>
                            </div>  


                        </div>
                    </div>

                <div class="modal fade text-left" id="readmore%s" role="dialog">
                  <div class="modal-dialog">
                    <!-- Modal content-->
                    <div
                      class="modal-content"
                      style="
                        background-image: linear-gradient(
                          to bottom right,
                          #365486,
                          #7fc7d9
                        );
                        color: white;
                      "
                    >
                      <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">
                          View Details Here...
                        </h5>
                        <button
                          type="button"
                          class="close"
                          data-dismiss="modal"
                          aria-label="Close"
                        >
                          <span aria-hidden="true">&times;</span>
                        </button>
                      </div>
                      <div class="modal-body">
                          <div class="form-group input-group" >
                            <div class="input-group-prepend">
                              <span class="input-group-text" id="basic-addon1">Property Email</span>
                            </div>
                            <input type="text" class="form-control" value = "%s"readonly><br>
                          </div>
                          <div class="form-group input-group" >
                            <div class="input-group-prepend">
                              <span class="input-group-text" id="basic-addon1">Available BHK</span>
                            </div>
                            <input type="text" class="form-control" value = "%s"readonly><br>
                          </div>
                          <div class="form-group input-group" >
                            <div class="input-group-prepend">
                                <span class="input-group-text" id="basic-addon1">State</span>
                            </div>
                            <input type="text" class="form-control" value = "%s"readonly><br>
                          </div>
                          <div class="form-group input-group" >
                            <div class="input-group-prepend">
                              <span class="input-group-text" id="basic-addon1">City</span>
                            </div>
                            <input type="text" class="form-control" value = "%s"readonly><br>
                          </div>
                          <div class="form-group input-group" >
                            <div class="input-group-prepend">
                              <span class="input-group-text" id="basic-addon1">Pincode</span>
                            </div>
                            <input type="text" class="form-control" value = "%s"readonly><br>
                          </div>
                          <div class="form-group input-group" >
                            <div class="input-group-prepend">
                              <span class="input-group-text" id="basic-addon1">Facilities</span>
                            </div>
                            <input type="text" class="form-control" value = "%s"readonly><br>
                          </div>
                          <div class="form-group input-group" >
                            <div class="input-group-prepend">
                              <span class="input-group-text" id="basic-addon1">Description</span>
                            </div>
                            <input type="text" class="form-control" value = "%s"readonly><br>
                          </div>
                          <div class="form-group input-group" >
                            <div class="input-group-prepend">
                              <span class="input-group-text" id="basic-addon1">Landmark</span>
                            </div>
                            <input type="text" class="form-control" value = "%s"readonly><br>
                          </div>
                          <div class="form-group input-group" >
                            <div class="input-group-prepend">
                              <span class="input-group-text" id="basic-addon1">Address</span>
                            </div>
                            <input type="text" class="form-control" value = "%s"readonly><br>
                          </div>
                          <div class="form-group input-group" >
                            <div class="input-group-prepend">
                              <span class="input-group-text" id="basic-addon1">Property Image</span>
                            </div>
                            <img src = "%s" width= "100px">
                          </div>

                      </div>
                    </div>
                  </div>
                </div>  
                <div class="modal fade text-left" id="Complaintmod%s" role="dialog">
                    <div class="modal-dialog">
                    
                      <!-- Modal content-->
                      <div class="modal-content" style="background-image: linear-gradient(to bottom right,#365486,#7FC7D9);color: white;">
                        <div class="modal-header">
                          <h5 class="modal-title" id="exampleModalLabel">Enter Your Complaint here...</h5>
                          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                          </button>
                        </div>
                        <div class="modal-body">
                          <form method = "post" enctype="multipart/form-data" name="admin_login">
                            <div class="input-group mb-3">
                              <div class="input-group-prepend">
                                <span class="input-group-text" id="basic-addon1"><i class="fa fa-user-o" aria-hidden="true"></i></span>
                              </div>
                              <input type="text" name="ownerName" class="form-control" id="ownerName" aria-label="ownerName" value = "%s" readonly >
                            </div>
                            <div class="input-group mb-3">
                              <div class="input-group-prepend">
                                <span class="input-group-text" id="basic-addon1"><i class="fa fa-building" aria-hidden="true"></i></span>
                              </div>
                              <input type="text" name="propertyName" class="form-control" id="propertyName" aria-label="pname" value = "%s" readonly>
                            </div>
                            
                            <textarea name="query" cols="5" rows="8" class="form-control" placeholder="Enter Your Maintanance Request......"></textarea>

                            <input type="submit" class="btn btn-primary my-3" name="cmp_submit"  value="SUBMIT">
                            <button type="button" class="btn btn-outline-dark" data-dismiss="modal">CANCEL</button>
                          </form>
                        </div>
                      </div>
                      
                    </div>
                  </div>



    
    
    """ % (
        i[0], i[1], i[2], i[3], i[4],i[5],i[7],i[12],i[13],i[0],i[0],i[0],i[6],i[8],i[9],i[10],i[11],i[14],i[15],i[16],i[17],fn1,i[0],i[2],i[1]))

print("</table>")
print("""</div>
                                    
                                    <div class="card card-body mt-5" style="overflow:auto;text-wrap: nowrap;">
                                    <p> Vacate Request </p>
                                       <table class="table table-bordered table-responsive">
                                         <tr class="bg-dark text-light">
                                            <th>ID</th>
                                           <th>Property Name</th>
                                           <th>Owner Name</th>
                                           <th>Mobile</th>
                                           <th style = "width:50px;text-wrap:wrap">Property Type</th>
                                           <th>Owner Email</th>
                                           <th style = "width:30px;text-wrap:wrap">Plot/Home Number</th>

                                          
                                           <th>Rent</th>
                                           <th>Deposit</th>

                                         </tr>


""")

q1 = """select * from purchased_property where user_email = '%s' and status = 'Approve' and vacate_date = 0 and vacate_status = 'request'""" % uemail
cur.execute(q1)
rec1 = cur.fetchall()

for i in rec1:
        fn = "dbdoc/" + i[29]
        fn1 = "dbdoc/" + i[19]
        print("""

                                                <tr>
                                                 <form method="post" enctype="multipart/form-data">
                                                  <td><input name ="fid" value= "%s" style = "border:none;background:transparent;width:12px"></td>
                                                  <td><input name ="pname" value= "%s" style = "border:none;background:transparent;width:80px;text-wrap:wrap"></td>
                                                  <td>%s</td>
                                                  <td>%s</td>
                                                  <td>%s</td>
                                                  <td><input name ="pemail" value= "%s" style = "border:none;background:transparent;width:80px;text-wrap:wrap" readonly></td>
                                                  <td>%s</td>
                                                  <td>%s</td>
                                                  <td>%s</td>
                                                  <td><a data-toggle="modal" data-target="#readmore%s" href = "">Read More.. </a></td>
                                                 </form>
                                                </tr>

                                             </div>
                                        </div>
                                    </div>  
                                

                                </div>
                            </div>

                        <div class="modal fade text-left" id="readmore%s" role="dialog">
                          <div class="modal-dialog">
                            <!-- Modal content-->
                            <div
                              class="modal-content"
                              style="
                                background-image: linear-gradient(
                                  to bottom right,
                                  #365486,
                                  #7fc7d9
                                );
                                color: white;
                              "
                            >
                              <div class="modal-header">
                                <h5 class="modal-title" id="exampleModalLabel">
                                  View Details Here...
                                </h5>
                                <button
                                  type="button"
                                  class="close"
                                  data-dismiss="modal"
                                  aria-label="Close"
                                >
                                  <span aria-hidden="true">&times;</span>
                                </button>
                              </div>
                              <div class="modal-body">
                                  <div class="form-group input-group" >
                                    <div class="input-group-prepend">
                                      <span class="input-group-text" id="basic-addon1">Property Email</span>
                                    </div>
                                    <input type="text" class="form-control" value = "%s"readonly><br>
                                  </div>
                                  <div class="form-group input-group" >
                                    <div class="input-group-prepend">
                                      <span class="input-group-text" id="basic-addon1">Available BHK</span>
                                    </div>
                                    <input type="text" class="form-control" value = "%s"readonly><br>
                                  </div>
                                  <div class="form-group input-group" >
                                    <div class="input-group-prepend">
                                        <span class="input-group-text" id="basic-addon1">State</span>
                                    </div>
                                    <input type="text" class="form-control" value = "%s"readonly><br>
                                  </div>
                                  <div class="form-group input-group" >
                                    <div class="input-group-prepend">
                                      <span class="input-group-text" id="basic-addon1">City</span>
                                    </div>
                                    <input type="text" class="form-control" value = "%s"readonly><br>
                                  </div>
                                  <div class="form-group input-group" >
                                    <div class="input-group-prepend">
                                      <span class="input-group-text" id="basic-addon1">Pincode</span>
                                    </div>
                                    <input type="text" class="form-control" value = "%s"readonly><br>
                                  </div>
                                  <div class="form-group input-group" >
                                    <div class="input-group-prepend">
                                      <span class="input-group-text" id="basic-addon1">Facilities</span>
                                    </div>
                                    <input type="text" class="form-control" value = "%s"readonly><br>
                                  </div>
                                  <div class="form-group input-group" >
                                    <div class="input-group-prepend">
                                      <span class="input-group-text" id="basic-addon1">Description</span>
                                    </div>
                                    <input type="text" class="form-control" value = "%s"readonly><br>
                                  </div>
                                  <div class="form-group input-group" >
                                    <div class="input-group-prepend">
                                      <span class="input-group-text" id="basic-addon1">Landmark</span>
                                    </div>
                                    <input type="text" class="form-control" value = "%s"readonly><br>
                                  </div>
                                  <div class="form-group input-group" >
                                    <div class="input-group-prepend">
                                      <span class="input-group-text" id="basic-addon1">Address</span>
                                    </div>
                                    <input type="text" class="form-control" value = "%s"readonly><br>
                                  </div>
                                  <div class="form-group input-group" >
                                    <div class="input-group-prepend">
                                      <span class="input-group-text" id="basic-addon1">Property Image</span>
                                    </div>
                                    <img src = "%s" width= "100px">
                                  </div>
                            </div>
                              </div>
                            </div>
                          </div>
                        </div>
                        </main>

            </div>
        </div>
        

        <script >
            const sidebarToggle = document.querySelector("#sidebar-toggle");
            sidebarToggle.addEventListener("click",function(){
            document.querySelector("#sidebar").classList.toggle("collapsed");});
        </script>
    </body>

    </html>



            """ % (
            i[0], i[1], i[2], i[3], i[4], i[5], i[7], i[12], i[13], i[0], i[0], i[6], i[8], i[9], i[10], i[11], i[14],
            i[15], i[16], i[17], fn1))




Leave = form.getvalue("leave")


if Leave != None:
    today = date.today()
    fid = form.getvalue("fid")
    pname = form.getvalue("pname")
    pemail = form.getvalue("pemail")

    q1 = """update purchased_property set vacate_status = 'request' where id = '%s'"""%(fid)
    cur.execute(q1)
    con.commit()




complaint = form.getvalue("cmp_submit")


if complaint != None:
    owname = form.getvalue("ownerName")
    pname = form.getvalue("propertyName")
    complaint = form.getvalue("query")
    q = """select * from purchased_property where ownerName = '%s' and propertyName = '%s'""" % (owname,pname)
    cur.execute(q)
    emailrec = cur.fetchall()
    owemail = emailrec[0][5]
    today = date.today()
    q = """insert into complaints (userName,userEmail,ownerName,ownerEmail,propertyName,complaint,cdate) values ('%s','%s','%s','%s','%s','%s','%s')""" %(uname,uemail,owname,owemail,pname,complaint,today)
    cur.execute(q)
    con.commit()
    print("""<script>alert("your request is submited wait for reply")</script>""")