#!C:/Users/nandh/AppData/Local/Programs/Python/Python311/python.exe
import calendar

print("content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql
import datetime
import calendar
from  datetime import datetime

date = datetime.now().day
c= datetime.now().month
month = calendar.month_name[c]




cgitb.enable()
con= pymysql.connect(host="localhost", user="root", password="", database="user_register")
cur = con.cursor()
form = cgi.FieldStorage()
userid = form.getvalue("id")

q = """select * from userregform  where id = '%s'""" % userid
cur.execute(q)
rec = cur.fetchall()
uemail=rec[0][4]
uname = rec[0][1]
uphone =rec[0][3]
uprofile = rec[0][11]

q1 = """select * from property where status = 'Approve' and vacancies = 'vacant' and remaining_bhk > 0"""
cur.execute(q1)
allrecord = cur.fetchall()

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
                    <div class="row pt-3">
                      <div class="col-lg-12 back">
                        <div class="row">
                          <div class="col">
                            <div class="text-center" style="display: flex; justify-content: center">
                              <form method="post" enctype="multipart/form-data" class="form-inline lead bg-light p-2" style="border-radius: 10px">
                                <input type="text" name="search" placeholder="Search here.. Bhk, City" class="form-control mr-2"
                                  style="padding-left: 60px; text-align: left" />
                                  <button type="submit" name = "search_submit" class="btn btn-dark btn-sm">Search</button>
                              </form>
                            </div>
                          </div>
                        </div>
                        <div class="row pt-5">
                          <div class="col" style="display: flex; justify-content: end">
                            <form method="post" enctype="multipart/form-data" class="lead">
                              <label for="priceRange">Price Range:</label>
                              <input type="range" class="form-range" id="priceRange" name = "filter" min="0" max="10000" step="100" value="5000" />
                              <p>
                                Selected Price:
                                <span id="selectedPrice" class="badge bg-dark text-light">5000</span>
                              </p>
                              <input type = "submit" name = "range_submit" class = "btn btn-primary" value = "Filter">
                            
                              </div>
                              <div class="col lead">
                                  <label for="">No Of BHK</label> <br>
                                  <input type="checkbox" name="onebhk" value="1" >
                                  <label for="1 BHK">
                                    &nbsp;1 BHK  </label><br />
                                  <input type="checkbox" name="twobhk" value="2" >
                                  <label for="2 BHK">
                                    &nbsp;2 BHK </label><br />
                                  <input type="checkbox" name="threebhk" value="3" >
                                  <label for="3 BHK">
                                    &nbsp;3 BHK </label><br />
                            </form>
                          </div>
                        </div>
                      </div>
                        <div class="col-lg-12">
                            <div class="row ">
"""%(userid,userid,userid,userid,userid,userid))

search_submit = form.getvalue("search_submit")
r_submit = form.getvalue("range_submit")

if search_submit  != None :
    search = form.getvalue("search")
    q1 = """SELECT * FROM property WHERE (availableBhk = '%s' or city = '%s') and propertyType ='Apartment'  """ %(search,search)
    cur.execute(q1)
    con.commit()
    anorecord = cur.fetchall()
    for i in anorecord:
        fn = "dbdoc/" + i[18]
        fn1 = "dbdoc/" + i[19]
        fn2 = "dbdoc/" + i[20]
        print("""


                                <div class="col-lg-6 col-xl-4 col-md-12 d-flex justify-content-around">

                                    <div class="card mb-md-5" style="
                                                      background-image: linear-gradient(
                                                        to right top,
                                                        #e5e1da,
                                                        #7fc7d9
                                                      );width: 22rem;margin-top: 20px;
                                                    ">
                                        <div class="card-header" style="height: 270px">
                                            <center>
                                                <div id="carouselExampleIndicators%s" class="carousel slide d-block mb-5 bg-dark" data-ride="carousel"
                                                  style="margin-top: 15px;padding: 20px;padding-bottom: 40px;border-radius: 10px;">
                                                  <ol class="carousel-indicators">
                                                    <li data-target="#carouselExampleIndicators%s" data-slide-to="0" class="active"></li>
                                                    <li data-target="#carouselExampleIndicators%s" data-slide-to="1"></li>
                                                    <li data-target="#carouselExampleIndicators%s" data-slide-to="2"></li>
                                                  </ol>
                                                    <div class="carousel-inner col-sm-12">
                                                        <div class="carousel-item active">
                                                            <img class="d-block mx-auto" src="%s" alt="First slide"
                                                                height="150px" width="180px" />
                                                        </div>
                                                        <div class="carousel-item">
                                                            <img class="d-block mx-auto" src="%s" alt="Second slide"
                                                                height="150px" width="180px" />
                                                        </div>
                                                        <div class="carousel-item">
                                                            <img class="d-block mx-auto" src="%s" alt="Third slide"
                                                                height="150px" width="180px" />
                                                        </div>
                                                    </div>
                                                      <a class="carousel-control-prev" href="#carouselExampleIndicators%s" role="button" data-slide="prev">
                                                        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                                                        <span class="sr-only">Previous</span>
                                                      </a>
                                                      <a class="carousel-control-next" href="#carouselExampleIndicators%s" role="button" data-slide="next">
                                                        <span class="carousel-control-next-icon" aria-hidden="true"></span>
                                                        <span class="sr-only">Next</span>
                                                      </a>
                                                </div>
                                            </center>
                                        </div>

                                        <div class="card-body">
                                              <p class="display-4" style="font-size: 28px">Property Name</p>
                                              <p>
                                                %s
                                              </p>
                                            <p class="display-4" style="font-size: 28px">Address</p>
                                            <p>
                                                %s
                                            </p>
                                            <p class="display-4" style="font-size: 28px">Rent price :</p>
                                            <p>
                                                <b>%s onwards</b>
                                            </p>
                                            <button type="button" class="btn btn-primary" data-toggle="modal"
                                                data-target="#property%s">
                                                View Details...
                                            </button>

                                            <!-- Modal -->
                                              <div class="modal fade" id="property%s" role="dialog">
                                                <div class="modal-dialog">
                                                  <!-- Modal content-->
                                                  <div class="modal-content">
                                                    <div class="modal-header">
                                                      <h5 class="modal-title" id="exampleModalLabel">
                                                        Property details
                                                      </h5>
                                                      <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                                        <span aria-hidden="true">&times;</span>
                                                      </button>
                                                    </div>
                                                    <div class="modal-body">
                                                      <p style="font-size: 20px" class="text-secondary">
                                                        <b>House Owner Name : %s</b>
                                                        <b>House Owner Mobile : %s</b> <br>
                                                        <b>House Owner Email : %s</b> <br>
                                                      </p>
                                                      <br />
                                                      
                                                      <form method = "post" enctype="multipart/form-data">
                                                        <div style = "display:none">
                                                          <input type = "text" name = "pid" value = %s >
                                                          <input type = "text" name = "propertyName" value = "%s" >
                                                          <input type = "text" name = "ownername" value = "%s" >
                                                          <input type = "number" name = "mobile" value = "%s" >
                                                          <input type = "text" name = "propertyType" value = "%s" >
                                                          <input type = "text" name = "email" value = "%s" >
                                                          <input type = "text" name = "plotno" value = "%s" >
                                                          <input type = "text" name = "availableBhk" value = "%s" >
                                                          <input type = "text" name = "state" value = "%s" >
                                                          <input type = "text" name = "city" value = "%s" >
                                                          <input type = "number" name = "pincode" value = "%s" >
                                                          <input type = "number" name = "rent" value = "%s" >
                                                          <input type = "number" name = "deposit" value = "%s" >
                                                          <input type = "text" name = "facilities" value = "%s" >
                                                          <input type = "text" name = "description" value = "%s" >
                                                          <input type = "text" name = "landmark" value = "%s" >
                                                          <input type = "text" name = "address" value = "%s" >
                                                          <input type = "text" name = "vacancies" value = "%s" >
                                                          <input type = "text" name = "pimage" value = "%s" >
                                                          <input type = "text" name = "pimage2" value = "%s" >
                                                          <input type = "text" name = "pimage3" value = "%s" >
                                                        </div>
                                                          <p>Address : %s</p>
                                                          <p>Land Mark : %s</p>
                                                          <p>State : %s</p>
                                                          <p>City : %s</p>
                                                          <p>
                                                            PinCode : %s
                                                          </p>
                                                          <br />
                                                          <table class="table">
                                                            <tr>
                                                              <th>Rent/ Month</th>
                                                              <th>Deposit</th>
                                                              <th>BHK</th>
                                                            </tr>
                                                            <tr>
                                                              <td>+ %s</td>
                                                              <td>%s</td>
                                                              <td>%s</td>
                                                            </tr>
                                                          </table>
                                                          <br />
                                                          <p>
                                                            <b>Facilities :</b><span class="batch bg-dark text-light" style="
                                                                                            border-radius: 5px;
                                                                                            padding: 2px;
                                                                                            margin-left: 3px;
                                                                                          ">%s</span>
                                                                                          <span class="batch bg-dark text-light"
                                                          </p>
                                                          
                                                        </div>
                                                        <div class="modal-footer">
                                                    
                                                          <button type="submit" class="btn btn-primary" name="buy_submit" value="buy_submit">
                                                            Buy
                                                          </button>
                                                     </form>
                                                      <button type="button" class="btn btn-outline-primary" data-dismiss="modal">
                                                        Close
                                                      </button>
                                                    </div>
                                                  </div>
                                                </div>
                                              </div>
                                            </div>
                                        </div>
                                    </div>
       
"""%(i[0],i[0],i[0],i[0],fn,fn1,fn2,i[0],i[0],i[1],i[16],i[11],i[0],i[0],i[2],i[3],i[5],i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13],i[14],i[15],i[16],i[17],i[18],i[19],i[20],i[16],i[15],i[8],i[9],i[10],i[11],i[12],i[7],i[13]))

elif r_submit != None:
    onebhk = form.getvalue("onebhk")
    twobhk = form.getvalue("twobhk")
    threebhk = form.getvalue("threebhk")
    filter = form.getvalue("filter")

    if onebhk != None and twobhk != None and threebhk != None:
        q1 = """select * from property where (rent <= %s ) and propertyType ='Apartment' """ % filter
        cur.execute(q1)
        record = cur.fetchall()

        for i in record:
            fn = "dbdoc/" + i[18]
            fn1 = "dbdoc/" + i[19]
            fn2 = "dbdoc/" + i[20]
            print("""


                                        <div class="col-lg-6 col-xl-4 col-md-12 d-flex justify-content-around">

                                            <div class="card mb-md-5" style="
                                                              background-image: linear-gradient(
                                                                to right top,
                                                                #e5e1da,
                                                                #7fc7d9
                                                              );width: 22rem;margin-top: 20px;
                                                            ">
                                                <div class="card-header" style="height: 270px">
                                                    <center>
                                                        <div id="carouselExampleIndicators"
                                                            class="carousel slide d-block mb-5 bg-dark" data-ride="carousel"
                                                            style="
                                                                    margin-top: 15px;
                                                                    padding: 20px;
                                                                    padding-bottom: 40px;
                                                                    border-radius: 10px;
                                                                  ">
                                                            <ol class="carousel-indicators">
                                                                <li data-target="#carouselExampleIndicators" data-slide-to="0"
                                                                    class="active"></li>
                                                                <li data-target="#carouselExampleIndicators" data-slide-to="1">
                                                                </li>
                                                                <li data-target="#carouselExampleIndicators" data-slide-to="2">
                                                                </li>
                                                            </ol>
                                                            <div class="carousel-inner col-sm-12">
                                                                <div class="carousel-item active">
                                                                    <img class="d-block mx-auto" src="%s" alt="First slide"
                                                                        height="150px" width="180px" />
                                                                </div>
                                                                <div class="carousel-item">
                                                                    <img class="d-block mx-auto" src="%s" alt="Second slide"
                                                                        height="150px" width="180px" />
                                                                </div>
                                                                <div class="carousel-item">
                                                                    <img class="d-block mx-auto" src="%s" alt="Third slide"
                                                                        height="150px" width="180px" />
                                                                </div>
                                                            </div>
                                                            <a class="carousel-control-prev" href="#carouselExampleIndicators"
                                                                role="button" data-slide="prev">
                                                                <span class="carousel-control-prev-icon"
                                                                    aria-hidden="true"></span>
                                                                <span class="sr-only">Previous</span>
                                                            </a>
                                                            <a class="carousel-control-next" href="#carouselExampleIndicators"
                                                                role="button" data-slide="next">
                                                                <span class="carousel-control-next-icon"
                                                                    aria-hidden="true"></span>
                                                                <span class="sr-only">Next</span>
                                                            </a>
                                                        </div>
                                                    </center>
                                                </div>

                                                <div class="card-body">
                                                      <p class="display-4" style="font-size: 28px">Property Name</p>
                                                      <p>
                                                        %s
                                                      </p>
                                                    <p class="display-4" style="font-size: 28px">Address</p>
                                                    <p>
                                                        %s
                                                    </p>
                                                    <p class="display-4" style="font-size: 28px">Rent price :</p>
                                                    <p>
                                                        <b>%s onwards</b>
                                                    </p>
                                                    <button type="button" class="btn btn-primary" data-toggle="modal"
                                                        data-target="#property%s">
                                                        View Details...
                                                    </button>

                                                    <!-- Modal -->
                                                      <div class="modal fade" id="property%s" role="dialog">
                                                        <div class="modal-dialog">
                                                          <!-- Modal content-->
                                                          <div class="modal-content">
                                                            <div class="modal-header">
                                                              <h5 class="modal-title" id="exampleModalLabel">
                                                                Property details
                                                              </h5>
                                                              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                                                <span aria-hidden="true">&times;</span>
                                                              </button>
                                                            </div>
                                                            <div class="modal-body">
                                                              <p style="font-size: 20px" class="text-secondary">
                                                                <b>House Owner Name : %s</b>
                                                                <b>House Owner Mobile : %s</b> <br>
                                                                <b>House Owner Email : %s</b> <br>
                                                              </p>
                                                              <br />

                                                              <form method = "post" enctype="multipart/form-data">
                                                                <div style = "display:none">
                                                                  <input type = "text" name = "pid" value = %s >
                                                                  <input type = "text" name = "propertyName" value = "%s" >
                                                                  <input type = "text" name = "ownername" value = "%s" >
                                                                  <input type = "number" name = "mobile" value = "%s" >
                                                                  <input type = "text" name = "propertyType" value = "%s" >
                                                                  <input type = "text" name = "email" value = "%s" >
                                                                  <input type = "text" name = "plotno" value = "%s" >
                                                                  <input type = "text" name = "availableBhk" value = "%s" >
                                                                  <input type = "text" name = "state" value = "%s" >
                                                                  <input type = "text" name = "city" value = "%s" >
                                                                  <input type = "number" name = "pincode" value = "%s" >
                                                                  <input type = "number" name = "rent" value = "%s" >
                                                                  <input type = "number" name = "deposit" value = "%s" >
                                                                  <input type = "text" name = "facilities" value = "%s" >
                                                                  <input type = "text" name = "description" value = "%s" >
                                                                  <input type = "text" name = "landmark" value = "%s" >
                                                                  <input type = "text" name = "address" value = "%s" >
                                                                  <input type = "text" name = "vacancies" value = "%s" >
                                                                  <input type = "text" name = "pimage" value = "%s" >
                                                                  <input type = "text" name = "pimage2" value = "%s" >
                                                                  <input type = "text" name = "pimage3" value = "%s" >
                                                                </div>
                                                                  <p>Address : %s</p>
                                                                  <p>Land Mark : %s</p>
                                                                  <p>State : %s</p>
                                                                  <p>City : %s</p>
                                                                  <p>
                                                                    PinCode : %s
                                                                  </p>
                                                                  <br />
                                                                  <table class="table">
                                                                    <tr>
                                                                      <th>Rent/ Month</th>
                                                                      <th>Deposit</th>
                                                                      <th>BHK</th>
                                                                    </tr>
                                                                    <tr>
                                                                      <td>+ %s</td>
                                                                      <td>%s</td>
                                                                      <td>%s</td>
                                                                    </tr>
                                                                  </table>
                                                                  <br />
                                                                  <p>
                                                                    <b>Facilities :</b><span class="batch bg-dark text-light" style="
                                                                                                    border-radius: 5px;
                                                                                                    padding: 2px;
                                                                                                    margin-left: 3px;
                                                                                                  ">%s</span>
                                                                                                  <span class="batch bg-dark text-light"
                                                                  </p>

                                                                </div>
                                                                <div class="modal-footer">

                                                                  <button type="submit" class="btn btn-primary" name="buy_submit" value="buy_submit">
                                                                    Buy
                                                                  </button>
                                                             </form>
                                                              <button type="button" class="btn btn-outline-primary" data-dismiss="modal">
                                                                Close
                                                              </button>
                                                            </div>
                                                          </div>
                                                        </div>
                                                      </div>
                                                    </div>
                                                </div>
                                            </div>

        """ % (fn, fn1, fn2, i[1], i[16], i[11], i[0], i[0], i[2], i[3], i[5], i[0], i[1], i[2], i[3], i[4], i[5], i[6],
               i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[16],
               i[15], i[8], i[9], i[10], i[11], i[12], i[7], i[13]))

    if onebhk == None and twobhk == None and threebhk == None:
        q1 = """select * from property where (rent <= %s ) and propertyType ='Apartment' """ % filter
        cur.execute(q1)
        record = cur.fetchall()

        for i in record:
            fn = "dbdoc/" + i[18]
            fn1 = "dbdoc/" + i[19]
            fn2 = "dbdoc/" + i[20]
            print("""


                                        <div class="col-lg-6 col-xl-4 col-md-12 d-flex justify-content-around">

                                            <div class="card mb-md-5" style="
                                                              background-image: linear-gradient(
                                                                to right top,
                                                                #e5e1da,
                                                                #7fc7d9
                                                              );width: 22rem;margin-top: 20px;
                                                            ">
                                                <div class="card-header" style="height: 270px">
                                                    <center>
                                                        <div id="carouselExampleIndicators"
                                                            class="carousel slide d-block mb-5 bg-dark" data-ride="carousel"
                                                            style="
                                                                    margin-top: 15px;
                                                                    padding: 20px;
                                                                    padding-bottom: 40px;
                                                                    border-radius: 10px;
                                                                  ">
                                                            <ol class="carousel-indicators">
                                                                <li data-target="#carouselExampleIndicators" data-slide-to="0"
                                                                    class="active"></li>
                                                                <li data-target="#carouselExampleIndicators" data-slide-to="1">
                                                                </li>
                                                                <li data-target="#carouselExampleIndicators" data-slide-to="2">
                                                                </li>
                                                            </ol>
                                                            <div class="carousel-inner col-sm-12">
                                                                <div class="carousel-item active">
                                                                    <img class="d-block mx-auto" src="%s" alt="First slide"
                                                                        height="150px" width="180px" />
                                                                </div>
                                                                <div class="carousel-item">
                                                                    <img class="d-block mx-auto" src="%s" alt="Second slide"
                                                                        height="150px" width="180px" />
                                                                </div>
                                                                <div class="carousel-item">
                                                                    <img class="d-block mx-auto" src="%s" alt="Third slide"
                                                                        height="150px" width="180px" />
                                                                </div>
                                                            </div>
                                                            <a class="carousel-control-prev" href="#carouselExampleIndicators"
                                                                role="button" data-slide="prev">
                                                                <span class="carousel-control-prev-icon"
                                                                    aria-hidden="true"></span>
                                                                <span class="sr-only">Previous</span>
                                                            </a>
                                                            <a class="carousel-control-next" href="#carouselExampleIndicators"
                                                                role="button" data-slide="next">
                                                                <span class="carousel-control-next-icon"
                                                                    aria-hidden="true"></span>
                                                                <span class="sr-only">Next</span>
                                                            </a>
                                                        </div>
                                                    </center>
                                                </div>

                                                <div class="card-body">
                                                      <p class="display-4" style="font-size: 28px">Property Name</p>
                                                      <p>
                                                        %s
                                                      </p>
                                                    <p class="display-4" style="font-size: 28px">Address</p>
                                                    <p>
                                                        %s
                                                    </p>
                                                    <p class="display-4" style="font-size: 28px">Rent price :</p>
                                                    <p>
                                                        <b>%s onwards</b>
                                                    </p>
                                                    <button type="button" class="btn btn-primary" data-toggle="modal"
                                                        data-target="#property%s">
                                                        View Details...
                                                    </button>

                                                    <!-- Modal -->
                                                      <div class="modal fade" id="property%s" role="dialog">
                                                        <div class="modal-dialog">
                                                          <!-- Modal content-->
                                                          <div class="modal-content">
                                                            <div class="modal-header">
                                                              <h5 class="modal-title" id="exampleModalLabel">
                                                                Property details
                                                              </h5>
                                                              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                                                <span aria-hidden="true">&times;</span>
                                                              </button>
                                                            </div>
                                                            <div class="modal-body">
                                                              <p style="font-size: 20px" class="text-secondary">
                                                                <b>House Owner Name : %s</b>
                                                                <b>House Owner Mobile : %s</b> <br>
                                                                <b>House Owner Email : %s</b> <br>
                                                              </p>
                                                              <br />

                                                              <form method = "post" enctype="multipart/form-data">
                                                                <div style = "display:none">
                                                                  <input type = "text" name = "pid" value = %s >
                                                                  <input type = "text" name = "propertyName" value = "%s" >
                                                                  <input type = "text" name = "ownername" value = "%s" >
                                                                  <input type = "number" name = "mobile" value = "%s" >
                                                                  <input type = "text" name = "propertyType" value = "%s" >
                                                                  <input type = "text" name = "email" value = "%s" >
                                                                  <input type = "text" name = "plotno" value = "%s" >
                                                                  <input type = "text" name = "availableBhk" value = "%s" >
                                                                  <input type = "text" name = "state" value = "%s" >
                                                                  <input type = "text" name = "city" value = "%s" >
                                                                  <input type = "number" name = "pincode" value = "%s" >
                                                                  <input type = "number" name = "rent" value = "%s" >
                                                                  <input type = "number" name = "deposit" value = "%s" >
                                                                  <input type = "text" name = "facilities" value = "%s" >
                                                                  <input type = "text" name = "description" value = "%s" >
                                                                  <input type = "text" name = "landmark" value = "%s" >
                                                                  <input type = "text" name = "address" value = "%s" >
                                                                  <input type = "text" name = "vacancies" value = "%s" >
                                                                  <input type = "text" name = "pimage" value = "%s" >
                                                                  <input type = "text" name = "pimage2" value = "%s" >
                                                                  <input type = "text" name = "pimage3" value = "%s" >
                                                                </div>
                                                                  <p>Address : %s</p>
                                                                  <p>Land Mark : %s</p>
                                                                  <p>State : %s</p>
                                                                  <p>City : %s</p>
                                                                  <p>
                                                                    PinCode : %s
                                                                  </p>
                                                                  <br />
                                                                  <table class="table">
                                                                    <tr>
                                                                      <th>Rent/ Month</th>
                                                                      <th>Deposit</th>
                                                                      <th>BHK</th>
                                                                    </tr>
                                                                    <tr>
                                                                      <td>+ %s</td>
                                                                      <td>%s</td>
                                                                      <td>%s</td>
                                                                    </tr>
                                                                  </table>
                                                                  <br />
                                                                  <p>
                                                                    <b>Facilities :</b><span class="batch bg-dark text-light" style="
                                                                                                    border-radius: 5px;
                                                                                                    padding: 2px;
                                                                                                    margin-left: 3px;
                                                                                                  ">%s</span>
                                                                                                  <span class="batch bg-dark text-light"
                                                                  </p>

                                                                </div>
                                                                <div class="modal-footer">

                                                                  <button type="submit" class="btn btn-primary" name="buy_submit" value="buy_submit">
                                                                    Buy
                                                                  </button>
                                                             </form>
                                                              <button type="button" class="btn btn-outline-primary" data-dismiss="modal">
                                                                Close
                                                              </button>
                                                            </div>
                                                          </div>
                                                        </div>
                                                      </div>
                                                    </div>
                                                </div>
                                            </div>

        """ % (fn, fn1, fn2, i[1], i[16], i[11], i[0], i[0], i[2], i[3], i[5], i[0], i[1], i[2], i[3], i[4], i[5], i[6],
               i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[16],
               i[15], i[8], i[9], i[10], i[11], i[12], i[7], i[13]))

    if onebhk != None and twobhk != None and threebhk == None:
        q1 = """select * from property where (rent <= %s ) and availableBhk != '3' and propertyType ='Apartment';""" % filter
        cur.execute(q1)
        record = cur.fetchall()

        for i in record:
            fn = "dbdoc/" + i[18]
            fn1 = "dbdoc/" + i[19]
            fn2 = "dbdoc/" + i[20]
            print("""


                                        <div class="col-lg-6 col-xl-4 col-md-12 d-flex justify-content-around">

                                            <div class="card mb-md-5" style="
                                                              background-image: linear-gradient(
                                                                to right top,
                                                                #e5e1da,
                                                                #7fc7d9
                                                              );width: 22rem;margin-top: 20px;
                                                            ">
                                                <div class="card-header" style="height: 270px">
                                                    <center>
                                                        <div id="carouselExampleIndicators"
                                                            class="carousel slide d-block mb-5 bg-dark" data-ride="carousel"
                                                            style="
                                                                    margin-top: 15px;
                                                                    padding: 20px;
                                                                    padding-bottom: 40px;
                                                                    border-radius: 10px;
                                                                  ">
                                                            <ol class="carousel-indicators">
                                                                <li data-target="#carouselExampleIndicators" data-slide-to="0"
                                                                    class="active"></li>
                                                                <li data-target="#carouselExampleIndicators" data-slide-to="1">
                                                                </li>
                                                                <li data-target="#carouselExampleIndicators" data-slide-to="2">
                                                                </li>
                                                            </ol>
                                                            <div class="carousel-inner col-sm-12">
                                                                <div class="carousel-item active">
                                                                    <img class="d-block mx-auto" src="%s" alt="First slide"
                                                                        height="150px" width="180px" />
                                                                </div>
                                                                <div class="carousel-item">
                                                                    <img class="d-block mx-auto" src="%s" alt="Second slide"
                                                                        height="150px" width="180px" />
                                                                </div>
                                                                <div class="carousel-item">
                                                                    <img class="d-block mx-auto" src="%s" alt="Third slide"
                                                                        height="150px" width="180px" />
                                                                </div>
                                                            </div>
                                                            <a class="carousel-control-prev" href="#carouselExampleIndicators"
                                                                role="button" data-slide="prev">
                                                                <span class="carousel-control-prev-icon"
                                                                    aria-hidden="true"></span>
                                                                <span class="sr-only">Previous</span>
                                                            </a>
                                                            <a class="carousel-control-next" href="#carouselExampleIndicators"
                                                                role="button" data-slide="next">
                                                                <span class="carousel-control-next-icon"
                                                                    aria-hidden="true"></span>
                                                                <span class="sr-only">Next</span>
                                                            </a>
                                                        </div>
                                                    </center>
                                                </div>

                                                <div class="card-body">
                                                      <p class="display-4" style="font-size: 28px">Property Name</p>
                                                      <p>
                                                        %s
                                                      </p>
                                                    <p class="display-4" style="font-size: 28px">Address</p>
                                                    <p>
                                                        %s
                                                    </p>
                                                    <p class="display-4" style="font-size: 28px">Rent price :</p>
                                                    <p>
                                                        <b>%s onwards</b>
                                                    </p>
                                                    <button type="button" class="btn btn-primary" data-toggle="modal"
                                                        data-target="#property%s">
                                                        View Details...
                                                    </button>

                                                    <!-- Modal -->
                                                      <div class="modal fade" id="property%s" role="dialog">
                                                        <div class="modal-dialog">
                                                          <!-- Modal content-->
                                                          <div class="modal-content">
                                                            <div class="modal-header">
                                                              <h5 class="modal-title" id="exampleModalLabel">
                                                                Property details
                                                              </h5>
                                                              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                                                <span aria-hidden="true">&times;</span>
                                                              </button>
                                                            </div>
                                                            <div class="modal-body">
                                                              <p style="font-size: 20px" class="text-secondary">
                                                                <b>House Owner Name : %s</b>
                                                                <b>House Owner Mobile : %s</b> <br>
                                                                <b>House Owner Email : %s</b> <br>
                                                              </p>
                                                              <br />

                                                              <form method = "post" enctype="multipart/form-data">
                                                                <div style = "display:none">
                                                                  <input type = "text" name = "pid" value = %s >
                                                                  <input type = "text" name = "propertyName" value = "%s" >
                                                                  <input type = "text" name = "ownername" value = "%s" >
                                                                  <input type = "number" name = "mobile" value = "%s" >
                                                                  <input type = "text" name = "propertyType" value = "%s" >
                                                                  <input type = "text" name = "email" value = "%s" >
                                                                  <input type = "text" name = "plotno" value = "%s" >
                                                                  <input type = "text" name = "availableBhk" value = "%s" >
                                                                  <input type = "text" name = "state" value = "%s" >
                                                                  <input type = "text" name = "city" value = "%s" >
                                                                  <input type = "number" name = "pincode" value = "%s" >
                                                                  <input type = "number" name = "rent" value = "%s" >
                                                                  <input type = "number" name = "deposit" value = "%s" >
                                                                  <input type = "text" name = "facilities" value = "%s" >
                                                                  <input type = "text" name = "description" value = "%s" >
                                                                  <input type = "text" name = "landmark" value = "%s" >
                                                                  <input type = "text" name = "address" value = "%s" >
                                                                  <input type = "text" name = "vacancies" value = "%s" >
                                                                  <input type = "text" name = "pimage" value = "%s" >
                                                                  <input type = "text" name = "pimage2" value = "%s" >
                                                                  <input type = "text" name = "pimage3" value = "%s" >
                                                                </div>
                                                                  <p>Address : %s</p>
                                                                  <p>Land Mark : %s</p>
                                                                  <p>State : %s</p>
                                                                  <p>City : %s</p>
                                                                  <p>
                                                                    PinCode : %s
                                                                  </p>
                                                                  <br />
                                                                  <table class="table">
                                                                    <tr>
                                                                      <th>Rent/ Month</th>
                                                                      <th>Deposit</th>
                                                                      <th>BHK</th>
                                                                    </tr>
                                                                    <tr>
                                                                      <td>+ %s</td>
                                                                      <td>%s</td>
                                                                      <td>%s</td>
                                                                    </tr>
                                                                  </table>
                                                                  <br />
                                                                  <p>
                                                                    <b>Facilities :</b><span class="batch bg-dark text-light" style="
                                                                                                    border-radius: 5px;
                                                                                                    padding: 2px;
                                                                                                    margin-left: 3px;
                                                                                                  ">%s</span>
                                                                                                  <span class="batch bg-dark text-light"
                                                                  </p>

                                                                </div>
                                                                <div class="modal-footer">

                                                                  <button type="submit" class="btn btn-primary" name="buy_submit" value="buy_submit">
                                                                    Buy
                                                                  </button>
                                                             </form>
                                                              <button type="button" class="btn btn-outline-primary" data-dismiss="modal">
                                                                Close
                                                              </button>
                                                            </div>
                                                          </div>
                                                        </div>
                                                      </div>
                                                    </div>
                                                </div>
                                            </div>

        """ % (fn, fn1, fn2, i[1], i[16], i[11], i[0], i[0], i[2], i[3], i[5], i[0], i[1], i[2], i[3], i[4], i[5], i[6],
               i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[16],
               i[15], i[8], i[9], i[10], i[11], i[12], i[7], i[13]))

    if onebhk != None and twobhk == None and threebhk != None:
        q1 = """select * from property where (rent <= %s ) and availableBhk != '2' and propertyType ='Apartment';""" % filter
        cur.execute(q1)
        record = cur.fetchall()

        for i in record:
            fn = "dbdoc/" + i[18]
            fn1 = "dbdoc/" + i[19]
            fn2 = "dbdoc/" + i[20]
            print("""


                                        <div class="col-lg-6 col-xl-4 col-md-12 d-flex justify-content-around">

                                            <div class="card mb-md-5" style="
                                                              background-image: linear-gradient(
                                                                to right top,
                                                                #e5e1da,
                                                                #7fc7d9
                                                              );width: 22rem;margin-top: 20px;
                                                            ">
                                                <div class="card-header" style="height: 270px">
                                                    <center>
                                                        <div id="carouselExampleIndicators"
                                                            class="carousel slide d-block mb-5 bg-dark" data-ride="carousel"
                                                            style="
                                                                    margin-top: 15px;
                                                                    padding: 20px;
                                                                    padding-bottom: 40px;
                                                                    border-radius: 10px;
                                                                  ">
                                                            <ol class="carousel-indicators">
                                                                <li data-target="#carouselExampleIndicators" data-slide-to="0"
                                                                    class="active"></li>
                                                                <li data-target="#carouselExampleIndicators" data-slide-to="1">
                                                                </li>
                                                                <li data-target="#carouselExampleIndicators" data-slide-to="2">
                                                                </li>
                                                            </ol>
                                                            <div class="carousel-inner col-sm-12">
                                                                <div class="carousel-item active">
                                                                    <img class="d-block mx-auto" src="%s" alt="First slide"
                                                                        height="150px" width="180px" />
                                                                </div>
                                                                <div class="carousel-item">
                                                                    <img class="d-block mx-auto" src="%s" alt="Second slide"
                                                                        height="150px" width="180px" />
                                                                </div>
                                                                <div class="carousel-item">
                                                                    <img class="d-block mx-auto" src="%s" alt="Third slide"
                                                                        height="150px" width="180px" />
                                                                </div>
                                                            </div>
                                                            <a class="carousel-control-prev" href="#carouselExampleIndicators"
                                                                role="button" data-slide="prev">
                                                                <span class="carousel-control-prev-icon"
                                                                    aria-hidden="true"></span>
                                                                <span class="sr-only">Previous</span>
                                                            </a>
                                                            <a class="carousel-control-next" href="#carouselExampleIndicators"
                                                                role="button" data-slide="next">
                                                                <span class="carousel-control-next-icon"
                                                                    aria-hidden="true"></span>
                                                                <span class="sr-only">Next</span>
                                                            </a>
                                                        </div>
                                                    </center>
                                                </div>

                                                <div class="card-body">
                                                      <p class="display-4" style="font-size: 28px">Property Name</p>
                                                      <p>
                                                        %s
                                                      </p>
                                                    <p class="display-4" style="font-size: 28px">Address</p>
                                                    <p>
                                                        %s
                                                    </p>
                                                    <p class="display-4" style="font-size: 28px">Rent price :</p>
                                                    <p>
                                                        <b>%s onwards</b>
                                                    </p>
                                                    <button type="button" class="btn btn-primary" data-toggle="modal"
                                                        data-target="#property%s">
                                                        View Details...
                                                    </button>

                                                    <!-- Modal -->
                                                      <div class="modal fade" id="property%s" role="dialog">
                                                        <div class="modal-dialog">
                                                          <!-- Modal content-->
                                                          <div class="modal-content">
                                                            <div class="modal-header">
                                                              <h5 class="modal-title" id="exampleModalLabel">
                                                                Property details
                                                              </h5>
                                                              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                                                <span aria-hidden="true">&times;</span>
                                                              </button>
                                                            </div>
                                                            <div class="modal-body">
                                                              <p style="font-size: 20px" class="text-secondary">
                                                                <b>House Owner Name : %s</b>
                                                                <b>House Owner Mobile : %s</b> <br>
                                                                <b>House Owner Email : %s</b> <br>
                                                              </p>
                                                              <br />

                                                              <form method = "post" enctype="multipart/form-data">
                                                                <div style = "display:none">
                                                                  <input type = "text" name = "pid" value = %s >
                                                                  <input type = "text" name = "propertyName" value = "%s" >
                                                                  <input type = "text" name = "ownername" value = "%s" >
                                                                  <input type = "number" name = "mobile" value = "%s" >
                                                                  <input type = "text" name = "propertyType" value = "%s" >
                                                                  <input type = "text" name = "email" value = "%s" >
                                                                  <input type = "text" name = "plotno" value = "%s" >
                                                                  <input type = "text" name = "availableBhk" value = "%s" >
                                                                  <input type = "text" name = "state" value = "%s" >
                                                                  <input type = "text" name = "city" value = "%s" >
                                                                  <input type = "number" name = "pincode" value = "%s" >
                                                                  <input type = "number" name = "rent" value = "%s" >
                                                                  <input type = "number" name = "deposit" value = "%s" >
                                                                  <input type = "text" name = "facilities" value = "%s" >
                                                                  <input type = "text" name = "description" value = "%s" >
                                                                  <input type = "text" name = "landmark" value = "%s" >
                                                                  <input type = "text" name = "address" value = "%s" >
                                                                  <input type = "text" name = "vacancies" value = "%s" >
                                                                  <input type = "text" name = "pimage" value = "%s" >
                                                                  <input type = "text" name = "pimage2" value = "%s" >
                                                                  <input type = "text" name = "pimage3" value = "%s" >
                                                                </div>
                                                                  <p>Address : %s</p>
                                                                  <p>Land Mark : %s</p>
                                                                  <p>State : %s</p>
                                                                  <p>City : %s</p>
                                                                  <p>
                                                                    PinCode : %s
                                                                  </p>
                                                                  <br />
                                                                  <table class="table">
                                                                    <tr>
                                                                      <th>Rent/ Month</th>
                                                                      <th>Deposit</th>
                                                                      <th>BHK</th>
                                                                    </tr>
                                                                    <tr>
                                                                      <td>+ %s</td>
                                                                      <td>%s</td>
                                                                      <td>%s</td>
                                                                    </tr>
                                                                  </table>
                                                                  <br />
                                                                  <p>
                                                                    <b>Facilities :</b><span class="batch bg-dark text-light" style="
                                                                                                    border-radius: 5px;
                                                                                                    padding: 2px;
                                                                                                    margin-left: 3px;
                                                                                                  ">%s</span>
                                                                                                  <span class="batch bg-dark text-light"
                                                                  </p>

                                                                </div>
                                                                <div class="modal-footer">

                                                                  <button type="submit" class="btn btn-primary" name="buy_submit" value="buy_submit">
                                                                    Buy
                                                                  </button>
                                                             </form>
                                                              <button type="button" class="btn btn-outline-primary" data-dismiss="modal">
                                                                Close
                                                              </button>
                                                            </div>
                                                          </div>
                                                        </div>
                                                      </div>
                                                    </div>
                                                </div>
                                            </div>

        """ % (fn, fn1, fn2, i[1], i[16], i[11], i[0], i[0], i[2], i[3], i[5], i[0], i[1], i[2], i[3], i[4], i[5], i[6],
               i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[16],
               i[15], i[8], i[9], i[10], i[11], i[12], i[7], i[13]))

    if onebhk == None and twobhk != None and threebhk != None:
        q1 = """select * from property where (rent <= %s ) and availableBhk != '1'and propertyType ='Apartment';""" % filter
        cur.execute(q1)
        record = cur.fetchall()

        for i in record:
            fn = "dbdoc/" + i[18]
            fn1 = "dbdoc/" + i[19]
            fn2 = "dbdoc/" + i[20]
            print("""


                                        <div class="col-lg-6 col-xl-4 col-md-12 d-flex justify-content-around">

                                            <div class="card mb-md-5" style="
                                                              background-image: linear-gradient(
                                                                to right top,
                                                                #e5e1da,
                                                                #7fc7d9
                                                              );width: 22rem;margin-top: 20px;
                                                            ">
                                                <div class="card-header" style="height: 270px">
                                                    <center>
                                                        <div id="carouselExampleIndicators"
                                                            class="carousel slide d-block mb-5 bg-dark" data-ride="carousel"
                                                            style="
                                                                    margin-top: 15px;
                                                                    padding: 20px;
                                                                    padding-bottom: 40px;
                                                                    border-radius: 10px;
                                                                  ">
                                                            <ol class="carousel-indicators">
                                                                <li data-target="#carouselExampleIndicators" data-slide-to="0"
                                                                    class="active"></li>
                                                                <li data-target="#carouselExampleIndicators" data-slide-to="1">
                                                                </li>
                                                                <li data-target="#carouselExampleIndicators" data-slide-to="2">
                                                                </li>
                                                            </ol>
                                                            <div class="carousel-inner col-sm-12">
                                                                <div class="carousel-item active">
                                                                    <img class="d-block mx-auto" src="%s" alt="First slide"
                                                                        height="150px" width="180px" />
                                                                </div>
                                                                <div class="carousel-item">
                                                                    <img class="d-block mx-auto" src="%s" alt="Second slide"
                                                                        height="150px" width="180px" />
                                                                </div>
                                                                <div class="carousel-item">
                                                                    <img class="d-block mx-auto" src="%s" alt="Third slide"
                                                                        height="150px" width="180px" />
                                                                </div>
                                                            </div>
                                                            <a class="carousel-control-prev" href="#carouselExampleIndicators"
                                                                role="button" data-slide="prev">
                                                                <span class="carousel-control-prev-icon"
                                                                    aria-hidden="true"></span>
                                                                <span class="sr-only">Previous</span>
                                                            </a>
                                                            <a class="carousel-control-next" href="#carouselExampleIndicators"
                                                                role="button" data-slide="next">
                                                                <span class="carousel-control-next-icon"
                                                                    aria-hidden="true"></span>
                                                                <span class="sr-only">Next</span>
                                                            </a>
                                                        </div>
                                                    </center>
                                                </div>

                                                <div class="card-body">
                                                      <p class="display-4" style="font-size: 28px">Property Name</p>
                                                      <p>
                                                        %s
                                                      </p>
                                                    <p class="display-4" style="font-size: 28px">Address</p>
                                                    <p>
                                                        %s
                                                    </p>
                                                    <p class="display-4" style="font-size: 28px">Rent price :</p>
                                                    <p>
                                                        <b>%s onwards</b>
                                                    </p>
                                                    <button type="button" class="btn btn-primary" data-toggle="modal"
                                                        data-target="#property%s">
                                                        View Details...
                                                    </button>

                                                    <!-- Modal -->
                                                      <div class="modal fade" id="property%s" role="dialog">
                                                        <div class="modal-dialog">
                                                          <!-- Modal content-->
                                                          <div class="modal-content">
                                                            <div class="modal-header">
                                                              <h5 class="modal-title" id="exampleModalLabel">
                                                                Property details
                                                              </h5>
                                                              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                                                <span aria-hidden="true">&times;</span>
                                                              </button>
                                                            </div>
                                                            <div class="modal-body">
                                                              <p style="font-size: 20px" class="text-secondary">
                                                                <b>House Owner Name : %s</b>
                                                                <b>House Owner Mobile : %s</b> <br>
                                                                <b>House Owner Email : %s</b> <br>
                                                              </p>
                                                              <br />

                                                              <form method = "post" enctype="multipart/form-data">
                                                                <div style = "display:none">
                                                                  <input type = "text" name = "pid" value = %s >
                                                                  <input type = "text" name = "propertyName" value = "%s" >
                                                                  <input type = "text" name = "ownername" value = "%s" >
                                                                  <input type = "number" name = "mobile" value = "%s" >
                                                                  <input type = "text" name = "propertyType" value = "%s" >
                                                                  <input type = "text" name = "email" value = "%s" >
                                                                  <input type = "text" name = "plotno" value = "%s" >
                                                                  <input type = "text" name = "availableBhk" value = "%s" >
                                                                  <input type = "text" name = "state" value = "%s" >
                                                                  <input type = "text" name = "city" value = "%s" >
                                                                  <input type = "number" name = "pincode" value = "%s" >
                                                                  <input type = "number" name = "rent" value = "%s" >
                                                                  <input type = "number" name = "deposit" value = "%s" >
                                                                  <input type = "text" name = "facilities" value = "%s" >
                                                                  <input type = "text" name = "description" value = "%s" >
                                                                  <input type = "text" name = "landmark" value = "%s" >
                                                                  <input type = "text" name = "address" value = "%s" >
                                                                  <input type = "text" name = "vacancies" value = "%s" >
                                                                  <input type = "text" name = "pimage" value = "%s" >
                                                                  <input type = "text" name = "pimage2" value = "%s" >
                                                                  <input type = "text" name = "pimage3" value = "%s" >
                                                                </div>
                                                                  <p>Address : %s</p>
                                                                  <p>Land Mark : %s</p>
                                                                  <p>State : %s</p>
                                                                  <p>City : %s</p>
                                                                  <p>
                                                                    PinCode : %s
                                                                  </p>
                                                                  <br />
                                                                  <table class="table">
                                                                    <tr>
                                                                      <th>Rent/ Month</th>
                                                                      <th>Deposit</th>
                                                                      <th>BHK</th>
                                                                    </tr>
                                                                    <tr>
                                                                      <td>+ %s</td>
                                                                      <td>%s</td>
                                                                      <td>%s</td>
                                                                    </tr>
                                                                  </table>
                                                                  <br />
                                                                  <p>
                                                                    <b>Facilities :</b><span class="batch bg-dark text-light" style="
                                                                                                    border-radius: 5px;
                                                                                                    padding: 2px;
                                                                                                    margin-left: 3px;
                                                                                                  ">%s</span>
                                                                                                  <span class="batch bg-dark text-light"
                                                                  </p>

                                                                </div>
                                                                <div class="modal-footer">

                                                                  <button type="submit" class="btn btn-primary" name="buy_submit" value="buy_submit">
                                                                    Buy
                                                                  </button>
                                                             </form>
                                                              <button type="button" class="btn btn-outline-primary" data-dismiss="modal">
                                                                Close
                                                              </button>
                                                            </div>
                                                          </div>
                                                        </div>
                                                      </div>
                                                    </div>
                                                </div>
                                            </div>

        """ % (fn, fn1, fn2, i[1], i[16], i[11], i[0], i[0], i[2], i[3], i[5], i[0], i[1], i[2], i[3], i[4], i[5], i[6],
               i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[16],
               i[15], i[8], i[9], i[10], i[11], i[12], i[7], i[13]))

    if onebhk != None and twobhk == None and threebhk == None:
        q1 = """select * from property where (rent <= %s ) and availableBhk = '1' and propertyType ='Apartment';""" % filter
        cur.execute(q1)
        record = cur.fetchall()

        for i in record:
            fn = "dbdoc/" + i[18]
            fn1 = "dbdoc/" + i[19]
            fn2 = "dbdoc/" + i[20]
            print("""


                                        <div class="col-lg-6 col-xl-4 col-md-12 d-flex justify-content-around">

                                            <div class="card mb-md-5" style="
                                                              background-image: linear-gradient(
                                                                to right top,
                                                                #e5e1da,
                                                                #7fc7d9
                                                              );width: 22rem;margin-top: 20px;
                                                            ">
                                                <div class="card-header" style="height: 270px">
                                                    <center>
                                                        <div id="carouselExampleIndicators"
                                                            class="carousel slide d-block mb-5 bg-dark" data-ride="carousel"
                                                            style="
                                                                    margin-top: 15px;
                                                                    padding: 20px;
                                                                    padding-bottom: 40px;
                                                                    border-radius: 10px;
                                                                  ">
                                                            <ol class="carousel-indicators">
                                                                <li data-target="#carouselExampleIndicators" data-slide-to="0"
                                                                    class="active"></li>
                                                                <li data-target="#carouselExampleIndicators" data-slide-to="1">
                                                                </li>
                                                                <li data-target="#carouselExampleIndicators" data-slide-to="2">
                                                                </li>
                                                            </ol>
                                                            <div class="carousel-inner col-sm-12">
                                                                <div class="carousel-item active">
                                                                    <img class="d-block mx-auto" src="%s" alt="First slide"
                                                                        height="150px" width="180px" />
                                                                </div>
                                                                <div class="carousel-item">
                                                                    <img class="d-block mx-auto" src="%s" alt="Second slide"
                                                                        height="150px" width="180px" />
                                                                </div>
                                                                <div class="carousel-item">
                                                                    <img class="d-block mx-auto" src="%s" alt="Third slide"
                                                                        height="150px" width="180px" />
                                                                </div>
                                                            </div>
                                                            <a class="carousel-control-prev" href="#carouselExampleIndicators"
                                                                role="button" data-slide="prev">
                                                                <span class="carousel-control-prev-icon"
                                                                    aria-hidden="true"></span>
                                                                <span class="sr-only">Previous</span>
                                                            </a>
                                                            <a class="carousel-control-next" href="#carouselExampleIndicators"
                                                                role="button" data-slide="next">
                                                                <span class="carousel-control-next-icon"
                                                                    aria-hidden="true"></span>
                                                                <span class="sr-only">Next</span>
                                                            </a>
                                                        </div>
                                                    </center>
                                                </div>

                                                <div class="card-body">
                                                      <p class="display-4" style="font-size: 28px">Property Name</p>
                                                      <p>
                                                        %s
                                                      </p>
                                                    <p class="display-4" style="font-size: 28px">Address</p>
                                                    <p>
                                                        %s
                                                    </p>
                                                    <p class="display-4" style="font-size: 28px">Rent price :</p>
                                                    <p>
                                                        <b>%s onwards</b>
                                                    </p>
                                                    <button type="button" class="btn btn-primary" data-toggle="modal"
                                                        data-target="#property%s">
                                                        View Details...
                                                    </button>

                                                    <!-- Modal -->
                                                      <div class="modal fade" id="property%s" role="dialog">
                                                        <div class="modal-dialog">
                                                          <!-- Modal content-->
                                                          <div class="modal-content">
                                                            <div class="modal-header">
                                                              <h5 class="modal-title" id="exampleModalLabel">
                                                                Property details
                                                              </h5>
                                                              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                                                <span aria-hidden="true">&times;</span>
                                                              </button>
                                                            </div>
                                                            <div class="modal-body">
                                                              <p style="font-size: 20px" class="text-secondary">
                                                                <b>House Owner Name : %s</b>
                                                                <b>House Owner Mobile : %s</b> <br>
                                                                <b>House Owner Email : %s</b> <br>
                                                              </p>
                                                              <br />

                                                              <form method = "post" enctype="multipart/form-data">
                                                                <div style = "display:none">
                                                                  <input type = "text" name = "pid" value = %s >
                                                                  <input type = "text" name = "propertyName" value = "%s" >
                                                                  <input type = "text" name = "ownername" value = "%s" >
                                                                  <input type = "number" name = "mobile" value = "%s" >
                                                                  <input type = "text" name = "propertyType" value = "%s" >
                                                                  <input type = "text" name = "email" value = "%s" >
                                                                  <input type = "text" name = "plotno" value = "%s" >
                                                                  <input type = "text" name = "availableBhk" value = "%s" >
                                                                  <input type = "text" name = "state" value = "%s" >
                                                                  <input type = "text" name = "city" value = "%s" >
                                                                  <input type = "number" name = "pincode" value = "%s" >
                                                                  <input type = "number" name = "rent" value = "%s" >
                                                                  <input type = "number" name = "deposit" value = "%s" >
                                                                  <input type = "text" name = "facilities" value = "%s" >
                                                                  <input type = "text" name = "description" value = "%s" >
                                                                  <input type = "text" name = "landmark" value = "%s" >
                                                                  <input type = "text" name = "address" value = "%s" >
                                                                  <input type = "text" name = "vacancies" value = "%s" >
                                                                  <input type = "text" name = "pimage" value = "%s" >
                                                                  <input type = "text" name = "pimage2" value = "%s" >
                                                                  <input type = "text" name = "pimage3" value = "%s" >
                                                                </div>
                                                                  <p>Address : %s</p>
                                                                  <p>Land Mark : %s</p>
                                                                  <p>State : %s</p>
                                                                  <p>City : %s</p>
                                                                  <p>
                                                                    PinCode : %s
                                                                  </p>
                                                                  <br />
                                                                  <table class="table">
                                                                    <tr>
                                                                      <th>Rent/ Month</th>
                                                                      <th>Deposit</th>
                                                                      <th>BHK</th>
                                                                    </tr>
                                                                    <tr>
                                                                      <td>+ %s</td>
                                                                      <td>%s</td>
                                                                      <td>%s</td>
                                                                    </tr>
                                                                  </table>
                                                                  <br />
                                                                  <p>
                                                                    <b>Facilities :</b><span class="batch bg-dark text-light" style="
                                                                                                    border-radius: 5px;
                                                                                                    padding: 2px;
                                                                                                    margin-left: 3px;
                                                                                                  ">%s</span>
                                                                                                  <span class="batch bg-dark text-light"
                                                                  </p>

                                                                </div>
                                                                <div class="modal-footer">

                                                                  <button type="submit" class="btn btn-primary" name="buy_submit" value="buy_submit">
                                                                    Buy
                                                                  </button>
                                                             </form>
                                                              <button type="button" class="btn btn-outline-primary" data-dismiss="modal">
                                                                Close
                                                              </button>
                                                            </div>
                                                          </div>
                                                        </div>
                                                      </div>
                                                    </div>
                                                </div>
                                            </div>

        """ % (fn, fn1, fn2, i[1], i[16], i[11], i[0], i[0], i[2], i[3], i[5], i[0], i[1], i[2], i[3], i[4], i[5], i[6],
               i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[16],
               i[15], i[8], i[9], i[10], i[11], i[12], i[7], i[13]))

    if onebhk == None and twobhk != None and threebhk == None:
        q1 = """select * from property where (rent <= %s ) and availableBhk = '2' and propertyType ='Apartment';""" % filter
        cur.execute(q1)
        record = cur.fetchall()

        for i in record:
            fn = "dbdoc/" + i[18]
            fn1 = "dbdoc/" + i[19]
            fn2 = "dbdoc/" + i[20]
            print("""


                                        <div class="col-lg-6 col-xl-4 col-md-12 d-flex justify-content-around">

                                            <div class="card mb-md-5" style="
                                                              background-image: linear-gradient(
                                                                to right top,
                                                                #e5e1da,
                                                                #7fc7d9
                                                              );width: 22rem;margin-top: 20px;
                                                            ">
                                                <div class="card-header" style="height: 270px">
                                                    <center>
                                                        <div id="carouselExampleIndicators"
                                                            class="carousel slide d-block mb-5 bg-dark" data-ride="carousel"
                                                            style="
                                                                    margin-top: 15px;
                                                                    padding: 20px;
                                                                    padding-bottom: 40px;
                                                                    border-radius: 10px;
                                                                  ">
                                                            <ol class="carousel-indicators">
                                                                <li data-target="#carouselExampleIndicators" data-slide-to="0"
                                                                    class="active"></li>
                                                                <li data-target="#carouselExampleIndicators" data-slide-to="1">
                                                                </li>
                                                                <li data-target="#carouselExampleIndicators" data-slide-to="2">
                                                                </li>
                                                            </ol>
                                                            <div class="carousel-inner col-sm-12">
                                                                <div class="carousel-item active">
                                                                    <img class="d-block mx-auto" src="%s" alt="First slide"
                                                                        height="150px" width="180px" />
                                                                </div>
                                                                <div class="carousel-item">
                                                                    <img class="d-block mx-auto" src="%s" alt="Second slide"
                                                                        height="150px" width="180px" />
                                                                </div>
                                                                <div class="carousel-item">
                                                                    <img class="d-block mx-auto" src="%s" alt="Third slide"
                                                                        height="150px" width="180px" />
                                                                </div>
                                                            </div>
                                                            <a class="carousel-control-prev" href="#carouselExampleIndicators"
                                                                role="button" data-slide="prev">
                                                                <span class="carousel-control-prev-icon"
                                                                    aria-hidden="true"></span>
                                                                <span class="sr-only">Previous</span>
                                                            </a>
                                                            <a class="carousel-control-next" href="#carouselExampleIndicators"
                                                                role="button" data-slide="next">
                                                                <span class="carousel-control-next-icon"
                                                                    aria-hidden="true"></span>
                                                                <span class="sr-only">Next</span>
                                                            </a>
                                                        </div>
                                                    </center>
                                                </div>

                                                <div class="card-body">
                                                      <p class="display-4" style="font-size: 28px">Property Name</p>
                                                      <p>
                                                        %s
                                                      </p>
                                                    <p class="display-4" style="font-size: 28px">Address</p>
                                                    <p>
                                                        %s
                                                    </p>
                                                    <p class="display-4" style="font-size: 28px">Rent price :</p>
                                                    <p>
                                                        <b>%s onwards</b>
                                                    </p>
                                                    <button type="button" class="btn btn-primary" data-toggle="modal"
                                                        data-target="#property%s">
                                                        View Details...
                                                    </button>

                                                    <!-- Modal -->
                                                      <div class="modal fade" id="property%s" role="dialog">
                                                        <div class="modal-dialog">
                                                          <!-- Modal content-->
                                                          <div class="modal-content">
                                                            <div class="modal-header">
                                                              <h5 class="modal-title" id="exampleModalLabel">
                                                                Property details
                                                              </h5>
                                                              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                                                <span aria-hidden="true">&times;</span>
                                                              </button>
                                                            </div>
                                                            <div class="modal-body">
                                                              <p style="font-size: 20px" class="text-secondary">
                                                                <b>House Owner Name : %s</b>
                                                                <b>House Owner Mobile : %s</b> <br>
                                                                <b>House Owner Email : %s</b> <br>
                                                              </p>
                                                              <br />

                                                              <form method = "post" enctype="multipart/form-data">
                                                                <div style = "display:none">
                                                                  <input type = "text" name = "pid" value = %s >
                                                                  <input type = "text" name = "propertyName" value = "%s" >
                                                                  <input type = "text" name = "ownername" value = "%s" >
                                                                  <input type = "number" name = "mobile" value = "%s" >
                                                                  <input type = "text" name = "propertyType" value = "%s" >
                                                                  <input type = "text" name = "email" value = "%s" >
                                                                  <input type = "text" name = "plotno" value = "%s" >
                                                                  <input type = "text" name = "availableBhk" value = "%s" >
                                                                  <input type = "text" name = "state" value = "%s" >
                                                                  <input type = "text" name = "city" value = "%s" >
                                                                  <input type = "number" name = "pincode" value = "%s" >
                                                                  <input type = "number" name = "rent" value = "%s" >
                                                                  <input type = "number" name = "deposit" value = "%s" >
                                                                  <input type = "text" name = "facilities" value = "%s" >
                                                                  <input type = "text" name = "description" value = "%s" >
                                                                  <input type = "text" name = "landmark" value = "%s" >
                                                                  <input type = "text" name = "address" value = "%s" >
                                                                  <input type = "text" name = "vacancies" value = "%s" >
                                                                  <input type = "text" name = "pimage" value = "%s" >
                                                                  <input type = "text" name = "pimage2" value = "%s" >
                                                                  <input type = "text" name = "pimage3" value = "%s" >
                                                                </div>
                                                                  <p>Address : %s</p>
                                                                  <p>Land Mark : %s</p>
                                                                  <p>State : %s</p>
                                                                  <p>City : %s</p>
                                                                  <p>
                                                                    PinCode : %s
                                                                  </p>
                                                                  <br />
                                                                  <table class="table">
                                                                    <tr>
                                                                      <th>Rent/ Month</th>
                                                                      <th>Deposit</th>
                                                                      <th>BHK</th>
                                                                    </tr>
                                                                    <tr>
                                                                      <td>+ %s</td>
                                                                      <td>%s</td>
                                                                      <td>%s</td>
                                                                    </tr>
                                                                  </table>
                                                                  <br />
                                                                  <p>
                                                                    <b>Facilities :</b><span class="batch bg-dark text-light" style="
                                                                                                    border-radius: 5px;
                                                                                                    padding: 2px;
                                                                                                    margin-left: 3px;
                                                                                                  ">%s</span>
                                                                                                  <span class="batch bg-dark text-light"
                                                                  </p>

                                                                </div>
                                                                <div class="modal-footer">

                                                                  <button type="submit" class="btn btn-primary" name="buy_submit" value="buy_submit">
                                                                    Buy
                                                                  </button>
                                                             </form>
                                                              <button type="button" class="btn btn-outline-primary" data-dismiss="modal">
                                                                Close
                                                              </button>
                                                            </div>
                                                          </div>
                                                        </div>
                                                      </div>
                                                    </div>
                                                </div>
                                            </div>

        """ % (fn, fn1, fn2, i[1], i[16], i[11], i[0], i[0], i[2], i[3], i[5], i[0], i[1], i[2], i[3], i[4], i[5], i[6],
               i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[16],
               i[15], i[8], i[9], i[10], i[11], i[12], i[7], i[13]))

    if onebhk == None and twobhk == None and threebhk != None:
        q1 = """select * from property where (rent <= %s ) and availableBhk = '3' and propertyType ='Apartment';""" % filter
        cur.execute(q1)
        record = cur.fetchall()

        for i in record:
            fn = "dbdoc/" + i[18]
            fn1 = "dbdoc/" + i[19]
            fn2 = "dbdoc/" + i[20]
            print("""


                                        <div class="col-lg-6 col-xl-4 col-md-12 d-flex justify-content-around">

                                            <div class="card mb-md-5" style="
                                                              background-image: linear-gradient(
                                                                to right top,
                                                                #e5e1da,
                                                                #7fc7d9
                                                              );width: 22rem;margin-top: 20px;
                                                            ">
                                                <div class="card-header" style="height: 270px">
                                                    <center>
                                                        <div id="carouselExampleIndicators"
                                                            class="carousel slide d-block mb-5 bg-dark" data-ride="carousel"
                                                            style="
                                                                    margin-top: 15px;
                                                                    padding: 20px;
                                                                    padding-bottom: 40px;
                                                                    border-radius: 10px;
                                                                  ">
                                                            <ol class="carousel-indicators">
                                                                <li data-target="#carouselExampleIndicators" data-slide-to="0"
                                                                    class="active"></li>
                                                                <li data-target="#carouselExampleIndicators" data-slide-to="1">
                                                                </li>
                                                                <li data-target="#carouselExampleIndicators" data-slide-to="2">
                                                                </li>
                                                            </ol>
                                                            <div class="carousel-inner col-sm-12">
                                                                <div class="carousel-item active">
                                                                    <img class="d-block mx-auto" src="%s" alt="First slide"
                                                                        height="150px" width="180px" />
                                                                </div>
                                                                <div class="carousel-item">
                                                                    <img class="d-block mx-auto" src="%s" alt="Second slide"
                                                                        height="150px" width="180px" />
                                                                </div>
                                                                <div class="carousel-item">
                                                                    <img class="d-block mx-auto" src="%s" alt="Third slide"
                                                                        height="150px" width="180px" />
                                                                </div>
                                                            </div>
                                                            <a class="carousel-control-prev" href="#carouselExampleIndicators"
                                                                role="button" data-slide="prev">
                                                                <span class="carousel-control-prev-icon"
                                                                    aria-hidden="true"></span>
                                                                <span class="sr-only">Previous</span>
                                                            </a>
                                                            <a class="carousel-control-next" href="#carouselExampleIndicators"
                                                                role="button" data-slide="next">
                                                                <span class="carousel-control-next-icon"
                                                                    aria-hidden="true"></span>
                                                                <span class="sr-only">Next</span>
                                                            </a>
                                                        </div>
                                                    </center>
                                                </div>

                                                <div class="card-body">
                                                      <p class="display-4" style="font-size: 28px">Property Name</p>
                                                      <p>
                                                        %s
                                                      </p>
                                                    <p class="display-4" style="font-size: 28px">Address</p>
                                                    <p>
                                                        %s
                                                    </p>
                                                    <p class="display-4" style="font-size: 28px">Rent price :</p>
                                                    <p>
                                                        <b>%s onwards</b>
                                                    </p>
                                                    <button type="button" class="btn btn-primary" data-toggle="modal"
                                                        data-target="#property%s">
                                                        View Details...
                                                    </button>

                                                    <!-- Modal -->
                                                      <div class="modal fade" id="property%s" role="dialog">
                                                        <div class="modal-dialog">
                                                          <!-- Modal content-->
                                                          <div class="modal-content">
                                                            <div class="modal-header">
                                                              <h5 class="modal-title" id="exampleModalLabel">
                                                                Property details
                                                              </h5>
                                                              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                                                <span aria-hidden="true">&times;</span>
                                                              </button>
                                                            </div>
                                                            <div class="modal-body">
                                                              <p style="font-size: 20px" class="text-secondary">
                                                                <b>House Owner Name : %s</b>
                                                                <b>House Owner Mobile : %s</b> <br>
                                                                <b>House Owner Email : %s</b> <br>
                                                              </p>
                                                              <br />

                                                              <form method = "post" enctype="multipart/form-data">
                                                                <div style = "display:none">
                                                                  <input type = "text" name = "pid" value = %s >
                                                                  <input type = "text" name = "propertyName" value = "%s" >
                                                                  <input type = "text" name = "ownername" value = "%s" >
                                                                  <input type = "number" name = "mobile" value = "%s" >
                                                                  <input type = "text" name = "propertyType" value = "%s" >
                                                                  <input type = "text" name = "email" value = "%s" >
                                                                  <input type = "text" name = "plotno" value = "%s" >
                                                                  <input type = "text" name = "availableBhk" value = "%s" >
                                                                  <input type = "text" name = "state" value = "%s" >
                                                                  <input type = "text" name = "city" value = "%s" >
                                                                  <input type = "number" name = "pincode" value = "%s" >
                                                                  <input type = "number" name = "rent" value = "%s" >
                                                                  <input type = "number" name = "deposit" value = "%s" >
                                                                  <input type = "text" name = "facilities" value = "%s" >
                                                                  <input type = "text" name = "description" value = "%s" >
                                                                  <input type = "text" name = "landmark" value = "%s" >
                                                                  <input type = "text" name = "address" value = "%s" >
                                                                  <input type = "text" name = "vacancies" value = "%s" >
                                                                  <input type = "text" name = "pimage" value = "%s" >
                                                                  <input type = "text" name = "pimage2" value = "%s" >
                                                                  <input type = "text" name = "pimage3" value = "%s" >
                                                                </div>
                                                                  <p>Address : %s</p>
                                                                  <p>Land Mark : %s</p>
                                                                  <p>State : %s</p>
                                                                  <p>City : %s</p>
                                                                  <p>
                                                                    PinCode : %s
                                                                  </p>
                                                                  <br />
                                                                  <table class="table">
                                                                    <tr>
                                                                      <th>Rent/ Month</th>
                                                                      <th>Deposit</th>
                                                                      <th>BHK</th>
                                                                    </tr>
                                                                    <tr>
                                                                      <td>+ %s</td>
                                                                      <td>%s</td>
                                                                      <td>%s</td>
                                                                    </tr>
                                                                  </table>
                                                                  <br />
                                                                  <p>
                                                                    <b>Facilities :</b><span class="batch bg-dark text-light" style="
                                                                                                    border-radius: 5px;
                                                                                                    padding: 2px;
                                                                                                    margin-left: 3px;
                                                                                                  ">%s</span>
                                                                                                  <span class="batch bg-dark text-light"
                                                                  </p>

                                                                </div>
                                                                <div class="modal-footer">

                                                                  <button type="submit" class="btn btn-primary" name="buy_submit" value="buy_submit">
                                                                    Buy
                                                                  </button>
                                                             </form>
                                                              <button type="button" class="btn btn-outline-primary" data-dismiss="modal">
                                                                Close
                                                              </button>
                                                            </div>
                                                          </div>
                                                        </div>
                                                      </div>
                                                    </div>
                                                </div>
                                            </div>

        """ % (fn, fn1, fn2, i[1], i[16], i[11], i[0], i[0], i[2], i[3], i[5], i[0], i[1], i[2], i[3], i[4], i[5], i[6],
               i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[16],
               i[15], i[8], i[9], i[10], i[11], i[12], i[7], i[13]))

else:
    for i in allrecord:
        fn = "dbdoc/" + i[18]
        fn1 = "dbdoc/" + i[19]
        fn2 = "dbdoc/" + i[20]
        print("""


                                    <div class="col-lg-6 col-xl-4 col-md-12 d-flex justify-content-around">

                                        <div class="card mb-md-5" style="
                                                          background-image: linear-gradient(
                                                            to right top,
                                                            #e5e1da,
                                                            #7fc7d9
                                                          );width: 22rem;margin-top: 20px;
                                                        ">
                                            <div class="card-header" style="height: 270px">
                                                <center>
                                                    <div id="carouselExampleIndicators%s"
                                                        class="carousel slide d-block mb-5 bg-dark" data-ride="carousel"
                                                        style="
                                                                margin-top: 15px;
                                                                padding: 20px;
                                                                padding-bottom: 40px;
                                                                border-radius: 10px;
                                                              ">
                                                        <ol class="carousel-indicators">
                                                            <li data-target="#carouselExampleIndicators%s" data-slide-to="0"
                                                                class="active"></li>
                                                            <li data-target="#carouselExampleIndicators%s" data-slide-to="1">
                                                            </li>
                                                            <li data-target="#carouselExampleIndicators%s" data-slide-to="2">
                                                            </li>
                                                        </ol>
                                                        <div class="carousel-inner col-sm-12">
                                                            <div class="carousel-item active">
                                                                <img class="d-block mx-auto" src="%s" alt="First slide"
                                                                    height="150px" width="180px" />
                                                            </div>
                                                            <div class="carousel-item">
                                                                <img class="d-block mx-auto" src="%s" alt="Second slide"
                                                                    height="150px" width="180px" />
                                                            </div>
                                                            <div class="carousel-item">
                                                                <img class="d-block mx-auto" src="%s" alt="Third slide"
                                                                    height="150px" width="180px" />
                                                            </div>
                                                        </div>
                                                        <a class="carousel-control-prev" href="#carouselExampleIndicators%s"
                                                            role="button" data-slide="prev">
                                                            <span class="carousel-control-prev-icon"
                                                                aria-hidden="true"></span>
                                                            <span class="sr-only">Previous</span>
                                                        </a>
                                                        <a class="carousel-control-next" href="#carouselExampleIndicators%s"
                                                            role="button" data-slide="next">
                                                            <span class="carousel-control-next-icon"
                                                                aria-hidden="true"></span>
                                                            <span class="sr-only">Next</span>
                                                        </a>
                                                    </div>
                                                </center>
                                            </div>

                                            <div class="card-body">
                                                  <p class="display-4" style="font-size: 28px">Property Name</p>
                                                  <p>
                                                    %s
                                                  </p>
                                                <p class="display-4" style="font-size: 28px">Address</p>
                                                <p>
                                                    %s
                                                </p>
                                                <p class="display-4" style="font-size: 28px">Rent price :</p>
                                                <p>
                                                    <b>%s onwards</b>
                                                </p>
                                                <button type="button" class="btn btn-primary" data-toggle="modal"
                                                    data-target="#property%s">
                                                    View Details...
                                                </button>

                                                <!-- Modal -->
                                                  <div class="modal fade" id="property%s" role="dialog">
                                                    <div class="modal-dialog">
                                                      <!-- Modal content-->
                                                      <div class="modal-content">
                                                        <div class="modal-header">
                                                          <h5 class="modal-title" id="exampleModalLabel">
                                                            Property details
                                                          </h5>
                                                          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                                            <span aria-hidden="true">&times;</span>
                                                          </button>
                                                        </div>
                                                        <div class="modal-body">
                                                          <p style="font-size: 20px" class="text-secondary">
                                                            <b>House Owner Name : %s</b>
                                                            <b>House Owner Mobile : %s</b> <br>
                                                            <b>House Owner Email : %s</b> <br>
                                                          </p>
                                                          <br />

                                                          <form method = "post" enctype="multipart/form-data">
                                                            <div style = "display:none">
                                                              <input type = "text" name = "pid" value = %s >
                                                              <input type = "text" name = "propertyName" value = "%s" >
                                                              <input type = "text" name = "ownername" value = "%s" >
                                                              <input type = "number" name = "mobile" value = "%s" >
                                                              <input type = "text" name = "propertyType" value = "%s" >
                                                              <input type = "text" name = "email" value = "%s" >
                                                              <input type = "text" name = "plotno" value = "%s" >
                                                              <input type = "text" name = "availableBhk" value = "%s" >
                                                              <input type = "text" name = "rebhk" value = "%s" >
                                                              <input type = "text" name = "state" value = "%s" >
                                                              <input type = "text" name = "city" value = "%s" >
                                                              <input type = "number" name = "pincode" value = "%s" >
                                                              <input type = "number" name = "rent" value = "%s" >
                                                              <input type = "number" name = "deposit" value = "%s" >
                                                              <input type = "text" name = "facilities" value = "%s" >
                                                              <input type = "text" name = "description" value = "%s" >
                                                              <input type = "text" name = "landmark" value = "%s" >
                                                              <input type = "text" name = "address" value = "%s" >
                                                              <input type = "text" name = "vacancies" value = "%s" >
                                                              <input type = "text" name = "pimage" value = "%s" >
                                                              <input type = "text" name = "pimage2" value = "%s" >
                                                              <input type = "text" name = "pimage3" value = "%s" >
                                                            </div>
                                                              <p>Address : %s</p>
                                                              <p>Land Mark : %s</p>
                                                              <p>State : %s</p>
                                                              <p>City : %s</p>
                                                              <p>
                                                                PinCode : %s
                                                              </p>
                                                              <br />
                                                              <table class="table">
                                                                <tr>
                                                                  <th>Rent/ Month</th>
                                                                  <th>Deposit</th>
                                                                  <th>Total BHK</th>
                                                                  <th>Remaining Bhk</th>
                                                                </tr>
                                                                <tr>
                                                                  <td>+ %s</td>
                                                                  <td>%s</td>
                                                                  <td>%s</td>
                                                                  <td>%s</td>
                                                                </tr>
                                                              </table>
                                                              <br />
                                                              <p>
                                                                <b>Facilities :</b><span class="batch bg-dark text-light" style="
                                                                                                border-radius: 5px;
                                                                                                padding: 2px;
                                                                                                margin-left: 3px;
                                                                                              ">%s</span>
                                                                                              <span class="batch bg-dark text-light"
                                                              </p>

                                                            </div>
                                                            <div class="modal-footer">

                                                              <button type="submit" class="btn btn-primary" name="buy_submit" value="buy_submit">
                                                                Buy
                                                              </button>
                                                         </form>
                                                          <button type="button" class="btn btn-outline-primary" data-dismiss="modal">
                                                            Close
                                                          </button>
                                                        </div>
                                                      </div>
                                                    </div>
                                                  </div>
                                                </div>
                                            </div>
                                        </div>

    """ % (i[0],i[0],i[0],i[0],fn, fn1, fn2,i[0],i[0], i[1], i[16], i[11], i[0], i[0], i[2], i[3], i[5], i[0], i[1], i[2], i[3], i[4], i[5], i[6],
           i[7],i[22], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[16],
           i[15], i[8], i[9], i[10], i[11], i[12], i[7],i[22], i[13]))

print("""                                               



                               
                                    
                                
                            
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
  <script>
    // JavaScript code to handle price range slider
    const priceRange = document.getElementById("priceRange");
    const selectedPrice = document.getElementById("selectedPrice");

    // Event listener for slider changes
    priceRange.addEventListener("input", function () {
      selectedPrice.textContent = priceRange.value;
      // Perform any action based on the selected price (e.g., filter properties)
      // You can add additional logic here based on the selected price range
    });
  </script>
</html>""")




# print(pname,owname,pmobile,ptype,pemail,uemail,plotNo,pavail,pstate,pcity,ppincode,prent,pdeposit,paccommodation,pdescription,plandmark,paddress,pvacancies,pimage,pimage2,pimage3)

buybtn = form.getvalue("buy_submit")
if buybtn != None:
    if len(form) != 0:
        pid = form.getvalue("pid")
        pname = form.getvalue("propertyName")
        owname = form.getvalue("ownername")
        pmobile = form.getvalue("mobile")
        ptype = form.getvalue("propertyType")
        pemail = form.getvalue("email")
        plotNo = form.getvalue("plotno")
        pavail = form.getvalue("availableBhk")
        pstate = form.getvalue("state")
        pcity = form.getvalue("city")
        ppincode = form.getvalue("pincode")
        prent = form.getvalue("rent")
        pdeposit = form.getvalue("deposit")
        paccommodation = form.getvalue("facilities")
        pdescription = form.getvalue("description")
        plandmark = form.getvalue("landmark")
        paddress = form.getvalue("address")
        pvacancies = form.getvalue("vacancies")
        pimage = form.getvalue("pimage")
        pimage2 = form.getvalue("pimage2")
        pimage3 = form.getvalue("pimage3")
        rebhk = form.getvalue("rebhk")

        balancebhk = int(rebhk) - 1

        if balancebhk == 0 :
            q8 = """update property set vacancies = 'occupied' , remaining_bhk = 0 where propertyName = '%s'   """ % pname
            cur.execute(q8)
            q9 = """update purchased_property set vacancies = 'occupied' , remaining_bhk = 0  where propertyName = '%s'""" % pname
            cur.execute(q9)
            con.commit()


        q = """insert into purchased_property (propertyName,ownerName,mobile,propertyType,owner_email,user_email,plotno,availableBhk,state,city,pincode,rent,deposit,facilities,description,landmark,address,vacancies,pimage1,pimage2,pimage3,balance,date,month,uname,umobile,uprofile,remaining_bhk)
        values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""\
            % (pname,owname,pmobile,ptype,pemail,uemail,plotNo,pavail,pstate,pcity,ppincode,prent,pdeposit,paccommodation,pdescription,plandmark,paddress,pvacancies,pimage,pimage2,pimage3,prent,date,month,uname,uphone,uprofile,balancebhk)
        cur.execute(q)

        q1 = """update purchased_property set remaining_bhk = '%s' where propertyName = '%s'""" % ( pname, balancebhk)
        cur.execute(q1)

        q2 = "update property set remaining_bhk = '%s' where propertyName ='%s'" % (balancebhk, pname)
        cur.execute(q2)

        q4 = """update purchased_property set vacancies = 'occupied' where id = '%s'""" % pid
        cur.execute(q4)

        q3 = """insert into payment (uid,propertyType,propertyName,uname,uemail,owname,owemail,rent,date,month,property_status,vacate_status) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','request','occupied')""" % (userid,ptype,pname,uname,uemail,owname,pemail,prent,date,month)
        cur.execute(q3)
        con.commit()
        print("""
        <script>
        alert("Successfully Property Registered to purchased property updated occupied");
        </script>
        """)