const geom = (() => {

    'use strict';

    // Variables Globales
    const valueResult = document.getElementById('result');
    const pi = Math.PI;

    //Cuadrado
    const perimSq = document.getElementById('perimSquare');
    const areaSq = document.getElementById('areaSquare');

    //Triángulo
    const perimTri = document.getElementById('perimTriagule');
    const areaTri = document.getElementById('areaTriangule');

    //Circulo
    const radio = document.getElementById('radio');
    const diamCirc = document.getElementById('diamCircle');
    const perimCirc = document.getElementById('perimCircle');
    const areaCirc = document.getElementById('areaCircle');

    // área y perímetro del cuadrado
    const perimSquare = (side) => side * 4;
    const areaSquare = (side) => side * side;

    // Área y Perímetro del Triángulo
    const side1 = document.getElementById('side1');
    const side2 = document.getElementById('side2');
    const side3 = document.getElementById('side3');
    const base = document.getElementById('base');
    const altura = document.getElementById('altura');

    // Parímetro del cuadrado
    perimSq.addEventListener('click',() => {
        let inputSide = document.getElementById('inputSide');
        let value = Number(inputSide.value);

        const result = `El perímetro del cuadrado es ${perimSquare(value)} cm  `;
        valueResult.innerText = result;
    });

    //Área del cuadrado
    areaSq.addEventListener('click',() => {
        let inputSide = document.getElementById('inputSide');
        let value = Number(inputSide.value);

        const result = `El Área del cuadrado es ${areaSquare(value)} cm²  `;
        valueResult.innerText = result;
    });

    // Parimetro del Triángulo
    perimTri.addEventListener('click',() => {

        let output = Number(side1.value) + Number(side2.value) + Number(side3.value);
        let inputSide = document.getElementById('inputSide');
        let perim = Number(output);

        const result = `El Perímetro del Triángulo es ${perim} cm`;
        valueResult.innerText = result;
    })
    // Área del Triángulo
    areaTri.addEventListener('click',() => {

        let inputSide = document.getElementById('inputSide');

        const area = ((base.value) * (altura.value)) / 2;
        let result = Number(area);

        const salida = `El área del Triangulo es ${result} cm`
        valueResult.innerText = salida;
    })

    // Calcular el diámetro, Perimetro y Área del círculo
    diamCirc.addEventListener('click',() => {

        let diametter = radio.value;
        const operation = Number((diametter)) * 2;

        const result = `El Diámetro del Círculo es ${operation} cm`;
        valueResult.innerText = result;
    })

    perimCirc.addEventListener('click',() => {

        const perim = radio.value;
        const operation = 2 * pi * Number(perim);

        const result = `El Perímetro del Círculo es ${operation} cm`;
        valueResult.innerText = result;
    })

    areaCirc.addEventListener('click',() => {

        const area = radio.value;
        const operation = pi * (Number(area ** 2));
        const result = `El Área del Círculo es ${operation} cm²`;
        valueResult.innerText = result;
    })

    // return {

    //     cpc: calculatePerimSquare,
    //     cac: calculateAreaSquare,
    //     cpt: triangulePerim,
    //     cat: areaTriangule,
    //     cdc: diametroCircule,
    //     carc: areaCircle,
    //     cpec: perimCircle
    // }
})();


