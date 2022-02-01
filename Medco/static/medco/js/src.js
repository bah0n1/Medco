$( function() {
  $( "#search" ).autocomplete({
    source:"/autocompleted",
    minLength:2,
  });
} );


$( function() {
  $( "#search_m" ).autocomplete({
    source:"/autocompleted",
    minLength:2,
  });
} );