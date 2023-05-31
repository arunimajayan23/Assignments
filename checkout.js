const checkoutForm = document.getElementById('checkout-form');
checkoutForm.addEventListener('submit', function (event) {
  event.preventDefault(); // Prevent form submission
  const name = document.getElementById('name').value;
  const address = document.getElementById('address').value;
  const payment = document.getElementById('payment').value;
  window.location.href = 'thankyou.html';
});
