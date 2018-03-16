import datetime
from blocksync import Blocksync

s = Blocksync(endpoints=['https://api.steemit.com'])

print('\nGetting block 1')
block = s.get_block(1)
print(block)

print('\nGetting blocks 1-5')
blocks = s.get_blocks(1, 5)
for block in blocks:
    print(block)

print('\nStreaming blocks...')
for block in s.get_block_stream(batch_size=100, mode='irreversible'):
    print("{}: {} - {}".format(datetime.datetime.now(), block['block_num'], block['witness']))

print('\nStreaming all ops...')
for op in s.get_op_stream():
    print("{}: {} - {}".format(datetime.datetime.now(), op['block_num'], op['operation_type']))

print('\nStreaming vote ops only...')
for op in s.get_op_stream(whitelist=['vote']):
    print("{}: {} - {} by {}".format(datetime.datetime.now(), op['block_num'], op['operation_type'], op['voter']))
