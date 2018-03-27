
var getAnswer = function() {
  var answers = ["Computer says no.", "Maybe", "Definitely","Yeah Mon", "Yup", "Not in a million years"];
  return answers[Math.floor(Math.random() * 6)]
  
}

var askQuestion = function() {
  var question = prompt("What is your question?");
  var answer = getAnswer();
  alert(answer);
};