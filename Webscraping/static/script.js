function changeText(){
    document.getElementById("title").innerHTML = "Test"; //gets the element with the id "title" and changes it to test
    document.getElementById("title").innerHTML = get_item();
}

$.ajax({
    type: "POST",
    url: "~/pythoncode.py",
    data: { param: text}
  }).done(function( o ) {
     // do something
  });