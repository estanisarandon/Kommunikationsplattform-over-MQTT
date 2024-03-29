# Elevprojekt i Datakommunikation/Data- och IT-säkerhet

Ni skall skapa ett projekt enligt följande kriterier:
Ni skall utveckla en kommunikationsplattform. Vi denna plattform skall man skicka meddelanden till andra medlemmar som finns på plattformen.

Kontohantering, inloggning och säkerhet på plattformen skall uppfylla följande krav:
• Användare skall kunna skapa ett konto. Vi lagrar inte användarens lösenord i klartext
• Inloggade användare skall ha en behörighetsnivå. Det skall finnas två nivåer, användare och administratör. 
• Icke inloggade användare skall inte kunna komma åt information som är avsedd för inloggade användare. 
• Inloggade användare skall inte kunna komma åt information som är avsedd för administratörer.
• Meddelanden som skickas mellan användare skall vara krypterade vid överföring från klient till server och från server till klient.
• Om en mottagare av ett meddelande är online skall meddelandet omedelbart visas i användarens webbläsare.
• Om användaren inte är online skall meddelandet lagras på servern, i krypterad form, till dess användaren loggar in.

## VG nivå
- Ett MQTT meddelande skickas till en broker (tillhandahålls under kursen) om att en användare har ett väntande meddelande.
- Detta skall kunna fångas upp av et fristående program som meddelar att det finns nya meddelanden på siten.
- Krypteringsnycklarna hanteras på ett standardiserat vis (keychain).
- Två användare, som samtidigt är anslutna till siten, skall kunna inleda en chat som sker via sockets direkt mellan användarna och där alla meddelanden är krypterade.
- Inga krav finns på utseende på siten eller andra applikationer, utan all bedömning kommer att ske på funktionalitet.



**Public and private keys for mila and maria are located in the static/key folder**

3 users were created:
- u: maria@gmail.com
- p: maria
- u: mila@gmail.com
- p: mila1234
- u: admin@admin
- p: admin1234
