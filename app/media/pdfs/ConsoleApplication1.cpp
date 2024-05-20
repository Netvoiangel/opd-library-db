#define size 20
#include <stdio.h>
#include <math.h>
void setka(double a, double b, double n, double s[size]) {
    for (int i = 0; i <= n; i++) {
        s[i] = a + (b - a) / n * i;
    }
}
double s(double a, double b, double n, int i) {
    return a + (b - a) / n * i;
}
double f(double x) {
    return exp(x) * (log(fabs(x)) + 1);
}
double f_d(double x, double y) {
    return exp(x) / x + y;
}
double euler(double x, double y1, double h) {
    double y2, ys;
    ys = y1 + h / 2 * f_d(x, y1);
    y2 = y1 + h * f_d(x + h / 2, ys);
    return y2;
}
double euler2(double x, double y, double h, int it) {
    double y1, y2;
    int n = pow(2, it);
    y1 = euler(x, y, h / n);
    for (int i = 1; i < n; i++) {
        y2 = euler(x + h / n * i, y1, h / n);
        y1 = y2;
    }
    return y2;
}
int main(){
    double x, y1, y2, ys, eps = 1e-10, err, mx = 0;
    double a = 1, b = 3;
    int n, it;
    int p = 5;
    for (eps = 1e-1; eps >= 1e-10; eps /= 10) {
        y1 = f(a);
        //printf("%.16lf ", y1);
        n = pow(2, p);
        double h = (b - a) / n;
        x = a;
        mx = 0;
        while (x <= b) {
            y2 = euler(x, y1, h);
            //printf("%lf ", y2);
            it = 0;

            do {
                ys = y2;
                it++;
                y2 = euler2(x, y1, h, it);
                err = fabs(ys - y2) / 3;
            } while (err > eps);
            
            //if (mx < fabs(y2 - f(x + h))) mx = fabs(y2 - f(x + h));
            //printf("%.16lf\n ", fabs(y2 - f(x)));
            //printf("%d ", it - 1);
            y1 = y2;
            x += h;
        }
        printf("%.16lf ", fabs(y1 - f(x)));
        //printf("%d ", it);
        //printf("%.16lf ", mx);
    }
    /*printf("\n\n");
    for (int i = 0; i <= n; i++) {
        printf("%.4lf ", (x[i]));
    }*/
}
