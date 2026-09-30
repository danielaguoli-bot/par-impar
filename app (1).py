
import streamlit as st

st.title("🔢 Analizador de números")

st.write("Ingresa un número para saber si es par, impar, primo y comprobar su divisibilidad.")

numero = st.number_input(
    "Ingresa un número:",
    min_value=0,
    step=1
)

if st.button("Analizar número"):

    # PAR O IMPAR
    if numero % 2 == 0:
        st.success("🟢 El número es PAR.")
    else:
        st.info("🔵 El número es IMPAR.")

    # PRIMO O NO PRIMO
    if numero < 2:
        st.warning("⚠️ El número NO es primo.")
    else:
        primo = True

        for i in range(2, int(numero)):
            if numero % i == 0:
                primo = False
                break

        if primo:
            st.success("⭐ El número ES PRIMO.")
        else:
            st.warning("❌ El número NO es primo.")

# DIVISIBILIDAD

st.subheader("➗ Comprobar divisibilidad")

divisor = st.number_input(
    "Ingresa otro número:",
    min_value=1,
    step=1
)

if st.button("Comprobar divisibilidad"):

    if numero % divisor == 0:
        st.success(
            f"✅ {int(numero)} es divisible entre {int(divisor)}."
        )
    else:
        st.error(
            f"❌ {int(numero)} no es divisible entre {int(divisor)}."
        )
