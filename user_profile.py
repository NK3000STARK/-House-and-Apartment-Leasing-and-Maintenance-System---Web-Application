#!C:/Users/nandh/AppData/Local/Programs/Python/Python311/python.exe
import os

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


for i in rec:
    fn = "dbdoc/" +i[11]
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

          <main class="content px-3 py-2" >
                <div class="container-fluid" >
                    <div class="row justify-content-center">
                        <div class="col-sm-12 col-lg-8 col-md-10">

                            <div id="profile" >
                                <div class="card card-body mt-5" style="overflow:auto;text-wrap: nowrap;">
                                    

                                    <form method="post" enctype="multipart/form-data" id="reg_form">
                                        <div class="dropdown " >
                                           <a  class="btn btn-primary float-right text-light dropdown-toggle"  data-toggle="dropdown"> <i class="fa fa-pencil"></i> Edit</a>
                                            
                                            <ul class="dropdown-menu ">
                                                <li  class="dropdown-item" data-toggle="modal" data-target="#changepass">
                                                    Change password
                                                </li>
                                                <li class="dropdown-item" data-toggle="modal" data-target="#changeprofile">
                                                    Change Profile
                                                </li>
                                                <li class="dropdown-item" data-toggle="modal" data-target="#updatedetails">
                                                    Update Profile
                                                </li>
                                            </ul>
                                          </div>
                                        <div class="row my-3">
                                          <div class="col">
                                            <center>
                                              <img
                                                src="%s"
                                                height="200px" width="200px"
                                                alt="user Profile" style="border-radius:90px;border:5px solid"
                                              />
                                            </center>
                                          </div>
                                        </div>
                                        <label class="form-control" style="text-transform: uppercase;">%s ( USER )</label>
                                        <label class="form-control">EMAIL : %s</label>
                                        <label class="form-control">PHONE : %s</label>
                        

                                        <div class="modal fade text-left" id="changepass" role="dialog">
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
                                                  Change Password Here...
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
                                                <form enctype="multipart/form-data" name="change_pass">
                                                  <input
                                                    type="text"
                                                    name="ch_pass"
                                                    class="form-control"
                                                    id="N_pass"
                                                    placeholder="Enter New Password...."
                                                    autofocus
                                                  /><br />
                                                  <input
                                                    type="text"
                                                    name="ch_pass2"
                                                    class="form-control"

                                                    placeholder="Retype Password...."
                                                  /><br />
                                                  <input
                                                    type="submit"
                                                    class="btn btn-primary my-3"
                                                    name="ch_pass_submit"
                                                    value="SUBMIT"
                                                  />
                                                  <button
                                                    type="button"
                                                    class="btn btn-outline-dark"
                                                    data-dismiss="modal"
                                                  >
                                                    CANCEL
                                                  </button>
                                                </form>
                                              </div>
                                            </div>
                                          </div>
                                        </div>
                                        <div class="modal fade text-left" id="changeprofile" role="dialog">
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
                                                  Change Profile Here...
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
                                                <form enctype="multipart/form-data" method="post" name="change_profile">
                                                  <input
                                                    type="file"
                                                    name="ch_profile"
                                                    class="form-control"
                                                  /><br />
                                                  <input
                                                    type="submit"
                                                    class="btn btn-primary my-3"
                                                    name="cp_submit"
                                                    value="SUBMIT"
                                                  />
                                                  <button
                                                    type="button"
                                                    class="btn btn-outline-dark"
                                                    data-dismiss="modal"
                                                  >
                                                    CANCEL
                                                  </button>
                                                </form>
                                              </div>
                                            </div>
                                          </div>
                                        </div>
                                        <div class="modal fade text-left" id="updatedetails" role="dialog">
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
                                                  Update Profile Here...
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
                                                <form method="post" enctype="multipart/form-data" name="o_reg_form">
                                                  <div class="form-group input-group">
                                                    <div class="input-group-prepend">
                                                      <span class="input-group-text" id="basic-addon1"><i class="fa fa-user-o" aria-hidden="true"></i></span>
                                                    </div>
                                                    <input
                                                      type="text"
                                                      name="uname"
                                                      class="form-control"
                                                      value = "%s"
                                                    /><br />
                                                  </div>
                       
                                      
                                                  <div class="form-group input-group">
                                                    <div class="input-group-prepend">
                                                      <span class="input-group-text" id="basic-addon1"><i class="fa fa-phone-square" aria-hidden="true"></i></span>
                                                    </div>
                                                    <input
                                                      type="text"
                                                      name="ugender"
                                                      class="form-control"
                                                      value= "%s"
                                                    /><br />
                                                  </div>
                                                  <div class="form-group input-group">
                                                    <div class="input-group-prepend">
                                                      <span class="input-group-text" id="basic-addon1"><i class="fa fa-envelope" aria-hidden="true"></i></span>
                                                    </div>
                                                    <input
                                                      type="number"
                                                      name="uphone"
                                                      class="form-control"
                                                      value= "%s"
                                                    /><br />
                                                  </div>
                                      
                                                  <div class="form-group input-group">
                                                    <div class="input-group-prepend">
                                                      <span class="input-group-text" id="basic-addon1"><i class="fa fa-envelope" aria-hidden="true"></i></span>
                                                    </div>
                                                    <input
                                                      type="email"
                                                      name="uemail"
                                                      class="form-control"
                                                      value= "%s"
                                                    /><br />
                                                  </div>
                                                  <div class="form-group input-group">
                                                    <div class="input-group-prepend">
                                                      <span class="input-group-text" id="basic-addon1"><i class="fa fa-calendar" aria-hidden="true"></i></span>
                                                    </div>
                                                    <input
                                                      type="date"
                                                      name="odob"
                                                      class="form-control"
                                                      value = "%s"
                                                    /><br />
                                                  </div>
                                                  <div class="form-group input-group">
                                                    <div class="input-group-prepend">
                                                      <span class="input-group-text" id="basic-addon1"><i class="fa fa-address-card-o" aria-hidden="true"></i></span>
                                                    </div>
                                                    <textarea
                                                      rows="1"
                                                      cols="15"
                                                      class="form-control"
                                                      name="uaddress"
                                                    >%s</textarea
                                                    ><br />
                                                  </div>


                                                  <div class="form-group input-group">
                                                    <div class="input-group-prepend">
                                                      <span class="input-group-text" id="basic-addon1"><i class="fa fa-location-arrow" aria-hidden="true"></i></span>
                                                    </div>
                                                    <input
                                                      type="number"
                                                      id="upincode"
                                                      class="form-control"
                                                      name="upincode"
                                                      value = "%s"
                                                    /><br />
                                                  </div>
                                                  <div class="form-group input-group">
                                                    <div class="input-group-prepend">
                                                      <span class="input-group-text" id="basic-addon1"><i class="fa fa-address-card-o" aria-hidden="true"></i></span>
                                                    </div>
                                                    <input
                                                      class="form-control"
                                                      type="text"
                                                      name="ustate"
                                                      value = "%s"
                                                    /><br />
                                                  </div>
                                                  <div class="form-group input-group">
                                                    <div class="input-group-prepend">
                                                      <span class="input-group-text" id="basic-addon1"><i class="fa fa-address-card-o" aria-hidden="true"></i></span>
                                                    </div>
                                                    <input
                                                      class="form-control"
                                                      type="text"
                                                      name="udistrict"
                                                      value = "%s"
                                                    /><br />
                                                  </div>
                                                  <div class="form-group input-group">
                                                    <div class="input-group-prepend">
                                                      <span class="input-group-text" id="basic-addon1"><i class="fa fa-address-card-o" aria-hidden="true"></i></span>
                                                    </div>
                                                    <input
                                                      class="form-control"
                                                      type="text"
                                                      name="uprofession"
                                                      value = "%s"
                                                    /><br />
                                                  </div>
                                                  <div class="form-group input-group">
                                                    <div class="input-group-prepend">
                                                      <span class="input-group-text" id="basic-addon1"><i class="fa fa-address-card-o" aria-hidden="true"></i></span>
                                                    </div>
                                                    <input
                                                      class="form-control"
                                                      type="text"
                                                      name="marrid_status"
                                                      value = "%s"
                                                    /><br />
                                                  </div>
                                                  
                                                  <div class="form-group input-group">
                                                    <div class="input-group-prepend">
                                                      <span class="input-group-text" id="basic-addon1"><i class="fa fa-unlock-alt" aria-hidden="true"></i></span>
                                                    </div>
                                                    <input
                                                      class="form-control"
                                                      type="text"
                                                      id="upass"
                                                      name="upass"
                                                      value = "%s"
                                                    /><br />
                                                  </div>
                                                  <div class="modal-footer">
                                                    <button type="submit"class="btn btn-primary" name="up_profile_submit">UPDATE</button>
                                                    <button type="button" class="btn btn-secondary" data-dismiss="modal">CANCEL</button>
                                                  </div>
                      
                                                </form>
                                              </div>
                                            </div>
                                          </div>
                                        </div>
                                    </form>
                                </div>

                            </div>
                        </div>  

                      
                    </div>
                </div>
            </main>

    </div>
  </div>

  <script>
    const sidebarToggle = document.querySelector("#sidebar-toggle");
    sidebarToggle.addEventListener("click", function () {
      document.querySelector("#sidebar").classList.toggle("collapsed");
    });


  </script>
</body>

</html>"""%(userid,userid,userid,userid,userid,userid,fn,i[1],i[4],i[3],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[12],i[14]))

chSubmit = form.getvalue("cp_submit")
if chSubmit != None:
    if len(form) != 0:
        chprofile = form['ch_profile']
        if chprofile.filename:
            fn1 = os.path.basename(chprofile.filename)
            open("dbdoc/" + fn1, "wb").write(chprofile.file.read())
            q = "update userregform set photo  = '%s' where id = '%s' " % (fn1, userid)
            cur.execute(q)
            con.commit()
            print("""
            <script>
                lert("Updated successfully")
            </script>""")

ch_pass_submit = form.getvalue("ch_pass_submit")
if ch_pass_submit != None:
    if len(form) != 0:
        change_pass = form.getvalue("ch_pass")
        retype_pass = form.getvalue("ch_pass2")
        if change_pass == retype_pass:
            q = "update userregform set Password = '%s' where id = '%s' " % (retype_pass, userid)
            cur.execute(q)
            con.commit()
            print("""
            <script>alert("Password updated")</script>""")

up_profile_Submit = form.getvalue("up_profile_submit")
if up_profile_Submit != None:
        upname = form.getvalue("uname")
        upgender = form.getvalue("ugender")
        upphone = form.getvalue("uphone")
        upemail = form.getvalue("uemail")
        updob = form.getvalue("udob")

        upaddress = form.getvalue("uaddress")
        uppincode = form.getvalue("upincode")
        upstate = form.getvalue("ustate")
        updistrict = form.getvalue("udistrict")
        upprofession = form.getvalue("uprofession")
        upmarriedstatus = form.getvalue("marrid_status")
        up_identity = form['uidentity']
        uppass = form.getvalue("upass")

        q = "update userregform set Name = '%s', Gender = '%s', Phone = '%s' ,Email = '%s' ,Dob = '%s',Address= '%s',Pincode = '%s',State = '%s',City = '%s', Profession = '%s', MarriedState = '%s',Password = '%s' where id = '%s' "\
            %(upname,upgender,upphone,upemail,updob,upaddress,uppincode,upstate,updistrict,upprofession,upmarriedstatus,uppass,userid)
        cur.execute(q)
        con.commit()
        print("""
        <script>
          alert("Details Updated successfully")
         </script>""")

