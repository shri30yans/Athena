# Encrypter
A simple encrypter and decrypter with a basic GUI with the Cryptography module.

### Cryptography
Cryptography is a way to communicate by concealing the message through the use of codes to introduce secrecy in confedential messages so that only those for whom the information is intended can read and process it.

### Cryptography Key
Crypotographic messages are encrypted using a key. 
There are two types of encryption based on keys. 
Symmetric-key (Single key for both encryption and decryption) and Asymmetric-key (Public key and Private Key) encryption.
In this program we will use Symmetric-Key encryption.

The Fernet module in the Cryptography library allow's us to generate an encryption key that can be used for encryption and decryption.
If a key is not found the program creates a key and stores it in a `.key`.
This same key is then used to encrypt the input and decrypted the messages.

### Working
The Tkinter window has encryption window and decryption windows.

The encryption window accept's some text through a text box.
This text is first converted to a Bytes object and then encrypted with the key.
The message is then displayed in a text box.
This message can now be shared. Only a person with the unique key can read this data.

The message can decrypted in the decryption window.
The message is converted to a bytes object and then decoded using the key.
The message is then displayed in a text box.

### Images
![encrypt_before](https://github.com/shri30yans/Encoder-Decoder/blob/images/encrypt_before.png)   
*Before encrypting* 

![encrypt_after](https://github.com/shri30yans/Encoder-Decoder/blob/images/encrypt_after.png)   
*After encrypting* 

![decrypt](https://github.com/shri30yans/Encoder-Decoder/blob/images/decrypt.png)  
*After decrypting* 


