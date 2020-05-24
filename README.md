# Ejemplo_Flask

Principios usados:

Principio de responsabilidad única puesto que cada clase debe realizar únicamente un trabajo, separando así qué funcionalidades tiene que
cumplir cada clase y que en caso de requerir modificaciones sólo se tenga que modificar una única cosa y esta se pueda encontrar con 
facilidad.
Tomando el ejemplo adjunto, la clase Banda crea una colección de músicos y les asigna sus respectivos instrumentos, cada músico tendrá un
instrumento el cual podrá tocar y preparar, y la clase Instrumento define la forma en que se tocará y prepará cada instrumento que herede
de esta

El principio de sustitución de Liskov está presente en el ejercicio ya que cuando heredamos de una clase padre, podemos usar cualquiera de
estos elementos y esto no afectará el comportamiento de la clase padre.
En el ejemplo vemos que muchos instrumentos heredan de la clase Instrumento, sin embargo, Instrumento nunca es modificada, sino que cada
nuevo instrumento que heredó de su clase padre crea su propio comportamiento

El principio de segregación de interfaces nos dice que no se deben implementar interfaces de las cuales no usaremos la totalidad de sus
métodos ya que esto nos obligaría a depender de métodos que no están acordes con lo que estamos modelando y a hacer excepciones 
innecesarias con el correcto uso de este principio
La interfaz dentro de este proyecto es Instrumento el cual hace uso de dos métodos, tocar y preparar, y, todos los instrumentos que
implementan esta interfaz pueden tocar y preparar a su manera, pero, no hay ninguno que no se pueda tocar o preparar, además de que
tampoco usan un método diferente a tocar o preparar, por lo que no hay que hacer ninguna excepción al momento de implementar nuestra 
interfaz Instrumento

![UML banda](https://user-images.githubusercontent.com/61293194/82743627-94966a80-9d33-11ea-88b8-b73048431fa4.png)


