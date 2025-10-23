"""7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir)."""

alumnos_parcial_uno = ["Emiliano", "Ivone", "Joaquin", "Brenda", "Agustina"]
alumnos_parcial_dos = ["Emiliano", "Ariadna", "Juan", "Brenda", "Barbara", "Silvina"]

set_parcial_uno = set(alumnos_parcial_uno)
set_parcial_dos = set(alumnos_parcial_dos)

print(f"Alumnos Parcial 1: {set_parcial_uno}")
print(f"Alumnos Parcial 2: {set_parcial_dos}")
print("-" * 30)

ambos_parciales = set_parcial_uno & set_parcial_dos
print(f"Aprobaron AMBOS: {ambos_parciales}")

solo_un_parcial = set_parcial_uno ^ set_parcial_dos
print(f"Aprobaron SOLO UNO: {solo_un_parcial}")

total_parcial = set_parcial_uno | set_parcial_dos
print(f"Lista total de estudiantes que aprobaron al menos un parcial: {total_parcial}")