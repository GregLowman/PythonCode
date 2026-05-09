# Binary Files — Bytes, BMP, and MP3

Low-level binary file handling in Python: byte manipulation, bitmap inversion, ID3 tag parsing, and checksum verification.

## Files

| File | Topic |
|---|---|
| `bytes_example.py` | Byte literals, iteration over bytes, and UTF-8 decoding |
| `invert_bitmap.py` | Reads a BMP file, inverts all pixel bits (XOR 255), writes a new inverted BMP |
| `read_id3.py` | Parses ID3v2.3 tags from an MP3 — extracts text frames, URLs, and embedded artwork |
| `id3_types.py` | ID3v2 constants: field encodings, APIC picture types, and frame type mappings |
| `sha_checksum.py` | Verifies a file's integrity by comparing its SHA-256 hash against a known value |

## Assets
- `edit.bmp` / `vintage-halloween-bat.bmp` — source bitmaps used by `invert_bitmap.py`
- `SampleSong.mp3` / `Someday.mp3` — MP3 files used by `read_id3.py`
- `colorama-0.4.4-py2.py3-none-any.whl` — wheel file used by `sha_checksum.py`

## Key Concepts
- Binary file I/O (`open(..., 'rb')` / `'wb'`)
- Byte slicing and `int.from_bytes()` for parsing binary headers
- BMP file structure: file header, DIB header, pixel array
- ID3v2 synchsafe integer encoding for tag sizes
- SHA-256 checksums with `hashlib`
