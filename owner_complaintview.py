#!C:/Users/nandh/AppData/Local/Programs/Python/Python311/python.exe


print("content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql
import smtplib
from datetime import date
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="user_register")
cur = con.cursor()
form = cgi.FieldStorage()
userid = form.getvalue("id")

q2 = """select * from ownerregform  where id = '%s' """ % (userid)
cur.execute(q2)
rec = cur.fetchall()

owemail = rec[0][3]

print("""<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Owner Dashboard</title>
     <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha2/dist/css/bootstrap.min.css">
     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha2/dist/js/bootstrap.bundle.min.js"></script>

     <link
     rel="stylesheet"
     href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" />

     <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css">
     <script src="https://cdn.jsdelivr.net/npm/jquery@3.7.1/dist/jquery.slim.min.js"></script>
     <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
     <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js"></script>
     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

<style>


/*@import url("https://fonts.googleapis.com/css2?family=Poppins&display=swap");*/

*,::after,::before {
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
.sidebar-dropdown .sidebar-item{
  background-color: rgb(92, 101, 109);
  transition: all 0.1s ease-out;
}

a.sidebar-link {
  padding: 0.625rem 1.625rem;

  color:rgb(255, 255, 255);
  position: relative;
  display: block;
  font-size: 0.875rem;
}
a.sidebar-link:hover{
  background-color:rgba(255, 255, 255, 0.447);
  transition: all 0.2s ease-out;
  color: rgb(0, 0, 0);
  text-decoration: none ;
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

@media (max-width:767.98px){
    .js-sidebar{
        margin-left: -264px;
    }
    #sidebar.collapsed{
        margin-left: 0;
    }
}

     </style>
</head>
""")
print("""
<!DOCTYPE html>
<html lang="en" >


<body>
    <div class="wrapper">
         <div id="sidebar" class="js-sidebar " style="background-color: #343a40;">
            <!-- Content For Sidebar -->
            <div class="h-100">
                <div class="sidebar-logo">
                    <a href="#"><img src="./media/logo_dash dark.png" alt="" height="64px" style="border-radius: 10px;"
                        /></a>
                </div>
                <ul class="sidebar-nav" >
                    <li >
                        <div
                        class="sidebar-header border-bottom bg-info text-light p-1 my-1"
                        style="border-radius: 30px;margin-left: 6px;margin-right:10px ;"
                      >
                        <p style="font-size: 15px; text-align: center" class="mt-3 ml-2">
                          <i
                            class="fa fa-tachometer"
                            aria-hidden="true"
                            style="justify-content: center"
                          ></i
                          > Welcome ( House Owner )
                        </p>
                      </div>
                    </li>
                    <li class="sidebar-item">
                        <div class="text-info small fw-bold text-uppercase px-3 pt-4">
                            PROFILE
                          </div>
                        <a href="owner_dashboard_profile.py?id=%s" class="sidebar-link " >
                            <span class="me-2"><i class="fa fa-user" aria-hidden="true"></i></span>
                            <span>PROFILE</span>
                        </a>
                    </li>
                    <li class="my-4"><hr class="bg-light"></li>

                    <li class="sidebar-item">
                        <div class="text-info small fw-bold text-uppercase px-3 mb-3">
                          PROPERTY DETAILS
                        </div>

                        <li class="sidebar-item">
                            <a href="#" class="sidebar-link collapsed" data-bs-target="#property" data-bs-toggle="collapse"
                                aria-expanded="false">
                                <span class="me-2"><i class="fa fa-building" aria-hidden="true"></i></span>
                                <span>PROPERTYS</span>
                            </a>
                            <ul id="property" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#sidebar">
                                <li class="sidebar-item">
                                    <a href="owner_dashboard_addprop.py?id=%s" class="sidebar-link " >
                                        <span class="me-2"
                                          ><i class="fa fa-clock-o" aria-hidden="true"></i></span>
                                        <span>Add Property</span>
                                    </a>
                                </li>
                                <li class="sidebar-item">
                                    <a href="owner_dashboard_existing.py?id=%s" class="sidebar-link ">
                                        <span class="me-2"
                                          ><i class="fa fa-check-circle" aria-hidden="true"></i></span>
                                        <span>Existing Property</span>
                                    </a>
                                </li>
                                <li class="sidebar-item">
                                    <a href="owner_dashboard_rentreq.py?id=%s" class="sidebar-link ">
                                        <span class="me-2"
                                          ><i class="fa fa-check-circle" aria-hidden="true"></i></span>
                                        <span>Rent Request</span>
                                    </a>
                                </li>
                                <li class="sidebar-item">
                                    <a href="owner_vacate_req.py?id=%s" class="sidebar-link ">
                                        <span class="me-2"
                                          ><i class="fa fa-check-circle" aria-hidden="true"></i></span>
                                        <span>Vacate Request</span>
                                    </a>
                                </li>
                            </ul>
                        </li>


                    </li>
                    <li class="sidebar-item">
                        <a href="owner_dashboard_tenantsdet.py?id=%s" class="sidebar-link ">
                            <span class="me-2"><i class="fa fa-users" aria-hidden="true"></i></span>
                            <span>TENANTS DETAILS</span>
                        </a>
                    </li>
                    <li class="sidebar-item">
                      <a href="owner_rentdet.py?id=%s" class="sidebar-link">
                      <span class="me-2"><i class="fa fa-list" aria-hidden="true"></i></span>
                      <span>RENT DETAILS</span>
                      </a>
                    </li>
                    <li class="sidebar-item">
                      <a href="owner_complaintview.py?id=%s" class="sidebar-link">
                      <span class="me-2"><i class="fa fa-comments" aria-hidden="true"></i></span>
                      <span>COMPLAINT SECTION</span>
                      </a>
                    </li>
                    <li class="sidebar-item">
                      <a href="owner_complaint_history.py?id=%s" class="sidebar-link">
                      <span class="me-2"><i class="fa fa-comments" aria-hidden="true"></i></span>
                      <span>COMPLAINT HISTORY</span>
                      </a>
                    </li>



                </ul>
            </div>
        </div>
        <div class="main"style="overflow:auto;height: 500px;" >
            <nav class="navbar navbar-expand px-4 border-bottom bg-dark navbar-dark" style="overflow: hidden;
                    text-wrap: nowrap;">
                <button class="btn btn-primary" id="sidebar-toggle" type="button">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="navbar-collapse navbar">

                </div>
                <a href="Home_page.py" class="btn btn-danger "
              ><i class="fa fa-sign-out" aria-hidden="true"></i> Logout</a
            >
            </nav>
            <main class="content px-3 py-2" >
                <div class="container-fluid" >
                    <div class="row justify-content-around">

"""% (userid,userid,userid,userid,userid,userid,userid,userid,userid))

q1 = """select * from complaints where ownerEmail = '%s' and status = 'new'""" % owemail
cur.execute(q1)
complaintrec = cur.fetchall()



for i in complaintrec:

    print("""
    
                       <div class="card " style="width: 23rem;margin-top:20px">
                          <form method = "post" enctype="multipart/form-data">
                            <div class="card-body">
                              <p style = "display:none">ID :<input type="text" value = "%s" name = "cid" style = "border:none;background:transparent;width:12px;" readonly></p>
                              <p>Tenant Name :<input type="text" value = "%s" name = "uname" style = "border:none;background:transparent;" readonly></p>
                              <p>Tenant Email :<input type="text" value = "%s" name = "uemail" style = "border:none;background:transparent" readonly></p>
                              <p>Property Name: <input type="text" value = "%s" name = "pname" style = "border:none;background:transparent" readonly></p>
                              <p>Complaint :<input type="text" value = "%s" name = "complaint" style = "border:none;background:transparent" readonly></p>
                              <p>Complaint Received Date :<input type="date" value = "%s" name = "cdate" style = "border:none;background:transparent" readonly></p>
                            
                            </div>
                            <div class="card-footer">
                              <textarea
                                    name="reply"        
                                          cols="5"
                                          rows="8"
                                          class="form-control"
                                          placeholder="Enter Your Reply......"
                                        ></textarea>
                              <button type="submit" name= "submit" value="solved" class="btn btn-primary">Reply</button>
                            </div>
                          </form>
                       </div>
                          

    """%(i[0],i[1],i[2],i[5],i[6],i[8]))

reply = form.getvalue("reply")
cid = form.getvalue("cid")
cuname = form.getvalue("uname")
complaint = form.getvalue("complaint")
cuemail = form.getvalue("uemail")
cpname = form.getvalue("pname")
submit = form.getvalue("submit")

if submit != None:
    today = date.today()
    q = """update complaints set status = '%s',solution = '%s',rdate= '%s' where id = '%s' """%(submit,reply,today,cid)
    cur.execute(q)
    con.commit()
    fromadd = "snandhu712@gmail.com"
    password = "rpqdkhnufllixgtq"
    toadd = cuemail
    subject = "Your Complaint regarding"
    body = "Your complaint ({}) and property name ({})  owner reply : {}".format(complaint, cpname,reply)
    msg = "Subject : {} \n\n {} ".format(subject, body)
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login(fromadd, password)
    server.sendmail(fromadd, toadd, msg)
    server.quit()
    print("""
                <script>
                alert("Reply submited to user regarding complaint")
                </script>
                """)

print("""            
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
    
    </html>""")
