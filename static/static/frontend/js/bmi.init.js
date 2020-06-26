var healthApp = (function(){
  
  // cache dom
  var _calc = id("btn-calc");
  var _outBMI = id("output-bmi");
  var _inHeight = id("in-height");
  var _inWeight = id("in-weight");

  // event listeners
  _calc.addEventListener("click", main);
  
  // functions
  function main() {
    var height = _inHeight.value;
    var weight = _inWeight.value;
    
    // validate inputs
    if (height && weight) {
      
      var bmi = calculateBMI(height, weight);

      render(bmi);
    } else {
      // invalid inputs
      console.log("woops");
    }
  }
  
  function calculateBMI(height, weight) {
    var h = height / 100;
    var c = (weight / (h * h));
    var out = Math.round(c * 100) / 100; // round to 2 dec
    
    return out;
  }

  function render(bmi) {
    _outBMI.innerHTML = bmi;
  }
  
  // helper functions
  function id(el) {
    return document.getElementById(el);
  }
  
})();