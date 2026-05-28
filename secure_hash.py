import hashlib
# print(sorted(hashlib.algorithms_available))
# print(sorted(hashlib.algorithms_guaranteed))

python_program = ''' for in in range(10):
print(i)'''
print(python_program)
original_hash = hashlib.sha256(python_program.encode('utf8'))

print(f'SHA 256 :{original_hash.hexdigest()}')

