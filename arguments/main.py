# Do not modify these lines
__winc_id__ = "7b9401ad7f544be2a23321292dd61cb6"
__human_name__ = "arguments"

# Add your code after this line

# Part 1: Greet Template


def greet(name: str, greeting: str = "Hello, <name>!"):
    return greeting.replace("<name>", name)


# Part 2: Force -> mass * surface_gravity


def force(mass: float, body: str = "earth"):
    surface_gravity_of_body = {
        "sun": 274,
        "jupiter": 24.9,
        "neptune": 11.2,
        "saturn": 10.4,
        "earth": 9.8,
        "uranus": 8.9,
        "venus": 8.9,
        "mars": 3.7,
        "mercury": 3.7,
        "moon": 1.6,
        "pluto": 0.6,
    }
    return mass * surface_gravity_of_body[body]


# Part 3: Gravity pull => G × ((m1×m2)/d2)


def pull(m1: float, m2: float, d: float):
    G = 6.674 * 10 ** -11
    return G * ((m1 * m2) / d ** 2)


print(greet("Doc"))  # "Hello, Doc!"
print(greet("Bob", "What's up, <name>!"))  # "What's up, Bob!"
print(force(150, "mars"))
print(force(14.2))
print(pull(800, 1500, 3))
