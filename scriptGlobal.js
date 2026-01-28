const canvas = document.querySelector("canvas");
const ctx = canvas.getContext("2d");
canvas.style.background = "lightgray";

ctx.beginPath();
ctx.strokeStyle="black";
ctx.lineWidth = 8;
ctx.strokeRect(0, 165, 700, 35);
ctx.fillStyle = "dimgray";
ctx.fillRect(0, 165, 700, 35);
ctx.closePath();

const BotonRuedas = document.getElementById("BotonRuedas")
BotonRuedas.addEventListener("click", Ruedas);
let ContadorCarroceria = 0;
let ContadorRuedas = 0;
let ContadorVentanas = 0;
let ContadorMotor = 0;
let ContadorLuces = 0;
let ContadorCoches = 0;

const ContenedorHistorial = document.getElementById("ContenedorHistorial");
ContenedorHistorial.style.display="none";
const ContenedorTiempos = document.getElementById("ContenedorTiempos");
ContenedorTiempos.style.display="none";
// Funcion para montar las ruedas
function Ruedas() {
    if (ContadorCarroceria == 1){
        ctx.fillStyle = "black";
        ctx.beginPath();
        ctx.fillStyle = "black";
        ctx.arc(50, 150, 15, 0, Math.PI * 2);
        ctx.fill();
        ctx.closePath();

        ctx.fillStyle = "black";
        ctx.arc(150,150,15,0, Math.PI * 2);
        ctx.fill();
        ctx.closePath();
        ContadorRuedas = 1;
    }
    else {
        MensajeError1();
    }
}

const BotonCarroceria = document.getElementById("BotonCarroceria")
BotonCarroceria.addEventListener("click", Carroceria);
// Funcion para montar la carroceria
function Carroceria() {
    if (ContadorCarroceria == 0){
        const ColorCarroceria = document.getElementById("ColorCarroceria");
        ctx.beginPath();
        ctx.fillStyle = ColorCarroceria.value;
        ctx.fillRect(15, 110, 170, 40);
        ctx.closePath();
    
        ctx.beginPath();
        ctx.fillStyle = ColorCarroceria.value;
        ctx.fillRect(40, 70, 120, 40);
        ctx.closePath();
        ContadorCarroceria = 1;
    }
}

const BotonVentanas = document.getElementById("BotonVentanas")
BotonVentanas.addEventListener("click", Ventanas);
// Funcion para montar las ventanas
function Ventanas() {
    if (ContadorCarroceria == 1){
    ctx.beginPath();
    ctx.fillStyle = "lightblue";
    ctx.fillRect(55, 80, 40, 30);
    ctx.stroke();
    ctx.closePath();
    
    ctx.beginPath();
    ctx.fillStyle = "lightblue";
    ctx.fillRect(105, 80, 40, 30);
    ctx.stroke();
    ctx.closePath();
    ContadorVentanas = 1;
    }
    else {
        MensajeError1();
    }
}

const BotonMotor = document.getElementById("BotonMotor")
BotonMotor.addEventListener("click", Motor);
// Funcion para montar el motor
function Motor() {
    if (ContadorCarroceria == 1){
        ContadorMotor = 1;
    }
    else {
        MensajeError1();
    }
}

const BotonLuces = document.getElementById("BotonLuces")
BotonLuces.addEventListener("click", Luces);
// Funcion para montar las luces
function Luces() {
    if (ContadorCarroceria == 1){
    ctx.beginPath();
    ctx.fillStyle = "yellow";
    ctx.fillRect(170, 120, 15, 10);
    ctx.stroke();
    ctx.closePath();
    
    ctx.beginPath();
    ctx.fillStyle = "yellow";
    ctx.fillRect(15, 120, 3, 10);
    ctx.stroke();
    ctx.closePath();
    ContadorLuces = 1;
    }
    else {
        MensajeError1();
    }
}

const BotonEnviar = document.getElementById("BotonEnviar")
BotonEnviar.addEventListener("click", Enviar);
// Funcion en la que se comprueba si esta montado correctamente y se envia si no faltan cosas por colocar.
function Enviar() {
    if (ContadorCarroceria && ContadorRuedas && ContadorVentanas && ContadorMotor && ContadorLuces == 1){
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ContadorCarroceria = ContadorRuedas = ContadorVentanas = ContadorMotor = ContadorLuces = 0
        const MensajeError = document.getElementById("MensajeError");
        MensajeError.innerText="";
        ctx.lineWidth = 4;
        ctx.strokeStyle = "black";
        const CantidadCoches = document.getElementById("CantidadCoches");
        ContadorCoches += 1;
        CantidadCoches.textContent="Cantidad de coches producida: "+ ContadorCoches;
        ctx.beginPath();
        ctx.strokeStyle="black";
        ctx.lineWidth = 8;
        ctx.strokeRect(0, 165, 700, 35);
        ctx.fillStyle = "dimgray";
        ctx.fillRect(0, 165, 700, 35);
        ctx.closePath();
        const Tiempos = document.getElementById("Tiempos");
        if (ContenedorTiempos.style.display=="none"){
            ContenedorTiempos.style.display="block";
        }
        // Mostrar el tiempo que tarda en cada parte para mostrar de una manera sencilla el cuello de botella en la línea de producción
        Tiempos.innerHTML="<div class='caja'>Carroceria:5s</div><div class='caja'>Ruedas: 5s</div><div class='caja'>Ventanas: 5s</div><div class='caja'>Motor: 20s</div><div class='caja'>Luces: 5s</div>";
        Historial();
    }
    else{
        const MensajeError = document.getElementById("MensajeError");
        MensajeError.innerHTML="<span style='color:red;'>No se puede enviar faltan cosas por colocar.</span>"
    }
}
// Funcion para guardar el historial de los coches producidos en una hora y dia determinado.
function Historial() {
    const Historial = document.getElementById("Historial");
    const ContenedorHistorial = document.getElementById("ContenedorHistorial");
    if (ContenedorHistorial.style.display=="none"){
        ContenedorHistorial.style.display="block";
    }

    const timestamp = Date.now();
    const date = new Date(timestamp);

    const formattedDate = date.toLocaleDateString();
    const formattedTime = date.toLocaleTimeString();
    
    let dia = date.getDate();
    if (dia <=9){
        dia = "0"+dia;
    }
    let mes = date.getMonth()+1;
    if (mes <= 9){
        mes = "0"+mes;
    }
    let minutos = date.getMinutes();
    if (minutos <=9){
        minutos = "0"+minutos;
    }
    let segundos = date.getSeconds();
    if (segundos <=9){
        segundos = "0"+segundos;
    }
    const fecha = dia+"/"+ mes+"/"+ date.getFullYear();
    const hora = date.getHours()+":"+minutos+":"+segundos;
    
    Historial.innerHTML +="Coche producido a las "+hora+ " el "+fecha+"<br>";
    Historial.style.paddingBottom="5px";
    Historial.style.fontSize="16px";
}
// Funcion para mostrar mensaje de error
function MensajeError1() {
    const MensajeError = document.getElementById("MensajeError");
    MensajeError.innerHTML="<span style='color:red;'>Debes poner primero la carroceria.</span>"

}