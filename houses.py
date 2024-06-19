#!C:/Users/nandh/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql, os, smtplib
import string
import random

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="user_register")
cur = con.cursor()
form = cgi.FieldStorage()

q = """select * from property  where propertyType ='House' and status = 'Approve'"""
cur.execute(q)
rec = cur.fetchall()

print("""<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Houses</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" />
  <script src="https://cdn.jsdelivr.net/npm/jquery@3.7.1/dist/jquery.slim.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js"></script>
  <script src="https://kit.fontawesome.com/a076d05399.js" crossorigin="anonymous"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" />
  <style>
    ::selection {
      background-color: black;
      color: white;
    }

    body {
      background-color: #dcf2f1;

    }

    .card {
      box-shadow: 1px 3px 10px 1px black, 0px 1px 10px 1px rgb(83, 78, 141);
      border-radius: 20px;
      border: none;
    }

    .row {
      padding-bottom: 20px;
    }

    #img-tog {
      border-radius: 20px;
      transition-delay: 2s;
      transition: linear 3s;
      display: flex;
      justify-content: space-between;
    }

    nav {
      border-radius: 6px 6px 6px 6px;
      margin-left: 13px;
      margin-right: 13px;
    }

    .back::before {
      content: "";
      position: absolute;
      top: 0px;
      right: 0px;
      bottom: 0px;
      left: 0px;
      background-image: url(./media/dash_bg.jpg);
      background-repeat: no-repeat;
      opacity: 20%;
      background-position: center;
      height: 100%;
      background-color: #0c0e3c6c;
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
""")
print("""
<body>
  <img src="./media/logo bg.png" alt="Logo Of this website" height="150px" width="200px" class="mx-auto d-block"
    style="border-radius: 15px; margin: 7px 7px 7px 7px" />
    <header>
          <nav class="navbar navbar-expand-lg navbar-dark" style="background-color:#0F1035;padding: 10px;">
              <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
              </button>

              <div class="collapse navbar-collapse my-2 " id="navbarSupportedContent">
                <ul class="navbar-nav mr-auto " >
                  <li class="nav-item ">
                    <a class="nav-link" href="Home_page.py">Home <span class="sr-only">(current)</span></a>
                  </li>

                  <li class="nav-item">
                    <a class="nav-link" href="apartments.py">Apartment</a>
                  </li>
                  <li class="nav-item active">
                    <a class="nav-link" href="houses.py">House</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" href="pg_home.py">PG Home</a>
                  </li>
                </ul>
                <ul class="form-inline my-lg-2  my-sm-0">
                  <li class="nav-item">
                    <div class="dropdown " >
                      <a  class="text-light dropdown-toggle my-2 my-sm-0 nav-link" style="margin-left: -49px;text-decoration: none;"  data-toggle="dropdown"> <i class="fa fa-user-plus"></i> Register</a>
                      <ul class="dropdown-menu ">
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
                                pattern="[6789]\d{9}"
                                class="form-control"
                                id="OPhone"
                                placeholder="Enter Mobile No...."
                                required
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
                                pattern="[a-zA-Z0-9\s]+"
                                class="form-control"
                                id="OAddress"
                                name="oaddress"
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
                                    pattern="[6789]\d{9}"
                                    class="form-control"
                                    id="Phone"
                                    placeholder="Enter Mobile No...."
                                    required
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
                                    pattern="[a-zA-Z0-9\s]+"
                                    class="form-control"
                                    id="Address"
                                    name="uaddress"
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

                            <input type="submit" class="btn btn-primary my-3" name="adminLogin"  value="SUBMIT">
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
                            <a href="check_email_owner.py" class="float-right text-reset">Forgot Password ?</a><br>
                            <input type="submit" name="O_submit"class="btn btn-primary my-3"   value="SUBMIT">
                            <button type="button" class="btn btn-outline-dark" class="d-flex float-right" data-dismiss="modal">CANCEL</button>
                          </form>
                      </div>

                    </div>
                  </div>
              </div>
          </nav>

    </header>

""")
print("""

  <div class="container-fluid">

    <div class="row pt-3">
      <div class="col-lg-3 back">
        <div class="row">
          <div class="col">
            <div class="text-center" style="display: flex; justify-content: center">
              <form method="post" enctype="multipart/form-data" class="form-inline lead bg-light p-2" style="border-radius: 10px">
                        <input type="text" name="search" placeholder="Search here.. Bhk, City" class="form-control mr-2"
                          style="padding-left: 60px; text-align: left" />
                          <button type="submit" name = "search_submit" class="btn btn-dark btn-sm">Search</button>

                    </div>
                  </div>
                </div>
                <div class="row pt-5">
                  <div class="col" style="display: flex; justify-content: end">

                      <label for="priceRange">Price Range:</label>
                      <input type="range" class="form-range" id="priceRange" name = "amount" min="0" max="10000" step="100" value="5000" />

                      <p class = "ml-4">
                        Selected Price:
                        <span id="selectedPrice" class="badge bg-dark text-light">5000</span>
                      </p>
                      <br>


                      </div>
                      <div class="col lead">
                          <label for="">No Of BHK</label> <br>
                          <input type="checkbox" name="onebhk" value="1 bhk" >
                          <label for="1 BHK">
                            &nbsp;1 BHK  </label><br />
                          <input type="checkbox" name="twobhk" value="2 bhk" >
                          <label for="2 BHK">
                            &nbsp;2 BHK </label><br />
                          <input type="checkbox" name="threebhk" value="3 bhk" >
                          <label for="3 BHK">
                            &nbsp;3 BHK </label><br />
                    <input type = "submit" name = "range_submit" class = "btn btn-primary btn-sm" value = "Click to Filter">     
            </form>
          </div>
        </div>
      </div>
      <div class="col-lg-9">
        <div style="
                  text-align: center;
                  padding: 10px;
                  margin-left: 13px;
                  background-size: contain;
                  border-radius: 50px;
                  background-image: linear-gradient(
                    to bottom right,
                    #365486,
                    #7fc7d9
                  );
                  display: flex;
                  justify-content: center;
                ">
          <h4 style="
                    font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial,
                      sans-serif;
                    font-size: 50px;
                    border-radius: 0px 0px 6px 6px;
                    background-image: linear-gradient( to right top,#e5e1da,#7fc7d9);
                    background-size: cover;
                    background-clip: text;
                    color: transparent;
                    letter-spacing: 7px;
                  ">
            APARTMENTS
          </h4>
        </div>
        <div class = "row">""")

search_submit = form.getvalue("search_submit")
r_submit = form.getvalue("range_submit")

if search_submit != None:
    amount = form.getvalue("amount")
    search = form.getvalue("search")
    onebhk = form.getvalue("onebhk")
    twobhk = form.getvalue("twobhk")
    threebhk = form.getvalue("threebhk")
    q1 = """SELECT * FROM property WHERE ((availableBhk = '%s' or  city ='%s') and rent <= '%s') and propertyType ='House'   """ % (
    search, search, amount)
    cur.execute(q1)
    con.commit()
    anorecord = cur.fetchall()

    for i in anorecord:
        fn = "dbdoc/" + i[18]

        print("""
                <div class = "col">
                   <div class="d-flex justify-content-around">

                      <div class="card mb-md-5  " style=" background-image: linear-gradient( to right top,#e5e1da,#7fc7d9);width: 22rem;margin-top: 20px;">
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
                                  <img class="d-block mx-auto" src="%s" alt="First slide" height="150px" width="180px" />
                                </div>
                                <div class="carousel-item">
                                  <img class="d-block mx-auto" src="%s" alt="Second slide" height="150px" width="180px" />
                                </div>
                                <div class="carousel-item">
                                  <img class="d-block mx-auto" src="%s" alt="Third slide" height="150px" width="180px" />
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

                        <div class="card-body" style = "line-height:11px">
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
                          <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#userLogMod">
                            View Details...
                          </button>

                          <!-- Modal -->
                          <div class="modal fade" id="property3%s" role="dialog" style = "line-height:24px">
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
                                  <button type="button" class="btn btn-primary">
                                    Buy
                                  </button>
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
                 </div>

                """ % (
            i[0], i[0], i[0], i[0], fn, fn, fn, i[0], i[0], i[1], i[16], i[11], i[0], i[2], i[3], i[5], i[16],
            i[15],
            i[8], i[9], i[10], i[11], i[12], i[7], i[13]))

elif r_submit != None:
    onebhk = form.getvalue("onebhk")
    twobhk = form.getvalue("twobhk")
    threebhk = form.getvalue("threebhk")
    filter = form.getvalue("filter")

    if onebhk != None and twobhk != None and threebhk != None:
        q1 = """select * from property where (rent <= %s ) and propertyType ='House' """ % filter
        cur.execute(q1)
        record = cur.fetchall()

        for i in record:
            fn = "dbdoc/" + i[18]

            print("""
                    <div class = "col">
                       <div class="d-flex justify-content-around">

                          <div class="card mb-md-5  " style=" background-image: linear-gradient( to right top,#e5e1da,#7fc7d9);width: 22rem;margin-top: 20px;">
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
                                      <img class="d-block mx-auto" src="%s" alt="First slide" height="150px" width="180px" />
                                    </div>
                                    <div class="carousel-item">
                                      <img class="d-block mx-auto" src="%s" alt="Second slide" height="150px" width="180px" />
                                    </div>
                                    <div class="carousel-item">
                                      <img class="d-block mx-auto" src="%s" alt="Third slide" height="150px" width="180px" />
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

                            <div class="card-body" style = "line-height:11px">
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
                              <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#userLogMod">
                                View Details...
                              </button>

                              <!-- Modal -->
                              <div class="modal fade" id="property3%s" role="dialog" style = "line-height:24px">
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
                                      <button type="button" class="btn btn-primary">
                                        Buy
                                      </button>
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
                     </div>

                    """ % (
                i[0], i[0], i[0], i[0], fn, fn, fn, i[0], i[0], i[1], i[16], i[11], i[0],  i[2], i[3], i[5], i[16],
                i[15],
                i[8], i[9], i[10], i[11], i[12], i[7], i[13]))

    if onebhk == None and twobhk == None and threebhk == None:
        q1 = """select * from property where (rent <= %s ) and propertyType ='House' """ % filter
        cur.execute(q1)
        record = cur.fetchall()

        for i in record:
            fn = "dbdoc/" + i[18]

            print("""
                    <div class = "col">
                       <div class="d-flex justify-content-around">

                          <div class="card mb-md-5  " style=" background-image: linear-gradient( to right top,#e5e1da,#7fc7d9);width: 22rem;margin-top: 20px;">
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
                                      <img class="d-block mx-auto" src="%s" alt="First slide" height="150px" width="180px" />
                                    </div>
                                    <div class="carousel-item">
                                      <img class="d-block mx-auto" src="%s" alt="Second slide" height="150px" width="180px" />
                                    </div>
                                    <div class="carousel-item">
                                      <img class="d-block mx-auto" src="%s" alt="Third slide" height="150px" width="180px" />
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

                            <div class="card-body" style = "line-height:11px">
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
                              <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#userLogMod">
                                View Details...
                              </button>

                              <!-- Modal -->
                              <div class="modal fade" id="property3%s" role="dialog" style = "line-height:24px">
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
                                      <button type="button" class="btn btn-primary">
                                        Buy
                                      </button>
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
                     </div>

                    """ % (
                i[0], i[0], i[0], i[0], fn, fn, fn, i[0], i[0], i[1], i[16], i[11], i[0],  i[2], i[3], i[5], i[16],
                i[15],
                i[8], i[9], i[10], i[11], i[12], i[7], i[13]))

    if onebhk != None and twobhk != None and threebhk == None:
        q1 = """select * from property where (rent <= %s ) and availableBhk != '3 bhk' and propertyType ='House';""" % filter
        cur.execute(q1)
        record = cur.fetchall()

        for i in record:
            fn = "dbdoc/" + i[18]

            print("""
                    <div class = "col">
                       <div class="d-flex justify-content-around">

                          <div class="card mb-md-5  " style=" background-image: linear-gradient( to right top,#e5e1da,#7fc7d9);width: 22rem;margin-top: 20px;">
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
                                      <img class="d-block mx-auto" src="%s" alt="First slide" height="150px" width="180px" />
                                    </div>
                                    <div class="carousel-item">
                                      <img class="d-block mx-auto" src="%s" alt="Second slide" height="150px" width="180px" />
                                    </div>
                                    <div class="carousel-item">
                                      <img class="d-block mx-auto" src="%s" alt="Third slide" height="150px" width="180px" />
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

                            <div class="card-body" style = "line-height:11px">
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
                              <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#property3%s">
                                View Details...
                              </button>

                              <!-- Modal -->
                              <div class="modal fade" id="property3%s" role="dialog" style = "line-height:24px">
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
                                      <button type="button" class="btn btn-primary">
                                        Buy
                                      </button>
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
                     </div>

                    """ % (
                i[0], i[0], i[0], i[0], fn, fn, fn, i[0], i[0], i[1], i[16], i[11], i[0], i[0], i[2], i[3], i[5], i[16],
                i[15],
                i[8], i[9], i[10], i[11], i[12], i[7], i[13]))

    if onebhk != None and twobhk == None and threebhk != None:
        q1 = """select * from property where (rent <= %s ) and availableBhk != '2 bhk' and propertyType ='House';""" % filter
        cur.execute(q1)
        record = cur.fetchall()

        for i in record:
            fn = "dbdoc/" + i[18]

            print("""
                    <div class = "col">
                       <div class="d-flex justify-content-around">

                          <div class="card mb-md-5  " style=" background-image: linear-gradient( to right top,#e5e1da,#7fc7d9);width: 22rem;margin-top: 20px;">
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
                                      <img class="d-block mx-auto" src="%s" alt="First slide" height="150px" width="180px" />
                                    </div>
                                    <div class="carousel-item">
                                      <img class="d-block mx-auto" src="%s" alt="Second slide" height="150px" width="180px" />
                                    </div>
                                    <div class="carousel-item">
                                      <img class="d-block mx-auto" src="%s" alt="Third slide" height="150px" width="180px" />
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

                            <div class="card-body" style = "line-height:11px">
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
                              <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#property3%s">
                                View Details...
                              </button>

                              <!-- Modal -->
                              <div class="modal fade" id="property3%s" role="dialog" style = "line-height:24px">
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
                                      <button type="button" class="btn btn-primary">
                                        Buy
                                      </button>
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
                     </div>

                    """ % (
                i[0], i[0], i[0], i[0], fn, fn, fn, i[0], i[0], i[1], i[16], i[11], i[0], i[0], i[2], i[3], i[5], i[16],
                i[15],
                i[8], i[9], i[10], i[11], i[12], i[7], i[13]))

    if onebhk == None and twobhk != None and threebhk != None:
        q1 = """select * from property where (rent <= %s ) and availableBhk != '1 bhk'and propertyType ='House';""" % filter
        cur.execute(q1)
        record = cur.fetchall()

        for i in record:
            fn = "dbdoc/" + i[18]

            print("""
                    <div class = "col">
                       <div class="d-flex justify-content-around">

                          <div class="card mb-md-5  " style=" background-image: linear-gradient( to right top,#e5e1da,#7fc7d9);width: 22rem;margin-top: 20px;">
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
                                      <img class="d-block mx-auto" src="%s" alt="First slide" height="150px" width="180px" />
                                    </div>
                                    <div class="carousel-item">
                                      <img class="d-block mx-auto" src="%s" alt="Second slide" height="150px" width="180px" />
                                    </div>
                                    <div class="carousel-item">
                                      <img class="d-block mx-auto" src="%s" alt="Third slide" height="150px" width="180px" />
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

                            <div class="card-body" style = "line-height:11px">
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
                              <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#property3%s">
                                View Details...
                              </button>

                              <!-- Modal -->
                              <div class="modal fade" id="property3%s" role="dialog" style = "line-height:24px">
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
                                      <button type="button" class="btn btn-primary">
                                        Buy
                                      </button>
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
                     </div>

                    """ % (
                i[0], i[0], i[0], i[0], fn, fn, fn, i[0], i[0], i[1], i[16], i[11], i[0], i[0], i[2], i[3], i[5], i[16],
                i[15],
                i[8], i[9], i[10], i[11], i[12], i[7], i[13]))

    if onebhk != None and twobhk == None and threebhk == None:
        q1 = """select * from property where (rent <= %s ) and availableBhk = '1 bhk' and propertyType ='House';""" % filter
        cur.execute(q1)
        record = cur.fetchall()

        for i in record:
            fn = "dbdoc/" + i[18]

            print("""
                    <div class = "col">
                       <div class="d-flex justify-content-around">

                          <div class="card mb-md-5  " style=" background-image: linear-gradient( to right top,#e5e1da,#7fc7d9);width: 22rem;margin-top: 20px;">
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
                                      <img class="d-block mx-auto" src="%s" alt="First slide" height="150px" width="180px" />
                                    </div>
                                    <div class="carousel-item">
                                      <img class="d-block mx-auto" src="%s" alt="Second slide" height="150px" width="180px" />
                                    </div>
                                    <div class="carousel-item">
                                      <img class="d-block mx-auto" src="%s" alt="Third slide" height="150px" width="180px" />
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

                            <div class="card-body" style = "line-height:11px">
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
                              <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#property3%s">
                                View Details...
                              </button>

                              <!-- Modal -->
                              <div class="modal fade" id="property3%s" role="dialog" style = "line-height:24px">
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
                                      <button type="button" class="btn btn-primary">
                                        Buy
                                      </button>
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
                     </div>

                    """ % (
                i[0], i[0], i[0], i[0], fn, fn, fn, i[0], i[0], i[1], i[16], i[11], i[0], i[0], i[2], i[3], i[5], i[16],
                i[15],
                i[8], i[9], i[10], i[11], i[12], i[7], i[13]))

    if onebhk == None and twobhk != None and threebhk == None:
        q1 = """select * from property where (rent <= %s ) and availableBhk = '2 bhk' and propertyType ='House';""" % filter
        cur.execute(q1)
        record = cur.fetchall()

        for i in record:
            fn = "dbdoc/" + i[18]

            print("""
                    <div class = "col">
                       <div class="d-flex justify-content-around">

                          <div class="card mb-md-5  " style=" background-image: linear-gradient( to right top,#e5e1da,#7fc7d9);width: 22rem;margin-top: 20px;">
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
                                      <img class="d-block mx-auto" src="%s" alt="First slide" height="150px" width="180px" />
                                    </div>
                                    <div class="carousel-item">
                                      <img class="d-block mx-auto" src="%s" alt="Second slide" height="150px" width="180px" />
                                    </div>
                                    <div class="carousel-item">
                                      <img class="d-block mx-auto" src="%s" alt="Third slide" height="150px" width="180px" />
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

                            <div class="card-body" style = "line-height:11px">
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
                              <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#property3%s">
                                View Details...
                              </button>

                              <!-- Modal -->
                              <div class="modal fade" id="property3%s" role="dialog" style = "line-height:24px">
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
                                      <button type="button" class="btn btn-primary">
                                        Buy
                                      </button>
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
                     </div>

                    """ % (
                i[0], i[0], i[0], i[0], fn, fn, fn, i[0], i[0], i[1], i[16], i[11], i[0], i[0], i[2], i[3], i[5], i[16],
                i[15],
                i[8], i[9], i[10], i[11], i[12], i[7], i[13]))

    if onebhk == None and twobhk == None and threebhk != None:
        q1 = """select * from property where (rent <= %s ) and availableBhk = '3 bhk' and propertyType ='House';""" % filter
        cur.execute(q1)
        record = cur.fetchall()

        for i in record:
            fn = "dbdoc/" + i[18]

            print("""
                    <div class = "col">
                       <div class="d-flex justify-content-around">

                          <div class="card mb-md-5  " style=" background-image: linear-gradient( to right top,#e5e1da,#7fc7d9);width: 22rem;margin-top: 20px;">
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
                                      <img class="d-block mx-auto" src="%s" alt="First slide" height="150px" width="180px" />
                                    </div>
                                    <div class="carousel-item">
                                      <img class="d-block mx-auto" src="%s" alt="Second slide" height="150px" width="180px" />
                                    </div>
                                    <div class="carousel-item">
                                      <img class="d-block mx-auto" src="%s" alt="Third slide" height="150px" width="180px" />
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

                            <div class="card-body" style = "line-height:11px">
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
                              <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#property3%s">
                                View Details...
                              </button>

                              <!-- Modal -->
                              <div class="modal fade" id="property3%s" role="dialog" style = "line-height:24px">
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
                                      <button type="button" class="btn btn-primary">
                                        Buy
                                      </button>
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
                     </div>

                    """ % (
                i[0], i[0], i[0], i[0], fn, fn, fn, i[0], i[0], i[1], i[16], i[11], i[0], i[0], i[2], i[3], i[5], i[16],
                i[15],
                i[8], i[9], i[10], i[11], i[12], i[7], i[13]))

else:
    for i in rec:
        fn = "dbdoc/" + i[18]

        print("""
        <div class = "col">
           <div class="d-flex justify-content-around">

              <div class="card mb-md-5  " style=" background-image: linear-gradient( to right top,#e5e1da,#7fc7d9);width: 22rem;margin-top: 20px;">
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
                          <img class="d-block mx-auto" src="%s" alt="First slide" height="150px" width="180px" />
                        </div>
                        <div class="carousel-item">
                          <img class="d-block mx-auto" src="%s" alt="Second slide" height="150px" width="180px" />
                        </div>
                        <div class="carousel-item">
                          <img class="d-block mx-auto" src="%s" alt="Third slide" height="150px" width="180px" />
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

                <div class="card-body" style = "line-height:11px">
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
                  <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#property3%s">
                    View Details...
                  </button>

                  <!-- Modal -->
                  <div class="modal fade" id="property3%s" role="dialog" style = "line-height:24px">
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
                          <button type="button" class="btn btn-primary">
                            Buy
                          </button>
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
         </div>

        """ % (
        i[0], i[0], i[0], i[0], fn, fn, fn, i[0], i[0], i[1], i[16], i[11], i[0], i[0], i[2], i[3], i[5], i[16], i[15],
        i[8], i[9], i[10], i[11], i[12], i[7], i[13]))

print("""




      </div>
    </div>
  </div>
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
</html>

""")

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
            open("dbdoc/" + fn, "wb").write(pphoto.file.read())

            fn1 = os.path.basename(pidentity.filename)
            open("dbdoc/" + fn1, "wb").write(pidentity.file.read())

            q = """insert into userregform (Name,Gender,Phone,Email,Dob,Address,Pincode,State,City,Profession,Photo,MarriedState,Identity,Password) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (
            pname, pgender, pphone, pemail, pdob, paddress, ppincode, pstate, pcity, pprofession, fn, pmarried, fn1,
            ppassword)
            cur.execute(q)
            con.commit()
            print("""
            <script>
            alert("Successfully Registered")
            </script>
            """)

# OWNER REGISTERATION FORM

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
    z = "000"
elif n == 10 or n <= 99:
    z = "00"
elif n > 99 or n <= 999:
    z = "0"
ownerid = "OWNERDH" + z + str(n + 1)

N = 7
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
            open("dbdoc/" + ofn, "wb").write(ophoto.file.read())

            ofn1 = os.path.basename(oidentity.filename)
            open("dbdoc/" + ofn1, "wb").write(oidentity.file.read())

            ofn2 = os.path.basename(o_p_document.filename)
            open("dbdoc/" + ofn1, "wb").write(o_p_document.file.read())
            q3 = """insert into ownerregform (name,phone,email,dob,gender,address,pincode,state,district,profile,identity,password,p_type,p_location,p_document,username) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (
            oname, ophone, oemail, odob, ogender, oaddress, opincode, ostate, ocity, ofn, ofn1, ownerpass, o_p_type,
            o_p_location, ofn2, ownerid)
            cur.execute(q3)
            con.commit()
            print("""
            <script>
            alert("Successfully Owner Registered")
            </script>
            """)

# Admin_Login


A_submit = form.getvalue("adminLogin")
adminu = "adminda"
adminpassword = "123"
if A_submit != None:
    A_username = form.getvalue("A_uname")
    A_password = form.getvalue("A_pass")
    if A_username == adminu:
        if A_password == adminpassword:
            print("""<script>
           alert("login successful");
           location.href="admin_dashboard.py"
           </script>""")
    else:
        print("""<script> alert("wrong username");""")

# User Login

U_username = form.getvalue("U_uname")
U_password = form.getvalue("U_pass")
U_submit = form.getvalue("U_submit")

if U_submit != None:
    q = """select id from userregform where Email ='%s' and Password = '%s' """ % (U_username, U_password)
    cur.execute(q)
    rec = cur.fetchone()
    print("""<script>
    alert("login successful");
    location.href="user_dashboard.py?id=%s"
    </script>""" % rec[0])

# Owner Login

O_username = form.getvalue("O_uname")
O_password = form.getvalue("O_pass")
O_submit = form.getvalue("O_submit")

if O_submit != None:
    q = """select id from ownerregform where username ='%s' and password = '%s' """ % (O_username, O_password)
    cur.execute(q)
    rec = cur.fetchone()
    print("""<script>
    alert("login successful");
    location.href="owner_dashboard.py?id=%s"
    </script>""" % rec[0])

ForgotEmail = form.getvalue("forgot_email")
ForgotSubmit = form.getvalue("forgot_submit")

if ForgotSubmit != None:
    q = """select  Name, Password, Email from userregform where Email = '%s'""" % (ForgotEmail)
    cur.execute(q)
    rec = cur.fetchall()
    for i in rec:
        fname = i[1]
        fpass = i[14]
        femail = i[4]
        q = """insert into forgot_pass (Name,Password,Email) values ('%s','%s','%s')""" % (fname, femail, fpass)
        print("""<script>alert("Inserted into table")</script>""")
