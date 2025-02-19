from stack import Stack
from memory_profiler import profile
import time

n = 25000000
star = time.time()

stacks = [
    Stack(n),
    Stack(2 * n),
    Stack(3 * n),
    Stack(4 * n),
    Stack(5 * n),
]

# Llenar cada pila con 'A' hasta su capacidad
for stack in stacks:
    for _ in range(stack.max):
        stack.push('A')

# Verificar los estados finales y realizar la búsqueda de un elemento inexistente
for i, stack in enumerate(stacks, start=1):
    print(f"Stack {i}: Último elemento ->", stack.peek())
    print(f"Stack {i}: Búsqueda de elemento inexistente (Z) ->", stack.search('Z'))

# Realizar un pop en cada pila
for i, stack in enumerate(stacks, start=1):
    popped_element = stack.pop()  # Realizamos el pop
    print(f"Stack {i}: Elemento eliminado -> {popped_element}")
    print(f"Stack {i}: Nuevo último elemento ->", stack.peek())

end = time.time()
print(end - star)


