//---------------------------------------------------------------------
// Get request when "Activate" button is clicked
//---------------------------------------------------------------------

$('#activate').click(function() {

  var keyword = document.getElementById("keyword").textContent;
  var requestUrl = 'http://parrot.holberton.us/start/' + keyword;

  console.log(keyword);
  $.ajax({
      url: requestUrl,
      type: 'GET',
      dataType: 'json',
      contentType: 'application/json',
      success: function (response) {
        console.log(response);
      }
  });
});

//---------------------------------------------------------------------
// Deactivates service when "Deactivate" button is clicked
//---------------------------------------------------------------------

$('#deactivate').click(function() {
  window.location.href = 'http://parrot.holberton.us/start/deactivate';
});
