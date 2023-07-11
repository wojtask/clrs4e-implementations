# Introduction to Algorithms, Fourth Edition &mdash; implementations of algorithms and data structures

![Build & test](https://github.com/wojtask/clrs4e-implementations/actions/workflows/build.yml/badge.svg)

### Overview

This project provides implementations of algorithms and data structures found in *Introduction to Algorithms, Fourth
Edition* by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest and Clifford Stein, as well as in the book's [
*Solutions to exercises and problems*](https://github.com/wojtask/clrs4e-solutions)
by Krzysztof Wojtas.
It serves as a companion to the solutions project helping in detecting and fixing bugs or limitations in the suggested
algorithms and data structures.

### Project objectives

* Adaptation of pseudocodes from the textbook and from the solutions to a real programming language.
* Implementation of algorithms and data structures with no explicit pseudocodes, yet precisely described in any of the
  source positions.
* Testing the implementations, especially those from the solutions, to increase confidence in algorithms correctness.
* Laying a foundation for a more sophisticated or practical library of algorithms and data structures for real use.

### Choice of a programming language

**Python 3** was chosen as a programming language for several reasons:

* Python is widely used in academia and is often the programming language of choice in introductory computer science
  courses.
  It is also widely used in many business applications.
  That makes it widely known in many communities, both academic and professional.
* Python's syntax and semantic show many similarities to pseudocode used in the textbook and the solutions.
  This enables easily transitioning between the two ways of expressing algorithms.
* Python does not limit developers with a single programming paradigm, making it elastic to adapt to different models
  found in pseudocodes.
* Python's typing system resembles the rules followed in pseudocode, particularly dynamic typing and duck typing.

The implementations are written in a way to be as close as possible to the algorithms in the textbook or in the
solutions, both in terms of syntax, and behavior.
This principle lead to using the procedural paradigm whenever possible and applicable, as well as translating pseudocode
instructions to most relevant Python statements or expressions.
Algorithms with no pseudocodes provided are implemented in a more flexible and often more concise way, more resembling
an idiomatic Python code.
The code in such cases is often appropriately structured to increase readability.

### History and Future

A couple of yeas ago I started implementing the algorithms from the second edition of the book while working on the
book's [solutions](https://github.com/wojtask/CormenSol) in Polish.
On GitHub there are legacy projects written in [Java](https://github.com/wojtask/CormenImpl)
and [Python](https://github.com/wojtask/CormenPy).
Soon after the fourth edition of the book got published, I deprecated those projects and began working on the solutions
to the fourth edition by migrating the old material, i.e. adapting it to the new edition and translating it to English.

I plan to adapt the implementations similarly by moving (and if necessary updating) the legacy code as I work on solving
exercises in each chapter.
Therefore, the progress on the implementations almost entirely depends on
the [progress](https://github.com/wojtask/clrs4e-solutions#progress) in the solutions.

I also plan to rethink the approach to testing by introducing two test categories &mdash; fast and deterministic unit
tests and robust property-based tests for generating random test cases.
The idea is to make writing tests easier and better control their execution.
By delegating the generation of test cases to libraries such as [Hypothesis](https://hypothesis.works/), I could
simplify many legacy tests that implemented their own test cases generators.
Also, keeping the two test types separated, I could better control when each are run, which would lead to speeding up
the testing process.
This can be achieved by running only the fast unit tests synchronously during build's test phase, and defining an
asynchronous mechanism for running the other tests.

### Pseudocode translation rules

The table below lists the rules followed in the implementation from translating pseudocode constructs into Python
instructions.

| Type                       | Pseudocode construct                                                                                                                                                                                                                                                                                                                                            | Translated Python code                                                                                     | Remarks                                                      |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| predefined constant        | ![](img/light/true.png#gh-light-mode-only)![](img/dark/true.png#gh-dark-mode-only)<br/>![](img/light/false.png#gh-light-mode-only)![](img/dark/false.png#gh-dark-mode-only)<br/>![](img/light/nil.png#gh-light-mode-only)![](img/dark/nil.png#gh-dark-mode-only)<br/>![](img/light/infinity.png#gh-light-mode-only)![](img/dark/infinity.png#gh-dark-mode-only) | `True`<br/>`False`<br/>`None`<br/>`math.inf`                                                               |                                                              |
| custom constant            | ![](img/light/constant.png#gh-light-mode-only)![](img/dark/constant.png#gh-dark-mode-only)<br/>![](img/light/dashed_constant.png#gh-light-mode-only)![](img/dark/dashed_constant.png#gh-dark-mode-only)                                                                                                                                                         | `RED`<br/>`NO_SUCH_PATH`                                                                                   | defined as a standalone or an enum value                     |
| variable                   | ![](img/light/variable.png#gh-light-mode-only)![](img/dark/variable.png#gh-dark-mode-only)<br/>![](img/light/decorated_variable.png#gh-light-mode-only)![](img/dark/decorated_variable.png#gh-dark-mode-only)<br/>![](img/light/dashed_variable.png#gh-light-mode-only)![](img/dark/dashed_variable.png#gh-dark-mode-only)                                      | `k`<br/>`k2_`<br/>`best_score`                                                                             |                                                              |
| object's attribute         | ![](img/light/attribute.png#gh-light-mode-only)![](img/dark/attribute.png#gh-dark-mode-only)<br/>![](img/light/dashed_attribute.png#gh-light-mode-only)![](img/dark/dashed_attribute.png#gh-dark-mode-only)<br/>![](img/light/indexed_attribute.png#gh-light-mode-only)![](img/dark/indexed_attribute.png#gh-dark-mode-only)                                    | `T.root`<br/>`A.heap_size`<br/>`x.key[i]`                                                                  | indexed attributes are implemented as an `Array`             |
| fixed function             | ![](img/light/fixed_function.png#gh-light-mode-only)![](img/dark/fixed_function.png#gh-dark-mode-only)                                                                                                                                                                                                                                                          | `out_degree(v)`                                                                                            | defined in a separate module                                 |
| assignment                 | ![](img/light/assignment.png#gh-light-mode-only)![](img/dark/assignment.png#gh-dark-mode-only)                                                                                                                                                                                                                                                                  | `x = y`                                                                                                    |                                                              |
| shifting a variable        | ![](img/light/increment.png#gh-light-mode-only)![](img/dark/increment.png#gh-dark-mode-only)<br/>![](img/light/decrement.png#gh-light-mode-only)![](img/dark/decrement.png#gh-dark-mode-only)                                                                                                                                                                   | `i += 1`<br/>`j -= 4`                                                                                      |                                                              |
| condition                  | ![](img/light/is_equal.png#gh-light-mode-only)![](img/dark/is_equal.png#gh-dark-mode-only)<br/>![](img/light/is_not_equal.png#gh-light-mode-only)![](img/dark/is_not_equal.png#gh-dark-mode-only)<br/>![](img/light/compound_condition.png#gh-light-mode-only)![](img/dark/compound_condition.png#gh-dark-mode-only)                                            | `x == y` or `x is y`<br/>`x != y` or `x is not y`<br/>`x < y or (x > y and not found)`                     | depends on the compared variables type: scalars or pointers  |
| procedure call             | ![](img/light/procedure_call.png#gh-light-mode-only)![](img/dark/procedure_call.png#gh-dark-mode-only)                                                                                                                                                                                                                                                          | `insertion_sort(A, n)`                                                                                     |                                                              |
| returning from a procedure | ![](img/light/return_no_value.png#gh-light-mode-only)![](img/dark/return_no_value.png#gh-dark-mode-only)<br/>![](img/light/return_single_value.png#gh-light-mode-only)![](img/dark/return_single_value.png#gh-dark-mode-only)<br/>![](img/light/return_multiple_values.png#gh-light-mode-only)![](img/dark/return_multiple_values.png#gh-dark-mode-only)        | `return`<br/>`return x`<br/>`return x, y`                                                                  |                                                              |
| exchanging values          | ![](img/light/exchange.png#gh-light-mode-only)![](img/dark/exchange.png#gh-dark-mode-only)<br/>![](img/light/swap.png#gh-light-mode-only)![](img/dark/swap.png#gh-dark-mode-only)                                                                                                                                                                               | `x, y = y, x`                                                                                              |
| signaling error            | ![](img/light/error.png#gh-light-mode-only)![](img/dark/error.png#gh-dark-mode-only)                                                                                                                                                                                                                                                                            | `raise ValueError('overflow')`                                                                             |
| printing                   | ![](img/light/print.png#gh-light-mode-only)![](img/dark/print.png#gh-dark-mode-only)                                                                                                                                                                                                                                                                            | `print(x)`                                                                                                 |
| creating a new array       | ![](img/light/new_array.png#gh-light-mode-only)![](img/dark/new_array.png#gh-dark-mode-only)                                                                                                                                                                                                                                                                    | `A = Array(0, n)`                                                                                          |
| referencing an array cell  | ![](img/light/array_cell.png#gh-light-mode-only)![](img/dark/array_cell.png#gh-dark-mode-only)                                                                                                                                                                                                                                                                  | `A[i]`                                                                                                     |
| creating a new set         | ![](img/light/new_set.png#gh-light-mode-only)![](img/dark/new_set.png#gh-dark-mode-only)                                                                                                                                                                                                                                                                        | `S = set()`                                                                                                |
| union of sets              | ![](img/light/set_union.png#gh-light-mode-only)![](img/dark/set_union.png#gh-dark-mode-only)                                                                                                                                                                                                                                                                    | `S \| {x}`                                                                                                 |
| set cardinality            | ![](img/light/set_cardinality.png#gh-light-mode-only)![](img/dark/set_cardinality.png#gh-dark-mode-only)                                                                                                                                                                                                                                                        | `len(S)`                                                                                                   |
| floor division             | ![](img/light/floor_division.png#gh-light-mode-only)![](img/dark/floor_division.png#gh-dark-mode-only)                                                                                                                                                                                                                                                          | `a // b`                                                                                                   |
| ceiling division           | ![](img/light/ceiling_division.png#gh-light-mode-only)![](img/dark/ceiling_division.png#gh-dark-mode-only)                                                                                                                                                                                                                                                      | `-(a // -b)`                                                                                               |
| minimum                    | ![](img/light/minimum.png#gh-light-mode-only)![](img/dark/minimum.png#gh-dark-mode-only)                                                                                                                                                                                                                                                                        | `min(x, y)`                                                                                                |
| maximum                    | ![](img/light/maximum.png#gh-light-mode-only)![](img/dark/maximum.png#gh-dark-mode-only)                                                                                                                                                                                                                                                                        | `max(x, y)`                                                                                                |
| *if* statement             | ![](img/light/if_statement.png#gh-light-mode-only)![](img/dark/if_statement.png#gh-dark-mode-only)                                                                                                                                                                                                                                                              | <pre>if condition1:<br/>  statement1<br/>elif condition2:<br/>  statement<br/>else:<br/>  statement3</pre> |
| indexed *for* loop         | ![](img/light/for_to_loop.png#gh-light-mode-only)![](img/dark/for_to_loop.png#gh-dark-mode-only)<br/>![](img/light/for_downto_loop.png#gh-light-mode-only)![](img/dark/for_downto_loop.png#gh-dark-mode-only)                                                                                                                                                   | <pre>for i in a \|to\| b:<br/>  body</pre><br/><pre>for i in b \|downto\| a:<br/>  body</pre>              | `\|to\|` and `\|downto\|` are custom defined infix operators |
| *for each* loop            | ![](img/light/for_each_loop.png#gh-light-mode-only)![](img/dark/for_each_loop.png#gh-dark-mode-only)                                                                                                                                                                                                                                                            | <pre>for v in V:<br/>  body</pre>                                                                          |                                                              |
| *while* loop               | ![](img/light/while_loop.png#gh-light-mode-only)![](img/dark/while_loop.png#gh-dark-mode-only)                                                                                                                                                                                                                                                                  | <pre>while condition:<br/>  body</pre>                                                                     |                                                              |
| *repeat* loop              | ![](img/light/repeat_loop.png#gh-light-mode-only)![](img/dark/repeat_loop.png#gh-dark-mode-only)                                                                                                                                                                                                                                                                | <pre>while True:<br/>  body<br/>  if condition:<br/>    break</pre>                                        |                                                              |

**Stay tuned for more information once I migrate some amount of code.**
