# dna_command_line
This project is used as a command line that manages a data structure that holds DNA sequences 
This project has a class for all the commands so that every command inherits from that class 
Other than that the commands are all executed each command in a separate class when each class has a single object,
for that I used SINGLE TON - desighn The commands are divided into packages according to their type. There is a class - CLI 
from which all the classes that print and receive the commands are inherited. To run the correct command I used FACTORY's DESIGHN, 
Which produces the appropriate quartet for each command at the time of execution. And there is an INVOKER who is responsible 
for running the actual commands he receives from the CLI
