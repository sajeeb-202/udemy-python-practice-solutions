def bytes_to_string(byte_data, encoding='utf-8'):
    if not isinstance(byte_data, bytes):
        raise ValueError("Input must be bytes")

    try:
        return byte_data.decode(encoding)
    except:
        return "Decoding failed: Invalid byte sequence for the specified encoding"