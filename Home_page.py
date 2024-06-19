#!C:/Users/nandh/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql,os, smtplib, math
import string
import random
cgitb.enable()
con= pymysql.connect(host="localhost", user="root", password="", database="user_register")
cur = con.cursor()

print(
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>House & Apartment Leasing and Maintenance</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css">
    <script src="https://cdn.jsdelivr.net/npm/jquery@3.7.1/dist/jquery.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <style>
      *{
        font-family:system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
      }
      ::selection{
        background-color: black;
        color: white;
      }
      body{
        background-color: #DCF2F1;
      }

        #img-tog{
          border-radius: 20px;
          transition-delay: 2s;
          transition: linear 3s;
          display: flex;
          justify-content: space-between;
        }
        .card{
          box-shadow: 1px 1px 7px 1px black;
          transition:0.5s;

        }
        .card:hover{
          
          transform: scale(0.97);
          
        }
        nav{
          border-radius: 6px;
        }


    </style>
    
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
<script>
  const odistrictsInTamilNadu = {
        "Tamil Nadu": ["Ariyalur","Chengalpattu","Chennai","Coimbatore","Cuddalore","Dharmapuri","Dindigul","Erode","Kallakurichi","Kanchipuram",
        "Kanyakumari","Karur","Krishnagiri","Madurai","Mayiladuthurai","Nagapattinam","Namakkal","Nilgiris","Perambalur","Pudukkottai","Ramanathapuram",
        "Ranipet","Salem","Sivaganga","Tenkasi","Thanjavur","Theni","Thoothukudi","Tiruchirappalli", "Tirunelveli","Tirupathur", "Tiruppur","Tiruvallur", "Tiruvannamalai", "Tiruvarur", "Vellore",
        "Viluppuram","Virudhunagar"]
        // Add more districts in Tamil Nadu as needed
    };

    const otaluksInDistricts = {
        "Chennai": ["Alandur", "Egmore", "Mylapore", "Saidapet"],
        "Coimbatore": ["Coimbatore North", "Coimbatore South", "Sulur"]
        // Add more taluks for each district as needed
    };

    function opopulateDistricts() {
    const stateDropdown = document.getElementById("ostateDropdown");
    const districtDropdown = document.getElementById("odistrictDropdown");
    const selectedState = stateDropdown.value;

    // Clear district and taluk dropdowns when state changes
    districtDropdown.innerHTML = "<option value=''>Select District</option>";
    // document.getElementById("talukDropdown").innerHTML = "<option value=''>Select Taluk</option>";

    if (selectedState === "Tamil Nadu") {
      odistrictsInTamilNadu[selectedState].forEach(district => {
        const option = document.createElement("option");
        option.text = district;
        option.value = district;
        districtDropdown.appendChild(option);
      });
    }
    }

    function opopulateTaluks() {
    const districtDropdown = document.getElementById("odistrictDropdown");
    // const talukDropdown = document.getElementById("talukDropdown");
    const selectedDistrict = districtDropdown.value;

    // Clear taluk dropdown when district changes
    talukDropdown.innerHTML = "<option value=''>Select Taluk</option>";

    if (otaluksInDistricts[selectedDistrict]) {
      otaluksInDistricts[selectedDistrict].forEach(taluk => {
        const option = document.createElement("option");
        option.text = taluk;
        option.value = taluk;
        talukDropdown.appendChild(option);
      });
    }
    }
</script>


</head>
<body>

  <div class="container-fluid ">

    <img src="./media/logo bg.png" alt="Logo Of this website" height="150px" width="200px"  class="mx-auto d-block" style="border-radius:15px;margin: 7px 7px 7px 7px;">
        <header>
         
          <nav class="navbar navbar-expand-lg navbar-dark" style="background-color:#0F1035;padding: 10px;">
              <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
              </button>
            
              <div class="collapse navbar-collapse my-2 " id="navbarSupportedContent">
                <ul class="navbar-nav mr-auto " >
                  <li class="nav-item active">
                    <a class="nav-link" href="Home_page.py">Home <span class="sr-only">(current)</span></a>
                  </li>

                  <li class="nav-item">
                    <a class="nav-link" href="apartments.py">Apartment</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" href="houses.py">House</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" href="pg_home.py">PG Home</a>
                  </li>
                </ul>
                <ul class="form-inline my-lg-2  my-sm-0 ">
                  <li class="nav-item">
                    <div class="dropdown " >
                      <a class="text-light dropdown-toggle my-2 my-sm-0 nav-link" style="margin-left: -49px;text-decoration: none;"  data-toggle="dropdown"> <i class="fa fa-user-plus"></i> Register</a>
                      <ul class="dropdown-menu">
                          <li>
                            <button type="button" class="btn btn-light" data-toggle="modal" data-target="#ownerRegMod">
                              Owner Register
                            </button>
                          </li>
                          <li>
                            <button type="button" class="btn btn-light" data-toggle="modal" data-target="#userRegMod">
                              User Register
                            </button>
                          </li>
                      </ul>
                    </div>
                  </li>
                  <li class="nav-item">
                    <div class="dropdown ">
                      <a   class="text-light dropdown-toggle my-2 my-sm-0 nav-link" style="margin-left: 8px;text-decoration: none;"   data-toggle="dropdown"> <i class="fa fa-user-o"></i> Login</a>
                      <ul class="dropdown-menu ">
                          <li>
                            <button type="button" class="btn btn-light" data-toggle="modal" data-target="#adminLogMod">
                              Admin Login
                            </button>
                          </li>
                          <li>
                            <button type="button" class="btn btn-light" data-toggle="modal" data-target="#userLogMod">
                              User login
                            </button>
                          </li>
                          <li>
                            <button type="button" class="btn btn-light" data-toggle="modal" data-target="#ownerLogMod">
                              Owner Login
                            </button>
                          </li>
                      </ul>
                    </div>
                  </li>
                </ul>
                  
                

                  <!-- Modal -->
                  <div class="modal fade" id="ownerRegMod" tabindex="-1" aria-labelledby="OwnerRegisterModal" aria-hidden="true">
                    <div class="modal-dialog">
                      <div class="modal-content" style="background-image: linear-gradient(to bottom right,#365486,#7FC7D9);color: white;">
                        <div class="modal-header">
                          <h5 class="modal-title" id="exampleModalLabel">Owner Register Form</h5>
                          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                          </button>
                        </div>
                        <div class="modal-body text-left">
                           <form method="post" enctype="multipart/form-data" name="o_reg_form">
                            <div class="form-group input-group">
                              <div class="input-group-prepend">
                                <span class="input-group-text" id="basic-addon1"><i class="fa fa-user-o" aria-hidden="true"></i></span>
                              </div>
                              <input
                                type="text"
                                name="oname"
                                class="form-control"
                                id="oname"
                                placeholder="Enter Your Name...."
                                required
                              /><br />
                            </div>
 
                
                            <div class="form-group input-group">
                              <div class="input-group-prepend">
                                <span class="input-group-text" id="basic-addon1"><i class="fa fa-phone-square" aria-hidden="true"></i></span>
                              </div>
                              <input
                                type="tel"
                                name="ophone"
                                class="form-control"
                                id="OPhone"
                                placeholder="Enter Mobile No...."
                                required
                                pattern="[6789]\d{9}"
                                maxlength="10"
                              /><br />
                            </div>
                
                            <div class="form-group input-group">
                              <div class="input-group-prepend">
                                <span class="input-group-text" id="basic-addon1"><i class="fa fa-envelope" aria-hidden="true"></i></span>
                              </div>
                              <input
                                type="oemail"
                                name="oemail"
                                class="form-control"
                                id="oemail"
                                placeholder="Enter Your Email Id...."
                                pattern="[a-z0-9._%+\-]+@[a-z0-9.\-]+\.[a-z]{2,}$"
                                required
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
                                id="ODob"
                                required
                              /><br />
                            </div>
                            <div class="form-group input-group">
                              <label for="ogender">GENDER</label>&nbsp;&nbsp;&nbsp;
                              <input type="radio" name="ogender" value="male" required />&nbsp;
                              <label for="ogender">MALE</label>&nbsp;
                              <input type="radio" name="ogender" value="female" required />&nbsp;<label
                                >FEMALE</label
                              >
                            </div>
                            <div class="form-group input-group">
                              <div class="input-group-prepend">
                                <span class="input-group-text" id="basic-addon1"><i class="fa fa-address-card-o" aria-hidden="true"></i></span>
                              </div>
                              <textarea
                                rows="1"
                                cols="15"
                                class="form-control"
                                id="OAddress"
                                name="oaddress"
                                pattern="[a-zA-Z0-9\s]+"
                                placeholder="Enter Your Address..."
                              ></textarea
                              ><br />
                            </div>
                            <div class="form-group input-group">
                              <div class="input-group-prepend">
                                <span class="input-group-text" id="basic-addon1"><i class="fa fa-location-arrow" aria-hidden="true"></i></span>
                              </div>
                              <input
                                type="number"
                                id="opincode"
                                class="form-control"
                                name="opincode"
                                placeholder="Enter Your Pincode Here...."
                                maxlength="7"
                                required
                              /><br />
                            </div>
                            <div class="form-group input-group">
                              <div class="input-group-prepend">
                                <span class="input-group-text" id="basic-addon1"><i class="fa fa-map-marker" aria-hidden="true"></i></span>
                              </div>
                              <select
                                id="ostateDropdown"
                                name="ostate"
                                onchange="opopulateDistricts()"
                                class="form-control"
                              >
                                <option value="">Select State</option>
                                <option value="Tamil Nadu">Tamil Nadu</option></select
                              ><br />
                            </div>
                            <div class="form-group input-group">
                              <div class="input-group-prepend">
                                <span class="input-group-text" id="basic-addon1"><i class="fa fa-map-marker" aria-hidden="true"></i></span>
                              </div>
                              <select
                                id="odistrictDropdown"
                                name="ocity"
                                onchange="opopulateTaluks()"
                                class="form-control"
                              >
                                <br />
                                <option value="">Select District</option>
                              </select>
                            </div>
    
                            <div class="form-group input-group">
                              <div class="input-group-prepend">
                                <span class="input-group-text" id="basic-addon1"><i class="fa fa-picture-o" aria-hidden="true"></i></span>
                                <span class="input-group-text" id="basic-addon2">Upload Your profile</span>
                              </div>
                              <input
                                class="form-control"
                                type="file"
                                name="ophoto"
                                id="oPhoto"
                                placeholder="Upload Your Profile"
                                required 
                              />
                            </div>

                            <div class="form-group input-group">
                              <div class="input-group-prepend">
                                <span class="input-group-text" id="basic-addon1"><i class="fa fa-id-card" aria-hidden="true"></i></span>
                                <span class="input-group-text" id="basic-addon2">Upload Identity Proof</span>
                              </div>
                              <input
                                class="form-control"
                                type="file"
                                name="oidentity"
                                id="oIdentity" placeholder="Upload Identity Document"
                                required
                              /><br />
                            </div>
                            <div class="form-group input-group">
                              <div class="input-group-prepend">
                                <span class="input-group-text" id="basic-addon1"><i class="fa fa-unlock-alt" aria-hidden="true"></i></span>
                              </div>
                              <select name="o_ptype"   class="form-control">
                                <optgroup label="PROPERTY TYPE">
                                    <option value="apartment">Apartment</option>                    
                                    <option value="house">House</option>                    
                                    <option value="pg">PG</option>                                       
                                </optgroup>
                              </select>
                            </div>
                            <div class="form-group input-group">
                              <div class="input-group-prepend">
                                <span class="input-group-text" id="basic-addon1"><i class="fa fa-unlock-alt" aria-hidden="true"></i></span>
                              </div>
                              <input type="text" id="location"  class="form-control" name="o_plocation" placeholder="Enter Location of the property..."><br>
                            </div>
                            <div class="form-group input-group">
                              <div class="input-group-prepend">
                                <span class="input-group-text" id="basic-addon1"><i class="fa fa-id-card" aria-hidden="true"></i></span>
                                <span class="input-group-text" id="basic-addon2">Upload Property Document</span>
                              </div>
                              <input type="file"  class="form-control" name="o_prop_doc" id="prop_doc"  required><br>
                            </div>
                            <div class="modal-footer">
                              <button type="submit"class="btn btn-primary" name="osubmit">SUBMIT</button>
                              <button type="button" class="btn btn-secondary" data-dismiss="modal">CANCEL</button>
                            </div>

                          </form>
                        </div>

                      </div>
                    </div>
                  </div>
                  <div class="modal fade" id="userRegMod" role="dialog" >
                    <div class="modal-dialog" >
                    
                      <!-- Modal content-->
                      <div class="modal-content" style="background-image: linear-gradient(to bottom right,#365486,#7FC7D9);color: white;">
                        <div class="modal-header">
                          <h5 class="modal-title" id="exampleModalLabel">User Register Form</h5>
                          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                          </button>
                        </div>
                        <div class="modal-body text-left">
                             <form method="post" enctype="multipart/form-data" name="u_reg_form">
                                <div class="form-group input-group">
                                  <div class = "input-group-prepend">
                                    <span class="input-group-text" id="basic-addon1"><i class="fa fa-user-o" aria-hidden="true"></i></span>
                                  </div>
                                  <input
                                    type="text"
                                    name="uname"
                                    class="form-control"
                                    id="name"
                                    placeholder="Enter Your Name...."
                                    required
                                  /><br />
                                </div>
                                <div class="form-group">
                                  <label for="ugender">GENDER</label>
                                  <input type="radio" name="ugender" value="male" required />
                                  <label for="ugender">MALE</label>
                                  <input type="radio" name="ugender" value="female" required /><label
                                    >FEMALE</label
                                  >
                                </div>
                    
                                <div class="form-group input-group">
                                  <div class = "input-group-prepend">
                                    <span class="input-group-text" id="basic-addon1"><i class="fa fa-phone-square" aria-hidden="true"></i></span>
                                  </div>
                                  <input
                                    type="tel"
                                    name="uphone"
                                    class="form-control"
                                    id="Phone"
                                    placeholder="Enter Mobile No...."
                                    required
                                    pattern="[6789]\d{9}"
                                    maxlength="10"
                                  /><br />
                                </div>
                    
                                <div class="form-group input-group">
                                  <div class = "input-group-prepend">
                                    <span class="input-group-text" id="basic-addon1"><i class="fa fa-envelope" aria-hidden="true"></i></span>
                                  </div>
                                  <input
                                    type="email"
                                    name="uemail"
                                    class="form-control"
                                    id="lname"
                                    placeholder="Enter Your Email Id...."
                                    pattern="[a-z0-9._%+\-]+@[a-z0-9.\-]+\.[a-z]{2,}$"
                                    required
                                  /><br />
                                </div>
                                <div class="form-group input-group">
                                  <div class = "input-group-prepend">
                                    <span class="input-group-text" id="basic-addon1"><i class="fa fa-calendar" aria-hidden="true"></i></span>
                                  </div>
                                  <input
                                    type="date"
                                    name="udob"
                                    class="form-control"
                                    id="Dob"
                                    required
                                  /><br />
                                </div>
                                <div class="form-group input-group">
                                  <div class = "input-group-prepend">
                                    <span class="input-group-text" id="basic-addon1"><i class="fa fa-address-card-o" aria-hidden="true"></i></span>
                                  </div>
                                  <textarea
                                    rows="1"
                                    cols="15"
                                    class="form-control"
                                    id="Address"
                                    name="uaddress"
                                    pattern="[a-zA-Z0-9\s]+"
                                    placeholder="Enter Your Address..."
                                  ></textarea
                                  ><br />
                                </div>
                                <div class="form-group input-group">
                                  <div class = "input-group-prepend">
                                    <span class="input-group-text" id="basic-addon1"><i class="fa fa-location-arrow" aria-hidden="true"></i></span>
                                  </div>
                                  <input
                                    type="number"
                                    id="pincode"
                                    class="form-control"
                                    name="upincode"
                                    placeholder="Enter Your Pincode Here...."
                                    maxlength="7"
                                    required
                                  /><br />
                                </div>
                                <div class="form-group input-group">
                                  <div class = "input-group-prepend">
                                    <span class="input-group-text" id="basic-addon1"><i class="fa fa-location-arrow" aria-hidden="true"></i></span>
                                  </div>
                                  <select id="ustateDropdown" name="ustate" onchange="upopulateDistricts()" class="form-control">
                                    <option value="">Select State</option>
                                    <option value="Tamil Nadu">Tamil Nadu</option>
                                  </select>
                                </div>
                                <div class="form-group input-group">
                                  <div class = "input-group-prepend">
                                    <span class="input-group-text" id="basic-addon1"><i class="fa fa-location-arrow" aria-hidden="true"></i></span>
                                  </div>
                                  <select id="udistrictDropdown" name="ucity" onchange="upopulateTaluks()" class="form-control">
                                    <option value="">Select District</option>
                                  </select>
                                </div>
                                <div class="form-group input-group">
                                  <div class = "input-group-prepend">
                                    <span class="input-group-text" id="basic-addon1"><i class="fa fa-location-arrow" aria-hidden="true"></i></span>
                                  </div>
                                  <select class="form-control" name="uprofession" id="profession">
                                    <optgroup label="profession">
                                      <option value="Doctor">Doctor</option>
                                      <option value="Engineer">Engineer</option>
                                      <option value="Lawyer">Lawyer</option>
                                      <option value="Bussiness">Business</option>
                                    </optgroup></select
                                  ><br />
                                </div>
                                <div class="form-group input-group">
                                  <div class = "input-group-prepend">
                                    <span class="input-group-text" id="basic-addon1"><i class="fa fa-location-arrow" aria-hidden="true"></i></span>
                                  </div>
                                  <input class="form-control" type="file" name="uphoto" required/>
                                </div>
                                <div class="form-group">
                                  <label for="gender">MARRIED STATUS :</label>
                                  <input type="radio" id="m1" name="umarried" value="married" required/>
                                  <label>Married</label>
                                  <input
                                    type="radio"
                                    id="m2"
                                    value="unmarried"
                                    name="umarried"
                                    required
                                  /><label>Un Married</label><br />
                                </div>
                                <div class="form-group input-group">
                                  <div class = "input-group-prepend">
                                    <span class="input-group-text" id="basic-addon1"><i class="fa fa-location-arrow" aria-hidden="true"></i></span>
                                  </div>
                                  <input class="form-control" type="file" value="identity" name="uidentity" id="Identity" required/>
                                </div>
                                <div class="form-group input-group">
                                  <div class = "input-group-prepend">
                                    <span class="input-group-text" id="basic-addon1"><i class="fa fa-unlock-alt" aria-hidden="true"></i></span>
                                  </div>
                                  <input
                                    class="form-control"
                                    type="password"
                                    id="pass"
                                    name="upass"
                                    placeholder="Enter password Here...."
                                  /><br />
                                </div>
                                <div class="form-group">
                                  <input
                                    type="submit"
                                    value="SUBMIT"
                                    name="usubmit"
                                    class="btn btn-primary"
                                  />
                                  <button type="button" class="btn btn-secondary" data-dismiss="modal">CANCEL</button>
                                </div>
                                
                              </form>
                        </div>
                      </div>
                      
                    </div>
                  </div>


                  <div class="modal fade text-left" id="adminLogMod" role="dialog">
                    <div class="modal-dialog">
                    
                      <!-- Modal content-->
                      <div class="modal-content" style="background-image: linear-gradient(to bottom right,#365486,#7FC7D9);color: white;">
                        <div class="modal-header">
                          <h5 class="modal-title" id="exampleModalLabel">Admin Login Form</h5>
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
                              <input type="text" name="A_uname" class="form-control" id="AUname" aria-label="Username" placeholder="Enter User Name...."  autofocus>
                            </div>
                            <div class="input-group mb-3">
                              <div class="input-group-prepend">
                                <span class="input-group-text" id="basic-addon1"><i class="fa fa-key" aria-hidden="true"></i></span>
                              </div>
                              <input type="password" name="A_pass" class="form-control" id="APass" aria-label="password" placeholder="Enter Password....">
                            </div>

                            <input type="submit" class="btn btn-primary my-3" name="a_log"  value="SUBMIT">
                            <button type="button" class="btn btn-outline-dark" data-dismiss="modal">CANCEL</button>
                          </form>
                        </div>
                      </div>
                      
                    </div>
                  </div>

                  <div class="modal fade text-left" id="userLogMod" role="dialog">
                    <div class="modal-dialog">
                      <!-- Modal content-->
                      <div class="modal-content " style="background-image: linear-gradient(to bottom right,#365486,#7FC7D9);color: white;">
                        <div class="modal-header">
                          <h5 class="modal-title" id="exampleModalLabel">User Login Form</h5>
                          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                          </button>
                        </div>
                        <div class="modal-body">
                          <form method="post" enctype="multipart/form-data" name="Ulogin">
                            <div class="input-group mb-3">
                              <div class="input-group-prepend">
                                <span class="input-group-text" id="basic-addon1"><i class="fa fa-user-o" aria-hidden="true"></i></span>
                              </div>
                              <input type="text" name="U_uname" class="form-control" id="AUname" placeholder="Enter User Name...."  autofocus><br>
                            </div>
                            <div class="input-group mb-3">
                              <div class="input-group-prepend">
                                <span class="input-group-text" id="basic-addon1"><i class="fa fa-key" aria-hidden="true"></i></span>
                              </div>
                              <input type="password" name="U_pass" class="form-control" id="APass" placeholder="Enter password...." ><br>
                            </div>
                            <a href="check_forgot.py" class="float-right text-reset" >Forgot Password ?</a>
                            <input type="submit" class="btn btn-primary my-3" name="U_submit"   value="SUBMIT">
                            <button type="button" class="btn btn-outline-dark" data-dismiss="modal">CANCEL</button>
                          </form>
                        </div>
                      </div>
                      
                    </div>
                  </div>
                  <div class="modal fade text-left" id="forgot_email" role="dialog">
                    <div class="modal-dialog">
                      <div class="modal-content"
                        style="background-image: linear-gradient(to bottom right,#365486,#7FC7D9);color: white;">
                        <div class="modal-header">
                          <h5 class="modal-title" id="exampleModalLabel">
                            Change Password Here...
                          </h5>
                          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                          </button>
                        </div>
                        <div class="modal-body">
                          <form method="post" enctype="multipart/form-data">
                            <input type="email" name="forgot_email" placeholder="Enter Your Email...." class="form-control">
                            <input type="submit" class="btn btn-primary" name="forgot_submit" id="forgot_submit">
                          </form>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="modal fade text-left" id="ownerLogMod" role="dialog">
                    <div class="modal-dialog">
                      <!-- Modal content-->
                      <div class="modal-content" style="background-image: linear-gradient(to bottom right,#365486,#7FC7D9);color: white;">
                        <div class="modal-header">
                          <h5 class="modal-title" id="exampleModalLabel">Owner Login Form</h5>
                          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                          </button>
                        </div>
                        <div class="modal-body">
                          <form enctype="multipart/form-data" name="Ologin" method="post">
                            <div class="input-group mb-3">
                              <div class="input-group-prepend">
                                <span class="input-group-text" id="basic-addon1"><i class="fa fa-user-o" aria-hidden="true"></i></span>
                              </div>
                              <input type="text" name="O_uname" class="form-control" id="AUname" placeholder="Enter User Name...."  autofocus><br>
                            </div>
                            <div class="input-group mb-3">
                              <div class="input-group-prepend">
                                <span class="input-group-text" id="basic-addon1"><i class="fa fa-key" aria-hidden="true"></i></span>
                              </div>
                              <input type="password" name="O_pass" class="form-control" id="APass" placeholder="Enter password...." >
                            </div>
                            <a href="check_email_owner.py" class="float-right text-reset" >Forgot Password ?</a>
                            <input type="submit" name="O_submit"class="btn btn-primary my-3"   value="SUBMIT">
                            <button type="button" class="btn btn-outline-dark" class="d-flex float-right" data-dismiss="modal">CANCEL</button>
                          </form>
                      </div>
                      
                    </div>
                  </div>
              </div>
          </nav>
        </header>

        <section>
          <div class="row">
            
            <div class="col-lg-6 col-sm-12">
              <div class="img-responsive img-fluid">
                <img name="images" width="380px" height="380px" class="p-3 img-fluid mx-auto d-block " id="img-tog">
              </div>

              
            </div>
            <div class="col-lg-5 col-sm-12 d-flex justify-content-center">
              <div class="card my-5 " style="background-image: linear-gradient(to bottom right, #7FC7D9,#365486);">
                <div class="card-head">
                  <p class="display-4 text-center ">Choose your Dream Home with us.....</p>
                  <div class="card-body">
                    <p class="text-light text-justify">Home is a safe haven and a comfort zone. A place to live with our families and pets and enjoy with friends. A place to build memories as well as a way to build future wealth. A place where we can truly just be ourselves.</p>
                  </div>
                </div>
              </div>
              
             
            </div>
          </div>

          <center>

            <div class="alert" id="apartment" style="background-image: linear-gradient(to bottom right,#365486,black);">
              <p class="display-5 lead text-left text-light "><i class="fa fa-house"></i> Explore All Apartments.... <a href="apartments.py" class="alert-link" style="color: white;">More</a></p>
            </div>
            <div class="container-fluid">
              <div class="row mb-3 " >
                <div class="col-lg-4 col-md-6 my-sm-2">
                  <div class="card bg-light mr-lg-0" style="width:23rem;background-image: linear-gradient(to right top,#E5E1DA,#7FC7D9);" >
                    <img src="./media/apartment2.jpg" alt="Apartment 1" class="card-img-top w-100" width="150px" height="200px">
                    <div class="card-body">
                      <h5 class="card-title">
                        1 BHK Apartments
                        <span class="badge badge-primary badge-pill"
                          >Most booked !</span
                        >
                      </h5>
                      <p class="card-text">
                        <span class="badge badge-success badge-pill"
                          ><i class="fa fa-child" aria-hidden="true"></i> Park</span
                        >
                        <span class="badge badge-warning badge-pill"
                          ><i class="fa fa-life-ring" aria-hidden="true"></i>
                          Swiming</span
                        >
                      </p>
                      <p class="card-text text-justify">
                        In a 1 bhk apartment, the full form is 1 Bedroom, Hall and Kitchen.
                        New ! BHK apartments available for low budject  Hospitals and
                        Schools are nearby.
                      </p>
                      <p class="card-text text-muted float-right">
                        <i class="fa fa-clock-o"></i> Last Updated 20 days ago...
                      </p>
                      <div class="clearfix"></div>
    
                      <a href="#!" data-toggle="modal" data-target="#userLogMod" class="btn btn-dark btn-block"
                        ><i class="fa fa-building" aria-hidden="true"></i> Book
                        Now</a
                      >
                    </div>
                  </div>
                </div>

                <div class="col-lg-4 col-md-6 my-sm-2 " >
                  <div class="card bg-light ml-lg-2" style="width: 23rem;background-image: linear-gradient(to right top,#E5E1DA,#7FC7D9);" >
                    <img src="./media/apartment1.png" alt="Apartment 1" class="card-img-top" width="150px" height="200px">
                    <div class="card-body">
                      <h5 class="card-title">
                        2 BHK Apartments
                      </h5>
                      <p class="card-text">
                        <span class="badge badge-light badge-pill"
                          ><i class="fa fa-arrows-h" aria-hidden="true"></i> spacious</span
                        >
                        <span class="badge badge-danger badge-pill"
                          ><i class="fa fa-heart-o" aria-hidden="true"></i>
                          Smart</span
                        >
                      </p>
                      <p class="card-text text-justify">
                        In 2bhk means 2 Bedrooms, Hall and Kitchen.While all of these properties have bath and toilet space and more spacious then the 1 BHK its has more features.
                      </p>
                      <p class="card-text text-muted float-right">
                        <i class="fa fa-clock-o"></i> Last Updated 10 days ago...
                      </p>
                      <div class="clearfix"></div>
    
                      <a href="#!"  data-toggle="modal" data-target="#userLogMod" class="btn btn-dark btn-block"
                        ><i class="fa fa-building" aria-hidden="true"></i> Book
                        Now</a
                      >
                    </div>
                  </div>
                </div>
                <div class="col-lg-4 col-md-6 my-sm-2">
                  <div class="card bg-light ml-lg-3" style="width: 23rem;background-image: linear-gradient(to right top,#E5E1DA,#7FC7D9);" ">
                    <img src="./media/apartment3.jpg" alt="Apartment 1" class="card-img-top" width="150px" height="200px">
                    <div class="card-body">
                      <h5 class="card-title">
                        3 BHK Apartments
                        <span class="badge badge-primary badge-pill"
                          >New Update !</span
                        >
                      </h5>
                      <p class="card-text">
                        <span class="badge badge-dark badge-pill"
                          ><i class="fa fa-cubes" aria-hidden="true"></i> Futuristic</span
                        >
                        <span class="badge badge-info badge-pill"
                          ><i class="fa fa-users" aria-hidden="true"></i> Wide Common Area. ...</span
                        >
                      </p>
                      <p class="card-text text-justify">
                        In 3BHK, the full form is 3 Bedrooms, Hall and Kitchen. While all of these properties have bath and toilet space, Most suitable for large families.
                      </p>
                      <p class="card-text text-muted float-right">
                        <i class="fa fa-clock-o"></i> Last Updated 5 Min ago...
                      </p>
                      <div class="clearfix"></div>
    
                      <a href="#!"  data-toggle="modal" data-target="#userLogMod"class="btn btn-dark btn-block"
                        ><i class="fa fa-building" aria-hidden="true"></i> Book
                        Now</a
                      >
                    </div>
                  </div>
                </div>

              </div>
            </div>
            <div class="alert alert-info" id="house"  style="background-image: linear-gradient(to bottom right,#365486,black);">
              <p class="display-5 lead text-left text-light ">  Explore All houses .... <a href="houses.py" class="alert-link" style="color: white;">More</a></p>
            </div>
            <div class="container-fluid">
              <div class="row  mb-3 my-sm-2">
                
                <div class="col-lg-4 col-md-6 my-sm-2">
                  <div class="card bg-light ml-lg-3" style="width: 23rem;background-image: linear-gradient(to right top,#E5E1DA,#7FC7D9);" >
                    <img src="./media/house1.png" alt="Apartment 1" class="card-img-top" width="150px" height="200px">
                    <div class="card-body">
                      <h5 class="card-title">
                        For Families...
                      </h5>
                      <p class="card-text">
                        <span class="badge badge-dark badge-pill"
                          ><i class="fa fa-shield" aria-hidden="true"></i> Secured</span
                        >
                        <span class="badge badge-secondary badge-pill"
                          ><i class="fa fa-users" aria-hidden="true"></i> Wide Common Area. ...</span
                        >
                      </p>
                      <p class="card-text text-justify">
                        The family home is the place where one or both spouses live the intention of that place being the family home.
                      </p>
                      <p class="card-text text-muted float-right">
                        <i class="fa fa-clock-o"></i> Last Updated 5 Min ago...
                      </p>
                      <div class="clearfix"></div>
    
                      <a href="#!"  data-toggle="modal" data-target="#userLogMod" class="btn btn-dark btn-block"
                        ><i class="fa fa-building" aria-hidden="true"></i> Book
                        Now</a
                      >
                    </div>
                  </div>
                </div>
                <div class="col-lg-4 col-md-6 my-sm-2 ">
                  <div class="card bg-light ml-lg-3" style="width: 23rem;background-image: linear-gradient(to right top,#E5E1DA,#7FC7D9);" >
                    <img src="./media/house2.jpg" alt="Apartment 1" class="card-img-top" width="150px" height="200px">
                    <div class="card-body">
                      <h5 class="card-title">
                        For bachelors...
                        <span class="badge badge-primary badge-pill"
                          >New Update !</span
                        >
                      </h5>
                      <p class="card-text">
                        <span class="badge badge-light badge-pill"
                          ><i class="fa fa-user-o" aria-hidden="true"></i> Simple</span
                        >
                        <span class="badge badge-success badge-pill"
                          ><i class="fa fa-credit-card-alt" aria-hidden="true"></i> Low Cost</span
                        >
                      </p>
                      <p class="card-text text-justify">
                        A bachelor home is a living space for a single man. It's also known as a bachelor pad or bachelor den.  Easy to rent it saves space and mony for bachelors.
                      </p>
                      <p class="card-text text-muted float-right">
                        <i class="fa fa-clock-o"></i> Last Updated 5 Min ago...
                      </p>
                      <div class="clearfix"></div>
    
                      <a href="#!" data-toggle="modal" data-target="#userLogMod" class="btn btn-dark btn-block"
                        ><i class="fa fa-building" aria-hidden="true"></i> Book
                        Now</a
                      >
                    </div>
                  </div>
                </div>
                <div class="col-lg-4 col-md-6 my-sm-2">
                  <div class="card bg-light ml-lg-3" style="width: 23rem;background-image: linear-gradient(to right top,#E5E1DA,#7FC7D9);" >
                    <img src="./media/apartment3.jpg" alt="Apartment 1" class="card-img-top" width="150px" height="200px">
                    <div class="card-body">
                      <h5 class="card-title">
                        For Company based...
                        <span class="badge badge-primary badge-pill"
                          >Large Scale !</span
                        >
                      </h5>
                      <p class="card-text">
                        <span class="badge badge-light badge-pill"
                          ><i class="fa fa-cubes" aria-hidden="true"></i> Futuristic</span
                        >
                        <span class="badge badge-warning badge-pill"
                          ><i class="fa fa-users" aria-hidden="true"></i> Wide Common Area. ...</span
                        >
                      </p>
                      <p class="card-text text-justify">
                        A corporate apartment is a standard rental unit that appeals to corporate professionals. Large space work area.
                      </p>
                      <p class="card-text text-muted float-right">
                        <i class="fa fa-clock-o"></i> Last Updated 5 Min ago...
                      </p>
                      <div class="clearfix"></div>
    
                      <a href="#!" class="btn btn-dark btn-block"
                        ><i  data-toggle="modal" data-target="#userLogMod" class="fa fa-building" aria-hidden="true"></i> Book
                        Now</a
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="alert alert-info" id="pg"  style="background-image: linear-gradient(to bottom right,#365486,black);">
              <p class="display-5 lead text-light text-left">Explore All PG Homes.... <a href="pg_home.py" class="alert-link" style="color: white;">More</a></p>
            </div>
            <div class="container-fluid">
              <div class="row   mb-3 my-sm-2">
                <div class="col-lg-4 col-md-6 my-sm-2">
                  <div class="card bg-light ml-lg-3" style="width: 23rem;background-image: linear-gradient(to right top,#E5E1DA,#7FC7D9);" >
                    <img src="./media/pg1.jpg" alt="pg3" class="card-img-top" width="150px" height="200px">
                    <div class="card-body">
                      <h5 class="card-title">
                        For Mens...
                        <span class="badge badge-primary badge-pill"
                          >New Update !</span
                        >
                      </h5>
                      <p class="card-text">
                        <span class="badge badge-light badge-pill"
                          ><i class="fa fa-cubes" aria-hidden="true"></i> Furnished</span
                        >
                        <span class="badge badge-success badge-pill"
                          ><i class="fa fa-wifi" aria-hidden="true"></i> WiFi</span
                        >
                      </p>
                      <p class="card-text text-justify">
                        It is a rental accommodation wherein a person has to pay a specific amount to live at the property and share facilities being offered with other people living in the house.
                      </p>
                      <p class="card-text text-muted float-right">
                        <i class="fa fa-clock-o"></i> Last Updated 5 Min ago...
                      </p>
                      <div class="clearfix"></div>
    
                      <a href="#!"  data-toggle="modal" data-target="#userLogMod" class="btn btn-dark btn-block"
                        ><i class="fa fa-building" aria-hidden="true"></i> Book
                        Now</a
                      >
                    </div>
                  </div>
                </div>
                <div class="col-lg-4 col-md-6 my-sm-2">
                  <div class="card bg-light ml-lg-3" style="width: 23rem;background-image: linear-gradient(to right top,#E5E1DA,#7FC7D9);" >
                    <img src="./media/pg2.jpg" alt="pg3" class="card-img-top" width="150px" height="200px">
                    <div class="card-body">
                      <h5 class="card-title">
                        For Womens... 
                        <span class="badge badge-primary badge-pill"
                          ><i class="fa fa-female" aria-hidden="true"></i></span
                        >
                      </h5>
                      <p class="card-text">
                        <span class="badge badge-danger badge-pill"
                          ><i class="fa fa-cutlery" aria-hidden="true"></i> Food</span
                        >
                        <span class="badge badge-success badge-pill"
                          ><i class="fa fa-money" aria-hidden="true"></i> No Commision</span
                        >
                      </p>
                      <p class="card-text text-justify">
                        It is a rental accommodation wherein a person has to pay a specific amount to live at the property and share facilities being offered with other people living in the house.
                      </p>
                      <p class="card-text text-muted float-right">
                        <i class="fa fa-clock-o"></i> Last Updated 5 Min ago...
                      </p>
                      <div class="clearfix"></div>
    
                      <a href="#!"  data-toggle="modal" data-target="#userLogMod" class="btn btn-dark btn-block"
                        ><i class="fa fa-building" aria-hidden="true"></i> Book
                        Now</a
                      >
                    </div>
                  </div>
                </div>
                <div class="col-lg-4 col-md-6 my-sm-2">
                  <div class="card bg-light ml-lg-3" style="width: 23rem;background-image: linear-gradient(to right top,#E5E1DA,#7FC7D9);" >
                    <img src="./media/pg3.jpg" alt="pg3" class="card-img-top" width="150px" height="200px">
                    <div class="card-body">
                      <h5 class="card-title">
                        For Students & Workers...
                        <span class="badge badge-primary badge-pill"
                          > <i class="fa fa-users" aria-hidden="true"></i> </span
                        >
                      </h5>
                      <p class="card-text">
                        <span class="badge badge-light badge-pill"
                          ><i class="fa fa-cubes" aria-hidden="true"></i> Furnished</span
                        >
                        <span class="badge badge-danger badge-pill"
                          ><i class="fa fa-cutlery" aria-hidden="true"></i> Food</span
                        >
                      </p>
                      <p class="card-text text-justify">
                        It is a rental accommodation wherein a person has to pay a specific amount to live at the property and share facilities being offered with other people living in the house.
                      </p>
                      <p class="card-text text-muted float-right">
                        <i class="fa fa-clock-o"></i> Last Updated 5 Min ago...
                      </p>
                      <div class="clearfix"></div>
    
                      <a href="#!"  data-toggle="modal" data-target="#userLogMod"class="btn btn-dark btn-block"
                        ><i class="fa fa-building" aria-hidden="true"></i> Book
                        Now</a
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
        </center>
        </section>
        <footer class="text-light" style="background-color: #0F1035;">
          
          <div class=" my-2 border-bottom" style="padding: 10px;text-wrap:nowrap">
            <div class = "row">
                <div class = "col-lg-6 col-md-6 col-sm-6">
                    <p style="font-size: 16px;" class="">Connect With Us....</p>

                </div>
                <div class = "col-lg-6 col-md-6 col-sm-6 d-flex justify-content-end" >
                    <a href="#"class="text-reset"><span class="fa fa-facebook-official"></span> &nbsp;Facebook &nbsp;</a>
                    <a href="#"class="text-reset "><span class="fa fa-whatsapp"></span>&nbsp; Whats App &nbsp;</a>
                    <a href="#"class="text-reset"><span class="fa fa-instagram"></span> Instagram &nbsp;</a>
                </div>
            </div>
          </div>
          <div class="container">
            <div class="row">
              <div class="col-lg-4 col-sm-12">
                <h6 class="fw-bold">About Cmpany</h6>
              <p class="text-secondary text-justify">
                House Leasing and Maintenance: When leasing a house, consider property management services like Housewise for seamless tenant search, rent collection, and property upkeep. Landlords should maintain properties to ensure tenant safety. Tenants must also fulfill their responsibilities. Regular maintenance preserves property value over time .
              </p>
              </div>
              <div class="col-lg-4 col-sm-6">
                <h6 class="fw-bold">Location</h6>
                <p class="text-secondary">Sai Baba Covil, Coimbatore- 641046</p>
              </div>
              <div class="col-lg-4 col-sm-6">
                <h6 class="fw-bold">Use Full Links</h6>
                <div class="text-secondary mx-auto d-inline-block">
                  <a href="apartments.py" class="text-reset">Apartments</a><br>
                  <a href="houses.py" class="text-reset">Houses</a><br>
                  <a href="pg_home.py" class="text-reset">PG - Homes</a><br>
                  
                </div>
              </div>
              
            </div>
   

            <div class="p-2 text-center text-light" >Dream Home @ Pvt.....</div>
          </div>
          
        </footer>
  </div>
  <script>
    i=0,img=[],time=1300;
    img[0]="./media/apartment.png";
    img[1]="./media/one.png";
    img[2]="./media/two.png";
    img[3]="./media/three.png";
    img[4]="./media/bgimg.jpg";
    
    function img_scrool(){
        document.images.src = img[i]
        if(i<img.length-1){
            i++;
        }
        else{
            i=0;
        }
        setTimeout(img_scrool,time);
    }
    img_scrool()
</script>
</body>
</html>"""
)

form = cgi.FieldStorage()
usubmit = form.getvalue("usubmit")


if usubmit != None:
    if len(form) != 0:
        pname = form.getvalue("uname")
        pgender = form.getvalue("ugender")
        pphone = form.getvalue("uphone")
        pemail = form.getvalue("uemail")
        pdob = form.getvalue("udob")
        paddress = form.getvalue("uaddress")
        ppincode = form.getvalue("upincode")
        pstate = form.getvalue("ustate")
        pcity = form.getvalue("ucity")
        pprofession = form.getvalue("uprofession")
        pphoto = form['uphoto']
        pmarried = form.getvalue("umarried")
        pidentity = form['uidentity']
        ppassword = form.getvalue("upass")

        if pphoto.filename:
            fn = os.path.basename(pphoto.filename)
            open("dbdoc/"+fn,"wb").write(pphoto.file.read())

            fn1 = os.path.basename(pidentity.filename)
            open("dbdoc/"+fn1,"wb").write(pidentity.file.read())

            q = """insert into userregform (Name,Gender,Phone,Email,Dob,Address,Pincode,State,City,Profession,Photo,MarriedState,Identity,Password) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""%(pname,pgender,pphone,pemail,pdob,paddress,ppincode,pstate,pcity,pprofession,fn,pmarried,fn1,ppassword)
            cur.execute(q)
            con.commit()
            print("""
            <script>
            alert("Successfully Registered")
            </script>
            """)


 #OWNER REGISTERATION FORM

q1 = """select  max(id) from ownerregform"""
cur.execute(q1)
con.commit()
rec = cur.fetchone()
if rec[0] != None:
    n = rec[0]
else:
    n = 0

z = ""
if n < 9:
    z="000"
elif n ==10 or n <= 99:
    z="00"
elif n > 99 or n <= 999:
    z="0"
ownerid = "OWNERDH" + z + str(n + 1)


N=7
res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
ownerpass = "DH@" + res


osubmit = form.getvalue("osubmit")
if osubmit != None:
    if len(form) != 0:
        oname = form.getvalue("oname")
        ophone = form.getvalue("ophone")
        oemail = form.getvalue("oemail")
        odob = form.getvalue("odob")
        ogender = form.getvalue("ogender")
        oaddress = form.getvalue("oaddress")
        opincode = form.getvalue("opincode")
        ostate = form.getvalue("ostate")
        ocity = form.getvalue("ocity")
        ophoto = form['ophoto']
        oidentity = form['oidentity']
        o_p_type = form.getvalue("o_ptype")
        o_p_location = form.getvalue("o_plocation")
        o_p_document = form['o_prop_doc']

        if ophoto.filename:
            ofn = os.path.basename(ophoto.filename)
            open("dbdoc/"+ofn,"wb").write(ophoto.file.read())

            ofn1 = os.path.basename(oidentity.filename)
            open("dbdoc/"+ofn1,"wb").write(oidentity.file.read())

            ofn2 = os.path.basename(o_p_document.filename)
            open("dbdoc/"+ofn1,"wb").write(o_p_document.file.read())
            q3 = """insert into ownerregform (name,phone,email,dob,gender,address,pincode,state,district,profile,identity,password,p_type,p_location,p_document,username) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""%(oname,ophone,oemail,odob,ogender,oaddress,opincode,ostate,ocity,ofn,ofn1,ownerpass,o_p_type,o_p_location,ofn2,ownerid)
            cur.execute(q3)
            con.commit()
            print("""
            <script>
            alert("Successfully Owner Registered")
            </script>
            """)



# Admin_Login

A_username = form.getvalue("A_uname")
A_password = form.getvalue("A_pass")
A_submit = form.getvalue("a_log")
adminu = "adminda"
adminpassword = "123"
if A_submit != None:
    if A_username == adminu:
        if A_password == adminpassword:
           print("""<script>
           alert("login successful");
           location.href="admin_dashboard.py"
           </script>""")

# User Login

U_username = form.getvalue("U_uname")
U_password = form.getvalue("U_pass")
U_submit = form.getvalue("U_submit")

if U_submit != None:

    q = """select id from userregform where Email ='%s' and Password = '%s' """%(U_username,U_password)
    cur.execute(q)
    rec = cur.fetchone()
    print("""<script>
    alert("login successful");
    location.href="user_dashboard.py?id=%s"
    </script>""" %rec[0])

# Owner Login

O_username = form.getvalue("O_uname")
O_password = form.getvalue("O_pass")
O_submit = form.getvalue("O_submit")

if O_submit != None:

    q = """select id from ownerregform where username ='%s' and password = '%s' """%(O_username,O_password)
    cur.execute(q)
    rec = cur.fetchone()
    print("""<script>
    alert("login successful");
    location.href="owner_dashboard.py?id=%s"
    </script>""" %rec[0])

ForgotEmail = form.getvalue("forgot_email")
ForgotSubmit = form.getvalue("forgot_submit")

if ForgotSubmit != None:
    q = """select  Name, Password, Email from userregform where Email = '%s'""" %(ForgotEmail)
    cur.execute(q)
    rec = cur.fetchall()
    for i in rec:
        fname = i[1]
        fpass = i[14]
        femail = i[4]
        q = """insert into forgot_pass (Name,Password,Email) values ('%s','%s','%s')"""%(fname,femail,fpass)
        print("""<script>alert("Inserted into table")</script>""")


