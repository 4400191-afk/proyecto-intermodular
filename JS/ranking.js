async function cargarDatos() {
    let peticion = await fetch("../../puntuaciones.txt", { cache: "no-store" });

    let texto = await peticion.text();

    console.log("Datos recibidos:", texto);

    let tabla = document.getElementById("tabla");

    let lineas = texto.split("\n");
    let jugadores = [];

    for (let i = 0; i < lineas.length; i++) {
        let lineaActual = lineas[i].trim();

        if (lineaActual === "") {
            continue;
        }

        let trozos = lineaActual.split(",");
        let nombre = trozos[0] ? trozos[0].trim() : "Desconocido";
        let puntos = trozos[1] ? parseInt(trozos[1].trim(), 10) : 0;

        let jugadorExistente = jugadores.find(j => j.nombre === nombre);

        if (jugadorExistente) {
            if (puntos > jugadorExistente.puntos) {
                jugadorExistente.puntos = puntos;
            }
        } else {
            jugadores.push({ nombre: nombre, puntos: puntos });
        }
    }

    jugadores.sort((a, b) => b.puntos - a.puntos);

    let mejores = jugadores.slice(0, 10);

    let codigoHtml = "";
    let posicion = 0;

    for (let jugador of mejores) {
        posicion++;

        let claseFila = "";

        if (posicion === 1) { claseFila = "top1"; }
        if (posicion === 2) { claseFila = "top2"; }
        if (posicion === 3) { claseFila = "top3"; }

        codigoHtml += "<tr class='" + claseFila + "'>";
        codigoHtml += "  <td class='posicion'>" + posicion + "</td>";
        codigoHtml += "  <td>" + jugador.nombre + "</td>";
        codigoHtml += "  <td>" + jugador.puntos + "</td>";
        codigoHtml += "</tr>";
    }

    tabla.innerHTML = codigoHtml;
}

cargarDatos();

setInterval(cargarDatos, 5000);