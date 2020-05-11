const inputFile = document.getElementById("image-input");
const workspace = document.getElementById("workspace");

// adding image
inputFile.addEventListener("change",function () {
    var workspaceItem = document.createElement("div");
    var resizer1 = document.createElement("div");
    var resizer2 = document.createElement("div");
    var resizer3 = document.createElement("div");
    var resizer4 = document.createElement("div");
    var image = document.createElement("img");
    
    workspaceItem.appendChild(resizer1);
    workspaceItem.appendChild(resizer2);
    workspaceItem.appendChild(resizer3);
    workspaceItem.appendChild(resizer4);
    workspaceItem.appendChild(image);
    workspace.appendChild(workspaceItem);
    image.classList.add("inpImg");
    workspaceItem.classList.add("workspace-item");
    resizer1.classList.add("resizer","ne");
    resizer2.classList.add("resizer","nw");
    resizer3.classList.add("resizer","se");
    resizer4.classList.add("resizer","sw");
    const file = this.files[0];
    if (file) {
        const reader = new FileReader();
        image.style.display = "block";
        reader.addEventListener("load", function(){
            image.setAttribute("src",this.result);
            image.setAttribute("draggable",false);
            image.setAttribute("id","inputImg");


        });
        reader.readAsDataURL(file);
    }  

});

$(function(){    
        var dragging = false;
        var iX, iY;
        $("#inputImg").mousedown(function(e) {
            dragging = true;
            iX = e.clientX - this.offsetLeft;
            iY = e.clientY - this.offsetTop;
            this.setCapture && this.setCapture();
            return false;
        });
        document.onmousemove = function(e) {
            if (dragging) {
                var e = e || window.event;
                var oX = e.clientX - iX;
                var oY = e.clientY - iY;
                $("#inputImg").css({"left":oX + "px", "top":oY + "px"});
                return false;
            }
        };
        $(document).mouseup(function(e) {
            dragging = false;
            $("#inputImg").releaseCapture();
            e.cancelBubble = true;
        })
    });
