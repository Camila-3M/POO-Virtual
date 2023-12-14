
package com.mycompany.crearpersona;


public class CrearPersona {

    public static void main(String[] args) {
        Persona p1 = new Persona();
        
        p1.nombre = "Laura";
        System.out.println(p1.nombre);
        
        p1.apellido = "Aguas";
        System.out.println(p1.apellido);
        
        p1.edad = 20;
        System.out.println(p1.edad);
        
        p1.SetCi("1722334455");
        System.out.println(p1.GetCI());
        
    }
}
