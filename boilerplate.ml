(* GRADE:  100% *)
(* Question 1 *)
(* TODO: Write your own tests for the fact function.
         See the provided tests for double, above, for how to write test cases.
         Remember that you should NOT test cases for n < 0.
*)
(* TODO: Correct these tests for the fact function. *)
let fact_tests = [
  (0, 1.);
  (1, 1.);
  (2, 2.);
  (3, 6.);
  (4, 24.);
  (5, 120.);
  (6, 720.);
]

(* TODO: Correct this implementation so that it compiles and returns
         the correct answers.
*)
let rec fact (n: int): float = match n with
  | 0 -> 1.0
  | _ -> (float n) *. fact (n-1)


(* TODO: Write your own tests for the binomial function.
         See the provided tests for fact, above, for how to write test cases.
         Remember that we assume that  n >= k >= 0; you should not write test cases where this assumption is violated.
*)
let binomial_tests = [
  (* Your test cases go here. Correct the incorrect test cases for the function. *)
  ((0, 0), 1.); 
  ((1, 0), 1.);
  ((2, 0), 1.);
  ((10,1), 10.);
  ((10,2), 45.)
]

(* TODO: Correct this implementation so that it compiles and returns
         the correct answers.
*)
let binomial (n: int) (k:int) =
  if n < 0 then domain ()
  else (if k = n then (if k = 0 then 1. else domain ())
        else fact n /. (fact k  *. fact (n-k)))


(* TODO: Write a good set of tests for ackerman. *)
let ackerman_tests = [
  (* Your test cases go here *)
  ((0,0),1);
  ((1,0),2);
  ((0,1),2);
  ((1,1),3);
  ((2,0),3);
  ((0,2),3);
]

(* TODO: Correct this implementation so that it compiles and returns
         the correct answers.
*)
let ackerman (n, k)  =
  if n < 0 || k < 0 then domain ()
  else (let rec ack n k = match (n,k) with
      | (0 , _ ) -> k + 1 
      | (_ , 0 ) -> ack (n-1) 1
      | (_ , _ ) -> ack (n-1) (ack n (k-1))
     in ack n k)


(* Question 2: is_prime *)

(* TODO: Write a good set of tests for is_prime. *)
let is_prime_tests = [
(* Your tests go here *)
  (2, true);
  (3, true);
  (4, false);
  (5, true);
  (100, false)
]

(* TODO: Correct this implementation so that it compiles and returns
         the correct answers.
*)
let is_prime (n:int):bool =
  let rec check_division x = 
    (x * x > n) || (n mod x <> 0) && (check_division(x+1))
  in 
  if n < 2 then domain()
  else (n = 2) || (check_division 2)
    


(* Question 3: Newton-Raphson method for computing the square root
*)

let square_root_tests = [ 
  (1., 1.);
  (4., 2.);
  (9., 3.);
  (100., 10.)
]

let square_root a =
  let rec findroot x acc =
    if abs_float(x -. ((a/.x)+.x)/.2.0) < acc then ((a/.x)+.x)/.2.0
    else findroot (((a/.x)+.x)/.2.0) epsilon_float
  in
  if a > 0.0 then
    findroot 1.0 epsilon_float
  else domain ()

 
(* Question 4: Fibonacci*)

(* TODO: Write a good set of tests for fib_tl. *)
let fib_tl_tests = [
  (0, 1);
  (1, 1);
  (2, 2);
  (3, 3);
  (4, 5);
  (5, 8);
  (10, 89);
  (20, 10946)
]

(* TODO: Implement a tail-recursive helper fib_aux. *)
let rec fib_aux n a b = match n with
  |0 -> a
  |_ -> fib_aux (n-1) (a+b) (a)

(* TODO: Implement fib_tl using fib_aux. *)
let fib_tl n =
  if n < 0 then domain ()
  else fib_aux n 1 0
 
