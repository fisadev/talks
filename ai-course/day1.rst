1. (T) ¿Por qué Inteligencia Artificial? 

   * normalmente cuando programamos actuamos como alguien dictando 
     instrucciones a otro. Le decimos a la computadora: "quiero obtener un 
     resultado, y para ello vas a seguir estos pasos"
   * qué pasa cuando no sabemos qué pasos seguir para obtener un resultado?
     es algo no tan común cuando programamos. Querer que la computadora 
     encuentre el camino de pasos o la forma de obtener el resultado, sin que
     nosotros tengamos que conocerla antes.
   * pero por lo general no es algo que asuste, el enfoque que casi siempre 
     terminamos tomando es "probá todos los caminos y decime cuando encuentres
     en resultado válido"
     Hasta que alguna vez nos chocamos con una pared.
   * veamos algunos ejemplos simples

   1. Ejemplos de problemas para despertar el interés en el tema.

      * qué pasa con problemas simples como el 8puzzle?
      * hasta un chico puede resolverlos, pero la computadora?
      * primera idea para resolver el 8puzzle: 
        árbol recorriendo todos los posibles caminos hasta la meta
      * ver cantidad de nodos, memoria y tiempo que llevaría
      * evidentemente la mente del chico hace algo diferente
      * evidentemente nuestro programa tiene que poder imitar a la mente del 
        chico. O no?

   2. Elección de un problema particular para aplicar todo lo que se vaya 
      viendo a lo largo del taller.

      * nos vamos a quedar con dos problemas de ejemplo:
        * 8puzzle
        * 8queens
      * para algunos casos muy especiales puede que usemos algún otro ejemplo 
        más evidente
      * pero en realidad lo que veamos se puede aplicar a muchísimos tipos de 
        problemas

   3. Introducción al concepto de Inteligencia Artificial, enfoques posibles, 
      rama elegida para el taller.

      * hay muchas diciplinas que caen dentro del nombre de "inteligencia 
        artificial", pero que son cosas muy, muy diferentes
      * explicación del cuadrante: 
        * racional o como humano?
          * definimos racional como tomar las decisiones que **con la 
            información disponible** podemos deducir que nos acercan más al 
            objetivo propuesto
          * evidentemente el humano no siempre es racional
        * imitar a la naturaleza o diseñar algoritmos más matemáticos?
          * entender el cerebro e intentar simularlo? redes neuronales por 
            ejemplo
          * o tratar de expresar en algoritmos el proceso de búsqueda de una 
            solución? abstracciones que conocemos y usamos al programar
      * nosotros vamos a ir por el lado de algoritmos matemáticos para lograr 
        racionalidad. Vamos a construir la lógica para que nuestros programas
        sepan encontrar soluciones a los problemas que les planteamos, por sí
        mismos.
        (nada de robots que lloran :)

2. (T) Agentes racionales, tipos de ambientes, limitaciones. 

   * vamos a empezar a definir más formalmente lo que vamos a desarrollar:
     vamos a programar **agentes racionales**, que queremos que logren un 
     **objetivo** por medio de la aplicación de **acciones** en el **ambiente**

   * agente:
     * racional, por lo que ya explicamos antes
     * va a poseer algún tipo de **sensores** con los cuales percibir el 
       ambiente
     * va a poseer algún tipo de **actuadores** para realizar sus acciones
     * puede o no tener algún tipo de **memoria** y **aprender** o no a partir
       del resultado de sus acciones en el ambiente.
     * podemos implementar muchos tipos de agentes racionales (no vemos todos)
       * por ejemplo: agente basado en reflejos, con una tabla de 
         estímulo-acción. Es re fácil de implementar, pero no siempre viable,
         y hay que reescribirlo completo cuando cambia el objetivo.
       * en nuestro caso vamos por los agentes basados en objetivos: tiene que
         elegir la acción que mejor lo acerque a su objetivo, evaluando de
         alguna manera las consecuencias de sus acciones en el mundo percibido.
         Cambiar el objetivo no implica cambiar su programación, pero son más
         difíciles de crear. Lo bueno cuesta :)
       * el siguiente paso son los agentes basados en utilidad, que no vamos a
         ver
      * su "ciclo" tiene 3/4 pasos:
        * percibe
        * delibera (planea)
        * actúa
        * [feedback?]
      * nosotros **solo** vamos a programar la parte de **deliberar**, no nos
        interesa ver cómo nos llegaron las percepciones, ni cómo después
        ejecutar las acciones planeadas. Ni vamos a tener feedback.
        Ej de 8puzzle: hacemos un programa que a partir de conocer cómo está
        el tablero, te da la lista de movimientos para llegar a la meta.
        No tiene un ocr para percibir el tablero, ni brazos para mover las
        piezas, ni nada que después le diga "cuando quise mover esta pieza, se
        trabó".

    * ambiente
      * qué tanto podemos observar?
      * cambia mientras estamos deliberando? -> para nosotros no
      * nuestras acciones tienen consecuencias predecibles? -> para nosotros sí
      * hay otros agentes compitiendo? -> para nosotros no
      * hay más aspectos para analizar, pero los dejamos de lado

3. (T) Noción básica de lo que es un problema de búsqueda. Diferencia entre 
   buscar un estado y buscar un camino de acciones.

   * un problema de búsqueda es un problema que podemos expresar como un "mapa"
     de posibles estados del mundo, entre los cuales podemos movernos con 
     acciones, y partiendo de un estado inicial, buscamos una de tres cosas: 
     * encontrar un estado meta, 
     * encontrar el mejor estado que podamos en base a algún criterio (fuzzy!)
     * conociendo un estado meta, encontrar el camino desde nuestro inicial
   * esos tres tipos de objetivos diferentes pueden cambiar mucho nuestro
     enfoque, más tarde lo vamos a entender, pero tengámoslo en cuenta
   * dónde se ubican nuestros ejemplos?
     * 8puzzle: encontrar camino a la meta
     * 8queens: encontrar meta, o encontrar más cercano, depende
   * lo que habíamos hecho en nuestro ejemplo inicial con el 8puzzle era
     justamente "navegar" el mapa buscando el camino hasta la meta, de una
     forma bastante "bruta"

4. (T+P) Formulación de problemas de búsqueda (elementos que debemos entender y 
   definir de nuestro problema).

   * para implementar nuestro agente, vamos a ver que ya existen muchos 
     algoritmos. Ya están probados, y programados! Pero lo que nosotros tenemos
     que darles como entrada, es la definición de nuestro problema.
     Qué tiene que tener esa definición? va a depender del algoritmo que 
     usemos, pero va a ser un subconjunto de estas cosas:

   1. Representación del estado.

      * Hablamos de navegar un mapa de estados, así que vamos a necesitar
        alguna forma de representar el estado del mundo.
        Tiene que ser:
        * completo, una foto de la info que tenemos del mundo que permita
          "rearmarlo" a partir de la foto, entender por completo cómo estaba
        * pero a la vez abstracto, sacando los detalles que a nuestro problema
          no interesan.
      * ej: en el 8puzzle nos interesa la posición de cada una de las fichas,
        no solo la última que hayamos movido. Pero a la vez, no nos interesa
        de qué color es la remera del dueño del puzzle, no es info relevante.

      * es **importantísimo** que logremos una buena representación del mundo.
        Puede afectar muchísimo a la performance del algoritmo.
        ej: de estado para 8queens, con 64 posibles acciones iniciales o solo
        8.

   2. Definición de las acciones posibles desde cada estado.

      * esto se descompone en dos partes:
        * función actions: qué acciones se pueden aplicar a partir de un estado
          particular del mundo? acciones válidas.
          firma: actions(estado) -> lista_acciones
        * función result: cuál es el estado resultante de aplicar X acción al
          mundo, cuando estaba en un estado determinado?
          firma: result(estado, acción) -> estado_resultado

      * a la combinación de ambas definiciones lo llamamos "modelo de 
        transición de estados". Es básicamente el cómo navegar el mapa, porque
        no lo tenemos en memoria, sino que se va a ir armando a medida que 
        recorramos.

   3. Función de costo.

      * Las acciones que realicemos van a tener algún costo, y ese valor va a
        ser útil para algunos algoritmos que van a intentar encontrar el camino
        más "barato" hasta la meta si es que hay varios.
      * En la formalización del problema, lo vamos a expresar como una función
        que dado un estado de partida, una acción, y un estado resultante, 
        devuelve el costo de haber realizado dicha acción partiendo de un 
        estado y llegando al otro.
        firma: cost(estado1, acción, estado2) -> costo_de_aplicar_acción

   4. Función de comprobación de meta o función de valoración.

      * cómo sabemos que un estado es meta? o que es mejor que otro?
      * si estamos en el caso de encontrar una meta, o el camino a una meta, es 
        una función que nos dice si un estado es meta o no.
        firma: is_goal(estado) -> bool_es_meta
      * si estamos en el caso de encontrar "el mejor estado", es una función
        que le asigna un valor numérico a un estado dado.
        firma: value(estado) -> int_valor

   5. Función heurística.

      * esta va a ser un poco la magia de algunos de los mejores algoritmos.
        Por ahora no profundizamos demasiado, después lo veremos. Pero la idea
        general es que es una función que dado un estado, nos "estima" más o
        menos cuánto nos falta para llegar a la meta desde ese estado.
        firma: heuristic(estado) -> int_cuanto_falta_para_meta
      * tiene una condición muy importante, que es que para ser válida, 
        **nunca** tiene que sobreestimar. No hay problema con que subestime.

5. (T) Algoritmos para resolver problemas de búsqueda. Idea general y 
   diferentes tipos.
  
   * vamos a partir de esa idea "bruta" que habíamos tenido inicialmente, y de
     a poco la vamos a mejorar. La idea es recorrer el grafo (mapa) de estados.
   * hay varios tipos de algoritmos, pero en especial podemos identificar 2
     grandes grupos:

     * búsqueda tradicional: algoritmos que arman un árbol, como el de nuestra
       idea inicial. Pueden diferir en cómo van armando/recorriendo ese árbol.
       Son más seguros de encontrar la meta o el camino. Pero no sirven para
       casos donde queremos ir "mejorando" un estado hasta donde se pueda, sin
       saber si es meta o no. Necesitan saber cuándo algo es meta o no.
       Siempre requieren mucha memoria.
       * tenemos dos subgrupos:
         * búsqueda no informada: el algoritmo no tiene información de qué 
           estados están más cerca de la meta y qué estados más lejos. No usa
           la función heurística.
         * búsqueda informada: el algoritmo usa la función heurística para 
           saber qué estados son más probables de llevar a la meta que otros.

     * búsqueda local: algoritmos que no llevan todo el árbol en memoria, sino
       solo un pequeño grupo limitado de estados, sin información sobre de 
       dónde vinieron.
       No garantizan encontrar la meta, no pueden darnos "caminos" porque no
       tienen el árbol (solo hojas sueltas), pero no requieren **nada** de
       memoria. Y sirven en los casos que queremos encontrar "el mejor estado 
       posible", pero no para encontrar caminos, y casi que no para encontrar
       una meta.
       Para problemas de "mejorar", no de "llegar".

6. (T) Presentación de la biblioteca a usar en la práctica: SimpleAI. Ventajas 
   de usar python para este tipo de programación.

7. (P) Instalación de las herramientas necesarias en las pcs de los asistentes.


