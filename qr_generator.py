import qrcode
from PIL import Image  

def generate_qr_code(data, file_name='qr_code.png'):
    
    qr = qrcode.QRCode(
        version=1,  
        error_correction=qrcode.constants.ERROR_CORRECT_L,  
        box_size=10,  
        border=4,  
    )
    
    qr.add_data(data)
    qr.make(fit=True)  
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    
    img.save(file_name)
    print(f"QR code saved as '{file_name}'")
    
    img.show()

if __name__ == "__main__":
    user_data = input("Enter the data to encode (e.g., URL or text): ")
    file_name = input("Enter the output file name (default: qr_code.png): ") or 'qr_code.png'
    generate_qr_code(user_data, file_name)