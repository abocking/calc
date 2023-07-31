# calc
Basic calculator task

1. Implement a basic calculator that supports the following operations:

Add
Subtract
Multiply
Divide 

Each operation should take as input two operands and produce as output one result.
e.g.
Add(2, 3) => 5
Multiply(5, -2.4) => -12 

Show your calculator being used for some typical scenarios to stress the operations you've created using various inputs.

**Operations:**
+ = Add
- = Subtract
* = Multiply
/ = Divide
^ = Power of

**ANS = Previous answer**

**Enter first number: 2
Enter operation:** (+, -, *, /, ^) +
**Enter second number (or "ANS" to use previous result): 3
2.0 + 3.0
= 5.0**

**Would you like to do another calculation? (yes/no): yes**

**Enter first number: 3**
**Enter operation:** (+, -, *, /, ^) **^**
**Enter second number (or "ANS" to use previous result): 2**
**3.0 ^ 2.0**
**= 9.0**

**Would you like to do another calculation? (yes/no): no**

**Process finished with exit code 0**

2. How might you implement a memory feature for your calculator?
i.e. Capture the result of one operation and then use it in a subsequent operation?
Produce an example using the calculator you created in part 1 to demonstrate this.

**I have added in the option to input ANS for a number which equals the previous result. I also added in an initial value for result (result = 0) to avoid any errors.**

4. How might you extend your calculator to support more than two operands for each operation?
e.g.
Add(1, 2, 3) => 6
**Create a tuple for numbers and operators and then add the inputed numbers, operators to the list.**

What considerations would you need to make for a feature such as this?
**BODMAS - add in a function to carry out the operations in the correct order
Catch any errors where two paranthesis aren't used**


4. How would you invoke your calculator to perform the following operations:

3 + 2 * 6
(3 + 2) * 6

**If I had the ability to enter >2 numbers/operators and successfully implemented a BODMAS function I would except:
a) 2 * 6 = 12, 12 + 3 = 15
b) 3 + 2 = 5, 5 * 6 = 30**

5. How would you expect the following to behave:

Multiply(3, 0) => **0**
Divide(3, 0) => **Error: Cannot divide by 0!**

 

5. How would you extend your calculator to provide a x^n operation?
e.g.
Power(2, 2) => 4
Power(2, 4) => 16

**I have added in the operation to create to the power (a ^ b)**
