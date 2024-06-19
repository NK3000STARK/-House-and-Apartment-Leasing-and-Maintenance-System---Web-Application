#!C:/Users/nandh/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="user_register")
cur = con.cursor()
form = cgi.FieldStorage()
userid = form.getvalue("id")
w="""select * from ownerregform where id='%s'"""%(userid)
cur.execute(w)
hodet=cur.fetchall()

homail=hodet[0][3]
q = """select * from property where email = '%s' and status= 'Approve'"""%(homail)
cur.execute(q)
rec = cur.fetchall()

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
                        <div class="row justify-content-center">
                            <div class="col-sm-12 col-lg-11 col-md-10">

                                <div id="acceptdiv" >
                                    <div class="card card-body mt-5" style="overflow:auto;text-wrap: nowrap;">
                                       <table class="table table-bordered table-responsive">
                                         <tr class="bg-dark text-light">
                                           <th>ID</th>
                                           <th>Property Name</th>
                                           <th>Owner Name</th>
                                           <th>Property Type</th>
                                           <th>Plot/Home Number</th>
                                           <th>Rent</th>
                                           <th>Deposit</th>
                                           <th>Address</th>
                                           <th>Vacant/Occupied </th>
                                           <th>Acknowledgement</th>
                                         </tr>










    """ % (userid,userid,userid,userid,userid,userid,userid,userid,userid,userid))


for i in rec:

        print("""

                                        <tr>
                                          <td>%s</td>
                                          <td>%s</td>
                                          <td>%s</td>
                                          <td>%s</td>
                                          <td>%s</td>
                                          <td>%s</td>
                                          <td>%s</td>
                                          <td>%s</td>
                                          <td>%s</td>

                                          
                                         
                                          
                                          <td><input data-toggle="modal" data-target="#updatedetails%s" type = "submit" value = "Update" name = "pupdate" class = "btn btn-warning"></td>
                                          
                                         </tr>

                                     </div>
                                </div>
                            </div>  


                        </div>
                    </div>
                <div class="modal fade text-left" id="updatedetails%s" role="dialog">
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
                          Update Property Details Here...
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
                        <form method="post" enctype="multipart/form-data" >
                          <div class="form-group input-group" style = "display:none">
                            <div class="input-group-prepend">
                              <span class="input-group-text" id="basic-addon1"><i class="fa fa-user-o" aria-hidden="true"></i></span>
                            </div>
                            <input
                              type="text"
                              name="upid"
                              class="form-control"
                              value = "%s"
                              readonly
                            /><br />
                          </div>
                          <div class="form-group input-group">
                            <div class="input-group-prepend">
                              <span class="input-group-text" id="basic-addon1"><i class="fa fa-user-o" aria-hidden="true"></i></span>
                            </div>
                            <input
                              type="text"
                              name="upname"
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
                              name="upowname"
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
                              type="text"
                              name="uptype"
                              class="form-control"
                              value= "%s"
                            /><br />
                          </div>
                          <div class="form-group input-group">
                            <div class="input-group-prepend">
                              <span class="input-group-text" id="basic-addon1"><i class="fa fa-calendar" aria-hidden="true"></i></span>
                            </div>
                            <input
                              type="email"
                              name="upemail"
                              class="form-control"
                              value = "%s"
                            /><br />
                          </div>
                          <div class="form-group input-group">
                            <div class="input-group-prepend">
                              <span class="input-group-text" id="basic-addon1"><i class="fa fa-location-arrow" aria-hidden="true"></i></span>
                            </div>
                            <input
                              type="text"
                              id="upplotno"
                              class="form-control"
                              name="upplotno"
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
                              name="upabhk"
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
                              name="upstate"
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
                              name="upcity"
                              value = "%s"
                            /><br />
                          </div>
                          <div class="form-group input-group">
                            <div class="input-group-prepend">
                              <span class="input-group-text" id="basic-addon1"><i class="fa fa-address-card-o" aria-hidden="true"></i></span>
                            </div>
                            <input
                              class="form-control"
                              type="number"
                              name="uppincode"
                              value = "%s"
                            /><br />
                          </div>
                          
                          <div class="form-group input-group">
                            <div class="input-group-prepend">
                              <span class="input-group-text" id="basic-addon1"><i class="fa fa-unlock-alt" aria-hidden="true"></i></span>
                            </div>
                            <input
                              class="form-control"
                              type="number"
                              name="uprent"
                              value = "%s"
                            /><br />
                          </div>
                          <div class="form-group input-group">
                            <div class="input-group-prepend">
                              <span class="input-group-text" id="basic-addon1"><i class="fa fa-address-card-o" aria-hidden="true"></i></span>
                            </div>
                            <input
                              class="form-control"
                              type="number"
                              name="updeposit"
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
                              name="upfacilities"
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
                              name="updescription"
                            >%s</textarea
                            ><br />
                          </div>
                          <div class="form-group input-group">
                            <div class="input-group-prepend">
                              <span class="input-group-text" id="basic-addon1"><i class="fa fa-address-card-o" aria-hidden="true"></i></span>
                            </div>
                            <input
                              class="form-control"
                              type="text"
                              name="uplandmark"
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
                              name="upaddress"
                            >%s</textarea
                            ><br />
                          </div>
                          <div class="form-group input-group">
                            <div class="input-group-prepend">
                              <span class="input-group-text" id="basic-addon1"><i class="fa fa-address-card-o" aria-hidden="true"></i></span>
                            </div>
                            <input
                              class="form-control"
                              type="text"
                              name="upvacancies"
                              value = "%s"
                            /><br />
                          </div>
                          
                          
                          
                          <div class="modal-footer">
                            <button type="submit"class="btn btn-primary" name="up_property_submit">UPDATE</button>
                            <button type="button" class="btn btn-secondary" data-dismiss="modal">CANCEL</button>
                          </div>

                        </form>
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

    </html>""" % (
        i[0], i[1], i[2],i[4],i[6],i[11],i[12],i[16],i[17],i[0],i[0],i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13],i[14],i[15],i[16],i[17]))


up_property_Submit = form.getvalue("up_property_submit")
if up_property_Submit != None:
        upid = form.getvalue("upid")
        upname = form.getvalue("upname")
        upowname = form.getvalue("upowname")
        upphone = form.getvalue("uphone")
        uptype = form.getvalue("uptype")
        upemail= form.getvalue("upemail")
        upplotno = form.getvalue("upplotno")
        upbhk = form.getvalue("upabhk")
        upstate = form.getvalue("upstate")
        upcity = form.getvalue("upcity")
        uppincode = form.getvalue("uppincode")
        uprent = form.getvalue("uprent")
        updeposit = form.getvalue("updeposit")
        upfacilities = form.getvalue("upfacilities")
        updescription = form.getvalue("updescription")
        uplandmark = form.getvalue("uplandmark")
        upaddress = form.getvalue("upaddress")
        upvacancies = form.getvalue("upvacancies")
        q = "update property set propertyName = '%s', ownerName = '%s', mobile = '%s' ,propertyType = '%s' ,email = '%s',plotNo= '%s',availableBhk = '%s',state = '%s',city = '%s', pincode = '%s', rent = '%s',deposit = '%s', facilities = '%s', description = '%s', landmark = '%s', address = '%s' , vacancies = '%s' where id = '%s' "\
            %(upname,upowname,upphone,uptype,upemail,upplotno,upbhk,upstate,upcity,uppincode,uprent,updeposit,upfacilities,updescription,uplandmark,upaddress,upvacancies,upid)
        cur.execute(q)
        con.commit()
        print("""
        <script>
          alert("Details Updated successfully")
         </script>""")


