
import '../css/estilos.css';
import wplogo from '../img/prueba.jpg';

export const saludar = (nombre) => {

    console.log('crando etiqueta H1');

    const h1 = document.createElement('H1');
    h1.innerText = `Hola ${nombre}`;
    document.body.append(h1);

    const img = document.createElement('IMG');
    img.src = wplogo;
    document.body.append(img);
}
