$(document).ready(function() {
  $(document).foundation();

  // Toggle the 'hide' class based on the data-id attribute.
  $('.toggle').on('click', function(e) {
    e.preventDefault();
    $('#' + $(this).data().id).toggleClass('hide');
  });

  $('.badge.tag').on('mouseenter', function(e) {
    $($(this).children()[1]).toggleClass('hide');
  });

  $('.badge.tag').on('mouseleave', function(e) {
    $($(this).children()[1]).toggleClass('hide');
  });

  $('.remove-tag').on('click', function(e) {
    e.preventDefault();
    var $this = $(this);
    var token = $($this.next()).val();
    $.ajax({
      url: '/books/' + $this.data().bookid + '/remove_tag',
      method: 'post',
      data: 'tagid=' + $this.data().tagid + '&csrfmiddlewaretoken=' + token,
      success: function(data) {
        console.log('data:', data);
        window.location.reload();
      }
    });
  });
});
