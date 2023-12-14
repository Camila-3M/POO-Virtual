
package com.mycompany.vehiculo;


public class Carro {
    public String marca;
    public String color;
    public int añofabricacion;
    private String placa;
    
    //Metodo Setter: Establecemos la placa.
    public void SetPlaca(String placa){
        this.placa = placa;
    }
    
    //Metodo Getter: Mostramos la placa.
    public String GetPlaca(){
        return placa;
    }
    
    public void AbrirPuerta (){
        System.out.println("Se abrió la puerta.");
    }
}
