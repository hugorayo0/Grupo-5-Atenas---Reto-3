function comprobar(){
  let Contador = 0;

  for (i =0; i<=TOTAL_PREGUNTAS; i++){
    let seleccion = document.querySelector(`input[name='pregunta${i}']:checked`);
    if (seleccion != null){
      if (seleccion.value === preguntasData.preguntas[`pregunta${i}`].correcta){
        Contador += 1;
        seleccion.nextElementSibling.style.color="green";
      } else{
        seleccion.nextElementSibling.style.color="red";
      }
    }
  }
  let Porcentaje = ((Contador / TOTAL_PREGUNTAS) * 100).toFixed(0)
  const resultado = document.getElementById("resultado");
  resultado.innerHTML = "Clasificación: "+Contador+"/20.<br>Porcentaje: "+Porcentaje+"%"
}
function BtnProduccion(){
    window.location.href = "Fabrica.html"
}
