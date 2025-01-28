import hashlib
from optparse import OptionParser

def create_hash(algorithm, string):
    hash_instance = hashlib.new(algorithm)
    
    hash_instance.update(string.encode('utf-8'))
    
    return hash_instance.hexdigest()

usage = '''
# Usage:
    python hash-code.py --password <password_vlaue> --hashtype <hash_type>
# Example:
    python hash-code.py --password password123 --hashtype md5
'''
optHandler = OptionParser(usage)

optHandler.add_option("--password", dest="password", type="string", help="Password to be hashed")
optHandler.add_option("--hashtype", dest="hashtype", type="string", help="Type of hash: md5, sha1, sha256, etc.")

(opts, argsList) = optHandler.parse_args()

if not (opts.password and opts.hashtype):
        print(optHandler.usage)
        exit(0)
else:
    hash_value = create_hash(opts.hashtype, opts.password)

print(f"The {opts.hashtype} hash of '{opts.password}' is: {hash_value}")
