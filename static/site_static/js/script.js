// Messages

setTimeout(function () {
  document.getElementById('msg').classList.add('hide');
}, 8000);


// Home page Menu tabs

$(document).ready(function () {
  // Activate the first tab by default
  $('#pills-tab a:first').tab('show');

  // Activate the selected tab on click
  $('#pills-tab a').click(function (e) {
    e.preventDefault();
    $(this).tab('show');
  });
});
