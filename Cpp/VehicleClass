#include <iostream>
#include <string>
using namespace std;

class Vehicle {
protected:
    string registration_number;
    string owner_name;
    int cc; 

public:
    Vehicle(string regNum, string owner, int engineCapacity)
        : registration_number(regNum), owner_name(owner), cc(engineCapacity) {}

    virtual double traffic_tax() const = 0;

    virtual ~Vehicle() {}

    virtual void print() const {
        cout << "Reg number: " << registration_number << "\n"
             << "Owner's Name: " << owner_name << "\n"
             << "The CC: " << cc << " cc\n";
    }
};

class Car : public Vehicle {
private:
    int number_of_doors;

public:
    Car(string regNum, string owner, int engineCapacity, int doors)
        : Vehicle(regNum, owner, engineCapacity), number_of_doors(doors) {}

    double traffic_tax() const override {
        if (cc <= 1000) return 140.0;
        return 140.0 + ((cc - 1000) / 100) * 10.0;
    }

    void print() const override {
        Vehicle::print();
        cout << "DOORS!!!: " << number_of_doors << "\n"
             << "TAX :( : " << traffic_tax() << "€\n";
    }
};

class Truck : public Vehicle {
private:
    int max_weight; 

public:
    Truck(string regNum, string owner, int engineCapacity, int weight)
        : Vehicle(regNum, owner, engineCapacity), max_weight(weight) {}

    
    double traffic_tax() const override {
        if (max_weight <= 3000) return 300.0;
        if (max_weight <= 6000) return 400.0;
        return 600.0;
    }

    void print() const override {
        Vehicle::print();
        cout << "Max kg: " << max_weight << " kg\n"
             << "TAX!!!: " << traffic_tax() << "€\n";
    }
};

double total_tax(Vehicle* vehicles[], int size) {
    double total = 0;
    for (int i = 0; i < size; i++) {
        total += vehicles[i]->traffic_tax();
    }
    return total;
}

int main() {
    Vehicle* vehicles[5];
    int choice;

    for (int i = 0; i < 5; i++) {
        cout << "Car or Truck??? " << i + 1 << ":\n";
        cout << "TYPE 1 for car TYPE 2 for truck (Don't type anything else or ded): ";
        cin >> choice;

        string regNum, owner;
        int cc;

        cout << "Register number?";
        cin >> regNum;
        cout << "What's da name?";
        cin >> owner;
        cout << "CC? ";
        cin >> cc;

        if (choice == 1) {
            int doors;
            cout << "Doors? (or...) ";
            cin >> doors;
            vehicles[i] = new Car(regNum, owner, cc, doors);
        } else if (choice == 2) {
            int weight;
            cout << "MAX KG? ";
            cin >> weight;
            vehicles[i] = new Truck(regNum, owner, cc, weight);
        } else {
            cout << "Try again!!! :)\n";
            i--; 
        }
    }

    for (int i = 0; i < 5; i++) {
        vehicles[i]->print();
        cout << endl;
    }
    double totalTax = total_tax(vehicles, 5);
    cout << "Total tax: " << totalTax << "€\n";

    for (int i = 0; i < 5; i++) {
        delete vehicles[i];
    }

    return 0;
}
