def print_multiple_chart(n):
    'Print the arithmetic chart'
    for i in range(n):
        for j in range(i + 1):
            print('%d * %d = %2d' %((j+1),(i+1),(j+1) * (i+1)), end = '  ')
        print('')

def test():
    print_multiple_chart(9)

__all__ = ['print_multiple_chart']

if __name__ == '__main__':
    test()