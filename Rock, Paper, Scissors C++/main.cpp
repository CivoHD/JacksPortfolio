#include <iostream>
#include <random>
#include <ctime>


const int ROCK = 1;
const int PAPER = 2;
const int SCISSORS = 3;


using namespace std;



int userChoice = 0;

int getComputerChoice(){
    srand (time(NULL));
    int compChoice = rand() % 3 + 1;
    return compChoice;
}

void determineWinner(int userChoice, int compChoice)
{
    if (userChoice == ROCK && compChoice == PAPER){
        cout << "Computer wins! Paper wraps rock" << endl;
    }
    else if (userChoice == PAPER && compChoice == SCISSORS){
        cout << "Computer wins! Scissors beats paper" << endl;
    }
    else if (userChoice == SCISSORS && compChoice == ROCK){
        cout << "Computer wins! Rock beats scissors" << endl;
    }
    else if (userChoice == ROCK && compChoice == PAPER){
        cout << "YOU win! Rock beats paper" << endl;
    }
    else if (userChoice == PAPER && compChoice == ROCK){
        cout << "YOU win! Paper beats rock" << endl;
    }
    else if (userChoice == SCISSORS && compChoice == PAPER){
        cout << "YOU win! Scissors cut paper" << endl;
    }
    else{
        cout << "Tie" << endl;
    }


}

void displayChoice(int choice)
{
    string result;
    if (choice == ROCK){
        result = "Rock";
    }
    else if (choice == PAPER){
        result = "Paper";
    }
    else {
        result = "Scissors";
    }
    cout << result << endl;
}

int main()
{
    cout << '\t' << "Rock Paper Scissors" << endl;
    cout << "Game Menu" << endl;
    cout << "---------" << endl;
    cout << "1. Rock" << endl;
    cout << "2. Paper" << endl;
    cout << "3. Scissors" << endl;

    cout << "Enter choice: ";
    cin >> userChoice;
    cout << "you selected: ";
    displayChoice(userChoice);

    int compChoice = getComputerChoice();
    cout << "The computer selected: ";
    displayChoice(compChoice);
    determineWinner(userChoice, compChoice);
}
