:- begin_tests(my_suite).
:- use_module(assignment4).

% 1. tests for predicate add/3
test(add1_2) :- add(1,2,Z), Z =:= 3.
test(add15_25) :- add(15,25,Z), Z =:= 40.
test(add_neg) :- add(-1, 1, Z), Z =:= 0.

% 2. tests for predicate even/1  
test(even_number) :- even(4).
test(odd_number, [fail]) :- even(5).
test(negative_even) :- even(-2).

% 3. tests for predicate max/3 
test(max_first, [nondet]) :- max(5, 3, 5).
test(max_second, [nondet]) :- max(2, 4, 4).
test(max_equal, [nondet]) :- max(3, 3, 3).

% 4. tests for predicate factorial/2
test_factorial(zero) :- factorial(0, 1).
test_factorial(five) :- factorial(5, 120).
test_factorial(negative, [fail]) :- factorial(-1, _).

% 5. tests for predicate palindrome/1
test(empty) :- palindrome([]).
test(singleton) :- palindrome([a]).
test(even_palindrome) :- palindrome([r, a, c, e, c, a, r]).
test(not_palindrome, [fail]) :- palindrome([a, r, t, a]).

% 6. tests for predicate sum_list/2
test(empty) :- sum_list([], 0).
test(normal) :- sum_list([1,2,3], 6).
test(negative) :- sum_list([-1, -2, -3], -6).

% 7. tests for predicate list_length/2
test(empty) :- list_length([], 0).
test(singleton) :- list_length([1], 1).
test(normal) :- list_length([1,2,3], 3).

% 8. tests for predicate last_element/2
test(singleton, [nondet]) :- last_element([1], 1).
test(normal, [nondet]) :- last_element([1,2,3], 3).
test(empty, [fail]) :- last_element([], _).

% 9. tests for predicate member_of/2
test(member, [nondet]) :- member_of(1, [1,2,3]).
test(duplicate_member, [nondet]) :- member_of(1, [1,2,1]).
test(not_member, [fail]) :- member_of(4, [1,2,3]).

% 10. tests for predicate count_occurrences/3
test(count_1, [nondet]) :- count_occurrences(1, [1,2,3,1], 2).
test(count_2, [nondet]) :- count_occurrences(2, [1,2,3,1], 1).
test(count_3, [nondet]) :- count_occurrences(3, [1,2,3,1], 1).

:- end_tests(my_suite).
