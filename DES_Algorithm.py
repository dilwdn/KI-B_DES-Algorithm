# Tabel konversi hexadecimal ke biner
hexa_to_bin = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'a': '1010', 'b': '1011',
    'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'
}

# S-Box (Substitution Box)
s_box = [
    # S1
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    # S2
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    # S3
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    # S4
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    # S5
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    # S6
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    # S7
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    # S8
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]

# Permutasi Awal (Initial Permutation)
initial_permutation = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

# Permutasi Akhir (Inverse Initial Permutation)
inverse_initial_permutation = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

# Permutasi Pilihan 1 (PC-1) dan Permutasi Pilihan 2 (PC-2)
pc1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

pc2 = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]

# Tabel Ekspansi (E-Table)
expansion_table = [
    32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1
]

# Permutasi P (Permutation)
p_table = [
    16, 7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2, 8, 24, 14,
    32, 27, 3, 9,
    19, 13, 30, 6,
    22, 11, 4, 25
]

# Fungsi untuk mengubah teks menjadi format biner
def text_to_binary(text):
    padded_text = text.ljust(8)
    return ''.join(format(ord(char), '08b') for char in padded_text)

# Fungsi untuk mengubah biner menjadi teks
def binary_to_text(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(char, 2)) for char in chars).strip()

# Fungsi untuk mengubah hexadecimal ke binary
def hex_to_binary(hex_string):
    return ''.join(hexa_to_bin[c] for c in hex_string.lower())

# Fungsi untuk mengubah biner menjadi hexadecimal
def binary_to_hex(binary):
    hex_string = ""
    for i in range(0, len(binary), 4):
        nibble = binary[i:i+4]
        hex_digit = hex(int(nibble, 2))[2:]  # Konversi 4-bit biner menjadi digit hexadecimal
        hex_string += hex_digit
    return hex_string

# Fungsi untuk permutasi dengan array yang diberikan
def permute(original, permutation):
    return ''.join(original[i-1] for i in permutation)

# Fungsi untuk rotasi ke kiri
def left_shift(bits, count):
    return bits[count:] + bits[:count]

# Fungsi XOR untuk dua string biner
def xor(bits1, bits2):
    return ''.join('1' if b1 != b2 else '0' for b1, b2 in zip(bits1, bits2))

# Fungsi pembangkitan sub-kunci (16 sub-kunci) dari kunci utama
def generate_keys(main_key):
    binary_key = hex_to_binary(main_key)  # Konversi kunci utama ke biner
    pc1_key = permute(binary_key, pc1)

    # Pisahkan kunci menjadi dua bagian (kiri dan kanan)
    left, right = pc1_key[:28], pc1_key[28:]

    # Tabel pergeseran bit
    shift_table = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

    # Generate 16 sub-kunci untuk setiap ronde
    sub_keys = []
    for i, shift in enumerate(shift_table):
        left = left_shift(left, shift)
        right = left_shift(right, shift)
        combined_key = left + right
        sub_key = permute(combined_key, pc2)
        sub_keys.append(sub_key)

        # Tampilkan sub-kunci dalam bentuk hexadecimal dan biner untuk setiap ronde
        print(f"Sub-key untuk ronde {i+1} (biner): {sub_key}")
        print(f"Sub-key untuk ronde {i+1} (hexa): {binary_to_hex(sub_key)}")

    return sub_keys

# Fungsi substitusi menggunakan S-box
def substitute(expanded_half_block):
    blocks = [expanded_half_block[i:i+6] for i in range(0, len(expanded_half_block), 6)]
    result = ""
    for i, block in enumerate(blocks):
        row = int(block[0] + block[5], 2)  # Mengambil bit pertama dan terakhir untuk menentukan baris
        col = int(block[1:5], 2)  # Mengambil bit tengah untuk menentukan kolom
        result += format(s_box[i][row][col], '04b')
    return result

# Fungsi F yang diterapkan pada blok kanan
def f_function(right, sub_key):
    expanded_right = permute(right, expansion_table)
    xored_right = xor(expanded_right, sub_key)  
    substituted = substitute(xored_right)  
    return permute(substituted, p_table)  

# Modifikasi fungsi enkripsi DES untuk menggunakan F-function
def des_encrypt(plaintext, key):
    sub_keys = generate_keys(key) 
    binary_plaintext = text_to_binary(plaintext) 
    ip = permute(binary_plaintext, initial_permutation)  
    
    # Pisahkan plaintext ke bagian kiri dan kanan
    left, right = ip[:32], ip[32:]
    
    # 16 Ronde Enkripsi DES
    for round_key in sub_keys:
        temp_right = right
        right = xor(left, f_function(right, round_key))  # Gunakan F-function
        left = temp_right  # Swap
    
    # Gabungkan bagian kiri dan kanan, lalu lakukan permutasi invers
    combined_text = right + left
    encrypted_text = permute(combined_text, inverse_initial_permutation)
    
    return encrypted_text

# Modifikasi fungsi dekripsi DES untuk menggunakan F-function
def des_decrypt(ciphertext, key):
    sub_keys = generate_keys(key)[::-1] 
    ip = permute(ciphertext, initial_permutation) 

    # Pisahkan ciphertext ke bagian kiri dan kanan
    left, right = ip[:32], ip[32:]

    # 16 Ronde Dekripsi DES
    for round_key in sub_keys:
        temp_right = right
        right = xor(left, f_function(right, round_key))  
        left = temp_right 

    # Gabungkan bagian kiri dan kanan, lalu lakukan permutasi invers
    combined_text = right + left
    decrypted_text = permute(combined_text, inverse_initial_permutation)

    return decrypted_text

# Input dari pengguna untuk kunci dan pesan
key = input("Masukkan kunci 16 digit hexadecimal (contoh: 133457799BBCDFF1): ").strip()
while len(key) != 16 or not all(c in '0123456789abcdef' for c in key.lower()):
    key = input("Kunci harus 16 digit hexadecimal (karakter 0-9 dan a-f)! Masukkan ulang: ").strip()

plaintext = input("Masukkan pesan (maksimal 8 karakter): ").strip()
while len(plaintext) > 8:
    plaintext = input("Pesan harus maksimal 8 karakter! Masukkan ulang: ").strip()

# Proses Enkripsi
print("\n--- Proses Enkripsi ---")
encrypted_text = des_encrypt(plaintext, key)
print(f"Ciphertext (biner): {encrypted_text}")

# Konversi hasil enkripsi ke hexa
encrypted_hex = binary_to_hex(encrypted_text)
print(f"Ciphertext (hexa): {encrypted_hex}")

# Pisahkan output untuk enkripsi dan dekripsi
print("\n--- Proses Dekripsi ---")

# Proses Dekripsi dari hexadecimal
decrypted_binary = des_decrypt(hex_to_binary(encrypted_hex), key)
decrypted_text = binary_to_text(decrypted_binary)
print(f"Teks hasil dekripsi: {decrypted_text}")
