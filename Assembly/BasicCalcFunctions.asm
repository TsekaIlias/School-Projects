.data
    prompt_name: .asciiz "Enter your full name: "
    prompt_am: .asciiz "Enter your student ID number (AM): "
    prompt_semester: .asciiz "Enter your semester: "
    prompt_num1: .asciiz "Enter the first number: "
    prompt_num2: .asciiz "Enter the second number: "
    prompt_choice: .asciiz "\nChoose operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Square the first number\n"
    result_label: .asciiz "Result: "
    newline: .asciiz "\n"
    error_msg: .asciiz "Invalid choice.\n"
    exit_msg: .asciiz "Program terminated.\n"
    name_input: .space 100  # Κρατήστε χώρο για 100 χαρακτήρες

.text
    .globl main

main:
    # Είσοδος δεδομένων για τα προσωπικά στοιχεία του χρήστη
    # Είσοδος για το πλήρες όνομα
    li $v0, 4              # Κωδικός syscall για εκτύπωση μηνύματος
    la $a0, prompt_name    # Μήνυμα: "Enter your full name: "
    syscall

    li $v0, 8              # Κωδικός syscall για είσοδο συμβολοσειράς
    la $a0, name_input     # Μνήμη για αποθήκευση του ονόματος
    li $a1, 100            # Μέγιστο μήκος της συμβολοσειράς
    syscall

    # Είσοδος για τον αριθμό μητρώου (AM)
    li $v0, 4              # Κωδικός syscall για εκτύπωση μηνύματος
    la $a0, prompt_am      # Μήνυμα: "Enter your student ID number (AM): "
    syscall

    li $v0, 5              # Κωδικός syscall για ανάγνωση ακέραιου
    syscall
    move $t0, $v0          # Αποθήκευση του αριθμού μητρώου στο $t0

    # Είσοδος για το εξάμηνο
    li $v0, 4              # Κωδικός syscall για εκτύπωση μηνύματος
    la $a0, prompt_semester    # Μήνυμα: "Enter your semester: "
    syscall

    li $v0, 5              # Κωδικός syscall για ανάγνωση ακέραιου
    syscall
    move $t1, $v0          # Αποθήκευση του εξαμήνου στο $t1

    # Είσοδος για δύο αριθμούς
    li $v0, 4              # Κωδικός syscall για εκτύπωση μηνύματος
    la $a0, prompt_num1    # Μήνυμα: "Enter the first number: "
    syscall

    li $v0, 5              # Κωδικός syscall για ανάγνωση ακέραιου
    syscall
    move $t2, $v0          # Αποθήκευση του πρώτου αριθμού στο $t2

    li $v0, 4              # Κωδικός syscall για εκτύπωση μηνύματος
    la $a0, prompt_num2    # Μήνυμα: "Enter the second number: "
    syscall

    li $v0, 5              # Κωδικός syscall για ανάγνωση ακέραιου
    syscall
    move $t3, $v0          # Αποθήκευση του δεύτερου αριθμού στο $t3

    # Εμφάνιση επιλογών λειτουργίας
    li $v0, 4              # Κωδικός syscall για εκτύπωση μηνύματος
    la $a0, prompt_choice   # Εμφάνιση μενού επιλογών λειτουργίας
    syscall

    li $v0, 5              # Κωδικός syscall για ανάγνωση ακέραιου
    syscall
    move $t4, $v0          # Αποθήκευση της επιλογής λειτουργίας στο $t4

    # Επιλογή λειτουργίας
    beq $t4, 1, addition   # Αν είναι 1, πηγαίνουμε στην πρόσθεση
    beq $t4, 2, subtraction  # Αν είναι 2, πηγαίνουμε στην αφαίρεση
    beq $t4, 3, multiplication  # Αν είναι 3, πηγαίνουμε στον πολλαπλασιασμό
    beq $t4, 4, division  # Αν είναι 4, πηγαίνουμε στη διαίρεση
    beq $t4, 5, square  # Αν είναι 5, πηγαίνουμε στην τετραγωνική λειτουργία
    j invalid_choice  # Αν είναι άκυρη επιλογή, πηγαίνουμε στην επεξεργασία σφάλματος

addition:
    add $t5, $t2, $t3     # Εκτέλεση πρόσθεσης
    j print_result

subtraction:
    sub $t5, $t2, $t3     # Εκτέλεση αφαίρεσης
    j print_result

multiplication:
    mul $t5, $t2, $t3     # Εκτέλεση πολλαπλασιασμού
    j print_result

division:
    beqz $t3, division_by_zero  # Έλεγχος αν ο δεύτερος αριθμός είναι μηδέν
    div $t2, $t3                # Εκτέλεση διαίρεσης
    mflo $t5                    # Μεταφορά του πηλίκου στο $t5
    j print_result

division_by_zero:
    li $v0, 4                  # Κωδικός syscall για εκτύπωση μηνύματος
    la $a0, error_msg          # Μήνυμα: "Cannot divide by zero."
    syscall
    j main

square:
    mul $t5, $t2, $t2     # Τετραγωνίζουμε τον πρώτο αριθμό
    j print_result

invalid_choice:
    li $v0, 4              # Κωδικός syscall για εκτύπωση μηνύματος
    la $a0, error_msg      # Μήνυμα: "Invalid choice."
    syscall
    j main

print_result:
    li $v0, 4              # Κωδικός syscall για εκτύπωση μηνύματος
    la $a0, result_label   # Μήνυμα: "Result: "
    syscall

    li $v0, 1              # Κωδικός syscall για εκτύπωση ακέραιου
    move $a0, $t5          # Εκτύπωση του αποτελέσματος
    syscall

    li $v0, 4              # Κωδικός syscall για εκτύπωση νέας γραμμής
    la $a0, newline
    syscall

    # Ερώτηση αν ο χρήστης θέλει να συνεχίσει
    li $v0, 4              # Κωδικός syscall για εκτύπωση μηνύματος
    la $a0, exit_msg       # Μήνυμα: "Program terminated."
    syscall
    li $v0, 10             # Κωδικός syscall για έξοδο από το πρόγραμμα
    syscall
