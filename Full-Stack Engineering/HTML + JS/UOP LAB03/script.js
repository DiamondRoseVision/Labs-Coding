function divideArray(numbers) {
   let odd = [];
   let even = [];
   for (let i = 0; i < numbers.length; i++) {
      if (numbers[i] % 2 === 0) {
         even.push(numbers[i]);
      } else {
         odd.push(numbers[i])
      };
   };

   let evenS = [];
   evenS = even.sort(function(a, b){return a - b});
   console.log("Even numbers:");
   if (evenS.length === 0) {
         console.log("None");
   } else {
      for (let n = 0; n < even.length; n++) {
         console.log(evenS[n]);
      };
   };

   let oddS = [];
   oddS = odd.sort(function(a, b){return a- b});
   console.log("Odd numbers:");
   if (oddS.length === 0) {
      console.log("None");
   } else {
      for (let o = 0; o < odd.length; o++) {        
         console.log(oddS[o]);
      };
   };
}

