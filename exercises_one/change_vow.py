
print("")
usu_sent = input("Ingrese una oración: ")
print("")

mod_sent = usu_sent.replace("a", "i")
mod_sent = mod_sent.replace("A", "i")
mod_sent = mod_sent.replace("e", "i")
mod_sent = mod_sent.replace("E", "i")
mod_sent = mod_sent.replace("I", "i")
mod_sent = mod_sent.replace("o", "i")
mod_sent = mod_sent.replace("O", "i")
mod_sent = mod_sent.replace("u", "i")
mod_sent = mod_sent.replace("U", "i")

print(mod_sent)
