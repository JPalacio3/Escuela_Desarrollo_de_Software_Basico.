let c = 0;

// Break: ROMPE EL BUCLE EN UNA DETERMINADA PARTE EN ESPECÍFICO
while (c < 10) {
    c++;
    if (c === 5) {
        console.log('Aqui se termina el bucle usando break');
        break;
    }
    console.log(c);
}

//continue: SALTA LA EJECUCIÓN DEL BUCLE Y SALTA A LA SIGUIENTE EJECUCIÓN A PARTIR DE UN DETERMINADO PUNTO
while (c < 10) {
    c++;
    if (c === 5) {
        console.log('Aqui se termina el bucle usando continue');
        continue;
    }
    console.log(c);
}
