$(document).ready(
    function() {
        $('#tabs').tabify();
        setInterval(reloadDocument, 1000);
    }
)

function reloadDocument(){
    //location.reload();
}