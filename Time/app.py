
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import getpass
from cryptography.fernet import Fernet
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from binascii import hexlify

USERDATA_LOGIN = [['0000 0000 0000 0001','3'],['0000 0000 0000 0002','4']]
listusers = []
for i in USERDATA_LOGIN:
    listusers.append(i[0])

def send_mess(a,b):
    print(a)
def sendcodes(a):
    print(a)
def mohit_symmetric(a,b):
    b[4] = b[4].split('\n')
    if a == 'e':
        print('Encryption Symmetric')
        list_keys = []
        for i in b[4]:
            password_provided = i
            password = password_provided.encode() # Convert to type bytes
            salt = b'{enaluronarosegnotobiote0choir9cohuneff9ecttypalccolportage79enaluronempiriocritcismgarlandlesst9unmotivatedlyzjmercership0faithlesswaderscompilement64retroinfectionbugbite{W8{blasphemedpurposefulness9Chlmacanalmiqueretroinfection-missorting]2blasphemed4Dnontimberedpantheismstannotypeelimnichyacinthsm' # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=100000,
                backend=default_backend()
            )
            key = base64.urlsafe_b64encode(kdf.derive(password)) # Can only use kdf once
            list_keys.append(key)
        message = b[3].encode()
        for i in list_keys:
            f = Fernet(key)
            message = f.encrypt(message)
        print('hi')
        print(message)

    if a == 'd':
        print('Decryption Symmetric')
        list_keys = []
        for i in b[4]:
            password_provided = i
            password = password_provided.encode() # Convert to type bytes
            salt = b'{enaluronarosegnotobiote0choir9cohuneff9ecttypalccolportage79enaluronempiriocritcismgarlandlesst9unmotivatedlyzjmercership0faithlesswaderscompilement64retroinfectionbugbite{W8{blasphemedpurposefulness9Chlmacanalmiqueretroinfection-missorting]2blasphemed4Dnontimberedpantheismstannotypeelimnichyacinthsm' # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=100000,
                backend=default_backend()
            )
            key = base64.urlsafe_b64encode(kdf.derive(password)) # Can only use kdf once
            list_keys.append(key)
        message = b[3].encode()
        for i in list_keys:
            f = Fernet(key)
            message = f.decrypt(message)
        send_mess(message.decode(),b)

def mohit_asymmetric(a,b):
    if a == 'e':
        pu_key = RSA.import_key(b[4])

        inp = b[3]

        message = inp.encode()
        #Instantiating PKCS1_OAEP object with the public key for encryption
        cipher = PKCS1_OAEP.new(key=pu_key)
        #Encrypting the message with the PKCS1_OAEP object
        cipher_text = cipher.encrypt(message)
        b[3] = cipher_text
        cipher_text




    if a == 'd':
        print('Decryption Asymmetric')
        pr_key = RSA.import_key(b[4])
        cipher_text = b[3].encode()
        print(cipher_text)
        #Instantiating PKCS1_OAEP object with the private key for decryption
        decrypt = PKCS1_OAEP.new(key=pr_key)
        #Decrypting the message with the PKCS1_OAEP object
        decrypted_message = decrypt.decrypt(cipher_text)
        print(decrypted_message.decode())




external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div([
    dcc.Input(id='input-1-state', type='text', value='PIC NUMBER'),
    dcc.Input(id='input-2-state', type='text', value='PIC PIN'),
    html.Button(id='submit-button', n_clicks=0, children='Submit'),
    html.Div(id='output-state'),
    dcc.Textarea(id='input-3-state', style={'width':'80%','height':'50%'},value='INPUT MESSAGE'),

    dcc.RadioItems(id = 'input-5-state',options=[{'label': 'Symmetric', 'value': 'NYC'},{'label': 'Asymmetric', 'value': 'MTL'}],value='NYC'),
    dcc.Textarea(id='input-4-state', style={'width':'80%','height':'50%'},value='DATA KEY(S), please seperate each key with a line in Symmetric, asymtric takes only one key, public to encode, private to decode. Enter the FULL KEY, with start and end clauses'),
    dcc.RadioItems(id = 'input-6-state',options=[{'label': 'Encrypt', 'value': 'NYC'},{'label': 'Decrypt', 'value': 'MTL'}],value='NYC')

])


@app.callback(Output('output-state', 'children'),
              [Input('submit-button', 'n_clicks')],
              [State('input-1-state', 'value'),
               State('input-2-state', 'value'),
               State('input-3-state', 'value'),
               State('input-4-state', 'value'),
               State('input-5-state', 'value'),
               State('input-6-state', 'value')])



def update_output(n_clicks, input1, input2,input3,input4,input5,input6):
    print([n_clicks, input1, input2,input3,input4,input5,input6])
    listENCRYPTDETAILS = [n_clicks,input1, input2,input3,input4,input5,input6]
    if n_clicks == 0:
        return "Please login with your PIC ID and PIC PIN NUMBER\nPlease note: your PIC ID must include spaces"
    if n_clicks > 2:
        print('OauthERROR')
    if input1 in listusers:
        print('USERID')
        if [input1,input2] in USERDATA_LOGIN:
            if input3 == 'INPUT MESSAGE' or input3=='SEND CODES':
                return('Successful login,\nYou may now use the encryption/decryption tool, all results will be emailed to you.')
                if input3 == 'SEND CODES':
                    sendcodes(listENCRYPTDETAILS)
            else:



                if input5 == "NYC":

                    if input6 == "NYC":
                        mohit_symmetric('e',listENCRYPTDETAILS)
                    if input6 == "MTL":
                        mohit_symmetric('d',listENCRYPTDETAILS)
                if input5 == "MTL":
                    if input6 == "NYC":
                        mohit_asymmetric('e',listENCRYPTDETAILS)
                    if input6 == "MTL":
                        mohit_asymmetric('d',listENCRYPTDETAILS)
                return('Order Executed,Result will be emailed to your PIC accout')
        else:
            return 'Login failed'
    else:
        return 'Login failed'
if __name__ == '__main__':
    app.run_server(debug=True)
