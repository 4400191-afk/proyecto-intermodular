document.getElementById("btnDescarga").addEventListener("click", function () {

    const enlace = document.createElement("a");

    enlace.href = "../main.py";
    enlace.download = "neondash.py";

    document.body.appendChild(enlace);
    enlace.click();
    document.body.removeChild(enlace);

});