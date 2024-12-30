// Even Fibonacci numbers
// Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2,
// the first 10 terms will be: # 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
// By considering the terms in the Fibonacci sequence whose values do not exceed four million,
// find the sum of the even-valued terms.
// Answer:  4613732
fn main() {
    let mut a: u32 = 1;
    let mut b: u32 = 2;
    let mut c: u32;
    let mut soma: u32 = 0;

    /*
    for i in 1..11 {
        println!("{i} -> a = {}, b = {}", a, b);
        c = a + b;
        a = b;
        b = c;
        println!("Próximo número = {}", c);
    }

    a = 1;
    b = 2;
    c = 0;
    */

    while a < 4000000 {
       if a % 2 == 0 {
          println!("{soma} = {soma} + {a}");
          soma = soma + a; 
          println!("parcial: {}", soma);
       } 
       c = a + b;
       a = b;
       b = c;
    }
    println!("final: {}", soma);
}