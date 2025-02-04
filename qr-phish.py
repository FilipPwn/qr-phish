import qrcode
import argparse

def generate_qr(url, output='qr.html'):
    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=1,
        border=1,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Get the QR code matrix
    qr_matrix = qr.get_matrix()
    matrix_size = len(qr_matrix)

    # Create HTML content with div-based grid
    html_content = f'''<!DOCTYPE html>
<html>
<head>
    <title>QR Code</title>
    <style>
        .container {{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f0f0f0;
        }}
        .qr-code {{
            display: grid;
            grid-template-columns: repeat({matrix_size}, 1fr);
            gap: 0;
            padding: 20px;
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }}
        .qr-pixel {{
            width: 10px;
            height: 10px;
        }}
        .black {{
            background-color: black;
        }}
        .white {{
            background-color: white;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="qr-code">'''

    # Add QR code pixels as divs
    for row in qr_matrix:
        for pixel in row:
            color_class = "black" if pixel else "white"
            html_content += f'\n            <div class="qr-pixel {color_class}"></div>'

    # Close HTML content
    html_content += '''
        </div>
    </div>
</body>
</html>'''

    # Save as HTML file
    with open(output, 'w') as f:
        f.write(html_content)

def main():
    parser = argparse.ArgumentParser(description='Generate QR code in HTML format')
    parser.add_argument('-u', '--url', required=True, help='URL to encode in QR code')
    parser.add_argument('-o', '--output', default='qr.html', help='Output HTML file name (default: qr.html)')
    
    args = parser.parse_args()
    
    try:
        generate_qr(args.url, args.output)
        print(f'QR code generated successfully in {args.output}')
    except Exception as e:
        print(f'Error generating QR code: {str(e)}')

if __name__ == '__main__':
    main()
