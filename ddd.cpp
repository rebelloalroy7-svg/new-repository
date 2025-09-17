#include <iostream>
#include <string>
using namespace std;

// Function to check if parentheses are balanced
bool areParenthesesBalanced(const string &expr) {
    char stack[1000];  // Array as stack
    int top = -1;      // Top pointer

    for (char ch : expr) {
        // Push opening brackets
        if (ch == '(' || ch == '{' || ch == '[') {
            stack[++top] = ch;  // Push
        }
        // Check closing brackets
        else if (ch == ')' || ch == '}' || ch == ']') {
            if (top == -1) return false; // Stack empty
            
            char topChar = stack[top--]; // Pop variable char type topchar
            
            // Check for matching pair
            if ((ch == ')' && topChar != '(') |  //ch==')' && topchar!='('
                (ch == '}' && topChar != '{') |
                (ch == ']' && topChar != '[')) {
                return false;
            }
        }
    }
   return top == -1; // Balanced if stack is empty
}

int main() {
    string expr;
    cout << "Enter an expression: ";
    getline(cin, expr);

    if (areParenthesesBalanced(expr))
        cout << "Parentheses are Balanced " << endl;
    else
        cout << "Parentheses are NOT Balanced " << endl;

    return 0;
}