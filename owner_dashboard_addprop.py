#!C:/Users/nandh/AppData/Local/Programs/Python/Python311/python.exe
import os

print("content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="user_register")
cur = con.cursor()
form = cgi.FieldStorage()
userid = form.getvalue("id")

q = """select * from ownerregform  where id = '%s'""" % userid
cur.execute(q)
rec = cur.fetchall()

for i in rec:
    fn = "dbdoc/" + i[11]
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
<script>
      const udistrictsInTamilNadu = {
            "Tamil Nadu": ["Ariyalur","Chengalpattu","Chennai","Coimbatore","Cuddalore","Dharmapuri","Dindigul","Erode","Kallakurichi","Kanchipuram",
            "Kanyakumari","Karur","Krishnagiri","Madurai","Mayiladuthurai","Nagapattinam","Namakkal","Nilgiris","Perambalur","Pudukkottai","Ramanathapuram",
            "Ranipet","Salem","Sivaganga","Tenkasi","Thanjavur","Theni","Thoothukudi","Tiruchirappalli", "Tirunelveli","Tirupathur", "Tiruppur","Tiruvallur", "Tiruvannamalai", "Tiruvarur", "Vellore",
            "Viluppuram","Virudhunagar"]
            // Add more districts in Tamil Nadu as needed
        };

        const utaluksInDistricts = {
            "Chennai": ["Alandur", "Egmore", "Mylapore", "Saidapet"],
            "Coimbatore": ["Coimbatore North", "Coimbatore South", "Sulur"]
            // Add more taluks for each district as needed
        };

        function upopulateDistricts() {
        const stateDropdown = document.getElementById("ustateDropdown");
        const districtDropdown = document.getElementById("udistrictDropdown");
        const selectedState = stateDropdown.value;

        // Clear district and taluk dropdowns when state changes
        districtDropdown.innerHTML = "<option value=''>Select District</option>";
        // document.getElementById("talukDropdown").innerHTML = "<option value=''>Select Taluk</option>";

        if (selectedState === "Tamil Nadu") {
          udistrictsInTamilNadu[selectedState].forEach(district => {
            const option = document.createElement("option");
            option.text = district;
            option.value = district;
            districtDropdown.appendChild(option);
          });
        }
        }

        function upopulateTaluks() {
        const districtDropdown = document.getElementById("districtDropdown");
        // const talukDropdown = document.getElementById("talukDropdown");
        const selectedDistrict = districtDropdown.value;

        // Clear taluk dropdown when district changes
        talukDropdown.innerHTML = "<option value=''>Select Taluk</option>";

        if (utaluksInDistricts[selectedDistrict]) {
          utaluksInDistricts[selectedDistrict].forEach(taluk => {
            const option = document.createElement("option");
            option.text = taluk;
            option.value = taluk;
            talukDropdown.appendChild(option);
          });
        }
        }
</script>
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
        <div class="main">
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
                        <div class="col-sm-12 col-lg-8 col-md-10">

                            <div id="add_prop" style="overflow:hidden;text-wrap:nowrap">
                                <div class="card card-body mt-5">
                                    <h2 class="text-center">Add your Property Here...</h2>
                                    <form action="" method="post" enctype="multipart/form-data">
                                      <div class="row">
                                        <div class="col-md-4">
                                          <div class="form-group">
                                            <label for="fullname">Property Full Name</label>
                                            <input
                                              type="text"
                                              class="form-control"
                                              id="pfullname"
                                              placeholder="Full Name"
                                              name="pfullname"
                                              required
                                            />
                                          </div>
                                        </div>
                                        <div class="col-md-4">
                                          <div class="form-group">
                                            <label for="owname">Owner Name</label>
                                            <input
                                              type="text"
                                              class="form-control"
                                              id="owname"
                                              value = "%s"
                                              name="owname"
                                              required
                                              readonly
                                            />
                                          </div>
                                        </div>
                                        <div class="col-md-4">
                                          <div class="form-group">
                                            <label for="ptype">Property Type</label>
                                              <select class="form-control" name="ptype" id="profession">
                                                <optgroup label="Select Property Type">
                                                  <option value="Apartment">Apartment</option>
                                                  <option value="House">House</option>
                                                  <option value="Pg">Pg Home</option>
                                                </optgroup>
                                              </select>
                                          </div>
                                        </div>
                                      </div>
                
                                      <div class="row">
                                        <div class="col-md-4">
                                          <div class="form-group">
                                            <label for="pemail">Email</label>
                                            <input
                                              type="email"
                                              class="form-control"
                                              id="email"
                                              placeholder="Email"
                                              value = "%s"
                                              name="pemail"
                                              required
                                              readonly
                                            />
                                          </div>
                                        </div>
                                        <div class="col-md-4">
                                          <div class="form-group">
                                            <label for="pmobile">Mobile</label>
                                            <input
                                              type="tel"
                                              class="form-control"
                                              id="Pmobile"
                                              pattern="[6789]\d{9}"
                                              title="10 digit mobile number"
                                              placeholder="10 digit mobile number"
                                              name="pmobile"
                                              required
                                            />
                                          </div>
                                        </div>
                                        <div class="col-md-4">
                                          <div class="form-group">
                                            <label for="pavailable_room">Available Rooms</label>
                                              <select class="form-control" name="pavailable_room" id="available_room">
                                                <optgroup label = "select available BHK">
                                                  <option value="1">1 BHK</option>
                                                  <option value="2">2 BHK</option>
                                                  <option value="3">3 BHK</option>
                                                </optgroup>
                                              </select>
                                          </div>
                                        </div>
                                      </div>
                
                                      <div class="row">

                                        <div class="col-md-4">
                                          <div class="form-group">
                                            <label for="pstate">State</label>
                                              <select id="ustateDropdown" name="pstate" onchange="upopulateDistricts()" class="form-control">
                                                <option value="">Select State</option>
                                                <option value="Tamil Nadu">Tamil Nadu</option>
                                              </select>
                                          </div>
                                        </div>
                                        <div class="col-md-4">
                                          <div class="form-group">
                                            <label for="pcity">City</label>
                                              <select id="udistrictDropdown" name="pcity" onchange="upopulateTaluks()" class="form-control">
                                                <option value="">Select District</option>
                                              </select>
                                          </div>
                                        </div>
                                        <div class="col-md-4">
                                          <div class="form-group">
                                            <label for="ppincode">Pincode</label>
                                            <input
                                              type="number"
                                              class="form-control"
                                              id="pincode"
                                              placeholder="Pincode"
                                              name="ppincode"
                                              required
                                            />
                                          </div>
                                        </div>
                                      </div>
                
                                      <div class="row">
                                        <div class="col-md-4">
                                          <div class="form-group">
                                            <label for="rent">Rent</label>
                                            <input
                                              type="number"
                                              class="form-control"
                                              id="rent"
                                              placeholder="Rent"
                                              name="prent"
                                              required
                                            />
                                          </div>
                                        </div>
                
                                        <div class="col-md-4">
                                          <div class="form-group">
                                            <label for="deposit">Deposit</label>
                                            <input
                                              type="number"
                                              class="form-control"
                                              id="deposit"
                                              placeholder="Deposit"
                                              name="pdeposit"
                                              required
                                            />
                                          </div>
                                        </div>
                                        <div class="col-md-4">
                                          <div class="form-group">
                                            <label for="plot_number"
                                              >Plot Number/Home Number</label
                                            >
                                            <input
                                              type="text"
                                              class="form-control"
                                              id="plot_number"
                                              placeholder="Plot Number/Home Number"
                                              name="plot_number"
                                              required
                                            />
                                          </div>
                                        </div>

                                      </div>
                
                                      <div class="row">
                                        <div class="col-md-4">
                                          <div class="form-group">
                                            <label for="pdescription">Description</label>
                                            <textarea   
                                              class="form-control"
                                              id="description"
                                              placeholder="Description"
                                              name="pdescription"
                                              rows =1
                                            >
                                            </textarea>
                                          </div>
                                        </div>
                                        <div class="col-md-4">
                                          <div class="form-group">
                                            <label for="plandmark">Landmark</label>
                                            <input
                                              type="landmark"
                                              class="form-control"
                                              id="landmark"
                                              placeholder="landmark"
                                              name="plandmark"
                                            />
                                          </div>
                                        </div>
                                        <div class="col-md-4">
                                          <div class="form-group">
                                            <label for="paddress">Address</label>
                                            <textarea   
                                              class="form-control"
                                              id="address"
                                              pattern="[a-zA-Z0-9\s]+"
                                              placeholder="Address"
                                              name="paddress"
                                              rows =1
                                            >
                                            </textarea>
                                          </div>
                                        </div>
                                      </div>
                
                                      <div class="row">
                                        <div class="col-4">
                                          <div class="form-group">
                                            <label for="vacant">Vacant/Occupied</label>
                                            <select
                                              class="form-control"
                                              id="vacant"
                                              name="pvacancies"
                                            >
                                              <option value="vacant">Vacant</option>
                                              <option value="occupied">Occupied</option>
                                            </select>
                                          </div>
                                        </div>

                                        <div class="col-md-4">
                                          <div class="form-group">
                                            <label for="paccommodation">Facilities</label>
                                              <select class="form-control" name="paccommodation" id="accommodation">
                                                <optgroup label = "select Available Facilities">
                                                  <option value="wifi">WiFi</option>
                                                  <option value="food">FOOD</option>
                                                  <option value="wifi_food">WiFi & FOOD</option>
                                                </optgroup>
                                              </select>
                                          </div>
                                        </div>
                                        <div class="col-md-4">
                                          <div class="form-group">
                                            <label for="pimage">Property Image 1</label>
                                            <input type="file" name="pimage" id="image" />
                                          </div>
                                        </div>
                                      </div>
                                      <div class = "row">

                                        <div class="col-md-6">
                                          <div class="form-group">
                                            <label for="pimage2">Property Image 2</label>
                                            <input type="file" name="pimage2" id="image" />
                                          </div>
                                        </div>
                                        <div class="col-md-6">
                                          <div class="form-group">
                                            <label for="pimage3">Property Image 3</label>
                                            <input type="file" name="pimage3" id="image" />
                                          </div>
                                        </div>
                                      </div>
                                      <button
                                        type="submit"
                                        class="btn btn-primary"
                                        name="property_submit"
                                        value="property_submit"
                                      >
                                        Submit
                                      </button>
                                    </form>
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









""" % (userid,userid,userid,userid,userid,userid,userid,userid,userid,i[1],i[3]))

psubmit = form.getvalue("property_submit")

if psubmit != None:
    if len(form) != 0:
        pname = form.getvalue("pfullname")
        owname = form.getvalue("owname")
        pmobile = form.getvalue("pmobile")
        ptype = form.getvalue("ptype")
        pemail = form.getvalue("pemail")
        plotNo = form.getvalue("plot_number")
        pavail = form.getvalue("pavailable_room")
        pstate = form.getvalue("pstate")
        pcity = form.getvalue("pcity")
        ppincode = form.getvalue("ppincode")
        prent = form.getvalue("prent")
        pdeposit = form.getvalue("pdeposit")
        paccommodation = form.getvalue("paccommodation")
        pdescription = form.getvalue("pdescription")
        plandmark = form.getvalue("plandmark")
        paddress = form.getvalue("paddress")
        pvacancies = form.getvalue("pvacancies")
        pimage = form ["pimage"]
        pimage2 = form["pimage2"]
        pimage3 = form["pimage3"]


        if pimage.filename:
            fn = os.path.basename(pimage.filename)
            open("dbdoc/"+fn,"wb").write(pimage.file.read())
            fn1 = os.path.basename(pimage2.filename)
            open("dbdoc/"+fn1,"wb").write(pimage2.file.read())
            fn2 = os.path.basename(pimage3.filename)
            open("dbdoc/"+fn2,"wb").write(pimage3.file.read())

            q = """insert into property (propertyName,ownerName,mobile,propertyType,email,plotNo,availableBhk,state,city,pincode,rent,deposit,facilities,description,landmark,address,vacancies,pimage,pimage2,pimage3,remaining_bhk) 
                values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""%(pname,owname,pmobile,ptype,pemail,plotNo,pavail,pstate,pcity,ppincode,prent,pdeposit,paccommodation,pdescription,plandmark,paddress,pvacancies,fn,fn1,fn2,pavail)
            cur.execute(q)
            con.commit()
            print("""
            <script>
            alert("Successfully Property Registered")
            </script>
            """)

