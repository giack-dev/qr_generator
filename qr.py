import qrcode

def create_qr_code(input_data: str) -> None:
    file_name = "generated_qr.jpg"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(input_data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img = img.resize((256, 256))
    img.save(file_name)
    print(f"Saved image as: {file_name}")


