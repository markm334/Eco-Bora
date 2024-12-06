// Show Farmer options and hide Customer options
function showFarmerOptions() {
    document.getElementById('farmer-options').style.display = 'block';
    document.getElementById('customer-options').style.display = 'none';
}

// Show Customer options and hide Farmer options
function showCustomerOptions() {
    document.getElementById('customer-options').style.display = 'block';
    document.getElementById('farmer-options').style.display = 'none';
}

// Handle the search functionality or redirect based on the user selection
function handleSearch() {
    var userRole = document.querySelector('select#user-role').value;

    if (userRole === 'farmer') {
        window.location.href = '/farmer/dashboard';  // Example URL for Farmer Dashboard
    } else if (userRole === 'customer') {
        window.location.href = '/customer/dashboard';  // Example URL for Customer Dashboard
    } else {
        alert('Please select a role');
    }
}
// Redirect to Farmer Registration Form
function redirectToFarmerForm() {
    window.location.href = 'farmer-register.html';  // Replace with the actual URL for the farmer registration form
}

// Redirect to Customer Registration Form
function redirectToCustomerForm() {
    window.location.href = 'customer-register.html';  // Replace with the actual URL for the customer registration form
}
// Redirect to Farmer Registration Form
function redirectToFarmerForm() {
    window.location.href = '/farmer/register';  // Replace with the correct URL in Django
}

// Redirect to Customer Registration Form
function redirectToCustomerForm() {
    window.location.href = '/customer/register';  // Replace with the correct URL in Django
}
