$(document).ready(function() {
    $('#btn_translate').click(function() {
      const languageCode = $('#language_code').val();
  
      // Make a GET request to the translation API
      $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function(data) {
        // Extract the translation from the response
        const translation = data.hello;
  
        // Display the translation in the #hello div
        $('#hello').text(translation);
      });
    });
  });
