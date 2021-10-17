package fibonacci;

import java.util.HashMap;
import java.util.Map;

public class Fibonacci {
    
    public static void main(String[] args) {
        System.out.println(fibo1(5));
        System.out.println(fibo2(5));
        System.out.println(fibo3(5));
        System.out.println(fibo4(5));
        System.out.println(fibo5(5));
        
    }
    
    // Algoritmo recursivo
    static int fibo1(int n) {
        if (n < 2)
            return 1;
        else
            return fibo1(n - 1) + fibo1 (n - 2);
    }
    
    // Algoritmo recursivo con memoria
    static Map<Integer, Integer> memoria = new HashMap<Integer, Integer>();
    
    static int fibo2(int n) {
        if (n < 2)
            return 1;
        Integer resultado = memoria.get(n);
        if (resultado != null)
            return resultado;
        resultado = fibo2(n - 1) + fibo2(n - 2);
        memoria.put(n, resultado);
        return resultado;
    }
    
    // Algoritmo con memoria limitada
    private static int[] tabla = new int[20];
    
    public static int fibo3(int n) {
        if (n < 2)
            return 1;
        if (n < tabla.length) {
            int resultado = tabla[n];
            if (resultado > 0)
                return resultado;
            resultado = fibo3(n - 1) + fibo3(n - 2);
            tabla[n] = resultado;
            return resultado;
        }
        return fibo3(n - 1) + fibo3(n - 2);
    }
    
    // Algoritmo iterativo
    static int fibo4(int n) {
        int n0 = 1;
        int n1 = 1;
        for (int i = 2; i <= n; i++) {
            int ni = n0 + n1;
            n0 = n1;
            n1 = ni;
        }
        return n1;
    }
    
    // Algoritmo directo
    static final double SQRT_5 = Math.sqrt(5);
    
    static int fibo5(int n) {
        if (n < 2)
            return 1;
        n += 1;
        double t1 = Math.pow((1 + SQRT_5) / 2, n);
        double t2 = Math.pow((1 - SQRT_5) / 2, n);
        double t = (t1 - t2) / SQRT_5;
        return (int) Math.round(t);
    }
}
