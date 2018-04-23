def main():
    def a():
        for i in range(10):
            print 'i:' + str(i)
            yield i

    for j in a():
        print 'j:' + str(j)
if __name__ == '__main__':
    main()