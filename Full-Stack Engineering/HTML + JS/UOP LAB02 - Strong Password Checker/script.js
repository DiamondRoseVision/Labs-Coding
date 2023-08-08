function isStrongPassword(passwd) {
   let one 
   let two
   let three

   if (passwd.length >= 8) {
     one = true;
   } else {
        return false;
   };

   if ((passwd.indexOf("password")) < 0) {
      two = true;
   } else {
      return false;	        
   };

   if (passwd !== passwd.toLowerCase()) {
        three = true;
   } else {
        return false;
   };
   
   if (one === false) {
       return passwd = false; 
   } else if (two === false) {
      return passwd = false; 
   } else if (three === false) {
      return passwd = false; 
   } else {
      return passwd = true;
   };

};
