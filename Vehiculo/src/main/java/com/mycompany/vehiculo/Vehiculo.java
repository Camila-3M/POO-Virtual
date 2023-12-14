
package com.mycompany.vehiculo;


public class Vehiculo {

    public static void main(String[] args) {
        Carro c1 = new Carro();
        Moto m1 = new Moto();
        
        System.out.println("Carro");
        
        c1.marca = "Toyota";
        System.out.println("La marca es: "+c1.marca);
        
        c1.color = "Amarillo";
        System.out.println("El color es: "+c1.color);
        
        c1.añofabricacion = 2005;
        System.out.println("El año de fabricación es: "+c1.añofabricacion);
        
        c1.SetPlaca("PCZ-4409");
        System.out.println("La placa es: "+c1.GetPlaca());
        
        c1.AbrirPuerta();
        
        System.out.println("Moto");
        
        m1.marca = "Yamaha";
        System.out.println("La marca es: "+m1.marca);
        
        m1.color = "Negro";
        System.out.println("El color es: "+m1.color);
        
        m1.añofabricacion = 2018;
        System.out.println("El año de fabricación es: "+m1.añofabricacion);
        
        m1.SetPlaca("HU-856L");
        System.out.println("La placa es: "+m1.GetPlaca());
        
        m1.LevantarRueda();
    }
}