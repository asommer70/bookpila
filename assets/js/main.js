$(document).ready(function() {
  $(document).foundation();

  // Toggle the 'hide' class based on the data-id attribute.
  $('.toggle').on('click', function(e) {
    e.preventDefault();
    $('#' + $(this).data().id).toggleClass('hide');
  })
});
