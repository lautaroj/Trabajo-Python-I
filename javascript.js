// 1)Complete en un script que muestre como resultado los elementos f, g y h. Explique la solución.
//   `lettters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]`

    function show(letters)
        {
            for(var x=0; x<letters.length;x++)
            {
                if(letters[x]=="f" || letters[x]=="g")
                {
                    return letters[x];
                }
                else if(letters[x]=="h")
                {
                    return letters[x];
                }
            }
        }
    //Se toma cada valor del array, y se lo devuelve si cumple el requerimiento de igualdad con alguna de las letras.

// 2)Tomando dos valores del usuario, calculamos la multiplicación
    function producto(x, y)
    {
        return x*y;
    }

// 3)Mostrar la salida de una la lista de 5 números flotantes ingresados por el usuario.
    function show(arr)
    {
        for(var x=0; x<5; x++)
        {
            return arr[x];
        }
    }

// 6)Partiendo de la lista a continuación, mostrá solamente los números divisibles por 5. La iteración se debe detner cuando encuentre un número mayor a 150
    var list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
    for(var x=0; x<list1.length; x++) {
        if(list1[x]%5 == 0)
        {
            if(list1[x]<151)
            {
                return list1[x];
            }
        }
    }

/* 7)Quiero que imprimas el siguiente patrón. Fundamenta la solución.
    5 4 3 2 1 
    4 3 2 1 
    3 2 1 
    2 1 
    1*/
    var piramide = "";
    for(var x=5;x>=1;x--)
    {
        for(var y=x;y>=1;y--)
        {
            piramide+=y+" ";
        }
        console.log(piramide);
        piramide = "";
    }
    //Se crea un loop en el que por cada vuelta de "x", se genera un "y" igualado a "x" que sigue descendiendo hasta
    //igualar a 1. Por lo tanto, al ser "x"=5, "y" imprime 4321, y así sucesivamente hasta llegar a "x"=1, donde se corta el loop.

/* 11)Partiendo de dos strings: str1 y str2, necesito una función que cree una nueva y única cadena formada por el primero,
el medio y el último carácter de str1 y str2*/
    function mixStr(str1,str2)
    {
        var primeraletra1 = str1.charAt(0);
        var primeraletra2 = str2.charAt(0);
        var letramedio1 = str1.charAt((str1.length)/2);
        var letramedio2 = str2.charAt((str2.length)/2);
        var letrafinal1 = str1.charAt((str1.length)-1);
        var letrafinal2 = str2.charAt((str2.length)-1);

        return primeraletra1+primeraletra2+letramedio1+letramedio2+letrafinal1+letrafinal2;
    }
// 12)Necesito saber que un script me pueda informar cuantas ocurrencias se dan por cada letra en el siguiente string “acoltrapersobrabilacodaNaNy!
    var palabra = "acoltrapersobrabilacodaNaNy";
    var letras = palabra.split("");
    var contador = [];
    for(var x = 0; x<letras.length; x++ )
    {
        if(contador[letras[x]]==undefined)
        {
        contador[letras[x]] = 0;
        }
        contador[letras[x]]++;
    }
    for(var x in contador)
    {
        return x+": "+contador[x]+"<br>";
    }

/* 13)Un vecino de Cañuelas cría gallínas, vacas y cerdos. Necesitamos saber cuantas patas hay en total entre todas las especies.
Ahora resulta que un programador anterior, le envió un e-mail al granjero con el siguiente array y el mensaje, "perdón, pero no puedo seguir"*/
//  animales(12,23,11) = 12*2 23*4 11*4
    function animales(gallinas, vacas, cerdos)
    {
        patasG = gallinas*2;
        patasV = vacas*4;
        patasC = cerdos*4;

        return patasG+patasV+patasC;
    }
    animales(12,23,11);