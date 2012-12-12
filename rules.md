# Style Guide Summary

This is an extensive list of style rules implemented (or, to implement).
For the full set of official rules and examples, consult the style guide itself.

## Braces

1. Use braces around the body of control statements (except `case` and `default`
   within a switch statement).
2. The open brace should be on the same line as the control statement with at
   least one space before.
3. The close brace should be at the start of a line.
4. `else` and `else if` clauses, and the `while` part of a `do`-`while` loop,
   should be on the same line as the close brace before it.
5. The open brace for a function definition may be at the end of the line or
   at the start of the next line (with no indentation).
6. Structure declarations and array initialisations don't need to follow these rules.

Note indentation rule 5.1 implies that the close brace should have the same
indentation as the open brace.

## Vertical Whitespace

1. Functions are separated by blank lines.

## Indentation

1. Each indentation level is 4 spaces.
2. A tab character is equivalent to 8 spaces.
3. Indent level increases by 1 for subsequent lines when one of the following occurs:
<!-- 1. an open brace `{` is found at the start of a code block. (See TODO notes below) -->
<!-- 3. a control structure is found which does not have its body in braces.-->
 1. a control strutcure, or `case` or `default` statement is found. Indentation
    increases after the statement is complete (in case
    it spans over multiple lines).
 2. The open brace `{` at the start of a function definition is found.
    (See the TODO notes below)
4. Indent level should increase by 2 for subsequent lines when:
 1. a statement that began on the current line did not finish on the current line
    (Either it is not a control statement which does not end in a `;`, or it is
    a control statement that has not yet ended).
5. Indent level should decrease by 1 when:
 1. a close brace `}` is found ending a code block.
    If the `}` is the first non-whitespace token of
    the line, the indentation level should decrease for that line, otherwise the
    indentation should decrease only for subsequent lines.
 2. directly in a `case` or `default` body, and a `case` or `default` line
    is found, indentation should decrease for that line.
 3. a control structure which does not have its body in braces has reached the
    end of its body statement.
6. Indent level should decrease by 2 for subsequent lines when:
 1. a statement that has continued over multiple lines (cf. rule 4.1) has finished.
 2. directly in a `case`/`default` body, and the end of the `switch` statement
    is detected (cf. rules 5.1 and 5.3).

### Notes

* For switch statements, rules 5.2 and 3.2 combine to provide the expected behaviour.
  Rule 5.2 makes sure that the `case` and `default` statements are always one indent
  behind the body above, and 3.2 makes sure that the body below is one indent ahead:

        switch(x) {
            case 1:
                ...
                ... // Indentation must decrease after this
            case 2: // Indentation must increase after this
                ...
        }

* Multiple rules can be applied in the same line. For instance, at the end of
  a control statement which spans multiple lines, rules 6.1 and 3 both apply,
  giving a net loss of one indentation level:

        if (a && b && ...
                && x && y && z) {
            ...
        }

* Rules 3.3 and 5.3 are necessary to avoid applying double penalties for misuse
  of braces.

## Horizontal Whitespace

1. Space (or a newline) must be added after each comma `,` and semicolon `;`.
2. Space must be added before and after assignment operator `=`, `+=`, etc.

## Line Length

1. Line length must be &lt;= 79 characters, including comments and spaces.
   Recall that a tab character is equivalent to 8 spaces.

## Overall

1. Functions should be "about 50 lines maximum".
2. Don't use `goto`.

## Manual checks

This section lists style points which are impractical for simpatico to check,
and so must be checked by hand.

1. Comments
2. Vertical Whitespace
2. Readability
3. Modularity
4. Code repetition
5. Compiler warnings and errors
6. Code with syntax errors (which could confuse the tokeniser and give incorrect
   output)


## Thoughts and TODOs

* Indentation - should indentation increase when an open brace is found, or
  when a control structure is found?
  * If indentation is done when a brace is found, it's easier to code, but is
   susceptible to breaking when the control structure is missing a brace.
  * If indentation is done when a control structure is found, it will be necessary
   to hard-code all possible control structures, including function definitions.
  * Braces may not always indicate code blocks (e.g. initialising an array).
* Vertical whitespace - should separate statements be separated by newlines?
  * It makes sense to insert newlines after statements, but it's not mentioned in
   the style guide.
* What are all possible control statements?
  * `if`
  * `else`
  * `else if` (keeping sure not to count this as both `else` and `if`)
  * `for`
  * `while` (but not the `while` part of a `do`-`while`)
  * `do`
  * `switch`
  * `case`
  * `default`
  * `struct` (no need to treat `typedef struct` separately)
  * `union`
  * function definitions.
  * more?