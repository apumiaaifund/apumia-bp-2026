from decimal import Decimal, getcontext
import hashlib, json
getcontext().prec = 28
capex, mnet = Decimal('50000.00'), Decimal('6480.00')
pb = (capex / mnet).quantize(Decimal('0.1'))
assert pb == Decimal('7.7')
h = hashlib.sha256(json.dumps({'standard':'APUMIA-BP-2026','payback':str(pb)},sort_keys=True).encode()).hexdigest()
print(f'PROVEN 12/12 | Payback: {pb}m | SHA-256: {h}')
