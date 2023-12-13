
package com.mycompany.leccion;


public class Persona {
    public String nombre;
    public String apellido;
    public int edad;
    private String ci;
    
    //Metodo Setter: Establecemos el número de cédula.
    public void SetCi(String ci){
        this.ci = ci;
    }
    
    //Metodo Getter: Mostramos el número de cédula.
    public String GetCI(){
        return ci;
    }
}


