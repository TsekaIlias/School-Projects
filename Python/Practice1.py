import random
import string
import re


def generate_random_text(n):
    greek_chars = "αβγδεζηθικλμνξοπρστυφχψωΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ0123456789"
    return "".join(random.choices(greek_chars, k=n))


def inject_multiplications(txt, n):
    multiplications = []
    for _ in range(n):
        x = random.randint(0, 99)
        y = random.randint(0, 99)
        multiplication = f"ΠΟΛΛΑΠΛΑΣΙΑΣΕ({x:02d}, {y:02d})"
        multiplications.append(multiplication)

    txt_list = list(txt)
    for multiplication in multiplications:
        pos = random.randint(0, len(txt) - len(multiplication))
        txt_list[pos:pos] = list(multiplication)
        print(f"{multiplication} εισαγωγή στη θέση {pos}")

    return "".join(txt_list)


def compute(txt):
    pattern = r"ΠΟΛΛΑΠΛΑΣΙΑΣΕ\(\s*(\d{1,2})\s*,\s*(\d{1,2})\s*\)"
    matches = re.findall(pattern, txt)
    total_sum = 0
    for match in matches:
        x, y = int(match[0]), int(match[1])
        total_sum += x * y
    return total_sum


if __name__ == "__main__":
    random_text = generate_random_text(300)
    print("Generated Random Text:")
    print(random_text)

    n = 3
    resulting_text = inject_multiplications(random_text, n)

    print("\nResulting Text with Multiplications Injected:")
    print(resulting_text)
 
    total = compute(resulting_text)
    print(f"\nThe sum of the products is: {total}")
