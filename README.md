# Hash Cracker

A tool for brute-forcing hashes using a provided wordlist.

## **Features**
- **Multiple Algorithm Support:** Crack hashes made with md5, sha1, sha256, and more.
- **User-friendly CLI:** Intuitive and easy to use.
- **Helpful Feedback:** Receive clear and concise error messages when things go wrong.

## **Prerequisites**

- Python 3.x

## **Usage**
Run the cracker with:

```
python hash-cracker.py --hashvalue <hash_value> --hashtype <hash_type> --wordlist <path_to_wordlist>
```

## Parameters

- `--hashvalue`: The hash string you want to decode.
- `--hashtype`: The algorithm used to encode the hash. (e.g., md5, sha1, sha256, etc.)
- `--wordlist`: Path to the wordlist file you want to use for brute-forcing.

## Example
1) Generate the wordlist.txt file using `generate-wordlist.py` and change the wordlist.txt to desired wordlist.

```
python generate-wordlist.py
```

2) Hash any word using `hash-code.py`. Hash type can be `sha224, sha256, sha1, sha512, shake_128, blake2s, blake2b, sha3_256, sha384, sha3_384, shake_256, md5, sha3_224, sha3_512`.
`

```
python hash-code.py --password password123 --hashtype md5
```

3) To crack an `md5` hash using the `wordlist.txt` wordlist.

```
python hash-cracker.py --hashvalue 482c811da5d5b4bc6d497ffa98491e38 --hashtype md5 --wordlist wordlist.txt
```

