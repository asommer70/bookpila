$(document).ready(function() {
  $(document).foundation();

  // Register callbacks to use arrow keys to turn pages.
  // Needs to be up here before the Book is rendered.... I guess.
  EPUBJS.Hooks.register("beforeChapterDisplay").pageTurns = function (callback, renderer) {
      var lock = false;
      var arrowKeys = function (e) {
          e.preventDefault();
          if (lock) return;

          if (e.keyCode == 37) {
              window.Book.prevPage();
              lock = true;
              setTimeout(function () {
                  lock = false;
              }, 100);
              return false;
          }

          if (e.keyCode == 39) {
              window.Book.nextPage();
              lock = true;
              setTimeout(function () {
                  lock = false;
              }, 100);
              return false;
          }

      };
      renderer.doc.addEventListener('keydown', arrowKeys, false);
      if (callback) callback();
  }


  // Toggle the 'hide' class based on the data-id attribute.
  $('.toggle').on('click', function(e) {
    e.preventDefault();
    $('#' + $(this).data().id).toggleClass('hide');
  });

  // Control remove tag button on tag badges.
  $('.badge.tag').on('mouseenter', function(e) {
    $($(this).children()[1]).toggleClass('hide');
  });

  $('.badge.tag').on('mouseleave', function(e) {
    $($(this).children()[1]).toggleClass('hide');
  });

  // Send remove tag POST.
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


  // Execute search based on button click and Enter key.
  $('#searchbtn').on('click', function(e) {
    e.preventDefault();
    window.location.href = '/books/search/' + $('#search').val();
  });

  $('#search').keydown(function(e) {
    if (e.keyCode == 13) {
      window.location.href = '/books/search/' + this.value;
    }
  });


  // Display the book on the entire screen.
  $('#read-book').on('click', function(e) {
    e.preventDefault();
    $this = $(this);

    var idParts = window.location.pathname.split('/');
    var bookId = idParts[idParts.length - 1];
    var bookData;

    // Display the book-reader div.
    $bookReader = $('#book-reader');
    $bookReader.toggleClass('reading');
    $bookReader.css('display', 'block');

    // Render the book put the object on the window object.
    window.Book = ePub($this.data().url);
    window.Book.renderTo("book-area");
    window.Book.locChangeCount = 0;

    window.Book.on('book:ready', function() {
      $.ajax({
        method: 'get',
        url: '/api/books/' + bookId,
        headers: {
            Authorization: 'Token ' + token,
            contentType: 'application/json; charset=utf-8',
        },
        success: function(data) {
          bookData = data;
          window.Book.goto(data.current_loc);
        }
      });
    });

    window.Book.on('renderer:locationChanged', function(locationCfi) {
      localStorage.setItem(bookId, locationCfi);

      if (window.Book.locChangeCount > 1) {
        bookData.current_loc = locationCfi;
        $.ajax({
          method: 'put',
          url: '/api/books/' + bookId,
          data: bookData,
          headers: {
              Authorization: 'Token ' + token,
              contentType: 'application/json; charset=utf-8',
          },
          dataType: 'json',
          success: function(data) {
            console.log('put success data:', data);
          }
        });
      }
      window.Book.locChangeCount++;
    });

    $('#book-prev').on('click', function(e) {
      e.preventDefault();
      window.Book.prevPage();
    });


    $('#book-next').on('click', function(e) {
      e.preventDefault();
      window.Book.nextPage();
    });

    $('#book-close').on('click', function(e) {
      e.preventDefault();

      $bookReader.toggleClass('reading');
      $bookReader.css('display', 'none');
      window.Book = undefined;
      $('#book-area').html('');
    });
  });
});
