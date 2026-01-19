const arrayPalabras = [];
let mapa;
//hacemos una primera lectura adelantada
var palabra = prompt("Escriba una palabra (o nada si desea acabar)");
while (palabra != null && palabra != "") {
  arrayPalabras.push(palabra);
  palabra = prompt("Escriba una palabra (o nada si desea acabar)");
}
//ordenamos el array
arrayPalabras.sort((a, b) => a.localeCompare(b, "es"));
//convertimos en mapa
mapa = mapaRepeticiones(arrayPalabras);
//recorremos el mapa y mostramos las repeticiones
for ([palabra, cont] of mapa) {
  document.body.innerHTML += `<p>${palabra}, ${cont} repeticiones`;
} 

function mapaRepeticiones(array){
    if(array instanceof Array==false){
        //no es un array
        return null;
    }
    else{
        let mapa=new Map();
        //en este caso llamamos clave a cada valor del array
        //porque serán las claves del mapa
        for(let clave of array){
            //comprobamos si el valor está en el mapa
            if(mapa.get(clave)!=undefined){
                //si lo está incrementamos el contador
                mapa.set(clave,mapa.get(clave)+1);
            }
            else{
                //si no, la añadimos con contador a 1
                mapa.set(clave,1);
            }
        }
        return mapa;
    }
} 