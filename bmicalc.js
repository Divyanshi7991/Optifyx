function calculateBMI()
{
  const weight = parseFloat(document.getElementById('weight').value);
  const height = parseFloat(document.getElementById('height').value);

  if(isNaN(weight)|| isNaN(height))
  {
    alert("Please enter valid numbers for weight and height.");
    return;
  }
  const bmi = (weight/(height*height)).toFixed(2);
  let category = "";

  if (bmi < 18.5)
  {
    category = "Underweight";
  }
  else if(bmi >= 18.5 && bmi <= 24.9)
  {
    category = "Normal weight";
  }
  else
  {
    category = "Obesity";
  }
  document.getElementById('result').innerText = 'Your BMI is ${bmi} and you areclassified as ${category}.';
}