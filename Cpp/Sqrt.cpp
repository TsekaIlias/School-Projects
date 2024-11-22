#include <iostream>
#include <stdexcept>
#include <cmath> 

using namespace std;

class NegativeValueException : public exception {
public:
    const char* what() const noexcept override {
        return "Error: Negative value is not allowed.";
    }
};

double calculateSquareRoot(double number) {
    if (number < 0) {
        throw NegativeValueException();
    }
    return sqrt(number);
}

int main() {
    double input;

    cout << "Enter a number to calculate its square root: ";
    cin >> input;

    try {
        double result = calculateSquareRoot(input);
        cout << "Square root: " << result << endl;
    } catch (const NegativeValueException& error) {
        cout << error.what() << endl;
    }

    return 0;
}
