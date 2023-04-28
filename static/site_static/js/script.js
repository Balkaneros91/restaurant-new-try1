// Messages

setTimeout(function () {
    document.getElementById('msg').classList.add('hide');
}, 10000);


// Home page Menu tabs

setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
  }, 2500);

  $(document).ready(function () {
    // Activate the first tab by default
    $('#pills-tab a:first').tab('show');

    // Activate the selected tab on click
    $('#pills-tab a').click(function (e) {
      e.preventDefault();
      $(this).tab('show');
    });
  });