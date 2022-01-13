function validateForm() {
    if (document.forms["cvForm"]["fname"].value == "") {
      alert("First name and last name must be filled out");
      return false;
    }
    if (document.forms["cvForm"]["fav_language"].value == "") {
        alert("fav language must be filled out");
        return false;
    }

    console.log('Great Job!, we will contact you soon')
  }