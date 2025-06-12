# Regular Expression to DFA Converter

This project implements a Python program to convert regular expressions (ERs) to Deterministic Finite Automata (DFAs) via Nondeterministic Finite Automata (NFAs). It uses ANTLR 4 for parsing regular expressions and Python for constructing and transforming automata. The program supports regular expression operations (concatenation, union, and Kleene star) and converts the resulting NFA to a DFA using the subset construction algorithm. This is an educational project demonstrating key concepts in automata theory and compiler design.

## Purpose

The program takes a regular expression as input, parses it into an abstract syntax tree (AST) using ANTLR, constructs an equivalent NFA, and converts it to a DFA. The output NFAs and DFAs are written to files in a specific format. This process is fundamental in applications like lexical analysis in compilers and pattern matching.

## Features

- **Regular Expression Parsing**: Uses ANTLR to parse regular expressions with operators for concatenation, union (`|`), Kleene star (`*`), and parentheses for grouping.
- **NFA Construction**: Builds NFAs from regular expressions using operations for concatenation, union, and Kleene star.
- **NFA to DFA Conversion**: Converts NFAs to DFAs using the subset construction algorithm, handling epsilon transitions and sink states.
- **File I/O**: Reads regular expressions from input files and writes NFA and DFA descriptions to output files.
- **Type Hints**: Uses Python type hints for better code clarity and maintainability.

## File Structure

- `main.py`: Entry point; reads a regular expression from a file, parses it, constructs an NFA, converts it to a DFA, and writes results to output files.
- `NFA.py`: Defines the `NFA` class for representing and parsing NFAs.
- `DFA.py`: Defines the `DFA` class, including methods for parsing DFAs and converting NFAs to DFAs.
- `ERtoNFA.py`: Implements functions (`concatenation`, `reunion`, `star`) to construct NFAs for regular expression operations.
- `ERVisitorToNFA.py`: Custom ANTLR visitor to convert a parsed regular expression AST into an NFA.
- `ERVisitorShow.py`: Custom ANTLR visitor to print variable tokens (for debugging).
- `ERVisitor.py`: Generic ANTLR visitor base class for traversing the parse tree.
- `ERParser.py`: ANTLR-generated parser for regular expressions.
- `ERLexer.py`: ANTLR-generated lexer for tokenizing regular expressions.
- `ER.g4`, `ER.tokens`, `ERLexer.tokens`, `ER.interp`, `ERLexer.interp`: ANTLR grammar and generated files defining the regular expression syntax.

## Regular Expression Grammar

The grammar (`ER.g4`) supports the following constructs:

```
KLEENE : '*'+;         // Kleene star
REUNION : '|';         // Union operator
OPEN : '(';            // Left parenthesis
CLOSED : ')';          // Right parenthesis
WHITESPACE : [ \t\n]+ -> skip; // Ignore whitespace
VAR : [A-Z] | [a-z];   // Single alphabetic character

expr : c_expr REUNION expr | c_expr;
c_expr : c_expr c_expr | k_expr | atom;
k_expr : atom KLEENE;
sub_expr : OPEN expr CLOSED;
atom : variable | sub_expr;
variable : VAR;
```

This grammar supports:

- Single alphabetic characters (`a`, `b`, etc.).
- Concatenation (implicit, e.g., `ab`).
- Union (`a|b`).
- Kleene star (`a*`).
- Parenthesized sub-expressions (`(a|b)*`).

## Input/Output File Formats

### Input File

A text file containing a single regular expression (e.g., `input.txt`):

```
(a|b)*a
```

### NFA Output File

Format:

```
<number_of_states>
<final_state_1> <final_state_2> ...
<state> <symbol> <next_state_1> <next_state_2> ...
...
```

Example for `(a|b)*a`:

```
8
7
0 eps 1 5
1 a 2
2 eps 3 7
3 eps 1 5
5 b 6
6 eps 3 7
```

### DFA Output File

Format:

```
<number_of_states>
<final_state_1> <final_state_2> ...
<state> <symbol> <next_state>
...
```

Example for the DFA:

```
4
1 3
0 a 1
0 b 2
1 a 1
1 b 3
2 a 1
2 b 2
3 a 1
3 b 3
```

## Usage

1. **Install Dependencies**:

   - Install Python 3.7+.
   - Install ANTLR4 Python runtime:

     ```bash
     pip install antlr4-python3-runtime==4.7.2
     ```

2. **Prepare Input**: Create a text file (e.g., `input.txt`) with a regular expression.

3. **Run the Program**:

   ```bash
   python main.py input.txt nfa_output.txt dfa_output.txt
   ```

   - `input.txt`: File containing the regular expression.
   - `nfa_output.txt`: Output file for the NFA.
   - `dfa_output.txt`: Output file for the DFA.

4. **Example**: For input `a|b` in `input.txt`:

   ```bash
   python main.py input.txt nfa.txt dfa.txt
   ```

   This generates `nfa.txt` and `dfa.txt` with the respective automata.

## Algorithm Overview

1. **Parsing Regular Expression**:

   - The `ERLexer` and `ERParser` (generated from `ER.g4`) tokenize and parse the input regular expression into an AST.
   - `ERVisitorToNFA` traverses the AST, constructing an NFA for each node:
     - `visitVariable`: Creates an NFA with two states and a transition on the variable’s symbol.
     - `visitSub_expr`: Processes parenthesized expressions.
     - `visitAtom`: Handles variables or sub-expressions.
     - `visitK_expr`: Applies the Kleene star operation (`star`).
     - `visitC_expr`: Handles concatenation (`concatenation`) or delegates to `k_expr`/`atom`.
     - `visitExpr`: Handles union (`reunion`) or delegates to `c_expr`.

2. **NFA to DFA Conversion** (in `DFA.py`):

   - Uses the subset construction algorithm:
     - Computes epsilon closures for each state.
     - Treats sets of NFA states as DFA states.
     - Constructs DFA transitions by following NFA transitions and their epsilon closures.
     - Marks DFA states containing NFA final states as final.
     - Adds a sink state for undefined transitions.
   - Removes unreachable states to optimize the NFA before conversion.

3. **Output**:

   - The NFA and DFA are written to files in the specified format.

## Key Concepts

- **Regular Expressions**: Formal descriptions of regular languages using operators like union, concatenation, and Kleene star.
- **Finite Automata**: Computational models for recognizing regular languages.
  - **NFA**: Supports multiple transitions per symbol and epsilon transitions.
  - **DFA**: Requires one transition per symbol per state, ensuring determinism.
- **Epsilon Closure**: Set of states reachable via epsilon transitions.
- **Subset Construction**: Algorithm to convert an NFA to a DFA by treating sets of NFA states as DFA states.
- **ANTLR**: A parser generator for processing structured text, used here to parse regular expressions.

## Limitations

- Input regular expressions are limited to alphabetic characters (`a-z`, `A-Z`) as variables.
- The initial state is hardcoded to 0.
- No validation for empty or malformed regular expressions.
- The program assumes well-formed input files.
- Debugging output (e.g., transition printing in `DFA.from_nfa`) may clutter the console.

## Further Reading

- **Automata Theory**:
  - Sipser, M. (2012). *Introduction to the Theory of Computation*. Cengage Learning. \[Chapter 1: Regular Languages\]
  - Wikipedia: Finite-state machine
- **Regular Expressions and NFAs**:
  - Wikipedia: Thompson’s construction
  - Hopcroft, J. E., & Ullman, J. D. (1979). *Introduction to Automata Theory, Languages, and Computation*. Addison-Wesley.
- **Subset Construction**:
  - Wikipedia: Powerset construction
- **ANTLR**:
  - Parr, T. (2013). *The Definitive ANTLR 4 Reference*. Pragmatic Bookshelf.
  - ANTLR Official Site

## License

This project is for educational purposes and is not licensed for commercial use.
