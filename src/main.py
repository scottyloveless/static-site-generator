from markdown_to_blocks import block_to_block_type

def main():
    block = """1. Test
    2. Ordered
    3. List"""
    block_to_block_type(block)
    
main()
