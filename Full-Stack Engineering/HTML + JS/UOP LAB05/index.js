let scoresStringArray;
function parseScores(scoresString) {
   scoresStringArray = scoresString.split(" ");
   return scoresStringArray;
}

function buildDistributionArray(scoresArray) {
   let gradeA = 0;
   let gradeB = 0;
   let gradeC = 0;
   let gradeD = 0;
   let gradeF = 0;
   

   if (scoresArray == "") {
      return scoresArray = [0, 0, 0, 0, 0];      
   } else {
      for (let i = 0; i < scoresArray.length; i++) {
         if ((scoresArray[i] <= 100) && (scoresArray[i] >=90)) {
            gradeA++;
         } else if ((scoresArray[i] <= 89) && (scoresArray[i] >=80)) {
             gradeB++;
         } else if ((scoresArray[i] <= 79) && (scoresArray[i] >=70)) {
            gradeC++;
         } else if ((scoresArray[i] <= 69) && (scoresArray[i] >= 60)) {
            gradeD++;
         } else if ((scoresArray[i] <= 59) && (scoresArray[i] > 0))  {
            gradeF++;
         } else {
            console.log("not valid grade");
         }
      }
         let gradeCount = []
         gradeCount = [gradeA, gradeB, gradeC, gradeD, gradeF]
         return scoresArray = gradeCount
   }
}

function setTableContent(userInput) {
   if (Array.isArray(userInput) === true) {
      userInput = userInput.join(" ");
   }
   let distGraph = buildDistributionArray(parseScores(userInput));
   let firstRow = document.querySelector('firstRow');
   let thirdRow = document.querySelector('thirdRow');

   for (i = 0; i < distGraph.length; i++) {
      let height = "height: " + (10 * distGraph[i]) + "px";
      let bar = "bar" + i;
      document.getElementById("firstRow").innerHTML += `<td><div style="${height}" class="${bar}"></div></td>
	`;
      let newTd = document.getElementById("thirdRow").innerHTML += `<td>${distGraph[i]}</td>`;
   } 
}
