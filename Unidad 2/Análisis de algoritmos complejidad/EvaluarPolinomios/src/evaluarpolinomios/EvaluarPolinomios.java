package evaluarpolinomios;

public class EvaluarPolinomios {

    /*
    Programa para evaluar un polinomio P(x) de grado N. Sea coef el vector de coeficientes
    */
    public static void main(String[] args) {
        double polinomio [] = {2, 3.5, 6}; 
        System.out.println(evaluaPolinomio1(polinomio, 2));
        System.out.println(evaluaPolinomio2(polinomio, 2));
        System.out.println(evaluaPolinomio3(polinomio, 2));
        System.out.println(evaluaPolinomio4(polinomio, 2));
    }

    static double evaluaPolinomio1(double[] coef, double x) {
        double total = 0;
        for (int i = 0; i < coef.length; i++) {
            // bucle 1
            double xn = 1.0;
            for (int j = 0; j < i; j++) // bucle 2
                xn *= x;
            total += coef[i] * xn;
        }
        return total;
    }
    
    /*
    static double potencia(double x, int y) {
        double t;
        if (y == 0)
            return 1.0;
        if (y % 2 == 1)
            return x * potencia(x, y - 1);
        else {
            t = potencia(x, y / 2);
            return t * t;
        }
    }
    */
    static double potencia(double x, int y) {
        if (y == 0)
            return 1.0;
        if (y == 1)
            return x;
        if (y % 2 == 1)
            return x * potencia(x * x, y / 2);
        else
            return potencia(x * x, y / 2);
    }
    
    static double evaluaPolinomio2(double [] coef, double x) {
        double total = 0;
        for (int i = 0; i < coef.length; i++)
            total += coef[i] * potencia(x, i);
        return total;
    }
    
    static double evaluaPolinomio3(double[] coef, double x) {
        double xn = 1;
        double total = coef[0];
        for ( int i = 1; i < coef.length; i++) {
            xn *= x;
            total += coef[i] * xn;
        }
        return total;
    }
    
    static double evaluaPolinomio4(double[] coef, double x) {
        double total = 0;
        for (int i = coef.length - 1; i >= 0; i--)
            total = total * x + coef[i];
        return total;
    }
    
    
}
