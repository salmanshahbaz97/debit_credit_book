const form = document.getElementById("expense-form");

form.addEventListener("submit", (event) => {
  // Prevent the form from submitting normally
  event.preventDefault();

  // Get the form data
  const formData = new FormData(form);

  // Construct the API request
  const url = "/core/sales/";
  const options = {
    method: "POST",
    body: formData,
  };

  // Send the API request
  fetch(url, options)
    .then((response) => response.json())
    .then((data) => {
      // Handle the API response
      console.log(data);
      alert("Expense added successfully!");
    })
    .catch((error) => {
      // Handle any errors that occur during the API request
      console.error(error);
      alert("An error occurred while adding the expense.");
    });
});
