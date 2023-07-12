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

<table>
  <tr>
    <th>Category</th>
    <th>Pseudocode construct</th>
    <th>Python code</th>
    <th>Remarks</th>
  </tr>
  <tr>
    <td rowspan="8">predefined constant</td>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/true.png">
        <img src="img/light/true.png">
      </picture>
    </td>
    <td>
      <pre lang="python">True</pre>
    </td>
    <td></td>
  </tr>
  <tr></tr>
  <tr>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/false.png">
        <img src="img/light/false.png">
      </picture>
    </td>
    <td>
      <pre lang="python">False</pre>
    </td>
    <td></td>
  </tr>
  <tr></tr>
  <tr>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/nil.png">
        <img src="img/light/nil.png">
      </picture>
    </td>
    <td>
      <pre lang="python">None</pre>
    </td>
    <td></td>
  </tr>
  <tr></tr>
  <tr>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/infinity.png">
        <img src="img/light/infinity.png">
      </picture>
    </td>
    <td>
      <pre lang="python">math.inf</pre>
    </td>
    <td></td>
  </tr>
  <tr></tr>
  <tr>
    <td rowspan="2">custom constant</td>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/constant.png">
        <img src="img/light/constant.png">
      </picture>
    </td>
    <td>
      <pre lang="python">NO_SUCH_PATH</pre>
    </td>
    <td>Defined as a standalone or an enum value.</td>
  </tr>
  <tr></tr>
  <tr>
    <td rowspan="6">variable</td>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/variable.png">
        <img src="img/light/variable.png">
      </picture>
    </td>
    <td>
      <pre lang="python">x</pre>
    </td>
    <td></td>
  </tr>
  <tr></tr>
  <tr>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/decorated_variable.png">
        <img src="img/light/decorated_variable.png">
      </picture>
    </td>
    <td>
      <pre lang="python">y2_</pre>
    </td>
    <td></td>
  </tr>
  <tr></tr>
  <tr>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/dashed_variable.png">
        <img src="img/light/dashed_variable.png">
      </picture>
    </td>
    <td>
      <pre lang="python">best_score</pre>
    </td>
    <td></td>
  </tr>
  <tr></tr>
  <tr>
    <td rowspan="6">object's attribute</td>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/attribute.png">
        <img src="img/light/attribute.png">
      </picture>
    </td>
    <td>
      <pre lang="python">T.root</pre>
    </td>
    <td></td>
  </tr>
  <tr></tr>
  <tr>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/dashed_attribute.png">
        <img src="img/light/dashed_attribute.png">
      </picture>
    </td>
    <td>
      <pre lang="python">A.heap_size</pre>
    </td>
    <td></td>
  </tr>
  <tr></tr>
  <tr>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/indexed_attribute.png">
        <img src="img/light/indexed_attribute.png">
      </picture>
    </td>
    <td>
      <pre lang="python">x.key[i]</pre>
    </td>
    <td>Implemented as an <code>Array</code>.</td>
  </tr>
  <tr></tr>
  <tr>
    <td rowspan="2">assignment</td>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/assignment.png">
        <img src="img/light/assignment.png">
      </picture>
    </td>
    <td>
      <pre lang="python">x = y</pre>
    </td>
    <td></td>
  </tr>
  <tr></tr>
  <tr>
    <td rowspan="12">scalar comparison</td>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/is_equal.png">
        <img src="img/light/is_equal.png">
      </picture>
    </td>
    <td>
      <pre lang="python">x == y</pre>
    </td>
    <td rowspan="12"><code>x</code> and <code>y</code> are scalars.</td>
  </tr>
  <tr></tr>
  <tr>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/is_not_equal.png">
        <img src="img/light/is_not_equal.png">
      </picture>
    </td>
    <td>
      <pre lang="python">x != y</pre>
    </td>
  </tr>
  <tr></tr>
  <tr>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/less.png">
        <img src="img/light/less.png">
      </picture>
    </td>
    <td>
      <pre lang="python">x &lt; y</pre>
    </td>
  </tr>
  <tr></tr>
  <tr>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/greater.png">
        <img src="img/light/greater.png">
      </picture>
    </td>
    <td>
      <pre lang="python">x &gt; y</pre>
    </td>
  </tr>
  <tr></tr>
  <tr>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/less_equal.png">
        <img src="img/light/less_equal.png">
      </picture>
    </td>
    <td>
      <pre lang="python">x &lt;= y</pre>
    </td>
  </tr>
  <tr></tr>
  <tr>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/greater_equal.png">
        <img src="img/light/greater_equal.png">
      </picture>
    </td>
    <td>
      <pre lang="python">x &gt;= y</pre>
    </td>
  </tr>
  <tr></tr>
  <tr>
    <td rowspan="4">pointer comparison</td>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/is_equal.png">
        <img src="img/light/is_equal.png">
      </picture>
    </td>
    <td>
      <pre lang="python">x is y</pre>
    </td>
    <td rowspan="4"><code>x</code> and <code>y</code> are pointers.</td>
  </tr>
  <tr></tr>
  <tr>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/is_not_equal.png">
        <img src="img/light/is_not_equal.png">
      </picture>
    </td>
    <td>
      <pre lang="python">x is not y</pre>
    </td>
  </tr>
  <tr></tr>
  <tr>
    <td rowspan="6">logical operation</td>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/and.png">
        <img src="img/light/and.png">
      </picture>
    </td>
    <td>
      <pre lang="python">&lt;condition1&gt; and &lt;condition2&gt;</pre>
    </td>
    <td></td>
  </tr>
  <tr></tr>
  <tr>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/or.png">
        <img src="img/light/or.png">
      </picture>
    </td>
    <td>
      <pre lang="python">&lt;condition1&gt; or &lt;condition2&gt;</pre>
    </td>
    <td></td>
  </tr>
  <tr></tr>
  <tr>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/not.png">
        <img src="img/light/not.png">
      </picture>
    </td>
    <td>
      <pre lang="python">not &lt;condition&gt;</pre>
    </td>
    <td></td>
  </tr>
  <tr></tr>
  <tr>
    <td rowspan="28">arithmetic operation</td>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/increment.png">
        <img src="img/light/increment.png">
      </picture>
    </td>
    <td>
      <pre lang="python">x += y</pre>
    </td>
    <td></td>
  </tr>
  <tr></tr>
  <tr>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/decrement.png">
        <img src="img/light/decrement.png">
      </picture>
    </td>
    <td>
      <pre lang="python">x -= y</pre>
    </td>
    <td></td>
  </tr>
  <tr></tr>
  <tr>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/addition.png">
        <img src="img/light/addition.png">
      </picture>
    </td>
    <td>
      <pre lang="python">x + y</pre>
    </td>
    <td></td>
  </tr>
  <tr></tr>
  <tr>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/subtraction.png">
        <img src="img/light/subtraction.png">
      </picture>
    </td>
    <td>
      <pre lang="python">x - y</pre>
    </td>
    <td></td>
  </tr>
  <tr></tr>
  <tr>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/multiplication.png">
        <img src="img/light/multiplication.png">
      </picture>
    </td>
    <td>
      <pre lang="python">x * y</pre>
    </td>
    <td></td>
  </tr>
  <tr></tr>
  <tr>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/floor_division.png">
        <img src="img/light/floor_division.png">
      </picture>
    </td>
    <td>
      <pre lang="python">x // y</pre>
    </td>
    <td></td>
  </tr>
  <tr></tr>
  <tr>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/ceiling_division.png">
        <img src="img/light/ceiling_division.png">
      </picture>
    </td>
    <td>
      <pre lang="python">-(x // -y)</pre>
    </td>
    <td></td>
  </tr>
  <tr></tr>
  <tr>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/modulo.png">
        <img src="img/light/modulo.png">
      </picture>
    </td>
    <td>
      <pre lang="python">x % y</pre>
    </td>
    <td></td>
  </tr>
  <tr></tr>
  <tr>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/exponent.png">
        <img src="img/light/exponent.png">
      </picture>
    </td>
    <td>
      <pre lang="python">x ** y</pre>
    </td>
    <td></td>
  </tr>
  <tr></tr>
  <tr>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/square_root.png">
        <img src="img/light/square_root.png">
      </picture>
    </td>
    <td>
      <pre lang="python">math.sqrt(x)</pre>
    </td>
    <td></td>
  </tr>
  <tr></tr>
  <tr>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/floor.png">
        <img src="img/light/floor.png">
      </picture>
    </td>
    <td>
      <pre lang="python">math.floor(x)</pre>
    </td>
    <td></td>
  </tr>
  <tr></tr>
  <tr>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/ceiling.png">
        <img src="img/light/ceiling.png">
      </picture>
    </td>
    <td>
      <pre lang="python">math.ceil(x)</pre>
    </td>
    <td></td>
  </tr>
  <tr></tr>
  <tr>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/minimum.png">
        <img src="img/light/minimum.png">
      </picture>
    </td>
    <td>
      <pre lang="python">min(x, y)</pre>
    </td>
    <td></td>
  </tr>
  <tr></tr>
  <tr>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/maximum.png">
        <img src="img/light/maximum.png">
      </picture>
    </td>
    <td>
      <pre lang="python">max(x, y)</pre>
    </td>
    <td></td>
  </tr>
  <tr></tr>
  <tr>
    <td rowspan="4">value exchange</td>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/exchange.png">
        <img src="img/light/exchange.png">
      </picture>
    </td>
    <td rowspan="4">
      <pre lang="python">x, y = y, x</pre>
    </td>
    <td></td>
  </tr>
  <tr></tr>
  <tr>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/swap.png">
        <img src="img/light/swap.png">
      </picture>
    </td>
    <td></td>
  </tr>
  <tr></tr>
  <tr>
    <td rowspan="2">printing</td>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/print.png">
        <img src="img/light/print.png">
      </picture>
    </td>
    <td>
      <pre lang="python">print(x)</pre>
    </td>
    <td></td>
  </tr>
  <tr></tr>
  <tr>
    <td rowspan="2">procedure definition</td>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/procedure_definition.png">
        <img src="img/light/procedure_definition.png">
      </picture>
    </td>
    <td>
      <pre lang="python">
def insertion_sort(A, n):
  &lt;block&gt;</pre>
    </td>
    <td></td>
  </tr>
  <tr></tr>
  <tr>
    <td rowspan="2">procedure call</td>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/procedure_call.png">
        <img src="img/light/procedure_call.png">
      </picture>
    </td>
    <td>
      <pre lang="python">insertion_sort(A, n)</pre>
    </td>
    <td></td>
  </tr>
  <tr></tr>
  <tr>
    <td rowspan="6">procedure return</td>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/return_no_value.png">
        <img src="img/light/return_no_value.png">
      </picture>
    </td>
    <td>
      <pre lang="python">return</pre>
    </td>
    <td></td>
  </tr>
  <tr></tr>
  <tr>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/return_single_value.png">
        <img src="img/light/return_single_value.png">
      </picture>
    </td>
    <td>
      <pre lang="python">return x</pre>
    </td>
    <td></td>
  </tr>
  <tr></tr>
  <tr>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/return_multiple_values.png">
        <img src="img/light/return_multiple_values.png">
      </picture>
    </td>
    <td>
      <pre lang="python">return x, y</pre>
    </td>
    <td></td>
  </tr>
  <tr></tr>
  <tr>
    <td rowspan="2">array creation</td>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/new_array.png">
        <img src="img/light/new_array.png">
      </picture>
    </td>
    <td>
      <pre lang="python">A = Array(0, n)</pre>
    </td>
    <td>The created array consists of <code>None</code> values on each position.</td>
  </tr>
  <tr></tr>
  <tr>
    <td rowspan="2">array cell reference</td>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/array_cell.png">
        <img src="img/light/array_cell.png">
      </picture>
    </td>
    <td>
      <pre lang="python">A[i]</pre>
    </td>
    <td>Either as an accessor or a mutator.</td>
  </tr>
  <tr></tr>
  <tr>
    <td rowspan="2">set creation</td>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/new_set.png">
        <img src="img/light/new_set.png">
      </picture>
    </td>
    <td>
      <pre lang="python">S = set()</pre>
    </td>
    <td></td>
  </tr>
  <tr></tr>
  <tr>
    <td rowspan="2">sets union</td>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/set_union.png">
        <img src="img/light/set_union.png">
      </picture>
    </td>
    <td>
      <pre lang="python">S | {x}</pre>
    </td>
    <td></td>
  </tr>
  <tr></tr>
  <tr>
    <td rowspan="2">set cardinality</td>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/set_cardinality.png">
        <img src="img/light/set_cardinality.png">
      </picture>
    </td>
    <td>
      <pre lang="python">len(S)</pre>
    </td>
    <td></td>
  </tr>
  <tr></tr>
  <tr>
    <td rowspan="2">error</td>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/error.png">
        <img src="img/light/error.png">
      </picture>
    </td>
    <td>
      <pre lang="python">raise ValueError('overflow')</pre>
    </td>
    <td></td>
  </tr>
  <tr></tr>
  <tr>
    <td rowspan="2"><em>if</em> statement</td>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/if_statement.png">
        <img src="img/light/if_statement.png">
      </picture>
    </td>
    <td>
      <pre lang="python">
if &lt;condition1&gt;:
  &lt;block1&gt;
elif &lt;condition2&gt;:
  &lt;block2&gt;
else:
  &lt;block3&gt;</pre>
    </td>
    <td>Can have zero or more <code>elif</code> branches and zero or one <code>else</code> branch.</td>
  </tr>
  <tr></tr>
  <tr>
    <td rowspan="4"><em>for</em> loop</td>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/for_to_loop.png">
        <img src="img/light/procedure_call.png">
      </picture>
    </td>
    <td>
      <pre lang="python">
for i in x |to| y:
  &lt;block&gt;</pre>
    </td>
    <td rowspan="4"><code>|to|</code> and <code>|downto|</code> are custom defined infix operators.</td>
  </tr>
  <tr></tr>
  <tr>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/for_downto_loop.png">
        <img src="img/light/procedure_call.png">
      </picture>
    </td>
    <td>
      <pre lang="python">
for i in y |downto| x:
  &lt;block&gt;</pre>
    </td>
  </tr>
  <tr></tr>
  <tr>
    <td rowspan="2"><em>for-each</em> loop</td>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/for_each_loop.png">
        <img src="img/light/for_each_loop.png">
      </picture>
    </td>
    <td>
      <pre lang="python">
for v in V:
  &lt;block&gt;</pre>
    </td>
    <td></td>
  </tr>
  <tr></tr>
  <tr>
    <td rowspan="2"><em>while</em> loop</td>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/while_loop.png">
        <img src="img/light/while_loop.png">
      </picture>
    </td>
    <td>
      <pre lang="python">
while &lt;condition&gt;:
  &lt;block&gt;</pre>
    </td>
    <td></td>
  </tr>
  <tr></tr>
  <tr>
    <td rowspan="2"><em>repeat</em> loop</td>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="img/dark/repeat_loop.png">
        <img src="img/light/repeat_loop.png">
      </picture></td>
    <td>
      <pre lang="python">
while True:
  &lt;block&gt;
  if &lt;condition&gt;:
    break</pre>
    </td>
    <td></td>
  </tr>
  <tr></tr>
</table>

**Stay tuned for more information once I migrate some amount of code.**
