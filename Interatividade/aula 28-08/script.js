
function drag(ev) {
        ev.dataTransfer.setData("text", ev.target.id);
       }
       

function allowDrop(ev) {
    ev.preventDefault();
    }
       
function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    ev.target.appendChild(document.getElementById(data));
       }
       

       function dragStart(event) {
        event.dataTransfer.setData("Text", event.target.id);
       }
       function dragging(event) {
        document.getElementById("demo").innerHTML = "O Texto está sendo arrastado";
       }
       function allowDrop(event) {
        event.preventDefault();
       }
       function drop(event) {
        event.preventDefault();
        const data = event.dataTransfer.getData("Text");
        event.target.appendChild(document.getElementById(data));
        document.getElementById("demo").innerHTML = "O texto foi solto.";
       }     

